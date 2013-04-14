from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (QVariant, Qt, SIGNAL, QStringList, QString,
						QAbstractTableModel, QTimer, QSize, QRect)
from PyQt4.QtGui import (QApplication, QDialog, QTableWidgetItem, 
							QStringListModel, QVBoxLayout, QTableWidget,
							QLineEdit, QLabel, QFont)

#class Button(QtGui.QPushButton):
	
#	def __init__(self, title, parent):
#		super(Button, self).__init__(title, parent)
		
#	def mouseMoveEvent(self, e):
#		if e.buttons() != QtCore.Qt.RightButton:
#			return 
		
#		mimeData = QtCore.QMimeData()
#		drag = QtGui.QDrag(self)
#		drag.setMimeData(mimeData)
#		drag.setHotSpot(e.pos() - self.rect().topLeft())
		
#		dropAction = drag.start(QtCore.Qt.MoveAction)
		
#	def mousePressEvent(self, e):
#		if e.button() == QtCore.Qt.LeftButton:
#			print 'Left Button Pressed'
			
	
class MyTable(QTableWidget):
	
	def __init__(self, rows, columns, parent):
		super(MyTable, self).__init__(rows, columns, parent)
		self.setAcceptDrops(True)
		self.setDragEnabled(True)
		#self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		#self.resizeRowsToContents()
		self.verticalHeader().geometriesChanged \
			.connect(self.updateGeometryAsync)
		self.verticalHeader().sectionResized \
			.connect(self.updateGeometryAsync)
		
		for index in range(0, rows):
			self.setRowHeight(index, 80)
			
		self.setFixedHeight(400)
	
	def sizeHint(self):
		height = QTableWidget.sizeHint(self).height()
		
		width = self.horizontalHeader().length()
		
		width = width + self.verticalHeader().width()
		width = width + self.verticalScrollBar().width()
		
		margins = self.contentsMargins()
		width = width + margins.left() + margins.right()
		
		return QSize(width, height)
		
	def updateGeometryAsync(self):
		QTimer.singleShot(0, self.updateGeometry)
		
	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat('text/plain'):
			e.accept()
		else:
			e.ignore()
		
	def dropEvent(self, e):
		position = e.pos()
		print(position)
		
		row = self.rowAt(position.y())
		
		column = self.rowAt(position.x())
		
		print (e.mimeData().text())
		item = QTableWidgetItem(QString(e.mimeData().text()))
		item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
							Qt.ItemIsUserCheckable | Qt.ItemIsEnabled))
		item.setCheckState(Qt.Unchecked)
		
		self.setItem(row, column, item)
		
		e.setDropAction(Qt.MoveAction)
		e.accept()
		
		#self.butObject.move(position)
		
		#row = self.rowAt(position.y())
		
		#column = self.columnAt(position.x())
		
		#item = QtGui.QTableWidgetItem(self.butObject)
		
		#self.setCellWidget(row, column, self.butObject)
		#self.setCellWidget(row, column, item)
		#self.setItem(row, column, item)
		
		
	def itemSelect(self, event):
		print ('Item clicked')
	
	def dragMoveEvent(self, e):
		e.accept()

class MyLineEdit(QLineEdit):
	
	def __init__(self, title, tableWidget, parent):
		super(MyLineEdit, self).__init__(title,parent)
		self.title = title
		self.tableWidget = tableWidget
	
	def focusInEvent(self, event):
		print ('here')
		print (self.text())
		self.selectAll()
		self.setSelection(0, len(self.title))
		item = QTableWidgetItem(QString(self.text()))
		item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
						Qt.ItemIsEnabled))
		print ('The index is' + str(self.selectedItemIndex))
		self.tableWidget.setItem(self.selectedItemIndex, 0, item)
			
