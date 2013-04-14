# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordflashresultdlg.ui'
#
# Created: Wed Jun 20 12:59:50 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WordFlashResultDlg(object):
    def setupUi(self, WordFlashResultDlg):
        WordFlashResultDlg.setObjectName(_fromUtf8("WordFlashResultDlg"))
        WordFlashResultDlg.resize(662, 495)
        WordFlashResultDlg.setWindowTitle(QtGui.QApplication.translate("WordFlashResultDlg", "WordFlash Result", None, QtGui.QApplication.UnicodeUTF8))
        WordFlashResultDlg.setStyleSheet(_fromUtf8("#WordFlashResultDlg {\n"
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
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
" }\n"
"\n"
"QGroupBox {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QTableWidget{\n"
"border-style:solid;\n"
"border:2px solid gray;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"background: #BCD4E6;\n"
"}\n"
""))
        self.mainFrame = QtGui.QFrame(WordFlashResultDlg)
        self.mainFrame.setGeometry(QtCore.QRect(50, 40, 581, 421))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.layoutWidget = QtGui.QWidget(self.mainFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 491, 371))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scoreLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setText(QtGui.QApplication.translate("WordFlashResultDlg", "Score", None, QtGui.QApplication.UnicodeUTF8))
        self.scoreLabel.setObjectName(_fromUtf8("scoreLabel"))
        self.gridLayout.addWidget(self.scoreLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.resultLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.resultLabel.setFont(font)
        self.resultLabel.setText(_fromUtf8(""))
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.gridLayout.addWidget(self.resultLabel, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WordFlashResultDlg", "User Entry", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WordFlashResultDlg", "Correct Word", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        spacerItem3 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(QtGui.QApplication.translate("WordFlashResultDlg", "Select To View", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem4 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.rightRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.rightRadioButton.setText(QtGui.QApplication.translate("WordFlashResultDlg", "Right Answers", None, QtGui.QApplication.UnicodeUTF8))
        self.rightRadioButton.setObjectName(_fromUtf8("rightRadioButton"))
        self.verticalLayout_2.addWidget(self.rightRadioButton)
        spacerItem5 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.wrongRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.wrongRadioButton.setText(QtGui.QApplication.translate("WordFlashResultDlg", "Wrong Answers", None, QtGui.QApplication.UnicodeUTF8))
        self.wrongRadioButton.setObjectName(_fromUtf8("wrongRadioButton"))
        self.verticalLayout_2.addWidget(self.wrongRadioButton)
        spacerItem6 = QtGui.QSpacerItem(20, 158, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setText(QtGui.QApplication.translate("WordFlashResultDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(WordFlashResultDlg)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), WordFlashResultDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(WordFlashResultDlg)

    def retranslateUi(self, WordFlashResultDlg):
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)

