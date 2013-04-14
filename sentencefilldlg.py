from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QStringList, QString,
						QAbstractTableModel, QTimer, QSize, QRect)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem, 
							QStringListModel, QVBoxLayout, QTableWidget,
							QLineEdit, QLabel, QFont, QPushButton, 
							QMessageBox, QBrush, QColor, QHeaderView,
							QSizePolicy, QFrame, QComboBox)

import ui_sentencefilldlg
import random
import data
import copy
import re
		
class MyLineEdit(QLineEdit):
	
	def __init__(self, title, tableWidget, parent):
		super(MyLineEdit, self).__init__(title, parent)
		self.title = title
		self.tableWidget = tableWidget
		
	
	def focusInEvent(self, event):
		self.selectAll()
		self.setSelection(0, len(self.title))
		if hasattr(self, 'selectedItemIndex'):
			strText = str(self.tableWidget.item(self.selectedItemIndex, 0).text())
			splittedText = strText.split('-')
			if len(splittedText) == 2:
				item = QTableWidgetItem(QString(splittedText[0] + ' '+self.text()+ ' '+ splittedText[1]))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
									Qt.ItemIsEnabled))
				self.tableWidget.setItem(self.selectedItemIndex, 0, item)
		else:
			print ('Select the Sentence First')
		
