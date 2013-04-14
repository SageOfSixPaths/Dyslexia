# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectpassagedlg.ui'
#
# Created: Mon Dec 24 06:50:08 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SelectPassageDlg(object):
    def setupUi(self, SelectPassageDlg):
        SelectPassageDlg.setObjectName(_fromUtf8("SelectPassageDlg"))
        SelectPassageDlg.resize(554, 300)
        SelectPassageDlg.setWindowTitle(QtGui.QApplication.translate("SelectPassageDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        SelectPassageDlg.setStyleSheet(_fromUtf8("#SelectPassageDlg {\n"
"background: gray;\n"
"}\n"
"\n"
"#passageframe {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eef, stop: 1 #ccf);\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 100px;\n"
"max-width: 100px;\n"
"min-height: 20px;\n"
"max-height: 20px;\n"
"}\n"
"\n"
"QComboBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 12em;\n"
" }\n"
"\n"
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}\n"
""))
        self.passageframe = QtGui.QFrame(SelectPassageDlg)
        self.passageframe.setGeometry(QtCore.QRect(20, 50, 501, 211))
        self.passageframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.passageframe.setFrameShadow(QtGui.QFrame.Raised)
        self.passageframe.setObjectName(_fromUtf8("passageframe"))
        self.gridLayout = QtGui.QGridLayout(self.passageframe)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.passageLabel = QtGui.QLabel(self.passageframe)
        self.passageLabel.setText(QtGui.QApplication.translate("SelectPassageDlg", "Select Passage", None, QtGui.QApplication.UnicodeUTF8))
        self.passageLabel.setObjectName(_fromUtf8("passageLabel"))
        self.gridLayout.addWidget(self.passageLabel, 0, 0, 1, 1)
        self.passagecomboBox = QtGui.QComboBox(self.passageframe)
        self.passagecomboBox.setObjectName(_fromUtf8("passagecomboBox"))
        self.gridLayout.addWidget(self.passagecomboBox, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(140, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(142, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.continueButton = QtGui.QPushButton(self.passageframe)
        self.continueButton.setText(QtGui.QApplication.translate("SelectPassageDlg", "Continue", None, QtGui.QApplication.UnicodeUTF8))
        self.continueButton.setObjectName(_fromUtf8("continueButton"))
        self.gridLayout.addWidget(self.continueButton, 1, 1, 1, 1)
        self.closeButton = QtGui.QPushButton(self.passageframe)
        self.closeButton.setText(QtGui.QApplication.translate("SelectPassageDlg", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 1, 2, 1, 1)

        self.retranslateUi(SelectPassageDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SelectPassageDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectPassageDlg)

    def retranslateUi(self, SelectPassageDlg):
        pass

