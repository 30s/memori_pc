# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_local_memori.ui'
#
# Created: Wed Jan 23 14:46:10 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DlgLocalMemori(object):
    def setupUi(self, DlgLocalMemori):
        DlgLocalMemori.setObjectName("DlgLocalMemori")
        DlgLocalMemori.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(DlgLocalMemori)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lst_memori = QtGui.QListWidget(DlgLocalMemori)
        self.lst_memori.setObjectName("lst_memori")
        self.horizontalLayout.addWidget(self.lst_memori)
        self.lst_photos = QtGui.QListWidget(DlgLocalMemori)
        self.lst_photos.setObjectName("lst_photos")
        self.horizontalLayout.addWidget(self.lst_photos)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DlgLocalMemori)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DlgLocalMemori)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DlgLocalMemori.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DlgLocalMemori.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgLocalMemori)

    def retranslateUi(self, DlgLocalMemori):
        DlgLocalMemori.setWindowTitle(QtGui.QApplication.translate("DlgLocalMemori", "Local Memoris", None, QtGui.QApplication.UnicodeUTF8))

