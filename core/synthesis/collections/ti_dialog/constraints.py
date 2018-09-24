# -*- coding: utf-8 -*-

"""The option dialog to set the constraint dependent."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    Tuple,
    Iterator,
    Union,
)
from networkx import Graph
from core.QtModules import (
    pyqtSlot,
    Qt,
    QDialog,
    QListWidget,
    QListWidgetItem,
)
from core.synthesis.collections import triangular_iteration_widget as ti
from core.graphics import edges_view
from .Ui_constraints import Ui_Dialog


def list_items(
    widget: QListWidget,
    return_row: bool = False
) -> Iterator[Union[Tuple[int, QListWidgetItem], QListWidgetItem]]:
    """A generator to get items from list widget."""
    for row in range(widget.count()):
        if return_row:
            yield row, widget.item(row)
        else:
            yield widget.item(row)


def _get_list(item: QListWidget) -> Iterator[str]:
    """A generator to get symbols from list widget."""
    if not item:
        return []
    for e in item.text().split(", "):
        yield e


def _four_bar_loops(graph: Graph) -> Iterator[Tuple[int, int, int, int]]:
    """A generator to find out the four bar loops."""
    result = set()
    vertexes = {v: k for k, v in edges_view(graph)}
    
    def loop_set(n: int, n1: int, n2: int, n3: int) -> Tuple[int, int, int, int]:
        """Return a loop set."""
        return (
            vertexes[tuple(sorted((n, n1)))],
            vertexes[tuple(sorted((n1, n2)))],
            vertexes[tuple(sorted((n2, n3)))],
            vertexes[tuple(sorted((n, n3)))],
        )
    
    for node in graph.nodes:
        if node in result:
            continue
        nb1s = graph.neighbors(node)
        # node not in nb1s
        for nb1 in nb1s:
            if nb1 in result:
                continue
            nb2s = graph.neighbors(nb1)
            # node can not in nb2s
            for nb2 in nb2s:
                if (nb2 == node) or (nb2 in result):
                    continue
                nb3s = graph.neighbors(nb2)
                # node can not in nb3s
                for nb3 in nb3s:
                    if (nb3 in (node, nb1)) or (nb3 in result):
                        continue
                    if node in graph.neighbors(nb3):
                        loop = [node, nb1, nb2, nb3]
                        result.update(loop)
                        yield loop_set(*loop)


class ConstraintsDialog(QDialog, Ui_Dialog):
    
    """Option dialog.
    
    Only edit the settings after closed.
    """
    
    def __init__(self, parent: 'ti.TriangularIterationWidget'):
        """Load constraints option from parent."""
        super(ConstraintsDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        cl = tuple(
            set(_get_list(item)) for item in list_items(parent.constraint_list)
        )
        for chain in _four_bar_loops(parent.PreviewWindow.G):
            chain = sorted(chain)
            chain_ = []
            for n in chain:
                if n in parent.PreviewWindow.same:
                    n = parent.PreviewWindow.same[n]
                chain_.append(f'P{n}')
            if set(chain_) not in cl:
                self.loops_list.addItem(", ".join(chain_))
        for item in list_items(parent.constraint_list):
            self.main_list.addItem(item.text())
    
    @pyqtSlot(int, name='on_loops_list_currentRowChanged')
    def __setLoops(self, row: int):
        """Update the joints of loop."""
        if not row > -1:
            return
        self.sorting_list.clear()
        for point in _get_list(self.loops_list.item(row)):
            self.sorting_list.addItem(point)
    
    @pyqtSlot(name='on_main_add_clicked')
    def __addCons(self):
        """Add the constraint dependent."""
        if not self.sorting_list.count():
            return
        self.main_list.addItem(", ".join(
            item.text() for item in list_items(self.sorting_list)
        ))
        self.sorting_list.clear()
        self.loops_list.takeItem(self.loops_list.currentRow())
    
    @pyqtSlot(name='on_sorting_add_clicked')
    def __removeCons(self):
        """Remove back to sorting list."""
        row = self.main_list.currentRow()
        if row > -1:
            self.loops_list.addItem(self.main_list.takeItem(row))