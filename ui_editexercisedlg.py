# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editexercisedlg.ui'
#
# Created: Sat Mar 31 09:19:03 2012
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
        ModifyExerciseDlg.resize(454, 377)
        ModifyExerciseDlg.setWindowTitle(QtGui.QApplication.translate("ModifyExerciseDlg", "ModifyExercise", None, QtGui.QApplication.UnicodeUTF8))
        self.widget = QtGui.QWidget(ModifyExerciseDlg)
        self.widget.setGeometry(QtCore.QRect(10, 20, 404, 337))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.selectExerciseLabel = QtGui.QLabel(self.widget)
        self.selectExerciseLabel.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "&Select Exercise", None, QtGui.QApplication.UnicodeUTF8))
        self.selectExerciseLabel.setObjectName(_fromUtf8("selectExerciseLabel"))
        self.gridLayout.addWidget(self.selectExerciseLabel, 0, 0, 1, 1)
        self.exerciseComboBox = QtGui.QComboBox(self.widget)
        self.exerciseComboBox.setObjectName(_fromUtf8("exerciseComboBox"))
        self.gridLayout.addWidget(self.exerciseComboBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.wordListTableWidget = QtGui.QTableWidget(self.widget)
        self.wordListTableWidget.setObjectName(_fromUtf8("wordListTableWidget"))
        self.wordListTableWidget.setColumnCount(1)
        self.wordListTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Word List", None, QtGui.QApplication.UnicodeUTF8))
        self.wordListTableWidget.setHorizontalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.wordListTableWidget)
        spacerItem1 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.addExerciseButton = QtGui.QPushButton(self.widget)
        self.addExerciseButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Add E&xercise", None, QtGui.QApplication.UnicodeUTF8))
        self.addExerciseButton.setObjectName(_fromUtf8("addExerciseButton"))
        self.gridLayout_2.addWidget(self.addExerciseButton, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.addWordButton = QtGui.QPushButton(self.widget)
        self.addWordButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "&Add Word", None, QtGui.QApplication.UnicodeUTF8))
        self.addWordButton.setObjectName(_fromUtf8("addWordButton"))
        self.verticalLayout_2.addWidget(self.addWordButton)
        self.editWordButton = QtGui.QPushButton(self.widget)
        self.editWordButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "&Edit Word", None, QtGui.QApplication.UnicodeUTF8))
        self.editWordButton.setObjectName(_fromUtf8("editWordButton"))
        self.verticalLayout_2.addWidget(self.editWordButton)
        self.deleteWordButton = QtGui.QPushButton(self.widget)
        self.deleteWordButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "&Delete Word", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteWordButton.setObjectName(_fromUtf8("deleteWordButton"))
        self.verticalLayout_2.addWidget(self.deleteWordButton)
        spacerItem4 = QtGui.QSpacerItem(20, 128, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setText(QtGui.QApplication.translate("ModifyExerciseDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.selectExerciseLabel.setBuddy(self.exerciseComboBox)

        self.retranslateUi(ModifyExerciseDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ModifyExerciseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ModifyExerciseDlg)

    def retranslateUi(self, ModifyExerciseDlg):
        item = self.wordListTableWidget.horizontalHeaderItem(0)

