import sys

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature, QTimer, QString,
							QPropertyAnimation, QRect)
from PyQt4.QtGui import (QApplication, QDialog, QFont, 
						QMessageBox, QPalette, QColor, QLabel,
						QWidget)

class Example(QWidget):
	
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.setGeometry(300, 300, 250, 150)
		label = QLabel("Vijayakumar Raju")
		animation = QPropertyAnimation(label, "geometry")
		animation.setDuration(10000)
		animation.setStartValue(QRect(0,0,100,30))
		animation.setEndValue(QRect(250,250,100,30))
		animation.start()

def main():
	
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	app.exec_()
	
	
	
if __name__ == '__main__':
	main()
	
	
	
	
