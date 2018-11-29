# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'structure_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 562)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/structure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_by_files_button = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/loadfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_by_files_button.setIcon(icon1)
        self.add_by_files_button.setObjectName("add_by_files_button")
        self.horizontalLayout.addWidget(self.add_by_files_button)
        self.add_by_edges_button = QtWidgets.QPushButton(Form)
        self.add_by_edges_button.setIcon(icon)
        self.add_by_edges_button.setObjectName("add_by_edges_button")
        self.horizontalLayout.addWidget(self.add_by_edges_button)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.save_atlas = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_atlas.setIcon(icon2)
        self.save_atlas.setObjectName("save_atlas")
        self.horizontalLayout.addWidget(self.save_atlas)
        self.save_edges = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/save_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_edges.setIcon(icon3)
        self.save_edges.setObjectName("save_edges")
        self.horizontalLayout.addWidget(self.save_edges)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clear_button = QtWidgets.QPushButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon4)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.delete_button = QtWidgets.QPushButton(Form)
        self.delete_button.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon5)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.collection_list = QtWidgets.QListWidget(self.splitter)
        self.collection_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.collection_list.setIconSize(QtCore.QSize(100, 100))
        self.collection_list.setMovement(QtWidgets.QListView.Static)
        self.collection_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.collection_list.setViewMode(QtWidgets.QListView.IconMode)
        self.collection_list.setUniformItemSizes(True)
        self.collection_list.setObjectName("collection_list")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.graph_engine_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout_7.addWidget(self.graph_engine_text)
        self.graph_engine = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout_7.addWidget(self.graph_engine)
        self.reload_atlas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reload_atlas.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/data_update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_atlas.setIcon(icon6)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout_7.addWidget(self.reload_atlas)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.graph_link_as_node = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.graph_link_as_node.setObjectName("graph_link_as_node")
        self.horizontalLayout_7.addWidget(self.graph_link_as_node)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selection_window = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.selection_window.setMinimumSize(QtCore.QSize(210, 230))
        self.selection_window.setMaximumSize(QtCore.QSize(210, 230))
        self.selection_window.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.selection_window.setIconSize(QtCore.QSize(200, 200))
        self.selection_window.setMovement(QtWidgets.QListView.Static)
        self.selection_window.setViewMode(QtWidgets.QListView.IconMode)
        self.selection_window.setObjectName("selection_window")
        self.horizontalLayout_2.addWidget(self.selection_window)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edges_text = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edges_text.setReadOnly(True)
        self.edges_text.setObjectName("edges_text")
        self.horizontalLayout_3.addWidget(self.edges_text)
        self.expr_copy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expr_copy.setIcon(icon7)
        self.expr_copy.setObjectName("expr_copy")
        self.horizontalLayout_3.addWidget(self.expr_copy)
        self.triangle_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.triangle_button.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/ti.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.triangle_button.setIcon(icon8)
        self.triangle_button.setObjectName("triangle_button")
        self.horizontalLayout_3.addWidget(self.triangle_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nl_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nl_text.setObjectName("nl_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nl_text)
        self.nl_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nl_label.setObjectName("nl_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nl_label)
        self.nj_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nj_text.setObjectName("nj_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nj_text)
        self.nj_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nj_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nj_label.setObjectName("nj_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nj_label)
        self.dof_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dof_text.setObjectName("dof_text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dof_text)
        self.dof_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dof_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dof_label.setObjectName("dof_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dof_label)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.link_assortments_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.link_assortments_text.setObjectName("link_assortments_text")
        self.verticalLayout_4.addWidget(self.link_assortments_text)
        self.link_assortments_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.link_assortments_label.setObjectName("link_assortments_label")
        self.verticalLayout_4.addWidget(self.link_assortments_label)
        self.contracted_link_assortments_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.contracted_link_assortments_text.setObjectName("contracted_link_assortments_text")
        self.verticalLayout_4.addWidget(self.contracted_link_assortments_text)
        self.contracted_link_assortments_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.contracted_link_assortments_label.setObjectName("contracted_link_assortments_label")
        self.verticalLayout_4.addWidget(self.contracted_link_assortments_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.grounded_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.grounded_button.setEnabled(False)
        self.grounded_button.setIcon(icon)
        self.grounded_button.setObjectName("grounded_button")
        self.horizontalLayout_5.addWidget(self.grounded_button)
        self.grounded_merge = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.grounded_merge.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grounded_merge.setIcon(icon9)
        self.grounded_merge.setObjectName("grounded_merge")
        self.horizontalLayout_5.addWidget(self.grounded_merge)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.grounded_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.grounded_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.grounded_list.setIconSize(QtCore.QSize(150, 150))
        self.grounded_list.setMovement(QtWidgets.QListView.Static)
        self.grounded_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.grounded_list.setViewMode(QtWidgets.QListView.IconMode)
        self.grounded_list.setUniformItemSizes(True)
        self.grounded_list.setObjectName("grounded_list")
        self.horizontalLayout_4.addWidget(self.grounded_list)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.graph_engine.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_by_files_button.setStatusTip(_translate("Form", "Add the chain by edge expression from text files."))
        self.add_by_edges_button.setStatusTip(_translate("Form", "Add the chain by edge expression."))
        self.save_atlas.setStatusTip(_translate("Form", "Save the atlas to image file."))
        self.save_edges.setStatusTip(_translate("Form", "Save the edges of atlas to text file."))
        self.clear_button.setStatusTip(_translate("Form", "Delete all of structures."))
        self.delete_button.setStatusTip(_translate("Form", "Delete this structure."))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_engine.setStatusTip(_translate("Form", "Layout engine from NetworkX."))
        self.reload_atlas.setToolTip(_translate("Form", "Re-layout"))
        self.graph_link_as_node.setText(_translate("Form", "Link as node"))
        self.expr_copy.setStatusTip(_translate("Form", "Copy expression."))
        self.triangle_button.setStatusTip(_translate("Form", "Use trangular formula to do dimentional synthesis."))
        self.nl_text.setText(_translate("Form", "Number of links:"))
        self.nl_label.setText(_translate("Form", "0"))
        self.nj_text.setText(_translate("Form", "Number of joints:"))
        self.nj_label.setText(_translate("Form", "0"))
        self.dof_text.setText(_translate("Form", "Degrees of freedom:"))
        self.dof_label.setText(_translate("Form", "0"))
        self.link_assortments_text.setText(_translate("Form", "Link assortments:"))
        self.contracted_link_assortments_text.setText(_translate("Form", "Contracted link assortments:"))
        self.grounded_button.setStatusTip(_translate("Form", "Re-layout the grounded chains."))
        self.grounded_button.setText(_translate("Form", "Ground"))
        self.grounded_merge.setStatusTip(_translate("Form", "Merge the specified chain to canvas with current layout."))
        self.grounded_merge.setText(_translate("Form", "Merge"))

import icons_rc
