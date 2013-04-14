#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import re
import sys
import MySQLdb
from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature, QTimer, QString)
from PyQt4.QtGui import (QApplication, QDialog, QFont, 
						QMessageBox, QPalette, QColor, QLabel)

import ui_selectsentencefillleveldlg
import sentencefilldlg
import data

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class SelectSentenceFillLevelDlg(QDialog,
				ui_selectsentencefillleveldlg.Ui_SelectSentenceFillLevelDlg):
	
	def __init__(self, parent=None):
		super(SelectSentenceFillLevelDlg, self).__init__(parent)
		self.setupUi(self)
		
		self.levelValues = {}
		self.levelValues['Low Beginning Level'] = 'LBL_Sentences'
		self.levelValues['High Beginning Level'] = 'Sentences'
		self.levelValues['Low Intermediate Level'] = 'LIL_Sentences'
		self.levelValues['High Intermediate Level'] = 'HIL_Sentences'
		self.levelValues['Low Advanced (SAT) Level'] = ' '
		self.levelValues['High Advanced (GRE) Level'] = ' '
		
		self.levelComboBox.addItem('           ')
		self.levelComboBox.addItems(self.levelValues.keys())
		
		self.rangeList = []
		self.rangeList.append('         ')
		self.rangeList.append('1 - 25')
		self.rangeList.append('26 - 50')
		self.rangeList.append('51 - 75')
		self.rangeList.append('76 - 100')
		self.rangeList.append('101 - 125')
		self.rangeList.append('126 - 150')
		self.rangeList.append('151 - 175')
		self.rangeList.append('176 - 200')
		
		self.rangeComboBox.addItems(self.rangeList)
		
		self.connect(self.levelComboBox, SIGNAL('currentIndexChanged(int)'), self.levelComboBoxSelected)
		self.connect(self.rangeComboBox, SIGNAL('currentIndexChanged(int)'), self.rangeComboBoxSelected)
		self.connect(self.continueButton, SIGNAL('clicked()'), self.continueClicked)
		
	def levelComboBoxSelected(self):
		## get the count of entries in the corresponding table
		selectedValue = str(self.levelComboBox.currentText()).strip()
		if len(selectedValue) > 0:
			self.tableName = self.levelValues[selectedValue]
	
	def rangeComboBoxSelected(self):
		selectedRange = str(self.rangeComboBox.currentText()).strip()
		if len(selectedRange) > 0:
			self.rangeValues = selectedRange.split('-')
		
	def continueClicked(self):
		if len(self.tableName) > 0 and len(self.rangeValues) == 2:
			self.ranges = []
			self.ranges.append(self.rangeValues[0].strip())
			self.ranges.append(self.rangeValues[1].strip())
			# set the range and table name to fetch the related data
			sentenceFillDlg = sentencefilldlg.SentenceFillDlg(self.tableName, self.ranges)
			if sentenceFillDlg.exec_():
				pass 

if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	form = SelectSentenceFillLevelDlg()
	form.show()
	app.exec_()
