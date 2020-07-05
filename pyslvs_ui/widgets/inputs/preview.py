# -*- coding: utf-8 -*-

"""The animation dialog."""

from typing import Sequence, Tuple, Mapping
from math import cos, sin, atan2, hypot
from qtpy.QtCore import Qt, Slot, QTimer
from qtpy.QtWidgets import (
    QWidget, QDialog, QVBoxLayout, QHBoxLayout, QSlider, QPushButton, QLabel,
    QSpacerItem, QSizePolicy, QDoubleSpinBox,
)
from qtpy.QtGui import QPaintEvent, QPen, QColor, QPixmap, QIcon
from numpy import array, ndarray, isclose
from pyslvs import VPoint, VLink, derivative
from pyslvs_ui.graphics import (
    AnimationCanvas, color_qt, convex_hull, LINK_COLOR,
)

_Coord = Tuple[float, float]
_Paths = Sequence[Sequence[_Coord]]
_SliderPaths = Mapping[int, Sequence[_Coord]]
_Vecs = Mapping[int, ndarray]


class _DynamicCanvas(AnimationCanvas):
    vel: _Vecs
    vel_slider: _Vecs
    acc: _Vecs
    acc_slider: _Vecs

    def __init__(
        self,
        vpoints: Sequence[VPoint],
        vlinks: Sequence[VLink],
        path: _Paths,
        slider_path: _SliderPaths,
        parent: QWidget
    ):
        super(_DynamicCanvas, self).__init__(parent)
        self.ind = 0
        self.vpoints = vpoints
        self.vlinks = vlinks
        self.path.path = path
        self.path.slider_path = slider_path
        self.vel = {i: derivative(array(path))
                    for i, path in enumerate(self.path.path)}
        self.vel_slider = {i: derivative(array(p))
                           for i, p in self.path.slider_path.items()}
        self.acc = {i: derivative(p) for i, p in self.vel.items()}
        self.acc_slider = {i: derivative(p)
                           for i, p in self.vel_slider.items()}
        self.max_ind = max(len(p) for p in self.path.path)
        self.factor = 1.

    @Slot(int)
    def set_index(self, ind: int):
        """Set current index."""
        self.ind = ind
        self.update()

    @Slot(float)
    def set_factor(self, scalar: float):
        """Set the size of the derived value."""
        self.factor = scalar
        self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        """Drawing function."""
        super(_DynamicCanvas, self).paintEvent(event)
        pen = QPen()
        pen.setWidth(self.path_width)
        for paths, vel, acc in [
            (enumerate(self.path.path), self.vel, self.acc),
            (self.path.slider_path.items(), self.vel_slider, self.acc_slider),
        ]:
            for i, path in paths:
                vpoint = self.vpoints[i]
                if self.monochrome:
                    pen.setColor(color_qt('gray'))
                elif vpoint.color is None:
                    pen.setColor(color_qt('green'))
                else:
                    pen.setColor(QColor(*vpoint.color))
                self.painter.setPen(pen)
                self.draw_curve(path)
                x, y = path[self.ind]
                zoom = 1.
                for vec, color in [(vel[i], Qt.blue), (acc[i], Qt.red)]:
                    if self.ind >= len(vec):
                        break
                    zoom *= self.factor
                    vx, vy = vec[self.ind]
                    r = hypot(vx, vy) * zoom
                    if isclose(r, 0):
                        break
                    th = atan2(vy, vx)
                    pen.setColor(color)
                    self.painter.setPen(pen)
                    self.draw_arrow(x, y, x + r * cos(th), y + r * sin(th))
                self.draw_point(i, x, y, vpoint.grounded(), vpoint.color)
        pen.setWidth(self.link_width)
        for vlink in self.vlinks:
            if vlink.name == VLink.FRAME or not vlink.points:
                continue
            # TODO
            qpoints = convex_hull(
                [(c.x * self.zoom, c.y * -self.zoom)
                 for c in vlink.points_pos(self.vpoints)], as_qpoint=True)
            pen.setColor(Qt.black if self.monochrome else QColor(*vlink.color))
            self.painter.setPen(pen)
            brush = color_qt('dark-gray') if self.monochrome else LINK_COLOR
            self.painter.setBrush(brush)
            self.painter.drawPolygon(*qpoints)
        self.painter.end()


class AnimateDialog(QDialog):

    def __init__(
        self,
        vpoints: Sequence[VPoint],
        vlinks: Sequence[VLink],
        path: _Paths,
        slider_path: _SliderPaths,
        monochrome: bool,
        parent: QWidget
    ):
        super(AnimateDialog, self).__init__(parent)
        self.setWindowTitle("Vector Animation")
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint
                            & ~Qt.WindowContextHelpButtonHint)
        self.setMinimumSize(800, 600)
        self.setModal(True)
        main_layout = QVBoxLayout(self)
        layout = QHBoxLayout(self)
        self.label = QLabel(self)
        layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding,
                                   QSizePolicy.Minimum))
        layout.addWidget(self.label)
        main_layout.addLayout(layout)
        self.canvas = _DynamicCanvas(vpoints, vlinks, path, slider_path, self)
        self.canvas.set_monochrome_mode(monochrome)
        self.canvas.update_pos.connect(self.__set_pos)
        main_layout.addWidget(self.canvas)
        layout = QHBoxLayout(self)
        self.play = QPushButton(QIcon(QPixmap(":/icons/play.png")), "", self)
        self.play.setCheckable(True)
        self.play.clicked.connect(self.__play)
        layout.addWidget(self.play)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMaximum(max(len(p) for p in path) - 1)
        self.slider.valueChanged.connect(self.canvas.set_index)
        layout.addWidget(self.slider)
        factor = QDoubleSpinBox(self)
        factor.valueChanged.connect(self.canvas.set_factor)
        factor.setRange(0.01, 9999)
        factor.setValue(50)
        layout.addWidget(factor)
        main_layout.addLayout(layout)
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.__move_ind)

    @Slot()
    def __move_ind(self):
        """Move indicator."""
        value = self.slider.value() + 1
        self.slider.setValue(value)
        if value > self.slider.maximum():
            self.slider.setValue(0)

    @Slot(float, float)
    def __set_pos(self, x: float, y: float) -> None:
        """Set mouse position."""
        self.label.setText(f"({x:.04f}, {y:.04f})")

    @Slot()
    def __play(self):
        """Start playing."""
        if self.play.isChecked():
            self.timer.start()
        else:
            self.timer.stop()
