from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QStringList, QString,
						QAbstractTableModel, QTimer, QSize, QRect)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem, 
							QStringListModel, QVBoxLayout, QTableWidget,
							QLineEdit, QLabel, QFont, QPushButton, 
							QMessageBox, QBrush, QColor, QHeaderView,
							QSizePolicy, QFrame, QComboBox)

import ui_passagecontentdlg
import random
import data
import passagequestionsdlg

class PassageContentDlg(QDialog, ui_passagecontentdlg.Ui_PassageContentDlg):
	
	def __init__(self, tableName, parent=None):
		super(PassageContentDlg, self).__init__(parent)
		self.tableName = tableName
		self.setupUi(self)
		# initialize the screen and load data from database
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle('Passage Content')
		#get the passage content from the database
		self.getPassageContent()
		self.connect(self.questionButton, SIGNAL('clicked()'), self.onQuestionClicked)
		
	def getPassageContent(self):
		self.textContent = data.Data().getPassageContent(self.tableName)
		self.passageText.setText(self.textContent)
		
	def onQuestionClicked(self):
		table = self.tableName
		passageQuestionsDlg = passagequestionsdlg.PassageQuestionsDlg(table, self)
		passageQuestionsDlg.show()
		#passageQuestionsDlg.activateWindow()
		#if passageQuestionsDlg.exec_():
		#	pass
	
def main():
	import sys
	app = QApplication(sys.argv)
	ex = PassageContentDlg()
	ex.show()
	app.exec_()
	
if __name__== '__main__':
	main()
