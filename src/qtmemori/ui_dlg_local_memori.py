# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_local_memori.ui'
#
# Created: Wed Jan 23 18:58:51 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DlgLocalMemori(object):
    def setupUi(self, DlgLocalMemori):
        DlgLocalMemori.setObjectName("DlgLocalMemori")
        DlgLocalMemori.resize(615, 414)
        self.verticalLayout = QtGui.QVBoxLayout(DlgLocalMemori)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lst_memori = QtGui.QListWidget(DlgLocalMemori)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_memori.sizePolicy().hasHeightForWidth())
        self.lst_memori.setSizePolicy(sizePolicy)
        self.lst_memori.setObjectName("lst_memori")
        self.horizontalLayout_2.addWidget(self.lst_memori)
        self.frame = QtGui.QFrame(DlgLocalMemori)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grid_photos = QtGui.QGridLayout()
        self.grid_photos.setObjectName("grid_photos")
        self.horizontalLayout.addLayout(self.grid_photos)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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

