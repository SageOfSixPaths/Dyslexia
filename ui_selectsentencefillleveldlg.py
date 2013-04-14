# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectsentencefillleveldlg.ui'
#
# Created: Sat Jun 30 23:07:40 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SelectSentenceFillLevelDlg(object):
    def setupUi(self, SelectSentenceFillLevelDlg):
        SelectSentenceFillLevelDlg.setObjectName(_fromUtf8("SelectSentenceFillLevelDlg"))
        SelectSentenceFillLevelDlg.resize(543, 328)
        SelectSentenceFillLevelDlg.setWindowTitle(QtGui.QApplication.translate("SelectSentenceFillLevelDlg", "Select Level and Range", None, QtGui.QApplication.UnicodeUTF8))
        SelectSentenceFillLevelDlg.setStyleSheet(_fromUtf8("#SelectSentenceFillLevelDlg {\n"
"background: gray;\n"
"}\n"
"\n"
"#mainFrame {\n"
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
"     min-width: 8em;\n"
" }\n"
"\n"
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}\n"
""))
        self.mainFrame = QtGui.QFrame(SelectSentenceFillLevelDlg)
        self.mainFrame.setGeometry(QtCore.QRect(30, 50, 481, 221))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.widget = QtGui.QWidget(self.mainFrame)
        self.widget.setGeometry(QtCore.QRect(20, 20, 445, 171))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.selectLevellabel = QtGui.QLabel(self.widget)
        self.selectLevellabel.setText(QtGui.QApplication.translate("SelectSentenceFillLevelDlg", "Select Level", None, QtGui.QApplication.UnicodeUTF8))
        self.selectLevellabel.setObjectName(_fromUtf8("selectLevellabel"))
        self.gridLayout.addWidget(self.selectLevellabel, 0, 0, 1, 1)
        self.levelComboBox = QtGui.QComboBox(self.widget)
        self.levelComboBox.setObjectName(_fromUtf8("levelComboBox"))
        self.gridLayout.addWidget(self.levelComboBox, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.selectRangeLabel = QtGui.QLabel(self.widget)
        self.selectRangeLabel.setText(QtGui.QApplication.translate("SelectSentenceFillLevelDlg", "Select Range", None, QtGui.QApplication.UnicodeUTF8))
        self.selectRangeLabel.setObjectName(_fromUtf8("selectRangeLabel"))
        self.gridLayout.addWidget(self.selectRangeLabel, 1, 0, 1, 1)
        self.rangeComboBox = QtGui.QComboBox(self.widget)
        self.rangeComboBox.setObjectName(_fromUtf8("rangeComboBox"))
        self.gridLayout.addWidget(self.rangeComboBox, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.continueButton = QtGui.QPushButton(self.widget)
        self.continueButton.setText(QtGui.QApplication.translate("SelectSentenceFillLevelDlg", "Continue", None, QtGui.QApplication.UnicodeUTF8))
        self.continueButton.setObjectName(_fromUtf8("continueButton"))
        self.gridLayout.addWidget(self.continueButton, 2, 1, 1, 1)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setText(QtGui.QApplication.translate("SelectSentenceFillLevelDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 2, 2, 1, 1)

        self.retranslateUi(SelectSentenceFillLevelDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SelectSentenceFillLevelDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectSentenceFillLevelDlg)

    def retranslateUi(self, SelectSentenceFillLevelDlg):
        pass

