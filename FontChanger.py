import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FontDialog(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		hbox = QHBoxLayout()

		self.setGeometry(500, 300, 250, 110)
		self.setWindowTitle('FontDialog')

		button = QPushButton('Change Font...', self)
		button.setFocusPolicy(Qt.NoFocus)
		button.move(20, 20)

		hbox.addWidget(button)

		self.connect(button, SIGNAL('clicked()'), self.showDialog)

		self.label = QLabel('This is some Sample Text', self)
		self.label.move(130, 20)

		hbox.addWidget(self.label, 1)
		self.setLayout(hbox)

	def showDialog(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.label.setFont(font)

app = QApplication(sys.argv)
cd = FontDialog()
cd.show()
app.exec_()
