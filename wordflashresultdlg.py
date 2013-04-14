#!/usr/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QStringList, QString)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem, QFont)

import ui_wordflashresultdlg


class WordFlashResultDlg(QDialog, ui_wordflashresultdlg.Ui_WordFlashResultDlg):
	
    def __init__(self, score, rightResult, wrongResult, parent=None):
        super(WordFlashResultDlg, self).__init__(parent)
        self.setupUi(self)
        self.score = unicode(score)
        self.resultLabel.setText(self.score)
        self.rightResult = rightResult
        self.wrongResult = wrongResult
        
        # headers for the table 
        headers = QStringList()
        #headers.append(QString("Index"))
        headers.append(QString("User Entry"))
        headers.append(QString("Correct Word"))
        
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        # signal for the right radio button
        self.connect(self.rightRadioButton, SIGNAL("clicked()"), self.rightClicked)
        
        # signal for the wrong radio button
        self.connect(self.wrongRadioButton, SIGNAL("clicked()"), self.wrongClicked)
        
        
    def rightClicked(self):
		#self.tableWidget.setColumnCount(3)
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(len(self.rightResult))
		self.tableWidget.removeColumn(1)
		cellList = []
		for word in self.rightResult:
			item = QTableWidgetItem(QString(word))
			item.setFlags(Qt.ItemIsEnabled) 
			cellList.append(item)
		
		cellList.reverse()
		for i in range(0, len(self.rightResult)):
			self.tableWidget.setItem(i, 0, cellList.pop())
		
		self.tableWidget.resizeColumnsToContents()
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		
    def wrongClicked(self):
		#self.tableWidget.setColumnCount(3)
		self.tableWidget.clearContents()
		#self.tableWidget.setColumnCount(2)
		self.tableWidget.removeColumn(0)
		self.tableWidget.setColumnCount(2)
		
		font = QFont()
		font.setBold(True)
		font.setWeight(75)
		
		item = QTableWidgetItem()
		item.setText(QApplication.translate("WordFalshResultDlg",
						"User Entry", None, QApplication.UnicodeUTF8))
		item.setFont(font)
		
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QTableWidgetItem()
		item.setText(QApplication.translate("WordFlashResultDlg",
						"Correct Word", None, QApplication.UnicodeUTF8))
		item.setFont(font)
		
		self.tableWidget.setHorizontalHeaderItem(1, item)
		
		self.tableWidget.setRowCount(len(self.wrongResult))
		#countIndex = 1
		cellList = []
		for r, w in self.wrongResult:
			itemr = QTableWidgetItem(QString(r))
			itemw = QTableWidgetItem(QString(w))
			itemr.setFlags(Qt.ItemIsEnabled)
			itemw.setFlags(Qt.ItemIsEnabled)
			cellList.append(itemr)
			cellList.append(itemw)
		cellList.reverse()	
		
		for i in range(0, len(self.wrongResult)):
			for j in range(0, 2):
				text = cellList.pop()
				self.tableWidget.setItem(i, j, text)
				
		self.tableWidget.resizeColumnsToContents()
		self.tableWidget.horizontalHeader().setStretchLastSection(True)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = WordFlashResultDlg(" ", ["V","I","J"], [("K","V"),("U","P"),("M","R")])
    form.show()
    app.exec_()
