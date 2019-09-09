# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/io/preference.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from core.QtModules import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(818, 664)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settings_ui_groupbox = QtWidgets.QGroupBox(Dialog)
        self.settings_ui_groupbox.setObjectName("settings_ui_groupbox")
        self.formLayout = QtWidgets.QFormLayout(self.settings_ui_groupbox)
        self.formLayout.setObjectName("formLayout")
        self.linewidth_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.linewidth_label.setObjectName("linewidth_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.linewidth_label)
        self.line_width_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.line_width_option.setMinimum(1)
        self.line_width_option.setMaximum(10)
        self.line_width_option.setDisplayIntegerBase(10)
        self.line_width_option.setObjectName("line_width_option")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_width_option)
        self.fontsize_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.fontsize_label.setObjectName("fontsize_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fontsize_label)
        self.font_size_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.font_size_option.setMinimum(1)
        self.font_size_option.setMaximum(30)
        self.font_size_option.setSingleStep(2)
        self.font_size_option.setObjectName("font_size_option")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.font_size_option)
        self.pathwidth_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.pathwidth_label.setObjectName("pathwidth_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pathwidth_label)
        self.path_width_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.path_width_option.setMinimum(1)
        self.path_width_option.setMaximum(5)
        self.path_width_option.setObjectName("path_width_option")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.path_width_option)
        self.scalefactor_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.scalefactor_label.setObjectName("scalefactor_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.scalefactor_label)
        self.scalefactor_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.scalefactor_option.setMinimum(5)
        self.scalefactor_option.setMaximum(100)
        self.scalefactor_option.setSingleStep(5)
        self.scalefactor_option.setObjectName("scalefactor_option")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.scalefactor_option)
        self.selectionradius_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.selectionradius_label.setObjectName("selectionradius_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.selectionradius_label)
        self.selection_radius_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.selection_radius_option.setMinimum(3)
        self.selection_radius_option.setMaximum(10)
        self.selection_radius_option.setObjectName("selection_radius_option")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.selection_radius_option)
        self.linktransparency_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.linktransparency_label.setObjectName("linktransparency_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.linktransparency_label)
        self.link_trans_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.link_trans_option.setMaximum(80)
        self.link_trans_option.setSingleStep(10)
        self.link_trans_option.setObjectName("link_trans_option")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.link_trans_option)
        self.marginfactor_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.marginfactor_label.setObjectName("marginfactor_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.marginfactor_label)
        self.margin_factor_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.margin_factor_option.setMaximum(30)
        self.margin_factor_option.setSingleStep(5)
        self.margin_factor_option.setObjectName("margin_factor_option")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.margin_factor_option)
        self.jointsize_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.jointsize_label.setObjectName("jointsize_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.jointsize_label)
        self.joint_size_option = QtWidgets.QSpinBox(self.settings_ui_groupbox)
        self.joint_size_option.setMinimum(1)
        self.joint_size_option.setMaximum(100)
        self.joint_size_option.setObjectName("joint_size_option")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.joint_size_option)
        self.zoomby_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.zoomby_label.setObjectName("zoomby_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.zoomby_label)
        self.zoom_by_option = QtWidgets.QComboBox(self.settings_ui_groupbox)
        self.zoom_by_option.setObjectName("zoom_by_option")
        self.zoom_by_option.addItem("")
        self.zoom_by_option.addItem("")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.zoom_by_option)
        self.snap_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.snap_label.setObjectName("snap_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.snap_label)
        self.snap_option = QtWidgets.QDoubleSpinBox(self.settings_ui_groupbox)
        self.snap_option.setMaximum(50.0)
        self.snap_option.setObjectName("snap_option")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.snap_option)
        self.background_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.background_label.setObjectName("background_label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.background_label)
        self.background_layout = QtWidgets.QHBoxLayout()
        self.background_layout.setObjectName("background_layout")
        self.background_option = QtWidgets.QLineEdit(self.settings_ui_groupbox)
        self.background_option.setClearButtonEnabled(True)
        self.background_option.setObjectName("background_option")
        self.background_layout.addWidget(self.background_option)
        self.background_choose_dir = QtWidgets.QToolButton(self.settings_ui_groupbox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/loadfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.background_choose_dir.setIcon(icon1)
        self.background_choose_dir.setObjectName("background_choose_dir")
        self.background_layout.addWidget(self.background_choose_dir)
        self.formLayout.setLayout(11, QtWidgets.QFormLayout.FieldRole, self.background_layout)
        self.background_opacity_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.background_opacity_label.setObjectName("background_opacity_label")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.background_opacity_label)
        self.background_opacity_option = QtWidgets.QDoubleSpinBox(self.settings_ui_groupbox)
        self.background_opacity_option.setMaximum(1.0)
        self.background_opacity_option.setSingleStep(0.1)
        self.background_opacity_option.setProperty("value", 1.0)
        self.background_opacity_option.setObjectName("background_opacity_option")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.background_opacity_option)
        self.background_scale_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.background_scale_label.setObjectName("background_scale_label")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.background_scale_label)
        self.background_scale_option = QtWidgets.QDoubleSpinBox(self.settings_ui_groupbox)
        self.background_scale_option.setMinimum(0.01)
        self.background_scale_option.setMaximum(10.0)
        self.background_scale_option.setSingleStep(0.02)
        self.background_scale_option.setObjectName("background_scale_option")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.background_scale_option)
        self.background_offset_label = QtWidgets.QLabel(self.settings_ui_groupbox)
        self.background_offset_label.setObjectName("background_offset_label")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.background_offset_label)
        self.background_offset_layout = QtWidgets.QHBoxLayout()
        self.background_offset_layout.setObjectName("background_offset_layout")
        self.background_offset_x_option = QtWidgets.QDoubleSpinBox(self.settings_ui_groupbox)
        self.background_offset_x_option.setMinimum(-999999.0)
        self.background_offset_x_option.setMaximum(999999.0)
        self.background_offset_x_option.setObjectName("background_offset_x_option")
        self.background_offset_layout.addWidget(self.background_offset_x_option)
        self.background_offset_y_option = QtWidgets.QDoubleSpinBox(self.settings_ui_groupbox)
        self.background_offset_y_option.setMinimum(-999999.0)
        self.background_offset_y_option.setMaximum(999999.0)
        self.background_offset_y_option.setObjectName("background_offset_y_option")
        self.background_offset_layout.addWidget(self.background_offset_y_option)
        self.formLayout.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.background_offset_layout)
        self.horizontalLayout.addWidget(self.settings_ui_groupbox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings_kernels_groupBox = QtWidgets.QGroupBox(Dialog)
        self.settings_kernels_groupBox.setObjectName("settings_kernels_groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.settings_kernels_groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.planarsolver_label = QtWidgets.QLabel(self.settings_kernels_groupBox)
        self.planarsolver_label.setObjectName("planarsolver_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.planarsolver_label)
        self.planar_solver_option = QtWidgets.QComboBox(self.settings_kernels_groupBox)
        self.planar_solver_option.setObjectName("planar_solver_option")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.planar_solver_option)
        self.pathpreview_label = QtWidgets.QLabel(self.settings_kernels_groupBox)
        self.pathpreview_label.setObjectName("pathpreview_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pathpreview_label)
        self.path_preview_option = QtWidgets.QComboBox(self.settings_kernels_groupBox)
        self.path_preview_option.setObjectName("path_preview_option")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.path_preview_option)
        self.verticalLayout.addWidget(self.settings_kernels_groupBox)
        self.settings_history_groupbox = QtWidgets.QGroupBox(Dialog)
        self.settings_history_groupbox.setObjectName("settings_history_groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.settings_history_groupbox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.UndoLimit_label = QtWidgets.QLabel(self.settings_history_groupbox)
        self.UndoLimit_label.setObjectName("UndoLimit_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.UndoLimit_label)
        self.undo_limit_option = QtWidgets.QSpinBox(self.settings_history_groupbox)
        self.undo_limit_option.setMinimum(5)
        self.undo_limit_option.setObjectName("undo_limit_option")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.undo_limit_option)
        self.verticalLayout.addWidget(self.settings_history_groupbox)
        self.settings_misc_groupBox = QtWidgets.QGroupBox(Dialog)
        self.settings_misc_groupBox.setObjectName("settings_misc_groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.settings_misc_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.title_full_path_option = QtWidgets.QCheckBox(self.settings_misc_groupBox)
        self.title_full_path_option.setObjectName("title_full_path_option")
        self.verticalLayout_7.addWidget(self.title_full_path_option)
        self.console_error_option = QtWidgets.QCheckBox(self.settings_misc_groupBox)
        self.console_error_option.setObjectName("console_error_option")
        self.verticalLayout_7.addWidget(self.console_error_option)
        self.monochrome_option = QtWidgets.QCheckBox(self.settings_misc_groupBox)
        self.monochrome_option.setObjectName("monochrome_option")
        self.verticalLayout_7.addWidget(self.monochrome_option)
        self.dontsave_option = QtWidgets.QCheckBox(self.settings_misc_groupBox)
        self.dontsave_option.setObjectName("dontsave_option")
        self.verticalLayout_7.addWidget(self.dontsave_option)
        self.verticalLayout.addWidget(self.settings_misc_groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_2.addWidget(self.button_box)

        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preference"))
        self.settings_ui_groupbox.setTitle(_translate("Dialog", "Main canvas"))
        self.linewidth_label.setText(_translate("Dialog", "Line width"))
        self.fontsize_label.setText(_translate("Dialog", "Font size"))
        self.pathwidth_label.setText(_translate("Dialog", "Path width"))
        self.scalefactor_label.setText(_translate("Dialog", "Scale factor"))
        self.selectionradius_label.setText(_translate("Dialog", "Selection radius"))
        self.linktransparency_label.setText(_translate("Dialog", "Link transparency"))
        self.link_trans_option.setSuffix(_translate("Dialog", " %"))
        self.marginfactor_label.setText(_translate("Dialog", "Margin of \"zoom to fit\""))
        self.margin_factor_option.setSuffix(_translate("Dialog", "%"))
        self.jointsize_label.setText(_translate("Dialog", "Joint annotation size (diameter)"))
        self.zoomby_label.setText(_translate("Dialog", "Center zooming by"))
        self.zoom_by_option.setItemText(0, _translate("Dialog", "Cursor"))
        self.zoom_by_option.setItemText(1, _translate("Dialog", "Cavas center"))
        self.snap_label.setText(_translate("Dialog", "Snap the mouse when dragging"))
        self.background_label.setText(_translate("Dialog", "Background"))
        self.background_opacity_label.setText(_translate("Dialog", "Background opacity"))
        self.background_scale_label.setText(_translate("Dialog", "Background scale"))
        self.background_offset_label.setText(_translate("Dialog", "Background offset"))
        self.settings_kernels_groupBox.setTitle(_translate("Dialog", "Kernels"))
        self.planarsolver_label.setText(_translate("Dialog", "Planar solving:"))
        self.pathpreview_label.setText(_translate("Dialog", "Path preview:"))
        self.settings_history_groupbox.setTitle(_translate("Dialog", "History"))
        self.UndoLimit_label.setText(_translate("Dialog", "Undo limit"))
        self.undo_limit_option.setSuffix(_translate("Dialog", " times"))
        self.settings_misc_groupBox.setTitle(_translate("Dialog", "Misc"))
        self.title_full_path_option.setText(_translate("Dialog", "Show full file path on window title."))
        self.console_error_option.setText(_translate("Dialog", "Show error messages in the console."))
        self.monochrome_option.setText(_translate("Dialog", "Monochrome mode for mechanism. (Excluding indicators)"))
        self.dontsave_option.setText(_translate("Dialog", "Do not save Pyslvs option."))
import icons_rc