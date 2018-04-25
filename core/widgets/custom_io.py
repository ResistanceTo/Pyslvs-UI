# -*- coding: utf-8 -*-

"""This module contain the functions that main window needed."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    Tuple,
    List,
    Dict,
)
from core.QtModules import (
    Qt,
    pyqtSlot,
    QApplication,
    QMessageBox,
    QDesktopServices,
    QUrl,
    QInputDialog,
    QFileInfo,
    QFileDialog,
    QProgressDialog,
)
from core.info import PyslvsAbout, check_update
from core.io import (
    Script_Dialog,
    PMKSArgsTransformer,
    PMKS_parser,
    AddTable,
    EditPointTable,
    slvs2D,
    dxfSketch,
    Qt_images,
    from_parenthesis,
)


class IOFunc:
    
    """A class contain IO functions."""
    
    def workbookNoSave(self):
        """Workbook not saved signal."""
        self.FileWidget.changed = True
        not_yet_saved = " (not yet saved)"
        self.setWindowTitle(
            self.windowTitle().replace(not_yet_saved, '') +
            not_yet_saved
        )
    
    def workbookSaved(self):
        """Workbook saved signal."""
        self.FileWidget.changed = False
        self.on_windowTitle_fullpath_clicked()
    
    @pyqtSlot()
    def on_windowTitle_fullpath_clicked(self):
        """Set the option 'window title will show the fullpath'."""
        file_name = self.FileWidget.file_name
        self.setWindowTitle("Pyslvs - {}".format(
            file_name.absoluteFilePath()
            if self.windowTitle_fullpath.isChecked()
            else file_name.fileName()
        ) + (" (not yet saved)" if self.FileWidget.changed else ''))
    
    @pyqtSlot()
    def on_action_Get_Help_triggered(self):
        """Open website: mde.tw"""
        self.__openURL("http://mde.tw")
    
    @pyqtSlot()
    def on_action_Pyslvs_com_triggered(self):
        """Open website: pyslvs.com"""
        self.__openURL("http://www.pyslvs.com/blog/index.html")
    
    @pyqtSlot()
    def on_action_github_repository_triggered(self):
        """Open website: Github repository."""
        self.__openURL("https://github.com/KmolYuan/Pyslvs-PyQt5")
    
    @pyqtSlot()
    def on_action_About_Pyslvs_triggered(self):
        """Open Pyslvs about."""
        about = PyslvsAbout(self)
        about.show()
    
    @pyqtSlot()
    def on_action_About_Qt_triggered(self):
        """Open Qt about."""
        QMessageBox.aboutQt(self)
    
    def __openURL(self, url: str):
        """Use to open link."""
        QDesktopServices.openUrl(QUrl(url))
    
    @pyqtSlot()
    def on_action_Console_triggered(self):
        """Open GUI console."""
        self.OptionTab.setCurrentIndex(2)
        self.History_tab.setCurrentIndex(1)
    
    @pyqtSlot()
    def on_action_Example_triggered(self):
        """Load examples from 'FileWidget'.
        Return true if successed.
        """
        if self.FileWidget.loadExample():
            self.DynamicCanvasView.zoomToFit()
    
    @pyqtSlot()
    def on_action_Import_Example_triggered(self):
        """Import a example and merge it to canvas."""
        self.FileWidget.loadExample(isImport=True)
    
    @pyqtSlot()
    def on_action_New_Workbook_triggered(self):
        """Create (Clean) a new workbook."""
        if self.checkFileChanged():
            return
        self.clear()
        self.FileWidget.reset()
        self.FileWidget.closeDatabase()
        print("Created a new workbook.")
    
    def clear(self):
        """Clear to create commit stage."""
        self.mechanism_storage_name_tag.clear()
        self.mechanism_storage.clear()
        self.CollectionTabPage.clear()
        self.NumberAndTypeSynthesis.clear()
        self.InputsWidget.clear()
        self.DimensionalSynthesis.clear()
        self.Entities_Point.clear()
        self.Entities_Link.clear()
        self.Entities_Expr.clear()
        self.resolve()
    
    @pyqtSlot()
    def on_action_Import_PMKS_server_triggered(self):
        """Load PMKS URL and turn it to expression."""
        URL, ok = QInputDialog.getText(self,
            "PMKS URL input",
            "Please input link string:"
        )
        if not ok:
            return
        if not URL:
            QMessageBox.warning(self,
                "Loading failed",
                "Your link is in an incorrect format."
            )
            return
        try:
            for s in URL.split('?')[-1].split('&'):
                if 'mech=' in s:
                    expr = s.replace('mech=', '').split('|')
                    break
            textList = [s for s in expr if s not in ('', " ", '\n')]
            expression = []
            while textList:
                item = textList.pop(0).split(',')[:-1]
                for i, e in enumerate(reversed(item)):
                    if e in ['R', 'P', 'RP']:
                        t = -(i+1)
                        break
                links = item[:t]
                item = item[t:]
                expression.append("J[{}, P[{}], L[{}]]".format(
                    "{}:{}".format(item[0], item[-1]) if item[0]!='R' else 'R',
                    ", ".join((item[1], item[2])),
                    ", ".join(links)
                ))
            expression = "M[{}]".format(", ".join(expression))
        except:
            QMessageBox.warning(self,
                "Loading failed",
                "Your link is in an incorrect format."
            )
        else:
            self.parseExpression(expression)
    
    def parseExpression(self, expr):
        """Parse expression."""
        try:
            args_list = PMKSArgsTransformer().transform(PMKS_parser.parse(expr))
        except Exception as e:
            print(e)
            QMessageBox.warning(self,
                "Loading failed",
                "Your expression is in an incorrect format."
            )
        else:
            for args in args_list:
                linkNames = tuple(
                    vlink.name for vlink in self.Entities_Link.data()
                )
                links = args[0].split(',')
                for linkName in links:
                    #If link name not exist.
                    if linkName not in linkNames:
                        self.addLink(linkName, 'Blue')
                rowCount = self.Entities_Point.rowCount()
                self.CommandStack.beginMacro("Add {{Point{}}}".format(rowCount))
                self.CommandStack.push(AddTable(self.Entities_Point))
                self.CommandStack.push(EditPointTable(
                    rowCount,
                    self.Entities_Point,
                    self.Entities_Link,
                    args
                ))
                self.CommandStack.endMacro()
    
    def addEmptyLinkGroup(self, linkcolor: Dict[str, str]):
        """Use to add empty link when loading database."""
        for name, color in linkcolor.items():
            if name != 'ground':
                self.addLink(name, color)
    
    @pyqtSlot()
    def on_action_Load_Workbook_triggered(self):
        """Load workbook."""
        if self.checkFileChanged():
            return
        file_name = self.inputFrom(
            "Workbook database",
            ["Pyslvs workbook (*.pyslvs)"]
        )
        if not file_name:
            return
        self.FileWidget.read(file_name)
        self.DynamicCanvasView.zoomToFit()
    
    @pyqtSlot()
    def on_action_Import_Workbook_triggered(self):
        """Import from workbook."""
        if self.checkFileChanged():
            return
        file_name = self.inputFrom(
            "Workbook database (Import)",
            ["Pyslvs workbook (*.pyslvs)"]
        )
        if not file_name:
            return
        self.FileWidget.importMechanism(file_name)
    
    @pyqtSlot()
    def on_action_Save_triggered(self, isBranch=False):
        """Save action."""
        file_name = self.FileWidget.file_name.absoluteFilePath()
        if self.FileWidget.file_name.suffix()=='pyslvs':
            self.FileWidget.save(file_name, isBranch)
        else:
            self.on_action_Save_as_triggered(isBranch)
    
    @pyqtSlot()
    def on_action_Save_as_triggered(self, isBranch=False):
        """Save as action."""
        file_name = self.outputTo("workbook", ["Pyslvs workbook (*.pyslvs)"])
        if file_name:
            self.FileWidget.save(file_name, isBranch)
            self.saveReplyBox("Workbook", file_name)
    
    @pyqtSlot()
    def on_action_Save_branch_triggered(self):
        """Save as new branch action."""
        self.on_action_Save_triggered(True)
    
    def __v_to_slvs(self) -> Tuple[Tuple[int, int]]:
        """Solvespace edges."""
        for vlink in self.Entities_Link.data():
            if vlink.name=='ground':
                continue
            for i, p in enumerate(vlink.points):
                if i==0:
                    continue
                yield (vlink.points[0], p)
                if i>1:
                    yield (vlink.points[i-1], p)
    
    @pyqtSlot()
    def on_action_Output_to_Solvespace_triggered(self):
        """Solvespace 2d save function."""
        file_name = self.outputTo(
            "Solvespace sketch",
            ["Solvespace module(*.slvs)"]
        )
        if not file_name:
            return
        slvs2D(
            self.Entities_Point.data(),
            self.Entities_Link.data(),
            self.__v_to_slvs,
            file_name
        )
        self.saveReplyBox("Solvespace sketch", file_name)
    
    @pyqtSlot()
    def on_action_Output_to_DXF_triggered(self):
        """DXF 2d save function."""
        file_name = self.outputTo(
            "Drawing Exchange Format",
            ["Drawing Exchange Format(*.dxf)"]
        )
        if not file_name:
            return
        dxfSketch(
            self.Entities_Point.data(),
            self.Entities_Link.data(),
            self.__v_to_slvs,
            file_name
        )
        self.saveReplyBox("Drawing Exchange Format", file_name)
    
    @pyqtSlot()
    def on_action_Output_to_Picture_triggered(self):
        """Picture save function."""
        file_name = self.outputTo("picture", Qt_images)
        if not file_name:
            return
        pixmap = self.DynamicCanvasView.grab()
        pixmap.save(file_name, format=QFileInfo(file_name).suffix())
        self.saveReplyBox("Picture", file_name)
    
    def outputTo(self, formatName: str, formatChoose: List[str]):
        """Simple to support mutiple format."""
        suffix0 = from_parenthesis(formatChoose[0], '(', ')').split('*')[-1]
        file_name, suffix = QFileDialog.getSaveFileName(
            self,
            "Save to {}...".format(formatName),
            self.env+'/'+self.FileWidget.file_name.baseName()+suffix0,
            ';;'.join(formatChoose)
        )
        if file_name:
            suffix = from_parenthesis(suffix, '(', ')').split('*')[-1]
            print("Format: {}".format(suffix))
            if QFileInfo(file_name).suffix()!=suffix[1:]:
                file_name += suffix
            self.setLocate(QFileInfo(file_name).absolutePath())
        return file_name
    
    def saveReplyBox(self, title: str, file_name: str):
        """Show message when successfully saved."""
        size = QFileInfo(file_name).size()
        print("Size: {}".format(
            "{} MB".format(round(size/1024/1024, 2))
            if size/1024//1024 else "{} KB".format(round(size/1024, 2))
        ))
        QMessageBox.information(self,
            title,
            "Successfully converted:\n{}".format(file_name)
        )
        print("Successful saved: [\"{}\"]".format(file_name))
    
    def inputFrom(self,
        formatName: str,
        formatChoose: List[str],
        multiple=False
    ):
        """Get file name(s)."""
        args = (
            "Open {} file{}...".format(formatName, 's' if multiple else ''),
            self.env,
            ';;'.join(formatChoose)
        )
        if multiple:
            file_name_s, suffix = QFileDialog.getOpenFileNames(self, *args)
        else:
            file_name_s, suffix = QFileDialog.getOpenFileName(self, *args)
        if file_name_s:
            suffix = from_parenthesis(suffix, '(', ')').split('*')[-1]
            print("Format: {}".format(suffix))
            if type(file_name_s)==str:
                self.setLocate(QFileInfo(file_name_s).absolutePath())
            else:
                self.setLocate(QFileInfo(file_name_s[0]).absolutePath())
        return file_name_s
    
    @pyqtSlot()
    def on_action_Output_to_PMKS_triggered(self):
        """Output to PMKS as URL."""
        url = "http://designengrlab.github.io/PMKS/pmks.html?mech="
        urlTable = []
        for row in range(self.Entities_Point.rowCount()):
            TypeAndAngle = self.Entities_Point.item(row, 2).text().split(':')
            pointData = [
                self.Entities_Point.item(row, 1).text(),
                TypeAndAngle[0],
                self.Entities_Point.item(row, 4).text(),
                self.Entities_Point.item(row, 5).text(),
            ]
            if len(TypeAndAngle)==2:
                pointData.append(TypeAndAngle[1])
            pointData.append('tfff')
            urlTable.append(','.join(pointData))
        url += '|'.join(urlTable)+'|'
        text = '\n'.join([
            "Copy and past this link to web browser:\n",
            url + '\n',
            "If you have installed Microsoft Silverlight in " +
            "Internet Explorer as default browser, " +
            "just click \"Open\" button to open it in PMKS website."
        ])
        reply = QMessageBox.information(self,
            "PMKS web server",
            text,
            (QMessageBox.Save | QMessageBox.Open | QMessageBox.Close),
            QMessageBox.Save
        )
        if reply == QMessageBox.Open:
            self.__openURL(url)
        elif reply == QMessageBox.Save:
            QApplication.clipboard().setText(url)
    
    @pyqtSlot()
    def on_action_Output_to_Picture_clipboard_triggered(self):
        """Capture the canvas image to clipboard."""
        QApplication.clipboard().setPixmap(self.DynamicCanvasView.grab())
        QMessageBox.information(self,
            "Captured!",
            "Canvas widget picture is copy to clipboard."
        )
    
    @pyqtSlot()
    def on_action_Output_to_Expression_triggered(self):
        """Output as expression."""
        data = self.Entities_Point.data()
        expr = "M[{}]".format(", ".join(vpoint.expr for vpoint in data))
        text = (
            "You can copy the expression and import to another workbook:" +
            "\n\n{}\n\nClick the save button to copy it.".format(expr)
        )
        reply = QMessageBox.question(self,
            "Pyslvs Expression",
            text,
            (QMessageBox.Save | QMessageBox.Close),
            QMessageBox.Save
        )
        if reply == QMessageBox.Save:
            QApplication.clipboard().setText(expr)
    
    @pyqtSlot()
    def on_action_See_Python_Scripts_triggered(self):
        """Output to Python script for Jupyter notebook."""
        dlg = Script_Dialog(
            self.Entities_Point.data(),
            self.Entities_Link.data(),
            self
        )
        dlg.show()
    
    @pyqtSlot()
    def on_action_Check_update_triggered(self):
        """Check for update."""
        progdlg = QProgressDialog("Checking update ...", "Cancel", 0, 3, self)
        progdlg.setAttribute(Qt.WA_DeleteOnClose, True)
        progdlg.setWindowTitle("Check for update")
        progdlg.resize(400, progdlg.height())
        progdlg.setModal(True)
        progdlg.show()
        url = check_update(progdlg)
        if not url:
            QMessageBox.information(self,
                "Pyslvs is up to date",
                "You are using the latest version of Pyslvs."
            )
            return
        reply = QMessageBox.question(
            self,
            "Pyslvs has update",
            "Do you want to get it from Github?",
            (QMessageBox.Ok | QMessageBox.Cancel),
            QMessageBox.Ok
        )
        if reply == QMessageBox.Ok:
            self.__openURL(url)