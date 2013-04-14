#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QStringList, QString,
						QAbstractTableModel, QTimer, QSize, QRect)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem, 
							QStringListModel, QVBoxLayout, QTableWidget,
							QLineEdit, QLabel, QFont, QPushButton, 
							QMessageBox, QBrush, QColor)

import ui_synonymmatchdlg
import random
import data

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False
	
class MyTable(QTableWidget):
	
	def __init__(self, rows, columns, parent):
		super(MyTable, self).__init__(rows, columns, parent)
		
		for index in range(0, rows):
			self.setRowHeight(index, 42)
			
		self.setFixedHeight(250)

class MyLineEdit(QLineEdit):
	
	def __init__(self, title, tableWidget, parent):
		super(MyLineEdit, self).__init__(title, parent)
		self.title = title
		self.tableWidget = tableWidget
	
	def focusInEvent(self, event):
		self.selectAll()
		self.setSelection(0, len(self.title))
		item = QTableWidgetItem(QString(self.text()))
		item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
						Qt.ItemIsEnabled))
		self.tableWidget.setItem(self.selectedItemIndex, 0, item)
			
class SynonymMatchDlg(QDialog, ui_synonymmatchdlg.Ui_SynonymMatchDlg):
	
	def __init__(self, option, parent=None):
		super(SynonymMatchDlg, self).__init__(parent)
		self.setupUi(self)
		self.userOption = option
		if option == 'Antonyms':
			self.setWindowTitle('Antonym Match')
		self.initUI()
		
	def initUI(self):
		fontLabel = QFont('SansSerif',14)
		
		self.wordsToMatch = MyTable(5, 1, self)
		self.wordsToMatch.move(70,80)
		
		self.setMinimumSize(950, 600)
		self.resize(950, 600)
		
		itemWordsToMatchColumn = QTableWidgetItem()
		itemWordsToMatchColumn.setText('Words To Match')
		font = QFont()
		font.setBold(True)
		font.setWeight(75)
		itemWordsToMatchColumn.setFont(font)
		
		self.wordsToMatch.setColumnCount(1)
		self.wordsToMatch.setHorizontalHeaderItem(0, itemWordsToMatchColumn)
		
		self.wordsToMatch.resizeColumnsToContents()
		self.wordsToMatch.horizontalHeader().setStretchLastSection(True)
		self.wordsToMatch.verticalHeader().setStretchLastSection(True)
		
		self.getWordsFromDatabase()
		
		# index the reference words 
		self.refWordListForIndex = self.refWordList[:]
		
		### Split words from the database into list of 5 word chunks
		self.iteration = 0
		self.wordMasterList = []
		self.wordSlaveList = []
		for word in self.wordList:
			if len(self.wordSlaveList) < 5:
				self.wordSlaveList.append(word)
			else:
				self.wordMasterList.append(self.wordSlaveList)
				self.wordSlaveList = []
				self.wordSlaveList.append(word)
				
		if len(self.wordSlaveList) <= 5:
			self.wordMasterList.append(self.wordSlaveList)
			
		self.maxIteration = len(self.wordMasterList)
		
		### Split words from the database into list of 5 word chunks
		
		self.refIteration = 0
		self.refWordMasterList = []
		self.refWordSlaveList = []
		for word in self.refWordList:
			if len(self.refWordSlaveList) < 5:
				self.refWordSlaveList.append(word)
			else:
				self.refWordMasterList.append(self.refWordSlaveList)
				self.refWordSlaveList = []
				self.refWordSlaveList.append(word)
				
		
		if len(self.refWordSlaveList) <= 5:
			self.refWordMasterList.append(self.refWordSlaveList)
		
		self.refMaxIteration = len(self.refWordMasterList)
		
		self.connect(self.wordsToMatch, SIGNAL("cellClicked(int, int)"), self.itemSelect)
		
		self.matchedTable = MyTable(5, 1, self)
		self.matchedTable.move(600, 80)
		
		itemMatchedTableColumn = QTableWidgetItem()
		itemMatchedTableColumn.setText('Matched Words')
		itemMatchedTableColumn.setFont(font)
		
		self.matchedTable.setColumnCount(1)
		self.matchedTable.setHorizontalHeaderItem(0, itemMatchedTableColumn)
		self.matchedTable.resizeColumnsToContents()
		self.matchedTable.horizontalHeader().setStretchLastSection(True)
		self.matchedTable.verticalHeader().setStretchLastSection(True)
		
		self.connect(self.matchedTable, SIGNAL("cellClicked(int, int)"), self.itemSelect)
		
		# insert Words into the wordsToMatch table
		self.insertWordsInTable()
		
		# create QLineEdits for the reference words
		self.createLineEdits()
		
		# create next submit and close button
		
		self.nextButton = QPushButton('Next', self)
		self.nextButton.move(170, 400)
		self.nextButton.setEnabled(False)  
		
		self.submitButton = QPushButton('Submit', self)
		self.submitButton.move(350, 400)
		
		self.closeButton = QPushButton('Close', self)
		self.closeButton.move(530, 400)
		
		self.connect(self.closeButton, SIGNAL('clicked()'), self.closeClicked)
		
		self.connect(self.submitButton, SIGNAL('clicked()'), self.onSubmitClicked)
		
		self.connect(self.nextButton, SIGNAL('clicked()'), self.onNextClicked)
		
		#self.setGeometry(800, 800, 950, 650)
	
	def getWordsFromDatabase(self):
		
		if self.userOption == 'Synonyms':
			self.twoWordList = data.Data().getSynonymWords(self.userOption)
		else:
			self.twoWordList = data.Data().getSynonymWords(self.userOption)
		
		if len(self.twoWordList) == 2:
			self.wordList = self.twoWordList[0]
			self.refWordList = self.twoWordList[1]
		
	def closeClicked(self):
		reply = QMessageBox.question(self,
					"Match the Synonyms",
					"You want to close the application?",
					QMessageBox.Yes | QMessageBox.No)
					
		if reply == QMessageBox.Yes:
			self.reject()
			
	def onNextClicked(self):
		if not self.iteration < self.maxIteration:
			QMessageBox.information(self,
					"Match the Synonyms",
					"All Levels Completed",
					QMessageBox.Ok)
		else:					
			self.matchedTable.clearContents()
			if len(self.lineEditList) > 0:
				# hide the previous QLineEdits
				for edit in self.lineEditList:
					edit.hide()
					
			self.insertWordsInTable()
			self.createLineEdits()
			self.nextButton.setEnabled(False) 
			
	def onSubmitClicked(self):
		self.allWordsMatched = True
		brushRed = QBrush(QColor(255,0,0))
		brushRed.setStyle(Qt.SolidPattern)
		
		brushGreen = QBrush(QColor(0,255,0))
		brushGreen.setStyle(Qt.SolidPattern)
		
		textNotFilled = False
		for row in range(0, len(self.currentWordListInTable)):
			if not self.matchedTable.item(row, 0):
				textNotFilled = True
		
		if textNotFilled:
			QMessageBox.information(self, 
						"Match the Synonyms",
						"Match all the words in the table",
						QMessageBox.Ok)
		else:
			self.createIndexForWords()			
			for row in range(0, len(self.currentWordListInTable)):
				wordToMatch = str(self.matchedTable.item(row, 0).text())
				if self.indexForWords[wordToMatch] != row:
					self.allWordsMatched = False
					self.matchedTable.item(row, 0).setBackground(brushRed)
				else:
					self.matchedTable.item(row, 0).setBackground(brushGreen)
			
			if self.allWordsMatched:
				self.nextButton.setEnabled(True)
				self.refWordListForIndex = self.refWordListForIndex[self.nextIndex:]
				QMessageBox.information(self,
					"Match the Synonyms",
					"All words are matched",
					QMessageBox.Ok)
	
	def insertWordsInTable(self):
		if self.iteration < self.maxIteration:			
			cellList = []
			self.col = 0
			self.currentWordListInTable = self.wordMasterList[self.iteration]
			for word in self.currentWordListInTable:
				item = QTableWidgetItem(QString(word))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
							Qt.ItemIsEnabled))
				cellList.append(item)
			cellList.reverse()
			
			for i in range(0, len(self.currentWordListInTable)):
				self.wordsToMatch.setItem(i, self.col, cellList.pop())
				
			self.wordsToMatch.setRowCount(len(self.wordMasterList[self.iteration]))
			self.matchedTable.setRowCount(len(self.wordMasterList[self.iteration]))
			self.wordsToMatch.horizontalHeader().setStretchLastSection(True)
			self.wordsToMatch.verticalHeader().setStretchLastSection(True)
			
			if len(self.wordMasterList[self.iteration]) == 4:
				self.wordsToMatch.setFixedHeight(200)
				self.matchedTable.setFixedHeight(200)
			elif len(self.wordMasterList[self.iteration]) == 3:
				self.wordsToMatch.setFixedHeight(150)
				self.matchedTable.setFixedHeight(150)
			elif len(self.wordMasterList[self.iteration]) == 2:
				self.wordsToMatch.setFixedHeight(100)
				self.matchedTable.setFixedHeight(100)
			
			# increment the count for the "Next button click"
			self.iteration = self.iteration + 1
			
	def createLineEdits(self):
		self.xAxis = 340
		self.yAxis = 80
		self.lineEditList = []
		if self.refIteration < self.refMaxIteration:
			referenceWords = self.refWordMasterList[self.refIteration]
			random.shuffle(referenceWords)
			for word in referenceWords:
				self.edit = MyLineEdit(word, self.matchedTable, self)
				self.edit.setReadOnly(True)
				self.edit.move(self.xAxis, self.yAxis)
				self.edit.show()
				self.lineEditList.append(self.edit)
				self.yAxis = self.yAxis + 30
			# increment the count for the "Next button click"
			self.refIteration = self.refIteration + 1
			
	def createIndexForWords(self):
		self.indexForWords = {}
		self.nextIndex = 0
		for word in self.refWordListForIndex:
			if self.nextIndex == 5:
				break
			self.indexForWords[word] = self.nextIndex
			self.nextIndex = self.nextIndex + 1
		
	def itemSelect(self,rowIndex):
		for lineEdit in self.lineEditList:
			lineEdit.selectedItemIndex = rowIndex
		
def main():
	import sys
	app = QApplication(sys.argv)
	ex = SynonymMatchDlg('Antonyms')
	ex.show()
	app.exec_()
	
if __name__ == '__main__':
	main()	
