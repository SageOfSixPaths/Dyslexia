#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import re
import sys
import MySQLdb
from PyQt4.QtCore import (Qt, SIGNAL, QTimer, QString, QRect)
from PyQt4.QtGui import (QApplication, QDialog, QFont,
					QMessageBox, QPalette, QColor, QLabel, QTableWidget,
					QPushButton,QTableWidgetItem)

import data
import random

MAC = True
try:
	from PyQt4.QtCore import qt_mac_set_native_menubar
except ImportError:
	MAC = False

class RemoveSentencesDlg(QDialog):
	
	def __init__(self):
		super(RemoveSentencesDlg, self).__init__()
		self.removeList = {}
		self.initUI()
		
	def initUI(self):
		## create a font type for the label
		fontLabel = QFont('SansSerif', 14)
		## create a label 
		self.label = QLabel(self)
		self.label.setAutoFillBackground(True)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setGeometry(QRect(200, 10, 400, 40))
		self.label.setFont(fontLabel)
		
		## set the text for the Label
		self.label.setText('Remove the Sentences')
		
		## Create a Table to hold all the sentences
		self.sentenceTable = QTableWidget(self)
		## set the size and the position of the table
		self.sentenceTable.setGeometry(QRect(10, 60, 800, 400))
		
		## set the column count for the table
		self.sentenceTable.setColumnCount(1)
		
		sentenceHeaderList = ['Sentences From Table']
		
		self.sentenceTable.setHorizontalHeaderLabels(sentenceHeaderList)
		self.sentenceTable.resizeColumnsToContents()
		self.sentenceTable.horizontalHeader().setStretchLastSection(True)
		self.sentenceTable.verticalHeader().setStretchLastSection(True)
		
		# Create a Remove button
		self.removeButton = QPushButton('Remove', self)
		self.removeButton.move(350, 600)
		
		# Create a close button
		self.closeButton = QPushButton('Close', self)
		self.closeButton.move(450, 600)
		
		## Create signal for the remove button 
		self.connect(self.removeButton, SIGNAL("clicked()"), self.onRemoveClicked)
		
		## Create signal for the close button
		self.connect(self.closeButton, SIGNAL("clicked()"), self.closeClicked)
		
		## Create signal for the sentence table
		self.connect(self.sentenceTable, SIGNAL('cellClicked(int, int)'), self.sentenceStateChanged)
		
		## Get sentences from the database table
		self.getSentencesFromDatabase()
		
		
		self.setGeometry(800, 800, 900, 650)
		
	def getSentencesFromDatabase(self):
		## returns the sentence and the corresponding word associated with it
		self.twoTypeList = data.Data().getSentencesFromDatabase()
		if len(self.twoTypeList) == 2:
			self.sentenceList = self.twoTypeList[0]
			
		## load the sentences in the Table Widget
		self.loadSentencesInTable()
	
	def loadSentencesInTable(self):
		self.col = 0
		if len(self.sentenceList) > 0:
			self.sentenceTable.setRowCount(len(self.sentenceList))
			cellList = []
			## Create QTableWidgetItems from the sentence list
			for sentence in self.sentenceList:
				item = QTableWidgetItem(QString(sentence))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
								Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
				item.setCheckState(Qt.Unchecked)
				cellList.append(item)
			cellList.reverse()
			# set the widget items in the table
			for item in range(0, len(self.sentenceList)):
				self.sentenceTable.setItem(item, self.col, cellList.pop())
			
			for index in range(0, len(self.sentenceList)):
				self.sentenceTable.verticalHeader().resizeSection(index, 100)
			
			if len(self.sentenceList) == 5:
				self.sentenceTable.setFixedHeight(500)
			if len(self.sentenceList) == 4:
				self.sentenceTable.setFixedHeight(400)
			elif len(self.sentenceList) == 3:
				self.sentenceTable.setFixedHeight(300)
			elif len(self.sentenceList) == 2:
				self.sentenceTable.setFixedHeight(200)
			elif len(self.sentenceList) == 1:
				self.sentenceTable.setFixedHeight(100)
		else:
			self.sentenceTable.clearContents()
		
	def sentenceStateChanged(self, row, col):
		if (self.sentenceTable.item(row, col).checkState() == 2):
			self.removeList[row] = self.sentenceTable.item(row, col).text()
			self.sentenceTable.item(row, col).setFlags(Qt.ItemFlags(Qt.ItemIsEditable |
									Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable))
		else:
			self.sentenceTable.item(row,col).setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
									Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
			del self.removeList[row]
	
	def onRemoveClicked(self):
		if len(self.removeList) == 0:
			QMessageBox.information(self, 'Remove Sentences',
					'Select the Sentences to Delete')
		else:
			reply = QMessageBox.question(self,
						'Remove Sentences',
						'You want to delete the selected sentences',
						QMessageBox.Yes | QMessageBox.No)
			if reply == QMessageBox.Yes:
				for sentence in self.removeList:
					if sentence in self.sentenceList:
						self.sentenceList.remove(sentence)
				
				## clear the contents of the Table
				self.sentenceTable.clearContents()
				
				cellList = []
				## Add the new entries into the table
				for sentence in self.sentenceList:
					item = QTableWidgetItem(QString(sentence))
					item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
									Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
					item.setCheckState(Qt.Unchecked)
					cellList.append(item)
				cellList.reverse()
				
				for index in range(0, len(self.sentenceList)):
					self.sentenceTable.setItem(index, self.col, cellList.pop())
					
				self.sentenceTable.setRowCount(len(self.sentenceList))
				
				deleteSentences = []
				for sentence in self.removeList.values():
					deleteSentences.append(sentence)
				
				rowsDeletec = data.Data().deleteSentencesFromDatabase(deleteSentences)
				self.getSentencesFromDatabase()
				
				self.removeList = {}
	
	def closeClicked(self):
		reply = QMessageBox.question(self,
				"Remove Sentences",
				"Do you want to close the application",
				QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.reject()

def main():
	import sys
	app = QApplication(sys.argv)
	rs = RemoveSentencesDlg()
	rs.show()
	app.exec_()
	
if __name__ == '__main__':
	main()