class Example(QDialog):
	
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()
		
	def initUI(self):
		#self.setAcceptDrops(True)
		
		fontLabel = QFont('SansSerif',14)
		
		self.label = QLabel(self)
		self.label.setAutoFillBackground(True)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setText('Match the Synonyms')
		self.label.setGeometry(QRect(200, 10, 231, 40))
		self.label.setFont(fontLabel)
		
		#self.button = Button('Button', self)
		#self.button.move(50, 200)
		
		#self.label = QtGui.QLabel('Vijayakumar Raju')
		#self.label.move(50,300)
		#mimeData = QtCore.QMimeData()
		#drag = QtGui.QDrag(self.label)
		#drag.setMimeData(mimeData)
		#drag.setHotSpot(e.pos() - self.rect().topLeft())
		
		
		self.wordsToMatch = MyTable(5, 1, self)
		self.wordsToMatch.move(10,80)
		self.wordsToMatch.setAcceptDrops(False)
		self.wordsToMatch.setDragEnabled(False)
		
		self.wordsToMatch.setColumnCount(1)
		wordsToMatchHeaderList = ['Words To Match']
		self.wordsToMatch.setHorizontalHeaderLabels(wordsToMatchHeaderList)
		self.wordsToMatch.resizeColumnsToContents()
		#self.wordsToMatch.resizeRowsToContents()
		self.wordsToMatch.horizontalHeader().setStretchLastSection(True)
		self.wordsToMatch.verticalHeader().setStretchLastSection(True)
		
		self.wordList = []
		self.wordList.append('Clever')
		self.wordList.append('disturbance')
		self.wordList.append('complexity')
		self.wordList.append('trivial')
		self.wordList.append('brave')
		
		cellList = []
		self.col = 0
		for word in self.wordList:
			item = QTableWidgetItem(QString(word))
			item.setFlags(Qt.ItemFlags(Qt.ItemIsSelectable |
						Qt.ItemIsEnabled))
			cellList.append(item)
		cellList.reverse()
		
		for i in range(0, len(self.wordList)):
			self.wordsToMatch.setItem(i, self.col, cellList.pop())			
		
		self.connect(self.wordsToMatch, SIGNAL("cellClicked(int, int)"), self.itemSelect)
		
		self.matchedTable = MyTable(5, 1, self)
		self.matchedTable.setAcceptDrops(True)
		self.matchedTable.setDragEnabled(True)
		self.matchedTable.move(500, 80)
		
		self.matchedTable.setColumnCount(1)
		matchedTableHeaderList = ['Matched Words']
		self.matchedTable.setHorizontalHeaderLabels(matchedTableHeaderList)
		self.matchedTable.resizeColumnsToContents()
		#self.matchedTable.resizeRowsToContents()
		self.matchedTable.horizontalHeader().setStretchLastSection(True)
		self.matchedTable.verticalHeader().setStretchLastSection(True)
		
		self.connect(self.matchedTable, SIGNAL("cellClicked(int, int)"), self.itemSelect)
		
		#self.edit = QLineEdit('Smart', self)
		#self.edit.setDragEnabled(True)
		#self.edit.setReadOnly(True)
		#self.edit.move(270,80)
		#self.edit.selectAll()
		
		self.edit = MyLineEdit('Smart', self.matchedTable, self)
		self.edit.setDragEnabled(True)
		self.edit.setReadOnly(True)
		self.edit.move(270, 80)
		
		self.edit.connect(self.edit, SIGNAL("clicked()"),
						self.editClicked)
		
		self.edit2 = MyLineEdit('entanglement', self.matchedTable , self)
		self.edit2.setDragEnabled(True)
		self.edit2.setReadOnly(True)
		self.edit2.move(270, 110)
		
		self.edit3 = MyLineEdit('agitation', self.matchedTable, self)
		self.edit3.setDragEnabled(True)
		self.edit3.setReadOnly(True)
		self.edit3.move(270, 140)
		
		self.edit4 = MyLineEdit('insignificant', self.matchedTable, self)
		self.edit4.setDragEnabled(True)
		self.edit4.setReadOnly(True)
		self.edit4.move(270, 170)
		
		self.edit5 = MyLineEdit('adventurous', self.matchedTable, self)
		self.edit5.setDragEnabled(True)
		self.edit5.setReadOnly(True)
		self.edit5.move(270, 200)
		
		self.setWindowTitle('Synonym Match')
		self.setGeometry(800, 800, 780, 550)
		
	def editClicked(self):
		print ('edit clicked')
		
	def itemSelect(self,rowIndex):
		print ('Item Select')
		#self.selectedItemIndex = rowIndex
		self.edit.selectedItemIndex = rowIndex
		self.edit2.selectedItemIndex = rowIndex
		self.edit3.selectedItemIndex = rowIndex
		self.edit4.selectedItemIndex = rowIndex
		self.edit5.selectedItemIndex = rowIndex
		
		
def main():
	import sys
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	app.exec_()
	
if __name__ == '__main__':
	main()	
