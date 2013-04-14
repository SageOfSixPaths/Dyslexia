#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import re
import sys
import MySQLdb
from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature, QTimer, QString,
							QRect)
from PyQt4.QtGui import (QApplication, QDialog, QFont, 
						QMessageBox, QPalette, QColor, QLabel,
						QTableWidgetItem, QHeaderView, QSizePolicy,
						QTextEdit)

import ui_removesentencedlg
import data
import random

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class RemoveSentenceDlg(QDialog,
			ui_removesentencedlg.Ui_RemoveSentenceDlg):
	
	def __init__(self, parent=None):
		super(RemoveSentenceDlg, self).__init__(parent)
		self.setupUi(self)
		if not MAC:
			self.removeButton.setFocusPolicy(Qt.NoFocus)
			self.closeButton.setFocusPolicy(Qt.NoFocus)
			
		## set the properties for the Table Widget
		self.sentenceTableWidget.horizontalHeader().setStretchLastSection(True)
		#self.sentenceTableWidget.resizeColumnsToContents()
		self.sentenceTableWidget.verticalHeader().setStretchLastSection(True)
		self.sentenceTableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch)
		self.sentenceTableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		
		## load the sentences from the table
		self.col = 0
		self.loadSentences()
		
	
	def loadSentences(self):
		self.contentList = data.Data().getSentencesFromDatabase()
		if len(self.contentList) > 1:
			self.sentenceList = self.contentList[0]
			self.sentenceTableWidget.setRowCount(len(self.sentenceList))
			cellList = []
			for sentence in self.sentenceList:
				##item = QTableWidgetItem(QString(sentence))
				item = QTextEdit()
				item.setText(QString(sentence))
				#item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
				#						Qt.ItemIsUserCheckable | 
				#						Qt.ItemIsEnabled))
				#item.setCheckState(Qt.Unchecked)
				cellList.append(item)
			cellList.reverse()
			
			# insert the sentences in the table
			for i in range(0, len(self.sentenceList)):
				self.sentenceTableWidget.setCellWidget(i, self.col, cellList.pop())
			
			for i in range(0, len(self.sentenceList)):
				self.sentenceTableWidget.setRowHeight(i, 42)
				
		else:
			QMessageBox.information(self, "Remove Sentence",
			"Data Load Error")

if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	form = RemoveSentenceDlg()
	form.show()
	app.exec_()

	
		
