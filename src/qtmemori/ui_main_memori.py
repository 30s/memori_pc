# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_memori.ui'
#
# Created: Fri Jan 25 14:34:04 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lst_memori = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_memori.sizePolicy().hasHeightForWidth())
        self.lst_memori.setSizePolicy(sizePolicy)
        self.lst_memori.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lst_memori.setObjectName("lst_memori")
        self.verticalLayout.addWidget(self.lst_memori)
        self.btn_export = QtGui.QPushButton(self.centralwidget)
        self.btn_export.setObjectName("btn_export")
        self.verticalLayout.addWidget(self.btn_export)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grid_photos = QtGui.QGridLayout()
        self.grid_photos.setObjectName("grid_photos")
        self.verticalLayout_2.addLayout(self.grid_photos)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_settings = QtGui.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_scan_path = QtGui.QAction(MainWindow)
        self.action_scan_path.setObjectName("action_scan_path")
        self.menu_settings.addAction(self.action_scan_path)
        self.menubar.addAction(self.menu_settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_export.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_settings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.action_scan_path.setText(QtGui.QApplication.translate("MainWindow", "ScanPath", None, QtGui.QApplication.UnicodeUTF8))

