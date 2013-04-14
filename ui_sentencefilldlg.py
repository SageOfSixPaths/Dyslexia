# -*- coding: utf-8 -*-

#
# Created: Tue Jun 19 20:56:43 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SentenceFillDlg(object):
    def setupUi(self, SentenceFillDlg):
        SentenceFillDlg.setObjectName(_fromUtf8("SentenceFillDlg"))
        SentenceFillDlg.resize(664, 495)
        SentenceFillDlg.setWindowTitle(QtGui.QApplication.translate("SentenceFillDlg", "Sentence Fill", None, QtGui.QApplication.UnicodeUTF8))
        SentenceFillDlg.setStyleSheet(_fromUtf8("#SentenceFillDlg {\n"
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
"QTableWidget{\n"
"border-style:solid;\n"
"border:2px solid gray;\n"
"border-radius:8px;\n"
"font: 14pt;\n"
"font-weight: bold;\n"
"background: #BCD4E6;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 7px;\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"padding-right: 15px;\n"
"min-width: 140px;\n"
"max-width: 120px;\n"
"min-height: 20px;\n"
"max-height: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QComboBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 9em;\n"
"	  font: 14pt; \n"
" }\n"
""))
        self.mainFrame = QtGui.QFrame(SentenceFillDlg)
        self.mainFrame.setGeometry(QtCore.QRect(50, 30, 1100, 550))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.widget = QtGui.QWidget(self.mainFrame)
        self.widget.setGeometry(QtCore.QRect(20, 30, 1020, 550))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
