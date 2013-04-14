from __future__ import division
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4 import QtCore
from PyQt4.QtGui import *
from numpy.random import *

class sheet(QDialog):
	def __init__(self, arr, parent=None):
		QWidget.__init__(self) 
	
		tablemodel = MyTableModel(arr, self) 
		self.tabmod=tablemodel
		tableview = QTableView() 
		tableview.setModel(tablemodel) 
	
		layout = QVBoxLayout(self) 
		layout.addWidget(tableview) 
		self.setLayout(layout)

class MyTableModel(QAbstractTableModel): 
	def __init__(self, datain, parent=None):
		QAbstractTableModel.__init__(self, parent) 
		self.arraydata = datain 
	
	def rowCount(self, parent): 
		return len(self.arraydata) 
	
	def columnCount(self, parent): 
		return len(self.arraydata[0]) 
	
	def data(self, index, role): 
		if not index.isValid(): 
			return QVariant() 
		elif role != Qt.DisplayRole and role != Qt.EditRole:
			return QVariant() 
		return QVariant(self.arraydata[index.row()][index.column()])
		
	def isEditable(self, index):
		""" Return true if the index is editable. """
		return True
		
	def flags(self, index):  #function is called to chaeck if itmes are changable etc, index is a PyQt4.QtCore.QModelIndex object
		if not index.isValid():
			return QtCore.Qt.ItemIsEnabled
		
		ret_flags = QtCore.Qt.ItemIsSelectable | QtCore.QAbstractItemModel.flags(self, index)
		if self.isEditable(index):
			#print index.row() #returns the selected elements row
			#print index.column()
			ret_flags = ret_flags | QtCore.Qt.ItemIsEditable
		return ret_flags


	def setData(self, index, value, role):
		""" if a item is edited, this command is called
		value.toString() constains the new value
		cahnge here to have it evaluate stuff!"""
		self.arraydata[index.row(),index.column()]=float(value.toString())
		return True
#<<<<<<<<<<< the problem (i think)

app = QApplication(sys.argv)
arr=rand(3,3)
form = sheet(arr)
form.show()
app.exec_()
