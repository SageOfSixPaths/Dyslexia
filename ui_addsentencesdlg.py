# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addsentencesdlg.ui'
#
# Created: Tue Jul 10 12:32:17 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddSentenceDlg(object):
    def setupUi(self, AddSentenceDlg):
        AddSentenceDlg.setObjectName(_fromUtf8("AddSentenceDlg"))
        AddSentenceDlg.resize(616, 491)
        AddSentenceDlg.setWindowTitle(QtGui.QApplication.translate("AddSentenceDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2 = QtGui.QLabel(AddSentenceDlg)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("AddSentenceDlg", "Add/Remove Sentences", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(AddSentenceDlg)
        self.line.setGeometry(QtCore.QRect(440, 90, 21, 261))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layoutWidget = QtGui.QWidget(AddSentenceDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(471, 101, 87, 226))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.removeButton = QtGui.QPushButton(self.layoutWidget)
        self.removeButton.setText(QtGui.QApplication.translate("AddSentenceDlg", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 158, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(self.layoutWidget)
        self.closeButton.setText(QtGui.QApplication.translate("AddSentenceDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 2, 0, 1, 1)
        self.widget = QtGui.QWidget(AddSentenceDlg)
        self.widget.setGeometry(QtCore.QRect(20, 94, 412, 352))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sentenceLlabel = QtGui.QLabel(self.widget)
        self.sentenceLlabel.setText(QtGui.QApplication.translate("AddSentenceDlg", "Sentence", None, QtGui.QApplication.UnicodeUTF8))
        self.sentenceLlabel.setObjectName(_fromUtf8("sentenceLlabel"))
        self.gridLayout_2.addWidget(self.sentenceLlabel, 0, 0, 1, 1)
        self.sentenceTextEdit = QtGui.QTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sentenceTextEdit.sizePolicy().hasHeightForWidth())
        self.sentenceTextEdit.setSizePolicy(sizePolicy)
        self.sentenceTextEdit.setMaximumSize(QtCore.QSize(256, 131))
        self.sentenceTextEdit.setObjectName(_fromUtf8("sentenceTextEdit"))
        self.gridLayout_2.addWidget(self.sentenceTextEdit, 0, 1, 2, 3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 4, 1, 1)
        self.option1Label = QtGui.QLabel(self.widget)
        self.option1Label.setText(QtGui.QApplication.translate("AddSentenceDlg", "Option One", None, QtGui.QApplication.UnicodeUTF8))
        self.option1Label.setObjectName(_fromUtf8("option1Label"))
        self.gridLayout_2.addWidget(self.option1Label, 3, 0, 1, 2)
        self.optionOneLineEdit = QtGui.QLineEdit(self.widget)
        self.optionOneLineEdit.setObjectName(_fromUtf8("optionOneLineEdit"))
        self.gridLayout_2.addWidget(self.optionOneLineEdit, 3, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 4, 1, 1)
        self.option1Label_2 = QtGui.QLabel(self.widget)
        self.option1Label_2.setText(QtGui.QApplication.translate("AddSentenceDlg", "Option Two", None, QtGui.QApplication.UnicodeUTF8))
        self.option1Label_2.setObjectName(_fromUtf8("option1Label_2"))
        self.gridLayout_2.addWidget(self.option1Label_2, 4, 0, 1, 2)
        self.optionTwoLineEdit = QtGui.QLineEdit(self.widget)
        self.optionTwoLineEdit.setObjectName(_fromUtf8("optionTwoLineEdit"))
        self.gridLayout_2.addWidget(self.optionTwoLineEdit, 4, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 4, 4, 1, 1)
        self.option1Label_3 = QtGui.QLabel(self.widget)
        self.option1Label_3.setText(QtGui.QApplication.translate("AddSentenceDlg", "Option Three", None, QtGui.QApplication.UnicodeUTF8))
        self.option1Label_3.setObjectName(_fromUtf8("option1Label_3"))
        self.gridLayout_2.addWidget(self.option1Label_3, 5, 0, 1, 2)
        self.optionThreeLineEdit = QtGui.QLineEdit(self.widget)
        self.optionThreeLineEdit.setObjectName(_fromUtf8("optionThreeLineEdit"))
        self.gridLayout_2.addWidget(self.optionThreeLineEdit, 5, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 5, 4, 1, 1)
        self.option1Label_4 = QtGui.QLabel(self.widget)
        self.option1Label_4.setText(QtGui.QApplication.translate("AddSentenceDlg", "Option Four", None, QtGui.QApplication.UnicodeUTF8))
        self.option1Label_4.setObjectName(_fromUtf8("option1Label_4"))
        self.gridLayout_2.addWidget(self.option1Label_4, 6, 0, 1, 2)
        self.optionFourLineEdit = QtGui.QLineEdit(self.widget)
        self.optionFourLineEdit.setObjectName(_fromUtf8("optionFourLineEdit"))
        self.gridLayout_2.addWidget(self.optionFourLineEdit, 6, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 6, 4, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setText(QtGui.QApplication.translate("AddSentenceDlg", "Option Five", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 7, 0, 1, 2)
        self.optionFiveLineEdit = QtGui.QLineEdit(self.widget)
        self.optionFiveLineEdit.setObjectName(_fromUtf8("optionFiveLineEdit"))
        self.gridLayout_2.addWidget(self.optionFiveLineEdit, 7, 2, 1, 1)
        self.addSentenceButton = QtGui.QPushButton(self.widget)
        self.addSentenceButton.setText(QtGui.QApplication.translate("AddSentenceDlg", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.addSentenceButton.setObjectName(_fromUtf8("addSentenceButton"))
        self.gridLayout_2.addWidget(self.addSentenceButton, 7, 3, 1, 2)

        self.retranslateUi(AddSentenceDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AddSentenceDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AddSentenceDlg)

    def retranslateUi(self, AddSentenceDlg):
        pass

