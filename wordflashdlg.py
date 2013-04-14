#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import re
import sys
import MySQLdb
from PyQt4.QtCore import (Qt, SIGNAL, QTimer, QString)
from PyQt4.QtGui import (QApplication, QDialog, QMessageBox, 
						QPalette, QColor, QLabel)
import ui_wordflashdlg
import wordflashresultdlg
import modifyexercisedlg
import data
import random

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class WordFlashDlg(QDialog,
			ui_wordflashdlg.Ui_WordFlashDlg):
	
	def __init__(self, parent=None):
		super(WordFlashDlg, self).__init__(parent)
		self.setupUi(self)
		if not MAC:
			self.settingsButton.setFocusPolicy(Qt.NoFocus)
			self.startButton.setFocusPolicy(Qt.NoFocus)
			self.submitButton.setFocusPolicy(Qt.NoFocus)
			self.nextButton.setFocusPolicy(Qt.NoFocus)
			self.closeButton.setFocusPolicy(Qt.NoFocus)
			
		self.wordIndex = 0
		
		# user speed choice
		self.speedSlot = {}
		self.speedSlot[1] = (20, 1)
		self.speedSlot[2] = (30, 2)
		self.speedSlot[3] = (40, 2)
		self.speedSlot[4] = (50, 3)
		self.speedSlot[5] = (60, 3)
		
		# set the correct result list
		self.rightResult = []
		
		# set the wrong result list
		self.wrongResult = []
		
		self.textEditor.selectAll()
		
		# set tool tip for Settings button
		self.settingsButton.setToolTip('Settings for Word Flash')
		
		# set tool tip for start button
		self.startButton.setToolTip('Start Word Flash')
		
		# set tool tip for shuffle button
		self.shuffleButton.setToolTip("Shuffle the words")
		
		# set tool tip for next button
		self.nextButton.setToolTip('Next Word')
		self.nextButton.setEnabled(False)
		
		# set tool tip for submit button
		self.submitButton.setToolTip('Submit Word')
		self.submitButton.setEnabled(False)
		
		# set tool tip for close button
		self.closeButton.setToolTip('Close Word Flash')
		
		# Action when start button is clicked
		self.connect(self.startButton, SIGNAL("clicked()"), self.startClicked)
		# Action when submit button is clicked
		self.connect(self.submitButton, SIGNAL("clicked()"), self.submitClicked)
		# Action when nextt button is clicked
		self.connect(self.nextButton, SIGNAL("clicked()"), self.nextClicked)
		# Action any text is typed and return is pressed
		self.connect(self.textEditor, SIGNAL("returnPressed()"),
						self.submitClicked)
						
		# Action when settings button is clicked
		self.connect(self.settingsButton, SIGNAL("clicked()"), self.settingsClicked)
		
		# Action when shuffle button is clicked
		self.connect(self.shuffleButton, SIGNAL("clicked()"), self.shuffleWords)
		
		# get the words for the exercise
		self.connect(self.exercisecomboBox, SIGNAL("currentIndexChanged(int)"),
						self.getWordForExercise)
		
		# create a Timer event
		self.displayTimer = QTimer()
		
		self.blankSpace = "         "
		# Add items into the combox box
		self.exercisecomboBox.addItem(self.blankSpace)
		self.exercisecomboBox.setDuplicatesEnabled(False)
		self.getExerciseList()
		
	
	def getExerciseList(self):
		self.exerciseList = []
		self.exerciseList = data.Data().getExerciseList()
		
		if len(self.exerciseList) > 0:
			for item in self.exerciseList:
				self.exercisecomboBox.addItem(item)
		
	def getWordForExercise(self):
		if not (self.exercisecomboBox.currentText() == self.blankSpace):
			self.wordList = data.Data().getWordList(str(self.exercisecomboBox.currentText()))
		
	def startClicked(self):
		if (self.exercisecomboBox.currentText() == self.blankSpace):
			QMessageBox.information(self, "WordFlash",
			"Select An Exercise")
			
		else:
			self.textEditor.setEnabled(False)
			self.callTimer()
			
			self.speedSpinBox.setEnabled(False)
			self.startButton.setEnabled(False)
			self.nextButton.setEnabled(True)
			self.exercisecomboBox.setEnabled(False)
			self.submitButton.setEnabled(True)
			
	
	def shuffleWords(self):
		if (self.exercisecomboBox.currentText() == self.blankSpace):
			QMessageBox.information(self, "WordFlash",
			"Select An Exercise")
		else:
			random.shuffle(self.wordList)
			self.shuffleButton.setEnabled(False)
			
		
	def callTimer(self):
		self.displayTimer = QTimer(interval=self.speedSlot[self.speedSpinBox.value()][0], timeout=self.timeOut)
		self.wordGen = self.generateWord()
		self.displayTimer.start()
		
		self.displayTimer.singleShot((self.speedSlot[self.speedSpinBox.value()][1] * 1000), self.hideLabel)
		
		self.displayTimer.singleShot((self.speedSlot[self.speedSpinBox.value()][1] * 1100), self.enableTextEditor)
		
	def generateWord(self):
		for i in range(len(self.wordList[self.wordIndex])+1):
			yield self.wordList[self.wordIndex][:i]
			
	def timeOut(self):
		for acum in self.wordGen:
			self.displayLabel.setText(acum)
			return
		self.displayTimer.stop()
		
	def hideLabel(self):
		self.displayLabel.setText("")
		
	def enableTextEditor(self):
		self.textEditor.setEnabled(True)
	
	def submitClicked(self):
		if not self.submitButton.isEnabled():
			self.textEditor.setText('')
			return
		
		self.submitButton.setEnabled(False)
		wordStr = self.wordList[self.wordIndex]
		
		# check whether the user has entered the right word
		
		if self.textEditor.text() != self.wordList[self.wordIndex]:
			self.resultLabel.setText(self.wordList[self.wordIndex])
			self.wrongResult.append((self.textEditor.text(),self.wordList[self.wordIndex]))
			self.judgeLabel.setText("Wrong!!!")
			self.judgeLabel.setStyleSheet("QLabel {color : red; }")
			self.textEditor.setEnabled(False)
		else:
			self.rightResult.append(self.textEditor.text())
			self.judgeLabel.setText("Right!!!")
			self.judgeLabel.setStyleSheet("QLabel {color : green; }")
			self.textEditor.setText("  ")
			self.textEditor.setEnabled(False)
		
	def nextClicked(self):
		# Add words to the wrong list if the user skips the word and
		# moves to the next word
		if len(self.textEditor.text()) == 0 and self.wordIndex < len(self.wordList):
			self.wrongResult.append((self.textEditor.text(),self.wordList[self.wordIndex]))
		
		self.textEditor.setText("")
		self.textEditor.setEnabled(False)
		self.resultLabel.setText("")
		self.judgeLabel.setText("")
		self.submitButton.setEnabled(True)
		
		# move to index position
		self.wordIndex = self.wordIndex + 1
		
		if self.wordIndex < len(self.wordList):
			self.callTimer()
			
		else:
			self.nextButton.setEnabled(False)
			self.startButton.setEnabled(True)
			self.shuffleButton.setEnabled(True)
			self.speedSpinBox.setEnabled(True)
			self.exercisecomboBox.setEnabled(True)
			self.submitButton.setEnabled(False)
			self.wordIndex = 0
			if self.showResult():
				self.score = "%d / %d" % (len(self.rightResult), len(self.wordList))
				# pass the parameters necessary for the wordFalshResultDlg
				resultDialog = wordflashresultdlg.WordFlashResultDlg(self.score, 
									self.rightResult, self.wrongResult)
				if resultDialog.exec_():
					pass 
			
			self.rightResult = []
			self.wrongResult = []
			
	def showResult(self):
		reply = QMessageBox.question(self,
				"WordFalsh Completed",
				"You want to see the results?",
				QMessageBox.Yes|QMessageBox.No)
		if reply == QMessageBox.No:
			return False
		elif reply == QMessageBox.Yes:
			return True
	
	def settingsClicked(self):
		settingsDialog = modifyexercisedlg.ModifyExerciseDlg(self)
		if settingsDialog.exec_():
			pass
		else:
			# remove the excercise list and re-populate it
			indexList = len(self.exerciseList)
			while indexList > 0:
				self.exercisecomboBox.removeItem(indexList)
				indexList = indexList - 1
			self.getExerciseList()
		
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	form = WordFlashDlg()
	form.show()
	app.exec_()
