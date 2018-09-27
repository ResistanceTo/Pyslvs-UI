# -*- coding: utf-8 -*-

"""The widget of 'Inputs' tab."""

import csv
from typing import (
    Tuple,
    Dict,
    Sequence,
    Iterator,
    Optional,
)
from core.QtModules import (
    pyqtSignal,
    pyqtSlot,
    QWidget,
    QDial,
    QTimer,
    QMenu,
    QMessageBox,
    QInputDialog,
    QListWidgetItem,
    QPoint,
    QApplication,
    QShortcut,
    QKeySequence,
)
from core.io import (
    AddVariable, DeleteVariable,
    AddPath, DeletePath,
)
from core import main_window as mw
from core.libs import VPoint
from .rotatable import RotatableView
from .Ui_inputs import Ui_Form


def _variable_int(text: str) -> int:
    """Change variable text to index."""
    return int(text.split()[-1].replace("Point", ""))


class InputsWidget(QWidget, Ui_Form):
    
    """There has following functions:
    
    + Function of mechanism variables settings.
    + Path recording.
    """
    
    aboutToResolve = pyqtSignal()
    
    def __init__(self, parent: 'mw.MainWindow'):
        super(InputsWidget, self).__init__(parent)
        self.setupUi(self)
        
        # parent's function pointer.
        self.freemode_button = parent.freemode_button
        self.EntitiesPoint = parent.EntitiesPoint
        self.EntitiesLink = parent.EntitiesLink
        self.MainCanvas = parent.MainCanvas
        self.solve = parent.solve
        self.reloadCanvas = parent.reloadCanvas
        self.outputTo = parent.outputTo
        self.conflict = parent.conflict
        self.DOF = lambda: parent.DOF
        self.rightInput = parent.rightInput
        self.CommandStack = parent.CommandStack
        self.setCoordsAsCurrent = parent.setCoordsAsCurrent
        
        # QDial: Angle panel.
        self.dial = QDial()
        self.dial.setStatusTip("Input widget of rotatable joint.")
        self.dial.setEnabled(False)
        self.dial.valueChanged.connect(self.__updateVar)
        self.dial_spinbox.valueChanged.connect(self.__setVar)
        self.inputs_dial_layout.addWidget(RotatableView(self.dial))
        
        # QDial ok check.
        self.variable_list.currentRowChanged.connect(self.__dialOk)
        
        # Play button.
        action = QShortcut(QKeySequence("F5"), self)
        action.activated.connect(self.variable_play.click)
        self.variable_stop.clicked.connect(self.variableValueReset)
        
        # Timer for play button.
        self.inputs_playShaft = QTimer(self)
        self.inputs_playShaft.setInterval(10)
        self.inputs_playShaft.timeout.connect(self.__changeIndex)
        
        # Change the point coordinates with current position.
        self.update_pos.clicked.connect(self.setCoordsAsCurrent)
        
        """Inputs record context menu
        
        + Copy data from Point0
        + Copy data from Point1
        + ...
        """
        self.popMenu_record_list = QMenu(self)
        self.record_list.customContextMenuRequested.connect(
            self.__record_list_context_menu
        )
        self.__path_data: Dict[str, Sequence[Tuple[float, float]]] = {}
    
    def clear(self):
        """Clear function to reset widget status."""
        self.__path_data.clear()
        for i in range(self.record_list.count() - 1):
            self.record_list.takeItem(1)
        self.variable_list.clear()
    
    def __setAngleMode(self):
        """Change to angle input."""
        self.dial.setMinimum(0)
        self.dial.setMaximum(36000)
        self.dial_spinbox.setMinimum(0)
        self.dial_spinbox.setMaximum(360)
    
    def __setUnitMode(self):
        """Change to unit input."""
        self.dial.setMinimum(-50000)
        self.dial.setMaximum(50000)
        self.dial_spinbox.setMinimum(-500)
        self.dial_spinbox.setMaximum(500)
    
    def pathData(self):
        """Return current path data."""
        return self.__path_data
    
    @pyqtSlot(tuple)
    def setSelection(self, selections: Tuple[int]):
        """Set one selection from canvas."""
        self.joint_list.setCurrentRow(selections[0])
    
    @pyqtSlot()
    def clearSelection(self):
        """Clear the points selection."""
        self.driver_list.clear()
        self.joint_list.setCurrentRow(-1)
    
    @pyqtSlot(int, name='on_joint_list_currentRowChanged')
    def __updateRelatePoints(self, _: int):
        """Change the point row from input widget."""
        self.driver_list.clear()
        
        item: Optional[QListWidgetItem] = self.joint_list.currentItem()
        if item is None:
            return
        p0 = _variable_int(item.text())
        
        vpoints = self.EntitiesPoint.dataTuple()
        type_int = vpoints[p0].type
        if type_int == VPoint.R:
            for i, vpoint in enumerate(vpoints):
                if i == p0:
                    continue
                if vpoints[p0].same_link(vpoint):
                    if vpoints[p0].grounded() and vpoint.grounded():
                        continue
                    self.driver_list.addItem(f"[{vpoint.typeSTR}] Point{i}")
        elif type_int in {VPoint.P, VPoint.RP}:
            self.driver_list.addItem(f"[{vpoints[p0].typeSTR}] Point{p0}")
    
    @pyqtSlot(int, name='on_driver_list_currentRowChanged')
    def __setAddVarEnabled(self, _: int):
        """Set enable of 'add variable' button."""
        driver = self.driver_list.currentIndex()
        self.variable_add.setEnabled(driver != -1)
    
    @pyqtSlot(name='on_variable_add_clicked')
    def __addInputsVariable(self, p0: Optional[int] = None, p1: Optional[int] = None):
        """Add variable with '->' sign."""
        if p0 is None:
            item: Optional[QListWidgetItem] = self.joint_list.currentItem()
            if item is None:
                return
            p0 = _variable_int(item.text())
        if p1 is None:
            item: Optional[QListWidgetItem] = self.driver_list.currentItem()
            if item is None:
                return
            p1 = _variable_int(item.text())
        
        # Check DOF.
        if self.DOF() <= self.inputCount():
            QMessageBox.warning(
                self,
                "Wrong DOF",
                "The number of variable must no more than degrees of freedom."
            )
            return
        
        # Check same link.
        vpoints = self.EntitiesPoint.dataTuple()
        if not vpoints[p0].same_link(vpoints[p1]):
            QMessageBox.warning(
                self,
                "Wrong pair",
                "The base point and driver point should at the same link."
            )
            return
        
        # Check repeated pairs.
        for p0_, p1_, a in self.inputPairs():
            if {p0, p1} == {p0_, p1_} and vpoints[p0].type == VPoint.R:
                QMessageBox.warning(
                    self,
                    "Wrong pair",
                    "There already have a same pair."
                )
                return
        
        name = f'Point{p0}'
        self.CommandStack.beginMacro(f"Add variable of {name}")
        if p0 == p1:
            # One joint by offset.
            value = vpoints[p0].true_offset()
        else:
            # Two joints by angle.
            value = vpoints[p0].slope_angle(vpoints[p1])
        self.CommandStack.push(AddVariable('->'.join((
            name,
            f'Point{p1}',
            f"{value:.02f}",
        )), self.variable_list))
        self.CommandStack.endMacro()
    
    def addInputsVariables(self, variables: Tuple[Tuple[int, int]]):
        """Add from database."""
        for p0, p1 in variables:
            self.__addInputsVariable(p0, p1)
    
    @pyqtSlot()
    def __dialOk(self):
        """Set the angle of base link and drive link."""
        row = self.variable_list.currentRow()
        enabled = row > -1
        rotatable = (
            enabled and
            not self.freemode_button.isChecked() and
            self.rightInput()
        )
        self.dial.setEnabled(rotatable)
        self.dial_spinbox.setEnabled(rotatable)
        self.oldVar = self.dial.value() / 100.
        self.variable_play.setEnabled(rotatable)
        self.variable_speed.setEnabled(rotatable)
        item: Optional[QListWidgetItem] = self.variable_list.currentItem()
        if item is None:
            return
        expr = item.text().split('->')
        p0 = int(expr[0].replace('Point', ''))
        p1 = int(expr[1].replace('Point', ''))
        value = float(expr[2])
        if p0 == p1:
            self.__setUnitMode()
        else:
            self.__setAngleMode()
        self.dial.setValue(value * 100 if enabled else 0)
    
    def variableExcluding(self, row: Optional[int] = None):
        """Remove variable if the point was been deleted. Default: all."""
        one_row: bool = row is not None
        for i, (b, d, a) in enumerate(self.inputPairs()):
            # If this is not origin point any more.
            if one_row and (row != b):
                continue
            self.CommandStack.beginMacro(f"Remove variable of Point{row}")
            self.CommandStack.push(DeleteVariable(i, self.variable_list))
            self.CommandStack.endMacro()
    
    @pyqtSlot(name='on_variable_remove_clicked')
    def __removeVar(self):
        """Remove and reset angle."""
        row = self.variable_list.currentRow()
        if not row > -1:
            return
        reply = QMessageBox.question(
            self,
            "Remove variable",
            "Do you want to remove this variable?"
        )
        if reply != QMessageBox.Yes:
            return
        self.variable_stop.click()
        self.CommandStack.beginMacro(f"Remove variable of Point{row}")
        self.CommandStack.push(DeleteVariable(row, self.variable_list))
        self.CommandStack.endMacro()
        self.EntitiesPoint.getBackPosition()
        self.solve()
    
    def interval(self) -> float:
        """Return interval value."""
        return self.record_interval.value()
    
    def inputCount(self) -> int:
        """Use to show input variable count."""
        return self.variable_list.count()
    
    def inputPairs(self) -> Iterator[Tuple[int, int, float]]:
        """Back as point number code."""
        for row in range(self.variable_list.count()):
            var = self.variable_list.item(row).text().split('->')
            p0 = int(var[0].replace('Point', ''))
            p1 = int(var[1].replace('Point', ''))
            angle = float(var[2])
            yield (p0, p1, angle)
    
    def variableReload(self):
        """Auto check the points and type."""
        self.joint_list.clear()
        for i in range(self.EntitiesPoint.rowCount()):
            type_text = self.EntitiesPoint.item(i, 2).text()
            self.joint_list.addItem(f"[{type_text}] Point{i}")
        self.variableValueReset()
    
    @pyqtSlot(float)
    def __setVar(self, value: float):
        self.dial.setValue(int(value * 100 % self.dial.maximum()))
    
    @pyqtSlot(int)
    def __updateVar(self, value: int):
        """Update the value when rotating QDial."""
        item = self.variable_list.currentItem()
        value /= 100.
        self.dial_spinbox.blockSignals(True)
        self.dial_spinbox.setValue(value)
        self.dial_spinbox.blockSignals(False)
        if item:
            item_text = item.text().split('->')
            item_text[-1] = f"{value:.02f}"
            item.setText('->'.join(item_text))
            self.aboutToResolve.emit()
        if (
            self.record_start.isChecked() and
            abs(self.oldVar - value) > self.record_interval.value()
        ):
            self.MainCanvas.recordPath()
            self.oldVar = value
    
    def variableValueReset(self):
        """Reset the value of QDial."""
        if self.inputs_playShaft.isActive():
            self.variable_play.setChecked(False)
            self.inputs_playShaft.stop()
        self.EntitiesPoint.getBackPosition()
        vpoints = self.EntitiesPoint.dataTuple()
        for i, (p0, p1, a) in enumerate(self.inputPairs()):
            self.variable_list.item(i).setText('->'.join([
                f'Point{p0}',
                f'Point{p1}',
                f"{vpoints[p0].slope_angle(vpoints[p1]):.02f}",
            ]))
        self.__dialOk()
        self.solve()
    
    @pyqtSlot(bool, name='on_variable_play_toggled')
    def __play(self, toggled: bool):
        """Triggered when play button was changed."""
        self.dial.setEnabled(not toggled)
        self.dial_spinbox.setEnabled(not toggled)
        if toggled:
            self.inputs_playShaft.start()
        else:
            self.inputs_playShaft.stop()
            if self.update_pos_option.isChecked():
                self.setCoordsAsCurrent()
    
    @pyqtSlot()
    def __changeIndex(self):
        """QTimer change index."""
        index = self.dial.value()
        speed = self.variable_speed.value()
        extreme_rebound = (
            self.conflict.isVisible() and
            self.extremeRebound.isChecked()
        )
        if extreme_rebound:
            speed = -speed
            self.variable_speed.setValue(speed)
        index += int(speed * 6 * (3 if extreme_rebound else 1))
        index %= self.dial.maximum()
        self.dial.setValue(index)
    
    @pyqtSlot(bool, name='on_record_start_toggled')
    def __startRecord(self, toggled: bool):
        """Save to file path data."""
        if toggled:
            self.MainCanvas.recordStart(int(
                self.dial_spinbox.maximum() / self.record_interval.value()
            ))
            return
        path = self.MainCanvas.getRecordPath()
        name, ok = QInputDialog.getText(
            self,
            "Recording completed!",
            "Please input name tag:"
        )
        i = 0
        name = name or f"Record_{i}"
        while name in self.__path_data:
            name = f"Record_{i}"
            i += 1
        QMessageBox.information(
            self,
            "Record",
            "The name tag is being used or empty."
        )
        self.addPath(name, path)
    
    def addPath(self, name: str, path: Sequence[Tuple[float, float]]):
        """Add path function."""
        self.CommandStack.beginMacro(f"Add {{Path: {name}}}")
        self.CommandStack.push(AddPath(
            self.record_list,
            name,
            self.__path_data,
            path
        ))
        self.CommandStack.endMacro()
        self.record_list.setCurrentRow(self.record_list.count() - 1)
    
    def loadPaths(self, paths: Dict[str, Sequence[Tuple[float, float]]]):
        """Add multiple path."""
        for name, path in paths.items():
            self.addPath(name, path)
    
    @pyqtSlot(name='on_record_remove_clicked')
    def __removePath(self):
        """Remove path data."""
        row = self.record_list.currentRow()
        if not row > 0:
            return
        name = self.record_list.item(row).text()
        self.CommandStack.beginMacro(f"Delete {{Path: {name}}}")
        self.CommandStack.push(DeletePath(
            row,
            self.record_list,
            self.__path_data
        ))
        self.CommandStack.endMacro()
        self.record_list.setCurrentRow(self.record_list.count() - 1)
        self.reloadCanvas()
    
    @pyqtSlot(QListWidgetItem, name='on_record_list_itemDoubleClicked')
    def __pathDlg(self, item: QListWidgetItem):
        """View path data."""
        name = item.text().split(":")[0]
        try:
            data = self.__path_data[name]
        except KeyError:
            return
        points_text = ", ".join(f"Point{i}" for i in range(len(data)))
        reply = QMessageBox.question(
            self,
            "Path data",
            f"This path data including {points_text}.",
            (QMessageBox.Save | QMessageBox.Close),
            QMessageBox.Close
        )
        if reply != QMessageBox.Save:
            return
        file_name = self.outputTo(
            "path data",
            ["Comma-Separated Values (*.csv)", "Text file (*.txt)"]
        )
        if not file_name:
            return
        with open(file_name, 'w', newline='') as stream:
            writer = csv.writer(stream)
            for point in data:
                for coordinate in point:
                    writer.writerow(coordinate)
                writer.writerow(())
        print(f"Output path data: {file_name}")
    
    @pyqtSlot(QPoint)
    def __record_list_context_menu(self, point):
        """Show the context menu.
        
        Show path [0], [1], ...
        Or copy path coordinates.
        """
        row = self.record_list.currentRow()
        if not row > -1:
            return
        showall_action = self.popMenu_record_list.addAction("Show all")
        showall_action.index = -1
        copy_action = self.popMenu_record_list.addAction("Copy as new")
        name = self.record_list.item(row).text().split(':')[0]
        try:
            data = self.__path_data[name]
        except KeyError:
            # Auto preview path.
            data = self.MainCanvas.Path.path
            showall_action.setEnabled(False)
        else:
            for action_text in ("Show", "Copy data from"):
                self.popMenu_record_list.addSeparator()
                for i in range(len(data)):
                    if data[i]:
                        action = self.popMenu_record_list.addAction(
                            f"{action_text} Point{i}"
                        )
                        action.index = i
        action_exec = self.popMenu_record_list.exec_(
            self.record_list.mapToGlobal(point)
        )
        if action_exec:
            if action_exec == copy_action:
                # Copy path data.
                num = 0
                name_copy = f"{name}_{num}"
                while name_copy in self.__path_data:
                    name_copy = f"{name}_{num}"
                    num += 1
                self.addPath(name_copy, data)
            elif "Copy data from" in action_exec.text():
                # Copy data to clipboard.
                QApplication.clipboard().setText('\n'.join(
                    f"{x},{y}" for x, y in data[action_exec.index]
                ))
            elif "Show" in action_exec.text():
                # Switch points enabled status.
                if action_exec.index == -1:
                    self.record_show.setChecked(True)
                self.MainCanvas.setPathShow(action_exec.index)
        self.popMenu_record_list.clear()
    
    @pyqtSlot(bool, name='on_record_show_toggled')
    def __setPathShow(self, toggled: bool):
        """Show all paths or hide."""
        self.MainCanvas.setPathShow(-1 if toggled else -2)
    
    @pyqtSlot(int, name='on_record_list_currentRowChanged')
    def __setPath(self, _: int):
        """Reload the canvas when switch the path."""
        if not self.record_show.isChecked():
            self.record_show.setChecked(True)
        self.reloadCanvas()
    
    def currentPath(self):
        """Return current path data to main canvas.
        
        + No path.
        + Show path data.
        + Auto preview.
        """
        row = self.record_list.currentRow()
        if row in {0, -1}:
            return ()
        path_name = self.record_list.item(row).text().split(':')[0]
        return self.__path_data.get(path_name, ())
    
    @pyqtSlot(name='on_variable_up_clicked')
    @pyqtSlot(name='on_variable_down_clicked')
    def __setVariablePriority(self):
        row = self.variable_list.currentRow()
        if not row > -1:
            return
        item = self.variable_list.currentItem()
        self.variable_list.insertItem(
            row + (-1 if self.sender() == self.variable_up else 1),
            self.variable_list.takeItem(row)
        )
        self.variable_list.setCurrentItem(item)
