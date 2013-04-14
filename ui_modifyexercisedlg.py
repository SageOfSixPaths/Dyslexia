# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifyexercisedlg.ui'
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

class Ui_ModifyExerciseDlg(object):
    def setupUi(self, ModifyExerciseDlg):
        ModifyExerciseDlg.setObjectName(_fromUtf8("ModifyExerciseDlg"))
        ModifyExerciseDlg.resize(664, 495)
        ModifyExerciseDlg.setWindowTitle(QtGui.QApplication.translate("ModifyExerciseDlg", "ModifyExercise", None, QtGui.QApplication.UnicodeUTF8))
        ModifyExerciseDlg.setStyleSheet(_fromUtf8("#ModifyExerciseDlg {\n"
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
"     min-width: 6em;\n"
" }\n"
""))
        self.mainFrame = QtGui.QFrame(ModifyExerciseDlg)
        self.mainFrame.setGeometry(QtCore.QRect(70, 30, 551, 421))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.widget = QtGui.QWidget(self.mainFrame)
        self.widget.setGeometry(QtCore.QRect(20, 30, 521, 367))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 2, 2)
        self.selectExerciseLabel = QtGui.QLabel(self.widget)
        self.selectExerciseLabel.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "&Select Exercise", None, QtGui.QApplication.UnicodeUTF8))
        self.selectExerciseLabel.setObjectName(_fromUtf8("selectExerciseLabel"))
        self.gridLayout.addWidget(self.selectExerciseLabel, 1, 1, 1, 1)
        self.exerciseComboBox = QtGui.QComboBox(self.widget)
        self.exerciseComboBox.setObjectName(_fromUtf8("exerciseComboBox"))
        self.gridLayout.addWidget(self.exerciseComboBox, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.wordListTableWidget = QtGui.QTableWidget(self.widget)
        self.wordListTableWidget.setObjectName(_fromUtf8("wordListTableWidget"))
        self.wordListTableWidget.setColumnCount(1)
        self.wordListTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Word List", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.wordListTableWidget.setHorizontalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.wordListTableWidget)
        spacerItem2 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.addWordLabel = QtGui.QLabel(self.widget)
        self.addWordLabel.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Add Word", None, QtGui.QApplication.UnicodeUTF8))
        self.addWordLabel.setObjectName(_fromUtf8("addWordLabel"))
        self.gridLayout_2.addWidget(self.addWordLabel, 0, 0, 1, 1)
        self.addWordLineEdit = QtGui.QLineEdit(self.widget)
        self.addWordLineEdit.setObjectName(_fromUtf8("addWordLineEdit"))
        self.gridLayout_2.addWidget(self.addWordLineEdit, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem4 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem6 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        spacerItem7 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.addExerciseButton = QtGui.QPushButton(self.widget)
        self.addExerciseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addExerciseButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Add Exercise", None, QtGui.QApplication.UnicodeUTF8))
        self.addExerciseButton.setObjectName(_fromUtf8("addExerciseButton"))
        self.verticalLayout_2.addWidget(self.addExerciseButton)
        spacerItem8 = QtGui.QSpacerItem(40, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.deleteExercisePushButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteExercisePushButton.sizePolicy().hasHeightForWidth())
        self.deleteExercisePushButton.setSizePolicy(sizePolicy)
        self.deleteExercisePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteExercisePushButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Delete Exercise", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteExercisePushButton.setObjectName(_fromUtf8("deleteExercisePushButton"))
        self.verticalLayout_2.addWidget(self.deleteExercisePushButton)
        spacerItem9 = QtGui.QSpacerItem(40, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem9)
        self.deleteWordButton = QtGui.QPushButton(self.widget)
        self.deleteWordButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteWordButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "&Delete Word", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteWordButton.setObjectName(_fromUtf8("deleteWordButton"))
        self.verticalLayout_2.addWidget(self.deleteWordButton)
        spacerItem10 = QtGui.QSpacerItem(40, 28, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem10)
        self.loadWordsButton = QtGui.QPushButton(self.widget)
        self.loadWordsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.loadWordsButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Load Words", None, QtGui.QApplication.UnicodeUTF8))
        self.loadWordsButton.setObjectName(_fromUtf8("loadWordsButton"))
        self.verticalLayout_2.addWidget(self.loadWordsButton)
        spacerItem11 = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.selectExerciseLabel.setBuddy(self.exerciseComboBox)

        self.retranslateUi(ModifyExerciseDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ModifyExerciseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ModifyExerciseDlg)
        ModifyExerciseDlg.setTabOrder(self.addWordLineEdit, self.exerciseComboBox)
        ModifyExerciseDlg.setTabOrder(self.exerciseComboBox, self.deleteWordButton)
        ModifyExerciseDlg.setTabOrder(self.deleteWordButton, self.loadWordsButton)
        ModifyExerciseDlg.setTabOrder(self.loadWordsButton, self.addExerciseButton)
        ModifyExerciseDlg.setTabOrder(self.addExerciseButton, self.wordListTableWidget)
        ModifyExerciseDlg.setTabOrder(self.wordListTableWidget, self.closeButton)

    def retranslateUi(self, ModifyExerciseDlg):
        item = self.wordListTableWidget.horizontalHeaderItem(0)

