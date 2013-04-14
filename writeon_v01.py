#!/usr/bin/env python

import os
import sys

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import ( QString )
from time import sleep

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

		self.label.setText('')
		self.pushButton.clicked.connect(self.DoIt)


	def DoIt(self):

		text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna"

		accum = QString("")

		for i in range(0, len(text)):
			accum = accum + text[i]
			self.label.setText(accum)
			self.label.update()
			sleep(.01)



        def exit(self):
			quit()



def main():
	app = QtGui.QApplication(sys.argv)
	global form
	form = BasicWindow()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()