class SentenceFillDlg(QDialog, ui_sentencefilldlg.Ui_SentenceFillDlg):
	
	def __init__(self, tableName, rangeValues, parent=None):
		super(SentenceFillDlg, self).__init__(parent)
		self.tableName = tableName
		self.rangeValues = rangeValues
		self.setupUi(self)
		self.initUI()
		
	def initUI(self):
		fontLabel = QFont('SansSerif', 14)
		
		self.setMinimumSize(1200, 600)
		self.resize(1200, 600)
		
		self.sentenceToFillTable = QTableWidget(5, 1, self)
		self.sentenceToFillTable.setGeometry(QRect(70, 60, 800, 400))
		
		self.sentenceToFillTable.setColumnCount(1)
		
		item = QTableWidgetItem()
		item.setText('Sentences To Match')
		font = QFont()
		font.setBold(True)
		font.setWeight(75)
		item.setFont(font)
		self.sentenceToFillTable.setHorizontalHeaderItem(0, item)
		self.sentenceToFillTable.resizeColumnsToContents()
		self.sentenceToFillTable.horizontalHeader().setStretchLastSection(True)
		self.sentenceToFillTable.verticalHeader().setStretchLastSection(True)
		
		self.sentenceList = []
		self.getSentencesFromDatabase()
		
		# split the sentences into chunks of 5
		# Map to hold the anwers
		self.rightWordList = {}
		
		self.iteration = 0
		self.sentenceMasterList = []
		self.sentenceSlaveList = []
		
		if len(self.sentenceList) > 0:			
			for sentence in self.sentenceList:
				if len(self.sentenceSlaveList) < 5:
					self.sentenceSlaveList.append(sentence)
				else:
					self.sentenceMasterList.append(self.sentenceSlaveList)
					self.sentenceSlaveList = []
					self.sentenceSlaveList.append(sentence)
					
			if len(self.sentenceSlaveList) <= 5:
				self.sentenceMasterList.append(self.sentenceSlaveList)
				
			self.maxIteration = len(self.sentenceMasterList)
		
		
		## set the row height
		self.tableHeightSize = 0
		## Only if there is atleast one sentence fetched from the database
		if len(self.sentenceList) > 0:			
			for index in range(0, 5):
				if len(self.sentenceList[index]) < 150:
					self.sentenceToFillTable.verticalHeader().resizeSection(index, 80)
					self.tableHeightSize = self.tableHeightSize + 90
				elif len(self.sentenceList[index]) < 200:
					self.sentenceToFillTable.verticalHeader().resizeSection(index, 100)
					self.tableHeightSize = self.tableHeightSize + 100
				else:
					self.sentenceToFillTable.verticalHeader().resizeSection(index, 120)
					self.tableHeightSize = self.tableHeightSize + 120
			
				
			# split words from databse into chunks of 5
		
			self.refIteration = 0
			self.refWordMasterList = []
			self.refWordSlaveList = []
			for wordList in self.wordMap.values():
				if len(self.refWordSlaveList) < 5:
					self.refWordSlaveList.append(wordList)
				else:
					self.refWordMasterList.append(self.refWordSlaveList)
					self.refWordSlaveList = []
					self.refWordSlaveList.append(wordList)
			
			if len(self.refWordSlaveList) <= 5:
				self.refWordMasterList.append(self.refWordSlaveList)
				
			self.refMaxIteration = len(self.refWordMasterList)
		
			self.insertSentencesInTable()
		
		self.connect(self.sentenceToFillTable, SIGNAL("cellClicked(int, int)"), self.itemSelect)
		
		# create next, submit and close buttons
		self.nextButton = QPushButton('Next', self)
		self.nextButton.move(170, 520)
		self.nextButton.setEnabled(False)  
		
		self.submitButton = QPushButton('Submit', self)
		self.submitButton.move(380, 520)
		
		self.closeButton = QPushButton('Close', self)
		self.closeButton.move(600, 520)
		
		self.connect(self.closeButton, SIGNAL('clicked()'), self.closeClicked)
		
		self.connect(self.submitButton, SIGNAL('clicked()'), self.onSubmitClicked)
		
		self.connect(self.nextButton, SIGNAL('clicked()'), self.onNextClicked)
		
		self.setWindowTitle('Sentence Fill')
		
		#self.setGeometry(10, 80, 1100, 750)


	def getSentencesFromDatabase(self):
		self.twoTypeList = data.Data().getSentencesFromDatabase(self.tableName, self.rangeValues)
		if len(self.twoTypeList) == 2:
			self.sentenceList = self.twoTypeList[0]
			self.wordMap = self.twoTypeList[1]

	def closeClicked(self):
		reply = QMessageBox.question(self,
					"Fill the Sentences",
					"You want to close the application",
					QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.reject()
			
	def onNextClicked(self):
		if not self.iteration < self.maxIteration:
			QMessageBox.information(self,
					"Fill the Sentences",
					"All Sentences are matched",
					QMessageBox.Ok)
		else:
			self.sentenceToFillTable.clearContents()
			## Fetch the next records
			self.refIteration = self.refIteration + 1
			self.rightWordList = {}
			## clear the contents of the combo box
			self.wordListComboBox.clear()
			self.insertSentencesInTable()
	
	# validate whether the user has matched the blanks with a value during next and submit button clicks
	def onNextSubmitValidation(self):
		self.textNotFilled = False
		for row in range(0, len(self.currentSentenceListInTable)):
			if self.sentenceToFillTable.item(row, 0).text() == self.currentSentenceListInTable[row]:
				self.textNotFilled = True
		if self.textNotFilled:
			QMessageBox.information(self,
						"Fill the sentences",
						"Match all the sentences in the table",
						QMessageBox.Ok)
			self.nextButton.setEnabled(False)
			
			
	def onSubmitClicked(self):
		self.wordsMatched = True
		self.allWordsMatched = True
		brushRed = QBrush(QColor(255,0,0))
		brushRed.setStyle(Qt.SolidPattern)
		
		brushGreen = QBrush(QColor(0,255,0))
		brushGreen.setStyle(Qt.SolidPattern)
		
		# validate whether the user all matched the blanks with a value
		#self.onNextSubmitValidation()
		textNotFilled = False
		for row in range(0, len(self.currentSentenceListInTable)):
			if self.sentenceToFillTable.item(row, 0).text() == self.currentSentenceListInTable[row]:
				textNotFilled = True
		if textNotFilled:
			QMessageBox.information(self,
						"Fill the sentences",
						"Match all the sentences in the table",
						QMessageBox.Ok)
		else:
			splittedSentence = []
			foundWordInSentence = ""
			self.rightWordListCopy = self.rightWordList
			for row in range(0, len(self.currentSentenceListInTable)):
				sentenceFilled = str(self.sentenceToFillTable.item(row, 0).text())
				newSplittedSentence = [word.strip() for word in sentenceFilled.split()]
				splittedSentence = []
				for word in newSplittedSentence:
					match = re.search(r'\w+', word)
					if match:
						splittedSentence.append(str(match.group()))
				
				wordList = self.rightWordListCopy[row]
				
				if len(wordList) > 1:
					firstWord = wordList[0].strip()
					secondWord = wordList[1].strip()
					if ' ' in firstWord:
						for word in firstWord.split():
							if word not in splittedSentence:
								self.wordsMatched = False
					else:
						if firstWord not in splittedSentence:
							self.wordsMatched = False
					
					if self.wordsMatched: ## check is valid only if the first word is matched
						if ' ' in secondWord:
							for word in secondWord.split():
								if word not in splittedSentence:
									self.wordsMatched = False
						else:
							if secondWord not in splittedSentence:
								self.wordsMatched = False
				elif len(wordList) == 1:
					word = wordList[0].strip()
					if word not in splittedSentence:
						self.wordsMatched = False
				
				if self.wordsMatched:
					self.sentenceToFillTable.item(row, 0).setBackground(brushGreen)
				else:
					self.sentenceToFillTable.item(row, 0).setBackground(brushRed)
					self.allWordsMatched = False
				
				self.wordsMatched = True
					
			if self.allWordsMatched:
				self.nextButton.setEnabled(True)
				QMessageBox.information(self,
								"Fill the sentences",
								"All sentences are matched",
								QMessageBox.Ok)

	def insertSentencesInTable(self):
		if self.iteration < self.maxIteration:
			cellList = []
			self.col = 0
			self.currentSentenceListInTable = self.sentenceMasterList[self.iteration]
			for sentence in self.currentSentenceListInTable:
				item = QTableWidgetItem(QString(sentence))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
								Qt.ItemIsEnabled))
				cellList.append(item)
			cellList.reverse()
			
			for index in range(0, len(self.currentSentenceListInTable)):
				self.sentenceToFillTable.setItem(index, self.col, cellList.pop())
				
			self.sentenceToFillTable.setRowCount(len(self.sentenceMasterList[self.iteration]))
			
			self.sentenceToFillTable.setFixedHeight(self.tableHeightSize)
			
			# increment the count for the next button click
			self.iteration = self.iteration + 1
			
	def createComboBox(self, rowIndex):
		self.xAxis = 1000
		self.yAxis = 80
		
		if self.refIteration < self.refMaxIteration:
			wordListWithFiveArrays = self.refWordMasterList[self.refIteration]
			requiredWordList = wordListWithFiveArrays[rowIndex]
			
			## Create a combo box
			self.wordListComboBox = QComboBox(self)
			self.wordListComboBox.setGeometry(900, 80, 100, 20)
			self.connect(self.wordListComboBox, SIGNAL("currentIndexChanged(int)"),
							self.wordSelected)
			self.wordListComboBox.show()
			
			## save the right word
			if len(requiredWordList) > 0:
				if rowIndex not in self.rightWordList.keys():
					if len(requiredWordList) > 0:
						wordList = requiredWordList[0].split('&')
						self.rightWordList[rowIndex] = wordList

			## insert words in the combo box
			random.shuffle(requiredWordList)
			random.shuffle(requiredWordList)
			
			self.wordListComboBox.addItem('         ')
			self.wordListComboBox.addItems(requiredWordList)
	
	def wordSelected(self):
		## Avoid the blank option
		if len(str(self.wordListComboBox.currentText()).strip()) > 0:
			sentence = self.currentSentenceListInTable[self.selectedSentenceIndex]
			splittedText = sentence.split('-')
			if len(splittedText) == 2:
				item = QTableWidgetItem(QString(splittedText[0] +
						str(self.wordListComboBox.currentText()) + ' ' + splittedText[1].strip()))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable | 
								Qt.ItemIsEnabled))
				self.sentenceToFillTable.setItem(self.selectedSentenceIndex, 0, item)
			elif len(splittedText) > 2:
				wordsFromCombobox = str(self.wordListComboBox.currentText()).split('&')
				item = QTableWidgetItem(QString(splittedText[0] + wordsFromCombobox[0]
							+ splittedText[1] + wordsFromCombobox[1] + ' ' + splittedText[2].strip()))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable | 
							Qt.ItemIsEnabled))
				self.sentenceToFillTable.setItem(self.selectedSentenceIndex, 0, item)
	
	def createIndexForWords(self):
		self.indexForWords = {}
		self.nextIndex = 0
		for word in self.refWordListForIndex:
			if self.nextIndex == 5:
				break
			self.indexForWords[word] = self.nextIndex
			self.nextIndex = self.nextIndex + 1
	
	def itemSelect(self,rowIndex):
		self.createComboBox(rowIndex)
		self.selectedSentenceIndex = rowIndex
		

def main():
	import sys
	app = QApplication(sys.argv)
	ex = SentenceFillDlg()
	ex.show()
	app.exec_()
	
if __name__ == '__main__':
	main()
