# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findandreplacedlg.ui'
#
# Created: Tue Mar 27 16:24:57 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FindAndReplaceDlg(object):
    def setupUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setObjectName(_fromUtf8("FindAndReplaceDlg"))
        FindAndReplaceDlg.resize(433, 248)
        FindAndReplaceDlg.setWindowTitle(QtGui.QApplication.translate("FindAndReplaceDlg", "Find And Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(FindAndReplaceDlg)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(FindAndReplaceDlg)
        self.label.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "Find &what:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.findLineEdit = QtGui.QLineEdit(FindAndReplaceDlg)
        self.findLineEdit.setObjectName(_fromUtf8("findLineEdit"))
        self.gridLayout.addWidget(self.findLineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(FindAndReplaceDlg)
        self.label_2.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "Replace w&ith", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.replaceLineEdit = QtGui.QLineEdit(FindAndReplaceDlg)
        self.replaceLineEdit.setObjectName(_fromUtf8("replaceLineEdit"))
        self.gridLayout.addWidget(self.replaceLineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(FindAndReplaceDlg)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.caseCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.caseCheckBox.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "&Case sensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.caseCheckBox.setObjectName(_fromUtf8("caseCheckBox"))
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.wholeCheckBox.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "Wh&ole words", None, QtGui.QApplication.UnicodeUTF8))
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName(_fromUtf8("wholeCheckBox"))
        self.horizontalLayout.addWidget(self.wholeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(FindAndReplaceDlg)
        self.label_3.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "&Syntax", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.syntaxComboBox = QtGui.QComboBox(FindAndReplaceDlg)
        self.syntaxComboBox.setObjectName(_fromUtf8("syntaxComboBox"))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.syntaxComboBox.setItemText(0, QtGui.QApplication.translate("FindAndReplaceDlg", "Literal text", None, QtGui.QApplication.UnicodeUTF8))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.syntaxComboBox.setItemText(1, QtGui.QApplication.translate("FindAndReplaceDlg", "Regular expression", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_2.addWidget(self.syntaxComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.findButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.findButton.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "&Find", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.verticalLayout_2.addWidget(self.findButton)
        self.replaceButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.replaceButton.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "&Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.verticalLayout_2.addWidget(self.replaceButton)
        self.replaceAllButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.replaceAllButton.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "Replace & All", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceAllButton.setObjectName(_fromUtf8("replaceAllButton"))
        self.verticalLayout_2.addWidget(self.replaceAllButton)
        spacerItem1 = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.closeButton.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.label.setBuddy(self.findLineEdit)
        self.label_2.setBuddy(self.replaceLineEdit)
        self.label_3.setBuddy(self.syntaxComboBox)

        self.retranslateUi(FindAndReplaceDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), FindAndReplaceDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplaceDlg)

    def retranslateUi(self, FindAndReplaceDlg):
        pass

