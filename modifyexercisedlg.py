#!/usr/bin/env python
from __future__ import division 
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QString, QStringList)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem,
						QMessageBox, QInputDialog, QFileDialog)
import ui_modifyexercisedlg
import addExerciseDlg
import sys
import MySQLdb
import data

class ModifyExerciseDlg(QDialog, 
					ui_modifyexercisedlg.Ui_ModifyExerciseDlg):
	
	def __init__(self, parent=None):
		super(ModifyExerciseDlg, self).__init__(parent)
		self.setupUi(self)
		self.wordList = []
		
		self.tableLoaded = True
		self.toModifyRows = {}
		self.col = 0
		# Add entries into the combo box
		self.blankSpace = "         "
		self.exerciseComboBox.addItem(self.blankSpace)
		
		# get the list of exercises
		self.getExerciseList()
		
		self.wordListTableWidget.horizontalHeader().setStretchLastSection(True)
		self.wordListTableWidget.resizeColumnsToContents()
		
		self.connect(self.exerciseComboBox, SIGNAL("currentIndexChanged(int)"),
						self.getWordForExercise)
						
		self.connect(self.wordListTableWidget, SIGNAL("cellClicked(int, int)"),
						self.wordStateChanged)
						
		self.connect(self.deleteWordButton, SIGNAL("clicked()"),
						self.deleteWordClicked)
						
		self.connect(self.addWordLineEdit, SIGNAL("returnPressed()"),
						self.addNewWord)
						
		self.connect(self.loadWordsButton, SIGNAL("clicked()"),
						self.loadWords)
						
		self.connect(self.addExerciseButton, SIGNAL("clicked()"),
						self.addExercise)
						
		#self.saveButton.setEnabled(False)
	
		# delete an exercise from the database
		self.connect(self.deleteExercisePushButton, SIGNAL("clicked()"),
						self.deleteExercise)
	
	def getExerciseList(self):
		self.exerciseList = data.Data().getExerciseList()
		
		if len(self.exerciseList) > 0:
			for item in self.exerciseList:
				self.exerciseComboBox.addItem(item)
		
	
	def getWordForExercise(self):
		
		exerciseName = str(self.exerciseComboBox.currentText()).strip()
		if len(exerciseName) > 0:			
			self.wordList = data.Data().getWordList(str(self.exerciseComboBox.currentText()))
			
			# from copy import deepcopy
			#listB = deepcopy(listA)
			self.oldCacheWordList = self.wordList[:]
			self.wordListTableWidget.setRowCount(len(self.wordList))
			cellList = []
			for word in self.wordList:
				item = QTableWidgetItem(QString(word))
				item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
								Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
				item.setCheckState(Qt.Unchecked)
				cellList.append(item)
			cellList.reverse()
			
			for i in range(0, len(self.wordList)):
				self.wordListTableWidget.setItem(i, self.col, cellList.pop())
	
	def loadWords(self):
		fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')
		if len(str(fname).strip()) > 0:			
			fileOpened = open(fname, 'r')
			wordList = []
			#cellList = []
			while 1:
				word = fileOpened.readline()
				if not word:
					break 
				else:
					wordList.append(str(word).strip().lower())
					
			#### Add the loadded words to the database 
			for word in wordList:
				if word not in self.wordList:
					data.Data().saveNewWordsToDatabase(str(self.exerciseComboBox.currentText()), word)
				else:
					pass
			
			#### call the getWords method to load all the values
			self.getWordForExercise()
		
	def addExercise(self):
		exerciseDialog = addExerciseDlg.AddExerciseDlg(self)
		
		if exerciseDialog.exec_():
			pass 
		else:
			if len(exerciseDialog.exerciseName.strip()) > 0:
				self.exerciseComboBox.addItem(exerciseDialog.exerciseName)
			
	def deleteExercise(self):
		# remove the exercise name from the exercise table
		if (self.exerciseComboBox.currentText() == self.blankSpace):
			QMessageBox.information(self, "Modify Exercise - Delete",
			"Select an Exercise")
		else:
			data.Data().deleteExerciseName(str(self.exerciseComboBox.currentText()).strip())
			# drop or delete the table from the database
			data.Data().removeExerciseTable(str(self.exerciseComboBox.currentText()).strip())
			self.wordListTableWidget.clearContents()
			self.exerciseComboBox.removeItem(self.exerciseComboBox.currentIndex())
			QMessageBox.information(self, "Modify Exercise - Delete",
			"Exercise Deleted")
			
	def addNewWord(self):
		if (self.exerciseComboBox.currentText() == self.blankSpace):
			QMessageBox.information(self, "Modify Exercise - Delete",
			"Select the an exercise")
		else:
			word = self.addWordLineEdit.text().trimmed().toLower()
			if(len(word) > 0):
				# get the words in the Table Widget
				self.getWordsInTableWidget()
				if word not in self.wordListInTableWidget:
					# insert the word in the database
					rowsAdded = data.Data().saveNewWordsToDatabase(str(self.exerciseComboBox.currentText()), word)
					# Add the current added word to the Table Widget
					item = QTableWidgetItem(QString(word))
					item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
									Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
					item.setCheckState(Qt.Unchecked)
					self.getWordForExercise()
					# set the line edit to empty
					self.addWordLineEdit.setText("")
					
				else:
					QMessageBox.information(self, "Modify Exercise - Add Word",
					"Word already exits in the exercise")
				
	def getWordsInTableWidget(self):
		self.wordListInTableWidget = []
		
		for index in range(0, self.wordListTableWidget.rowCount()):
			self.wordListInTableWidget.append(self.wordListTableWidget.item(index, self.col).text())
		
				
	def editWordClicked(self):
		self.userAction = "edit"
		#self.addWordButton.setEnabled(False)
		self.deleteWordButton.setEnabled(False)
		# Show information to the user when no exercise is selected
		if (self.exerciseComboBox.currentText() == self.blankSpace):
			QMessageBox.information(self, "Modify Exercise - Edit",
			"Select an exercise")
		else:
			col = 0		
			for row in range(0, self.wordListTableWidget.rowCount()):
				if (self.wordListTableWidget.item(row, col).checkState() == 2):
					#self.wordList.pop(row)
					#self.wordList.insert(row, self.wordListTableWidget.item(row,col).text())
					self.wordListTableWidget.item(row, col).setCheckState(Qt.Unchecked)
			
			#for j in range(0, len(self.wordList)):
			#	print(self.wordList[j])
			# empty the toModifyRows list
			#self.toModifyRows = []	
			self.saveButton.setEnabled(True)

	def wordStateChanged(self, row, col):
		if (self.wordListTableWidget.item(row, col).checkState() == 2):
			self.toModifyRows[row] = self.wordListTableWidget.item(row, col).text()
			#print(self.wordListTableWidget.item(row, col).text())
			self.wordListTableWidget.item(row, col).setFlags(Qt.ItemFlags(Qt.ItemIsEditable |
									Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable))
		else:
			self.wordListTableWidget.item(row,col).setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
						Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
			del self.toModifyRows[row]
		
	def deleteWordClicked(self):
		# Show information to the user when no exercise is selected
		if (self.exerciseComboBox.currentText() == self.blankSpace):
			QMessageBox.information(self, "Modify Exercise - Delete",
			"Select an exercise")
		elif len(self.toModifyRows) == 0:
			QMessageBox.information(self, "Modify Exercise - Delete",
			"Select the Words to Delete")
		else:
			reply = QMessageBox.question(self, 
					"Modify Exercise - Delete Words", 
					"You want to delete the selected rows?",
					QMessageBox.Yes | QMessageBox.No)
			
			if reply == QMessageBox.Yes:
				
				for word in self.toModifyRows:
					if word in self.wordList:
						self.wordList.remove(word)
				
				self.wordListTableWidget.clearContents()
				
				# to be put in a seperate method
				cellList = []
				for word in self.wordList:
					item = QTableWidgetItem(QString(word))
					item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
									Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
					item.setCheckState(Qt.Unchecked)
					cellList.append(item)
				# reverses the list 
				cellList.reverse()
				
				# cellList.pop() removes the item from the list and returns the item
				for i in range(0, len(self.wordList)):
					self.wordListTableWidget.setItem(i, self.col, cellList.pop())
				
				# sets the QTableWidget row length based on the wordList length
				self.wordListTableWidget.setRowCount(len(self.wordList))
				
				deleteWords = []
				for word in self.toModifyRows.values():
					deleteWords.append(word)
				
				rowsDeleted = data.Data().deleteWordsFromDatabase(str(self.exerciseComboBox.currentText()), deleteWords)
				self.getWordForExercise()
				
				self.toModifyRows = {}
				
	def addWordClicked(self):
		self.userAction = "add"
		self.deleteWordButton.setEnabled(False)
		self.editWordButton.setEnabled(False)
		# Show information to the user when no exercise is selected
		if (self.exerciseComboBox.currentText() == self.blankSpace):
			QMessageBox.information(self, "Modify Exercise - Add",
			"Select the an exercise")
		else:
			# Get the input using the QInputDialog
			rows, ok = QInputDialog.getInt(self, 'Add Words',
					'Enter the number of words to add')
			if ok:
				#print(rows)
				col = 0
				if rows > 0:
					rowCount = self.wordListTableWidget.rowCount()
					rowCount = rowCount + rows
					oldWordListTableLength = self.wordListTableWidget.rowCount()
					self.wordListTableWidget.setRowCount(rowCount)
					#print("The length is "+str(self.wordListTableWidget.rowCount()))
					#print("The total length is "+str(rowCount))
					for index in range(oldWordListTableLength, rowCount):
						item = QTableWidgetItem(QString(''))
						item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
										Qt.ItemIsUserCheckable |
										Qt.ItemIsEnabled))
						item.setCheckState(Qt.Unchecked)
						self.wordListTableWidget.setItem(index, col, item)
						
			self.saveButton.setEnabled(True)
	
	def saveClicked(self):
		modified = False
		col = 0
		self.wordListInTableWidget = []
		self.wordsToSaveInDatabase = []
		self.wordsToDeleteFromDatabase = []
		self.wordsToUpdateInDatabase = {}
		for index in range(0, self.wordListTableWidget.rowCount()):
			text = self.wordListTableWidget.item(index, col).text()
			if len(text) > 0:
				self.wordListInTableWidget.append(self.wordListTableWidget.item(index, col).text())
		
		
		if len(self.oldCacheWordList) == len(self.wordListInTableWidget) and (not self.isWordsChanged()):
			QMessageBox.information(self, "Modify Exercise",
			"Nothing To Change, No Modification Done")
			#self.addWordButton.setEnabled(True)
			self.deleteWordButton.setEnabled(True)
			self.editWordButton.setEnabled(True)
		else:
			# Logic to add the extra words in the Database
			if self.userAction == "add":
				for word in self.wordListInTableWidget:
					if word not in self.oldCacheWordList:
						self.wordsToSaveInDatabase.append(word)
			
				# save the new words in the database
				rowsAdded = data.Data().saveNewWordsToDatabase(str(self.exerciseComboBox.currentText()), self.wordsToSaveInDatabase)
				
				if (rowsAdded == len(self.wordsToSaveInDatabase)):
					modified = True
					QMessageBox.information(self, "Modify Exercise",
							"Successfully Added "+ str(rowsAdded) + " Rows")
			else:
				index = 0
				for word in self.wordListInTableWidget:
					if word not in self.oldCacheWordList:
						self.wordsToUpdateInDatabase[index] = word
					index = index + 1
				
				# update the words in the database
				rowsUpdated = data.Data().updateWordsFromDatabase(str(self.exerciseComboBox.currentText()), 
						self.wordsToUpdateInDatabase, self.oldCacheWordList)
				
				if (rowsUpdated == len(self.wordsToUpdateInDatabase)):
					modified = True
					QMessageBox.information(self, "Modify Exercise",
							"Successfully Updated "+ str(rowsUpdated) + " Rows")

			self.userAction = ""
			#self.toModifyRows = []
			#self.addWordButton.setEnabled(True)
			self.deleteWordButton.setEnabled(True)
			self.editWordButton.setEnabled(True)
			# reload all the contents after the changes
			if modified:
				self.getWordForExercise()
			
	def isWordsChanged(self):
		for word in self.wordListInTableWidget:
			if word in self.oldCacheWordList:
				continue 
			else:
				return True
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = ModifyExerciseDlg()
	form.show()
	app.exec_()
