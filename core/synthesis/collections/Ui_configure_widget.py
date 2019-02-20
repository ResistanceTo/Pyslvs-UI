# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/synthesis/collections/configure_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from core.QtModules import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 422)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/configure.png"), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_collection_button = QPushButton(Form)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/structure.png"), QIcon.Normal, QIcon.Off)
        self.add_collection_button.setIcon(icon1)
        self.add_collection_button.setObjectName("add_collection_button")
        self.horizontalLayout_4.addWidget(self.add_collection_button)
        self.line_5 = QFrame(Form)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.load_button = QPushButton(Form)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icons/collections.png"), QIcon.Normal, QIcon.Off)
        self.load_button.setIcon(icon2)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_4.addWidget(self.load_button)
        self.clear_button = QPushButton(Form)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icons/clean.png"), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon3)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_4.addWidget(self.clear_button)
        self.save_button = QPushButton(Form)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/save_file.png"), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon4)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_4.addWidget(self.save_button)
        self.clipboard_button = QPushButton(Form)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/icons/copy.png"), QIcon.Normal, QIcon.Off)
        self.clipboard_button.setIcon(icon5)
        self.clipboard_button.setObjectName("clipboard_button")
        self.horizontalLayout_4.addWidget(self.clipboard_button)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line = QFrame(Form)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.main_splitter = QSplitter(Form)
        self.main_splitter.setOrientation(Qt.Vertical)
        self.main_splitter.setObjectName("main_splitter")
        self.verticalLayoutWidget = QWidget(self.main_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.joint_name = QComboBox(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joint_name.sizePolicy().hasHeightForWidth())
        self.joint_name.setSizePolicy(sizePolicy)
        self.joint_name.setObjectName("joint_name")
        self.horizontalLayout_2.addWidget(self.joint_name)
        self.add_customization = QPushButton(self.verticalLayoutWidget)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(":/icons/properties.png"), QIcon.Normal, QIcon.Off)
        self.add_customization.setIcon(icon6)
        self.add_customization.setObjectName("add_customization")
        self.horizontalLayout_2.addWidget(self.add_customization)
        self.main_layout.addLayout(self.horizontalLayout_2)
        self.layoutWidget = QWidget(self.main_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.target_label = QLabel(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target_label.sizePolicy().hasHeightForWidth())
        self.target_label.setSizePolicy(sizePolicy)
        self.target_label.setObjectName("target_label")
        self.horizontalLayout_7.addWidget(self.target_label)
        self.target_button = QPushButton(self.layoutWidget)
        self.target_button.setObjectName("target_button")
        self.horizontalLayout_7.addWidget(self.target_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.target_list = QListWidget(self.layoutWidget)
        self.target_list.setObjectName("target_list")
        self.verticalLayout_3.addWidget(self.target_list)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.driver_base = QComboBox(self.layoutWidget)
        self.driver_base.setObjectName("driver_base")
        self.horizontalLayout_5.addWidget(self.driver_base)
        self.driver_arrow_label = QLabel(self.layoutWidget)
        self.driver_arrow_label.setObjectName("driver_arrow_label")
        self.horizontalLayout_5.addWidget(self.driver_arrow_label)
        self.driver_rotator = QComboBox(self.layoutWidget)
        self.driver_rotator.setObjectName("driver_rotator")
        self.horizontalLayout_5.addWidget(self.driver_rotator)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.driver_add = QPushButton(self.layoutWidget)
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(":/icons/motor.png"), QIcon.Normal, QIcon.Off)
        self.driver_add.setIcon(icon7)
        self.driver_add.setObjectName("driver_add")
        self.verticalLayout_2.addWidget(self.driver_add)
        self.driver_label = QLabel(self.layoutWidget)
        self.driver_label.setObjectName("driver_label")
        self.verticalLayout_2.addWidget(self.driver_label)
        self.driver_list = QListWidget(self.layoutWidget)
        self.driver_list.setObjectName("driver_list")
        self.verticalLayout_2.addWidget(self.driver_list)
        self.driver_del = QPushButton(self.layoutWidget)
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(":/icons/delete.png"), QIcon.Normal, QIcon.Off)
        self.driver_del.setIcon(icon8)
        self.driver_del.setObjectName("driver_del")
        self.verticalLayout_2.addWidget(self.driver_del)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.grounded_label = QLabel(self.layoutWidget)
        self.grounded_label.setObjectName("grounded_label")
        self.verticalLayout_15.addWidget(self.grounded_label)
        self.grounded_list = QListWidget(self.layoutWidget)
        self.grounded_list.setObjectName("grounded_list")
        self.verticalLayout_15.addWidget(self.grounded_list)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.main_splitter)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.expression_label = QLabel(Form)
        self.expression_label.setObjectName("expression_label")
        self.verticalLayout.addWidget(self.expression_label)
        self.expr_show = QLineEdit(Form)
        self.expr_show.setReadOnly(True)
        self.expr_show.setObjectName("expr_show")
        self.verticalLayout.addWidget(self.expr_show)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.main_splitter.raise_()
        self.line.raise_()

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_collection_button.setStatusTip(_translate("Form", "Turn this structure diagram back to structure collections."))
        self.load_button.setStatusTip(_translate("Form", "Triangular iteration data and common structure data collections."))
        self.clear_button.setStatusTip(_translate("Form", "Create a new iteration profile."))
        self.save_button.setStatusTip(_translate("Form", "Save this iteration profile to data collections."))
        self.clipboard_button.setStatusTip(_translate("Form", "Save this iteration profile to clipboard as a string."))
        self.add_customization.setStatusTip(_translate("Form", "Customize joints and multiple joints option interface."))
        self.add_customization.setText(_translate("Form", "Properties of Joints"))
        self.target_button.setText(_translate("Form", "Targets"))
        self.target_list.setStatusTip(_translate("Form", "Target points will match as the target path of dimensional synthesis."))
        self.driver_arrow_label.setText(_translate("Form", "->"))
        self.driver_label.setText(_translate("Form", "Inputs:"))
        self.driver_list.setStatusTip(_translate("Form", "These joints will setup an revolute input. The number of them as same as DOF."))
        self.grounded_label.setText(_translate("Form", "Gounded:"))
        self.grounded_list.setStatusTip(_translate("Form", "Set a link as the ground. Existing solutions will be reset."))
        self.expression_label.setText(_translate("Form", "Expression:"))
        self.expr_show.setStatusTip(_translate("Form", "Expression of the mechanism"))


import icons_rc
