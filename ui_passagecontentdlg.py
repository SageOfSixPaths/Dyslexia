# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passagecontent.ui'
#
# Created: Mon Dec 24 08:39:39 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PassageContentDlg(object):
    def setupUi(self, PassageContentDlg):
        PassageContentDlg.setObjectName(_fromUtf8("PassageContentDlg"))
        PassageContentDlg.resize(905, 690)
        PassageContentDlg.setWindowTitle(QtGui.QApplication.translate("PassageContentDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        PassageContentDlg.setStyleSheet(_fromUtf8("#passagecontentdlg {\n"
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
"     min-width: 8em;\n"
" 	  font: 14pt; \n"
" }\n"
"\n"
"QTextEdit {\n"
" 	  font: 14pt; \n"
" }\n"
"\n"
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}"))
        self.passageframe = QtGui.QFrame(PassageContentDlg)
        self.passageframe.setGeometry(QtCore.QRect(30, 10, 861, 676))
        self.passageframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.passageframe.setFrameShadow(QtGui.QFrame.Raised)
        self.passageframe.setObjectName(_fromUtf8("passageframe"))
        self.passageText = QtGui.QTextEdit(self.passageframe)
        self.passageText.setGeometry(QtCore.QRect(20, 50, 801, 541))
        self.passageText.setObjectName(_fromUtf8("passageText"))
        self.passagelabel = QtGui.QLabel(self.passageframe)
        self.passagelabel.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.passagelabel.setText(QtGui.QApplication.translate("PassageContentDlg", "Read the Passage", None, QtGui.QApplication.UnicodeUTF8))
        self.passagelabel.setObjectName(_fromUtf8("passagelabel"))
        self.widget = QtGui.QWidget(self.passageframe)
        self.widget.setGeometry(QtCore.QRect(230, 630, 346, 30))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.questionButton = QtGui.QPushButton(self.widget)
        self.questionButton.setText(QtGui.QApplication.translate("PassageContentDlg", "Questions", None, QtGui.QApplication.UnicodeUTF8))
        self.questionButton.setObjectName(_fromUtf8("questionButton"))
        self.horizontalLayout.addWidget(self.questionButton)
        spacerItem = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setText(QtGui.QApplication.translate("PassageContentDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)

        self.retranslateUi(PassageContentDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PassageContentDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(PassageContentDlg)

    def retranslateUi(self, PassageContentDlg):
        pass

