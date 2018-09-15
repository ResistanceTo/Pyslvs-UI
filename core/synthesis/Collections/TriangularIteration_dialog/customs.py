# -*- coding: utf-8 -*-

"""The option dialog to set
the custom joints and the multiple joints.
"""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from core.QtModules import pyqtSlot, Qt, QDialog
import core.synthesis.Collections.TriangularIteration as TrIt
from .Ui_customs import Ui_Dialog


class CustomsDialog(QDialog, Ui_Dialog):
    
    """Option dialog.
    
    name: str = 'P1', 'P2', ...
    num: int = 1, 2, ...
    
    Settings will be edited in each operation.
    """
    
    def __init__(self, parent: 'TrIt.TriangularIterationWidget'):
        """Add data and widget references from parent."""
        super(CustomsDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        self.cus = parent.PreviewWindow.cus
        self.same = parent.PreviewWindow.same
        self.pos = parent.PreviewWindow.pos
        self.status = parent.PreviewWindow.status
        self.joint_combobox = parent.joint_name
        
        for row in range(parent.grounded_list.count()):
            self.link_choose.addItem(parent.grounded_list.item(row).text())
        for name, link in self.cus.items():
            self.custom_list.addItem(f"{name} -> {link}")
        self.__reloadQuoteChoose()
        self.quote_choose.setCurrentIndex(0)
        for s, qs in self.same.items():
            self.multiple_list.addItem(f"P{s} -> P{qs}")
    
    def __reloadQuoteChoose(self):
        """Reload joints from 'pos' dict."""
        s_old = self.quote_choose.currentText()
        self.quote_choose.clear()
        for i in self.pos:
            if i not in self.same:
                self.quote_choose.addItem(f'P{i}')
        self.quote_choose.setCurrentIndex(self.quote_choose.findText(s_old))
    
    @pyqtSlot(name='on_add_button_clicked')
    def __addCus(self):
        """Add a custom joint by dependents."""
        row = self.link_choose.currentIndex()
        if not row > -1:
            return
        try:
            new_num = max(int(c.replace('P', '')) for c in self.cus)
        except ValueError:
            new_num = max(self.pos)
        new_num += 1
        new_name = f'P{new_num}'
        self.cus[new_name] = row
        self.pos[new_num] = (0., 0.)
        self.status[new_num] = False
        self.custom_list.addItem(f"{new_name} -> {self.link_choose.itemText(row)}")
        self.joint_combobox.addItem(new_name)
    
    @pyqtSlot(name='on_delete_button_clicked')
    def __deleteCus(self):
        """Remove a custom joint."""
        row = self.custom_list.currentRow()
        if not row > -1:
            return
        name = self.custom_list.item(row).text().split(" -> ")[0]
        num = int(name.replace('P', ''))
        self.cus.pop(name)
        self.pos.pop(num)
        self.status.pop(num)
        self.custom_list.takeItem(row)
        self.joint_combobox.removeItem(num)
    
    @pyqtSlot(str, name='on_quote_choose_currentIndexChanged')
    def __setQuote(self, s: str):
        """Update the joint symbols when switch quote."""
        self.quote_link_choose.clear()
        if not s:
            return
        for row in range(self.link_choose.count()):
            link_text = self.link_choose.itemText(row)
            if s in link_text.replace('(', '').replace(')', '').split(", "):
                self.quote_link_choose.addItem(link_text)
    
    @pyqtSlot(str, name='on_quote_link_choose_currentIndexChanged')
    def __setQuoteLink(self, s: str):
        """Update the joint symbols when switch quote link."""
        self.joint_choose.clear()
        if not s:
            return
        for joint in s.replace('(', '').replace(')', '').split(", "):
            if joint == self.quote_choose.currentText():
                continue
            if int(joint.replace('P', '')) in self.same:
                continue
            self.joint_choose.addItem(joint)
    
    @pyqtSlot(name='on_add_mj_button_clicked')
    def __addMultiJoint(self):
        """Add a multiple joint by dependents."""
        s = self.joint_choose.currentText()
        if not s:
            return
        joint = int(s.replace('P', ''))
        qs = self.quote_choose.currentText()
        quote = int(qs.replace('P', ''))
        self.same[joint] = quote
        self.multiple_list.addItem(f"P{s} -> P{qs}")
        self.__reloadQuoteChoose()
    
    @pyqtSlot(name='on_delete_mj_button_clicked')
    def __deleteMultiJoint(self):
        """Remove a multiple joint."""
        row = self.multiple_list.currentRow()
        if not row > -1:
            return
        name = self.multiple_list.item(row).text().split(" -> ")[0]
        joint = int(name.replace('P', ''))
        self.same.pop(joint)
        self.multiple_list.takeItem(row)
        self.__reloadQuoteChoose()
