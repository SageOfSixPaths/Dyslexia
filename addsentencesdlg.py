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
						QMessageBox, QPalette, QColor, QLabel)
import ui_addsentencesdlg
import data
import random

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class AddSentencesDlg(QDialog,
		ui_addsentencesdlg.Ui_AddSentenceDlg):
			
	def __init__(self, parent=None):
		super(AddSentencesDlg, self).__init__(parent)
		self.setupUi(self)
		if not MAC:
			self.addSentenceButton.setFocusPolicy(Qt.NoFocus)
			self.closeButton.setFocusPolicy(Qt.NoFocus)
			self.removeButton.setFocusPolicy(Qt.NoFocus)
		
		## connect the add button	
		self.connect(self.addSentenceButton, SIGNAL("clicked()"), self.addSentence)
		
		## connect the return key with the QLineEdit
		#self.connect(self.wordLineEdit, SIGNAL("returnPressed()"), self.addSentence)
		
		## connect the remove button
		self.connect(self.removeButton, SIGNAL("clicked()"), self.removeSentence)
		
			
	def addSentence(self):
		## add sentence to the database table
		print ()
		sentenceText = str(self.sentenceTextEdit.toPlainText()).strip()
		optionOneText = str(self.optionOneLineEdit.text()).strip()
		optionTwoText = str(self.optionTwoLineEdit.text()).strip()
		optionThreeText = str(self.optionThreeLineEdit.text()).strip()
		optionFourText = str(self.optionFourLineEdit.text()).strip()
		optionFiveText = str(self.optionFiveLineEdit.text()).strip()
		
		if len(sentenceText) >0:
			if (len(optionOneText) > 0 and len(optionTwoText) > 0 
				and len(optionThreeText) >0 and len(optionFourText) > 0 and len(optionFiveText) > 0):
				## insert the sentence and word to a table
				successFullyInserted = data.Data().insertSentenceInTable(sentenceText, optionOneText, 
										optionTwoText, optionThreeText, optionFourText, optionFiveText)
				if not successFullyInserted:
					QMessageBox.information(self, "Add Sentence",
					"Error in Inserting the data")
				else:
					self.sentenceTextEdit.clear()
					self.optionOneLineEdit.clear()
					self.optionTwoLineEdit.clear()
					self.optionThreeLineEdit.clear()
					self.optionFourLineEdit.clear()
					self.optionFiveLineEdit.clear()
			else:
				QMessageBox.information(self, "Add Sentence",
				"Enter a word")
		else:
			QMessageBox.information(self, "Add Sentence",
			"Enter a sentence")

	def removeSentence(self):
		print ('Remove button clicked')
		## remove sentence from the table
		
		
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	form = AddSentencesDlg()
	form.show()
	app.exec_()
	
