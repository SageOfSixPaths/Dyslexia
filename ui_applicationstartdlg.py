# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applicationstartdlg.ui'
#
# Created: Mon Dec 24 08:08:12 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ApplicationStartDlg(object):
    def setupUi(self, ApplicationStartDlg):
        ApplicationStartDlg.setObjectName(_fromUtf8("ApplicationStartDlg"))
        ApplicationStartDlg.resize(606, 442)
        ApplicationStartDlg.setWindowTitle(QtGui.QApplication.translate("ApplicationStartDlg", "Word Master", None, QtGui.QApplication.UnicodeUTF8))
        ApplicationStartDlg.setStyleSheet(_fromUtf8("#ApplicationStartDlg {\n"
"background: gray;\n"
"}\n"
"\n"
"#mainFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eef, stop: 1 #ccf);\n"
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
"padding-left: 3px;\n"
"padding-right: 30px;\n"
"min-width: 150px;\n"
"max-width: 300px;\n"
"min-height: 13px;\n"
"max-height: 26px;\n"
"}"))
        self.closeButton = QtGui.QPushButton(ApplicationStartDlg)
        self.closeButton.setGeometry(QtCore.QRect(360, 370, 185, 34))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setText(QtGui.QApplication.translate("ApplicationStartDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.mainFrame = QtGui.QFrame(ApplicationStartDlg)
        self.mainFrame.setGeometry(QtCore.QRect(60, 40, 431, 321))
        self.mainFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.widget = QtGui.QWidget(self.mainFrame)
        self.widget.setGeometry(QtCore.QRect(90, 75, 258, 181))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.wordFlashButton = QtGui.QPushButton(self.widget)
        self.wordFlashButton.setText(QtGui.QApplication.translate("ApplicationStartDlg", "Word Flash", None, QtGui.QApplication.UnicodeUTF8))
        self.wordFlashButton.setObjectName(_fromUtf8("wordFlashButton"))
        self.gridLayout.addWidget(self.wordFlashButton, 0, 0, 1, 1)
        self.synonymMatchButton = QtGui.QPushButton(self.widget)
        self.synonymMatchButton.setText(QtGui.QApplication.translate("ApplicationStartDlg", "Synonym Match", None, QtGui.QApplication.UnicodeUTF8))
        self.synonymMatchButton.setObjectName(_fromUtf8("synonymMatchButton"))
        self.gridLayout.addWidget(self.synonymMatchButton, 1, 0, 1, 1)
        self.antonymMatchButton = QtGui.QPushButton(self.widget)
        self.antonymMatchButton.setText(QtGui.QApplication.translate("ApplicationStartDlg", "Antonym Match", None, QtGui.QApplication.UnicodeUTF8))
        self.antonymMatchButton.setObjectName(_fromUtf8("antonymMatchButton"))
        self.gridLayout.addWidget(self.antonymMatchButton, 2, 0, 1, 1)
        self.sentenceFillButton = QtGui.QPushButton(self.widget)
        self.sentenceFillButton.setText(QtGui.QApplication.translate("ApplicationStartDlg", "Sentence Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.sentenceFillButton.setObjectName(_fromUtf8("sentenceFillButton"))
        self.gridLayout.addWidget(self.sentenceFillButton, 3, 0, 1, 1)
        self.readingComprehensionButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(17)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readingComprehensionButton.sizePolicy().hasHeightForWidth())
        self.readingComprehensionButton.setSizePolicy(sizePolicy)
        self.readingComprehensionButton.setText(QtGui.QApplication.translate("ApplicationStartDlg", "Reading Comprehension", None, QtGui.QApplication.UnicodeUTF8))
        self.readingComprehensionButton.setIconSize(QtCore.QSize(20, 16))
        self.readingComprehensionButton.setObjectName(_fromUtf8("readingComprehensionButton"))
        self.gridLayout.addWidget(self.readingComprehensionButton, 4, 0, 1, 1)

        self.retranslateUi(ApplicationStartDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ApplicationStartDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ApplicationStartDlg)

    def retranslateUi(self, ApplicationStartDlg):
        pass

