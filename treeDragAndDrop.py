#!/usr/local/bin/python
 
# dragdrop.py
 
import sys
from PyQt4 import QtGui,QtCore
 
class treeWidgetClass(QtGui.QTreeWidget):
	def mimeTypes(self):
		types = QtCore.QStringList()
		types.append("text/plain")
		return types
 
	def fmimeData(text):
		customMimeData = QtCore.QMimeData()
		customText = QtCore.QString()
		customMimeData.setText(customText)
		return customMimeData
 
	def mousePressEvent(self, event):
		button = event.button()
		item = self.itemAt(event.x(), event.y())
 
		if item:
			seqBrowserMimeData = self.fmimeData()
			seqBrowserMimeData.setText(item.text(0))
			print item.text(0)
			# select the item we clicked
			self.setCurrentItem(item)
			if button == 1:
				print ('LEFT CLICK - DRAG')
			if button == 2:
				print ('RIGHT CLICK')
			else:
				print("select something you goober")
				pass
 
	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat('text/plain'):
			event.accept()
 
	def dropEvent(self, event):
		list = QtCore.QStringList()
		list = self.mimeTypes()
 
##### THIS IS A COMPLETE HACK but for now 25 characters is what I need to strip off to make the string proper?
### its putting in a data structure array somehow still
		text = event.mimeData().text()
		text = text[25:]
		#print "dropped"
		print (text)

 
class DragDrop(QtGui.QDialog):
	
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
 
		self.resize(280, 150)
		self.setWindowTitle('Simple Drag & Drop')
 
		treeWidget = treeWidgetClass(self)
		treeWidget.setDragEnabled(True)
		treeWidget.setAcceptDrops(True)
		treeWidget.move(30, 65)
		 
		treeWidget2 = treeWidgetClass(self)
		treeWidget2.setDragEnabled(True)
		treeWidget2.setAcceptDrops(True)
		treeWidget2.move(300, 65)
 
 
		#button = Button("Button", self)
		#button.move(170, 65)
		item = QtGui.QTreeWidgetItem(treeWidget)
		item.setText(0,QtGui.QApplication.translate("", "Vijayakumar ", None, QtGui.QApplication.UnicodeUTF8))
		
		item2 = QtGui.QTreeWidgetItem(treeWidget)
		item2.setText(0,QtGui.QApplication.translate("", "Vijayakumar Raju ", None, QtGui.QApplication.UnicodeUTF8))
 
 
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
 
app = QtGui.QApplication(sys.argv)
icon = DragDrop()
icon.show()
app.exec_()
