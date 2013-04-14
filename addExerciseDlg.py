#!/usr/bin/env python
from __future__ import division 
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QString, QStringList)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem,
						QMessageBox, QInputDialog, QFileDialog)

import ui_addExercisedlg						
import sys
import data 

class AddExerciseDlg(QDialog, 
			ui_addExercisedlg.Ui_AddExerciseDlg):
	
	def __init__(self, parent=None):
		super(AddExerciseDlg, self).__init__(parent)
		self.setupUi(self)
		
		# load all the exercise names
		# get the exercise name, do validation, 
		# exercise name cannot be empty and description can be empty
		# Insert the exercise name and description in the table 
		# repopulate the values so that future checks for the exercise
		# name can be done. 
		
		self.exerciseName = ""
		
		self.getExerciseList()
		
		self.connect(self.addExerciseButton, SIGNAL("clicked()"),
						self.addExercise)
	
	def getExerciseList(self):
		self.exerciseList = data.Data().getExerciseList()
	
	def addExercise(self):
		self.exerciseName = str(self.exerciseNameLineEdit.text().trimmed()).lower()
		if len(self.exerciseName) > 0:
			for exercise in self.exerciseList:
				if exercise.lower() == self.exerciseName.lower():
					QMessageBox.information(self, "Add Exercise",
							"An exercise with this name already exist")
					break 
			else:
				textAreaString = str(self.descriptionTextEdit.toPlainText()).strip()
				# Add the exercise name in the Exercises table
				data.Data().addExercise(self.exerciseName, textAreaString)
				
				# create a table for this exercise
				data.Data().createExerciseTable(self.exerciseName)
				
				self.exerciseNameLineEdit.setText("")
				self.descriptionTextEdit.setText("")
				QMessageBox.information(self, "Add Exercise",
						"Exercise Created")
				self.getExerciseList()
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = AddExerciseDlg()
	form.show()
	app.exec_()
