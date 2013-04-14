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
import ui_applicationstartdlg
import wordflashdlg
import synonymmatchdlg
import selectsentencefillleveldlg
import selectpassagedlg

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class ApplicationStartDlg(QDialog, 
			ui_applicationstartdlg.Ui_ApplicationStartDlg):
				
	def __init__(self, parent=None):
		super(ApplicationStartDlg, self).__init__(parent)
		self.setupUi(self)
		
		self.connect(self.wordFlashButton, SIGNAL("clicked()"), self.wordFlashClicked)
		self.connect(self.synonymMatchButton, SIGNAL("clicked()"), self.synonymMatchClicked)
		self.connect(self.antonymMatchButton, SIGNAL("clicked()"), self.antonymMatchClicked)
		self.connect(self.sentenceFillButton, SIGNAL("clicked()"), self.sentenceFillClicked)
		self.connect(self.readingComprehensionButton, SIGNAL("clicked()"), self.readingComprehensionClicked)

	# logic to show the word flash dialog
	def wordFlashClicked(self):
		wordFlashObjDlg = wordflashdlg.WordFlashDlg()
		if wordFlashObjDlg.exec_():
			pass 
	
	# logic to show the synonym match dialog
	def synonymMatchClicked(self):
		option = 'Synonyms'
		synonymMatchObjDlg = synonymmatchdlg.SynonymMatchDlg(option)
		if synonymMatchObjDlg.exec_():
			pass 

	# logic to show the antonym match dialog
	def antonymMatchClicked(self):
		option = 'Antonyms'
		synonymMatchObjDlg = synonymmatchdlg.SynonymMatchDlg(option)
		if synonymMatchObjDlg.exec_():
			pass 
	
	# logic to show the sentence fill dialog
	def sentenceFillClicked(self):
		selectsentencefilllevelObjDlg = selectsentencefillleveldlg.SelectSentenceFillLevelDlg()
		if selectsentencefilllevelObjDlg.exec_():
			pass 
			
	# logic to show the reading comprehension dialog
	def readingComprehensionClicked(self):
		selectpassagedlgObjDlg = selectpassagedlg.SelectPassageDlg()
		if selectpassagedlgObjDlg.exec_():
			pass
		
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	# start the application dialog
	form = ApplicationStartDlg()
	form.show()
	app.exec_()
