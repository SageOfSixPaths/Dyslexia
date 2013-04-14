#!/usr/bin/env python

import os
import sys

from PyQt4 import QtCore, QtGui, uic, Qt
from PyQt4.QtCore import ( QString )

class BasicWindow(QtGui.QMainWindow):

	def __init__(self, parent=None):
		super(BasicWindow, self).__init__(parent)

		#self.setupUi(self)
		self.label = QtGui.QLabel(self)
		self.label.setGeometry(QtCore.QRect(73, 110, 574, 331))
		self.pushButton = QtGui.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(66, 30, 75, 27))
		self.pushButton.setText("DoIt")

		scrX = 2048
		scrY = 1150
		winX = 720
		winY = 530
		pX   = (scrX - winX) / 2
		pY   = (scrY - winY) / 2

		self.setGeometry(pX, pY, winX, winY)
		
		fontLabel = QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold)
		self.label.setFont(fontLabel)
		self.label.setStyleSheet("QLabel {color : blue; }")

		self.label.setText('')
		self.pushButton.clicked.connect(self.DoIt)
		self.label.setText(' ')
		self.timer = QtCore.QTimer(interval=100, timeout=self.timeout)
		#self.blankTimer = QtCore.QTimer(interval=5, timeout=self.timeoutBlank)
		
		# 400 - 300
		# 350 - 300
		# 200 - 250
		# 150 - 200
		# 130 - 200


	def DoIt(self):
		self.textGen = self.generateText()
		self.textBlank = "                "
		self.timer.start()
		print ('Call To Timer')
		
		#self.blankTimer.start()
		#self.timer.singleShot((1 * 3500), self.hideLabel)
	
	def hideLabel(self):
		self.label.setText('')
	
	def generateText(self):
		print ('Here in generateText')
		self.text = "misunderstanding"
		
		for i in range(1, len(self.text)+1):
			yield self.text[:i]

	def timeoutWord(self):
		print ('Here in Timeout')
		space = ''
		for accum in self.textGen:
			if len(accum) > 1:
				##print (accum[len(accum)-2])
				for i in range(0, (len(accum)-1)):
					space = space + ' '
					#print (space + accum[len(accum)-2])
				if len(self.text) == len(accum):
					self.label.setText(space + accum[len(accum)-2])
					
				else:
					self.label.setText(space + accum[len(accum)-2])
				return 
		for i in range(0, (len(self.text)-1)):
					space = space + ' '
		self.label.setText(space + self.text[len(self.text)-1])
		self.timer.stop()
		self.timer.singleShot((1 * 300), self.hideLabel)
		#self.label.setText('')
		
	def timeout(self):
		self.timeoutWord()
		self.label.repaint()
	
	def timeoutBlank(self):
		for let in self.textBlank:
			print (let[len(let)-2])
			self.label.setText(let[len(let)-2])
			return 
		self.blankTimer.stop()
		
def main():
	app = QtGui.QApplication(sys.argv)
	form = BasicWindow()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()


