# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removesentencedlg.ui'
#
# Created: Wed Jun  6 17:15:39 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RemoveSentenceDlg(object):
    def setupUi(self, RemoveSentenceDlg):
        RemoveSentenceDlg.setObjectName(_fromUtf8("RemoveSentenceDlg"))
        RemoveSentenceDlg.resize(506, 350)
        RemoveSentenceDlg.setWindowTitle(QtGui.QApplication.translate("RemoveSentenceDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(RemoveSentenceDlg)
        self.label.setGeometry(QtCore.QRect(150, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("RemoveSentenceDlg", "Remove Sentences", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.sentenceTableWidget = QtGui.QTableWidget(RemoveSentenceDlg)
        self.sentenceTableWidget.setGeometry(QtCore.QRect(70, 90, 256, 192))
        self.sentenceTableWidget.setColumnCount(1)
        self.sentenceTableWidget.setObjectName(_fromUtf8("sentenceTableWidget"))
        self.sentenceTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("RemoveSentenceDlg", "Sentences", None, QtGui.QApplication.UnicodeUTF8))
        self.sentenceTableWidget.setHorizontalHeaderItem(0, item)
        self.widget = QtGui.QWidget(RemoveSentenceDlg)
        self.widget.setGeometry(QtCore.QRect(390, 90, 87, 176))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.removeButton = QtGui.QPushButton(self.widget)
        self.removeButton.setText(QtGui.QApplication.translate("RemoveSentenceDlg", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.verticalLayout.addWidget(self.removeButton)
        spacerItem = QtGui.QSpacerItem(20, 108, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setText(QtGui.QApplication.translate("RemoveSentenceDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(RemoveSentenceDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), RemoveSentenceDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(RemoveSentenceDlg)

    def retranslateUi(self, RemoveSentenceDlg):
        item = self.sentenceTableWidget.horizontalHeaderItem(0)

