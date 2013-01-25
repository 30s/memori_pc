# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_scan_path.ui'
#
# Created: Fri Jan 25 17:57:07 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DlgScanPath(object):
    def setupUi(self, DlgScanPath):
        DlgScanPath.setObjectName("DlgScanPath")
        DlgScanPath.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DlgScanPath)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_scan_path = QtGui.QTableWidget(DlgScanPath)
        self.tbl_scan_path.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tbl_scan_path.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tbl_scan_path.setObjectName("tbl_scan_path")
        self.tbl_scan_path.setColumnCount(2)
        self.tbl_scan_path.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_scan_path.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_scan_path.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tbl_scan_path)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtGui.QPushButton(DlgScanPath)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_delete = QtGui.QPushButton(DlgScanPath)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_scan = QtGui.QPushButton(DlgScanPath)
        self.btn_scan.setObjectName("btn_scan")
        self.horizontalLayout.addWidget(self.btn_scan)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DlgScanPath)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DlgScanPath)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DlgScanPath.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DlgScanPath.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgScanPath)

    def retranslateUi(self, DlgScanPath):
        DlgScanPath.setWindowTitle(QtGui.QApplication.translate("DlgScanPath", "Scan Path", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_scan_path.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DlgScanPath", "Scan Path", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_scan_path.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DlgScanPath", "Photos Count", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setText(QtGui.QApplication.translate("DlgScanPath", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("DlgScanPath", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_scan.setText(QtGui.QApplication.translate("DlgScanPath", "Scan", None, QtGui.QApplication.UnicodeUTF8))

