# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addExercisedlg.ui'
#
# Created: Thu Apr 19 19:19:56 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddExerciseDlg(object):
    def setupUi(self, AddExerciseDlg):
        AddExerciseDlg.setObjectName(_fromUtf8("AddExerciseDlg"))
        AddExerciseDlg.resize(470, 340)
        AddExerciseDlg.setWindowTitle(QtGui.QApplication.translate("AddExerciseDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.widget = QtGui.QWidget(AddExerciseDlg)
        self.widget.setGeometry(QtCore.QRect(27, 12, 423, 307))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setText(QtGui.QApplication.translate("AddExerciseDlg", "Exercise Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(88, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.exerciseNameLineEdit = QtGui.QLineEdit(self.splitter_2)
        self.exerciseNameLineEdit.setObjectName(_fromUtf8("exerciseNameLineEdit"))
        self.gridLayout_4.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setText(QtGui.QApplication.translate("AddExerciseDlg", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(108, 13, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.descriptionTextEdit = QtGui.QTextEdit(self.splitter)
        self.descriptionTextEdit.setObjectName(_fromUtf8("descriptionTextEdit"))
        self.gridLayout_4.addWidget(self.splitter, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem4 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.addExerciseButton = QtGui.QPushButton(self.widget)
        self.addExerciseButton.setText(QtGui.QApplication.translate("AddExerciseDlg", "Add Exercise", None, QtGui.QApplication.UnicodeUTF8))
        self.addExerciseButton.setObjectName(_fromUtf8("addExerciseButton"))
        self.verticalLayout.addWidget(self.addExerciseButton)
        spacerItem5 = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setText(QtGui.QApplication.translate("AddExerciseDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(AddExerciseDlg)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), AddExerciseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AddExerciseDlg)

    def retranslateUi(self, AddExerciseDlg):
        pass

