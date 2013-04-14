from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QStringList, QString,
						QAbstractTableModel, QTimer, QSize, QRect)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem, 
							QStringListModel, QVBoxLayout, QTableWidget,
							QLineEdit, QLabel, QFont, QPushButton, 
							QMessageBox, QBrush, QColor, QHeaderView,
							QSizePolicy, QFrame, QComboBox)

import ui_passagequestionsdlg
import random
import data
import copy
import re

class PassageQuestionsDlg(QDialog, ui_passagequestionsdlg.Ui_PassageQuestionsDlg):
	
	def __init__(self, tableName, parent):
		super(PassageQuestionsDlg, self).__init__(parent)
		self.tableName = tableName
		self.setupUi(self)
		self.initUI()
		
	def initUI(self):
		fontLabel = QFont('SansSerif', 14)
		
		self.setWindowTitle('Passage Questions')
		self.passageQuestionsTable = QTableWidget(5, 1, self)
		self.passageQuestionsTable.setGeometry(QRect(70, 60, 800, 400))
		
		self.passageQuestionsTable.setColumnCount(1)
		
		self.setMinimumSize(1300, 650)
		self.resize(1300, 650)
		
		self.setModal(False)
		
		item = QTableWidgetItem()
		item.setText('Questions')
		font = QFont()
		font.setBold(True)
		font.setWeight(75)
		item.setFont(font)
		self.passageQuestionsTable.setHorizontalHeaderItem(0, item)
		self.passageQuestionsTable.resizeColumnsToContents()
		self.passageQuestionsTable.horizontalHeader().setStretchLastSection(True)
		self.passageQuestionsTable.verticalHeader().setStretchLastSection(True)
		
		self.questionsList = []
		## get questions from the database
		self.getQuestionsFromDatabase()
		
		# split the sentences into chunks of 5
		# Map to hold the anwers
		self.rightOptionList = {}
		
		self.iteration = 0
		self.questionsMasterList = []
		self.questionsSlaveList = []
		
		if len(self.questionsList) > 0:			
			for sentence in self.questionsList:
				if len(self.questionsSlaveList) < 5:
					self.questionsSlaveList.append(sentence)
				else:
					self.questionsMasterList.append(self.questionsSlaveList)
					self.questionsSlaveList = []
					self.questionsSlaveList.append(sentence)
					
			if len(self.questionsSlaveList) <= 5:
				self.questionsMasterList.append(self.questionsSlaveList)
				
			self.maxIteration = len(self.questionsMasterList)
		
		
		## set the row height
		self.tableHeightSize = 0
		## Only if there is atleast one sentence fetched from the database
		if len(self.questionsList) > 0:			
			for index in range(0, 5):
				if len(self.questionsList[index]) < 150:
					self.passageQuestionsTable.verticalHeader().resizeSection(index, 90)
					self.tableHeightSize = self.tableHeightSize + 100
				elif len(self.questionsList[index]) < 200:
					self.passageQuestionsTable.verticalHeader().resizeSection(index, 100)
					self.tableHeightSize = self.tableHeightSize + 100
				else:
					self.passageQuestionsTable.verticalHeader().resizeSection(index, 120)
					self.tableHeightSize = self.tableHeightSize + 120
			
				
			# split options from database into chunks of 5
		
			self.refIteration = 0
			self.refOptionMasterList = []
			self.refOptionSlaveList = []
			for optionList in self.optionsMap.values():
				if len(self.refOptionSlaveList) < 5:
					self.refOptionSlaveList.append(optionList)
				else:
					self.refOptionMasterList.append(self.refOptionSlaveList)
					self.refOptionSlaveList = []
					self.refOptionSlaveList.append(optionList)
			
			if len(self.refOptionSlaveList) <= 5:
				self.refOptionMasterList.append(self.refOptionSlaveList)
				
			self.refMaxIteration = len(self.refOptionMasterList)
		
			self.insertQuestionsInTable()
		
		self.connect(self.passageQuestionsTable, SIGNAL("cellClicked(int, int)"), self.itemSelect)
		
		# create next, submit and close buttons
		self.nextButton = QPushButton('Next', self)
		self.nextButton.move(170, 580)
		self.nextButton.setEnabled(False)  
		
		self.submitButton = QPushButton('Submit', self)
		self.submitButton.move(380, 580)
		
		self.closeButton = QPushButton('Close', self)
		self.closeButton.move(600, 580)
		
		self.connect(self.closeButton, SIGNAL('clicked()'), self.closeClicked)
		
		self.connect(self.submitButton, SIGNAL('clicked()'), self.onSubmitClicked)
		
		self.connect(self.nextButton, SIGNAL('clicked()'), self.onNextClicked)
		
		self.setWindowTitle('Passage Questions')
		
		#self.setGeometry(10, 80, 1100, 750)


	def getQuestionsFromDatabase(self):
		self.twoTypeList = data.Data().getQuestionsFromDatabase(self.tableName)
		if len(self.twoTypeList) == 2:
			self.questionsList = self.twoTypeList[0]
			self.optionsMap = self.twoTypeList[1]

	def closeClicked(self):
		reply = QMessageBox.question(self,
					"Passage Questions",
					"You want to close the application",
					QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.reject()
			
	def onNextClicked(self):
		if not self.iteration < self.maxIteration:
			QMessageBox.information(self,
					"Passage Questions",
					"All Sentences are matched",
					QMessageBox.Ok)
		else:
			self.passageQuestionsTable.clearContents()
			## Fetch the next records
			self.refIteration = self.refIteration + 1
			self.rightOptionList = {}
			## clear the contents of the combo box
			self.optionListComboBox.clear()
			self.insertQuestionsInTable()
	
	# validate whether the user has matched the blanks with a value during next and submit button clicks
	def onNextSubmitValidation(self):
		self.textNotFilled = False
		for row in range(0, len(self.currentQuestionListInTable)):
			if self.passageQuestionsTable.item(row, 0).text() == self.currentQuestionListInTable[row]:
				self.textNotFilled = True
		if self.textNotFilled:
			QMessageBox.information(self,
						"Passage Questions",
						"Answer all the Questions in the table",
						QMessageBox.Ok)
			self.nextButton.setEnabled(False)
			
			
	def onSubmitClicked(self):
		self.optionsMatched = True
		self.allOptionsMatched = True
		brushRed = QBrush(QColor(255,0,0))
		brushRed.setStyle(Qt.SolidPattern)
		
		brushGreen = QBrush(QColor(0,255,0))
		brushGreen.setStyle(Qt.SolidPattern)
		
		# validate whether the user all matched the blanks with a value
		#self.onNextSubmitValidation()
		textNotFilled = False
		for row in range(0, len(self.currentQuestionListInTable)):
			if self.passageQuestionsTable.item(row, 0).text() == self.currentQuestionListInTable[row]:
				textNotFilled = True
		if textNotFilled:
			QMessageBox.information(self,
						"Passage Questions",
						"Answer all the Questions in the table",
						QMessageBox.Ok)
		else:
			splittedSentence = []
			foundWordInSentence = ""
			self.rightOptionListCopy = self.rightOptionList
			for row in range(0, len(self.currentQuestionListInTable)):
				sentenceFilled = str(self.passageQuestionsTable.item(row, 0).text())
				splittedSentence = []
				splittedSentence = sentenceFilled.split('-')
				
				correctOption = str(self.rightOptionListCopy[row]).strip()
				
				if(len(splittedSentence) > 1):
					answerChoice = str(splittedSentence[1]).strip()
					if not (answerChoice == correctOption):
						self.optionsMatched = False
				
				if self.optionsMatched:
					self.passageQuestionsTable.item(row, 0).setBackground(brushGreen)
				else:
					self.passageQuestionsTable.item(row, 0).setBackground(brushRed)
					self.allOptionsMatched = False
				
				self.optionsMatched = True
					
			if self.allOptionsMatched:
				self.nextButton.setEnabled(True)
				QMessageBox.information(self,
								"Passage Questions",
								"All Questions are answered",
								QMessageBox.Ok)

	def insertQuestionsInTable(self):
		if self.iteration < self.maxIteration:
			cellList = []
			self.col = 0
			self.currentQuestionListInTable = self.questionsMasterList[self.iteration]
			for sentence in self.currentQuestionListInTable:
				item = QTableWidgetItem(QString(sentence))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
								Qt.ItemIsEnabled))
				cellList.append(item)
			cellList.reverse()
			
			for index in range(0, len(self.currentQuestionListInTable)):
				self.passageQuestionsTable.setItem(index, self.col, cellList.pop())
				
			self.passageQuestionsTable.setRowCount(len(self.questionsMasterList[self.iteration]))
			
			self.passageQuestionsTable.setFixedHeight(self.tableHeightSize)
			
			# increment the count for the next button click
			self.iteration = self.iteration + 1
			
	def createComboBox(self, rowIndex):
		self.xAxis = 1000
		self.yAxis = 80
		
		if self.refIteration < self.refMaxIteration:
			optionListWithFiveArrays = self.refOptionMasterList[self.refIteration]
			requiredWordList = optionListWithFiveArrays[rowIndex]
			
			## Create a combo box
			self.optionListComboBox = QComboBox(self)
			self.optionListComboBox.setGeometry(900, 80, 100, 20)
			self.optionListComboBox.setMinimumContentsLength(45)
			self.connect(self.optionListComboBox, SIGNAL("currentIndexChanged(int)"),
							self.optionSelected)
			self.optionListComboBox.show()
			
			## save the right word
			if len(requiredWordList) > 0:
				if rowIndex not in self.rightOptionList.keys():
					if len(requiredWordList) > 0:
						# the first item always hold the correct answer option
						correctOption = requiredWordList[0]
						## save the correct answer in the below list
						self.rightOptionList[rowIndex] = correctOption

			## insert words in the combo box
			random.shuffle(requiredWordList)
			random.shuffle(requiredWordList)
			
			self.optionListComboBox.addItem('               ')
			self.optionListComboBox.addItems(requiredWordList)
	
	def optionSelected(self):
		## Avoid the blank option
		if len(str(self.optionListComboBox.currentText()).strip()) > 0:
			sentence = self.currentQuestionListInTable[self.selectedSentenceIndex]
			item = QTableWidgetItem(QString(sentence + ' - ' + self.optionListComboBox.currentText()))
			item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable | 
										Qt.ItemIsEnabled))
			self.passageQuestionsTable.setItem(self.selectedSentenceIndex, 0, item)
	
	def createIndexForWords(self):
		self.indexForOptions = {}
		self.nextIndex = 0
		for option in self.refWordListForIndex:
			if self.nextIndex == 5:
				break
			self.indexForOptions[option] = self.nextIndex
			self.nextIndex = self.nextIndex + 1
	
	def itemSelect(self,rowIndex):
		self.createComboBox(rowIndex)
		self.selectedSentenceIndex = rowIndex
		

def main():
	import sys
	app = QApplication(sys.argv)
	ex = PassageQuestionsDlg()
	ex.show()
	app.exec_()
	
if __name__ == '__main__':
	main()
