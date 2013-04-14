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

import ui_selectpassagedlg
import passagecontentdlg
import random
import data

class SelectPassageDlg(QDialog, ui_selectpassagedlg.Ui_SelectPassageDlg):
	
	
	def __init__(self, parent=None):
		super(SelectPassageDlg, self).__init__(parent)
		self.setupUi(self)
		# initialize the screen and load data from database
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle('Reading Comprehension - Passage Select')
		# get the passage list from the database
		self.getPassagesFromDatabase()
		self.connect(self.continueButton, SIGNAL('clicked()'), self.onContinueClicked)
		

	def getPassagesFromDatabase(self):
		self.passageMap = data.Data().getPassageList()
		self.passageList = sorted(self.passageMap.keys())
		self.passagecomboBox.addItems(self.passageList)
		
		
	def onContinueClicked(self):
		passageName = str(self.passagecomboBox.currentText())
		if passageName in self.passageMap:
			self.passageTableName = self.passageMap[passageName]
			passageContentDlg = passagecontentdlg.PassageContentDlg(self.passageTableName)
			if passageContentDlg.exec_():
				pass
			

def main():
	import sys
	app = QApplication(sys.argv)
	ex = SelectPassageDlg()
	ex.show()
	app.exec_()
	
if __name__ == '__main__':
	main()
	
