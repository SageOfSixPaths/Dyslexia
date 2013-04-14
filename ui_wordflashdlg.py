# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordflash.ui'
#
# Created: Tue Jun 19 14:03:24 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WordFlashDlg(object):
    def setupUi(self, WordFlashDlg):
        WordFlashDlg.setObjectName(_fromUtf8("WordFlashDlg"))
        WordFlashDlg.resize(740, 503)
        WordFlashDlg.setWindowTitle(QtGui.QApplication.translate("WordFlashDlg", "WordFlash", None, QtGui.QApplication.UnicodeUTF8))
        WordFlashDlg.setStyleSheet(_fromUtf8("#WordFlashDlg {\n"
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
"     min-width: 6em;\n"
" }\n"
"\n"
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}\n"
""))
        self.mainFrame = QtGui.QFrame(WordFlashDlg)
        self.mainFrame.setGeometry(QtCore.QRect(20, 40, 671, 421))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QtCore.QSize(100, 100))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setLineWidth(20)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.gridLayout = QtGui.QGridLayout(self.mainFrame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.wordLabel = QtGui.QLabel(self.mainFrame)
        self.wordLabel.setText(QtGui.QApplication.translate("WordFlashDlg", "Word Display", None, QtGui.QApplication.UnicodeUTF8))
        self.wordLabel.setObjectName(_fromUtf8("wordLabel"))
        self.gridLayout.addWidget(self.wordLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(100, 81, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 30, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(25, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.settingsButton = QtGui.QPushButton(self.mainFrame)
        self.settingsButton.setText(QtGui.QApplication.translate("WordFlashDlg", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.verticalLayout.addWidget(self.settingsButton)
        self.line_5 = QtGui.QFrame(self.mainFrame)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.startButton = QtGui.QPushButton(self.mainFrame)
        self.startButton.setText(QtGui.QApplication.translate("WordFlashDlg", "St&art", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout.addWidget(self.startButton)
        self.line_4 = QtGui.QFrame(self.mainFrame)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.submitButton = QtGui.QPushButton(self.mainFrame)
        self.submitButton.setText(QtGui.QApplication.translate("WordFlashDlg", "Su&bmit", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.verticalLayout.addWidget(self.submitButton)
        self.line_3 = QtGui.QFrame(self.mainFrame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.nextButton = QtGui.QPushButton(self.mainFrame)
        self.nextButton.setText(QtGui.QApplication.translate("WordFlashDlg", "Ne&xt", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.verticalLayout.addWidget(self.nextButton)
        self.line_2 = QtGui.QFrame(self.mainFrame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.shuffleButton = QtGui.QPushButton(self.mainFrame)
        self.shuffleButton.setText(QtGui.QApplication.translate("WordFlashDlg", "Shuffle", None, QtGui.QApplication.UnicodeUTF8))
        self.shuffleButton.setObjectName(_fromUtf8("shuffleButton"))
        self.verticalLayout.addWidget(self.shuffleButton)
        self.line_6 = QtGui.QFrame(self.mainFrame)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        spacerItem2 = QtGui.QSpacerItem(20, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.closeButton = QtGui.QPushButton(self.mainFrame)
        self.closeButton.setText(QtGui.QApplication.translate("WordFlashDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 4, 5, 1)
        self.promptLabel = QtGui.QLabel(self.mainFrame)
        self.promptLabel.setText(QtGui.QApplication.translate("WordFlashDlg", "Enter &Word", None, QtGui.QApplication.UnicodeUTF8))
        self.promptLabel.setObjectName(_fromUtf8("promptLabel"))
        self.gridLayout.addWidget(self.promptLabel, 1, 0, 1, 1)
        self.textEditor = QtGui.QLineEdit(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditor.sizePolicy().hasHeightForWidth())
        self.textEditor.setSizePolicy(sizePolicy)
        self.textEditor.setMinimumSize(QtCore.QSize(194, 0))
        self.textEditor.setObjectName(_fromUtf8("textEditor"))
        self.gridLayout.addWidget(self.textEditor, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(100, 22, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.judgeLabel = QtGui.QLabel(self.mainFrame)
        self.judgeLabel.setText(_fromUtf8(""))
        self.judgeLabel.setObjectName(_fromUtf8("judgeLabel"))
        self.gridLayout.addWidget(self.judgeLabel, 2, 0, 1, 1)
        self.resultLabel = QtGui.QLabel(self.mainFrame)
        self.resultLabel.setText(_fromUtf8(""))
        self.resultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.gridLayout.addWidget(self.resultLabel, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.exerciseLabel = QtGui.QLabel(self.mainFrame)
        self.exerciseLabel.setText(QtGui.QApplication.translate("WordFlashDlg", "&Exercise", None, QtGui.QApplication.UnicodeUTF8))
        self.exerciseLabel.setObjectName(_fromUtf8("exerciseLabel"))
        self.horizontalLayout.addWidget(self.exerciseLabel)
        self.exercisecomboBox = QtGui.QComboBox(self.mainFrame)
        self.exercisecomboBox.setObjectName(_fromUtf8("exercisecomboBox"))
        self.horizontalLayout.addWidget(self.exercisecomboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(100, 80, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.speedLabel = QtGui.QLabel(self.mainFrame)
        self.speedLabel.setText(QtGui.QApplication.translate("WordFlashDlg", "S&peed", None, QtGui.QApplication.UnicodeUTF8))
        self.speedLabel.setObjectName(_fromUtf8("speedLabel"))
        self.horizontalLayout_2.addWidget(self.speedLabel)
        self.speedSpinBox = QtGui.QSpinBox(self.mainFrame)
        self.speedSpinBox.setMinimum(1)
        self.speedSpinBox.setMaximum(10)
        self.speedSpinBox.setObjectName(_fromUtf8("speedSpinBox"))
        self.horizontalLayout_2.addWidget(self.speedSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(100, 81, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 2, 1, 1)
        self.line = QtGui.QFrame(self.mainFrame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 3, 5, 1)
        self.displayLabel = QtGui.QLabel(self.mainFrame)
        self.displayLabel.setText(_fromUtf8(""))
        self.displayLabel.setObjectName(_fromUtf8("displayLabel"))
        self.gridLayout.addWidget(self.displayLabel, 0, 1, 1, 1)
        self.promptLabel.setBuddy(self.textEditor)
        self.exerciseLabel.setBuddy(self.exercisecomboBox)
        self.speedLabel.setBuddy(self.speedSpinBox)

        self.retranslateUi(WordFlashDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), WordFlashDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(WordFlashDlg)

    def retranslateUi(self, WordFlashDlg):
        pass

