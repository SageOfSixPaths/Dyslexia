#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import re
from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog)
import ui_findandreplacedlg

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class FindAndReplaceDlg(QDialog,
			ui_findandreplacedlg.Ui_FindAndReplaceDlg):
	
	def __init__(self, text, parent=None):
		super(FindAndReplaceDlg, self).__init__(parent)
		self.__text = unicode(text)
		self.__index = 0
		self.setupUi(self)
		if not MAC:
			self.findButton.setFocusPolicy(Qt.NoFocus)
			self.replaceButton.setFocusPolicy(Qt.NoFocus)
			self.replaceAllButton.setFocusPolicy(Qt.NoFocus)
			self.closeButton.setFocusPolicy(Qt.NoFocus)
		self.updateUi()
		
	@pyqtSignature("QString")	
	def on_findLineEdit_textEdited(self, text):
		self.__index = 0
		self.updateUi()
	
	def makeRegex(self):
		findText = unicode(self.findLineEdit.text())
		if unicode(self.syntaxComboBox.currentText()) == "Literal":
			findText = re.escape(findText)
		flags = re.MULTILINE|re.DOTALL|re.UNICODE
		if not self.caseCheckBox.isChecked():
			flags |= re.IGNORECASE
		
		if self.wholeCheckBox.isChecked():
			findText = r"\b{0}\b".format(findText)
		return re.compile(findText, flags)
	
	@pyqtSignature("")
	def on_findButton_clicked(self):
		regex = self.makeRegex()
		match = regex.search(self.__text, self.__index)
		if match is not None:
			self.__index = match.end()
			self.emit(SIGNAL("found"), match.start())
		else:
			self.emit(SIGNAL("notfound"))
	
	@pyqtSignature("")
	def on_replaceButton_clicked(self):
		regex = self.makeRegex()
		self.__text = regex.sub(unicode(self.replaceLineEdit.text()),
								self.__text, 1)
								
	@pyqtSignature("")
	def on_replaceAllButton_clicked(self):
		regex = self.makeRegex()
		self.__text = regex.sub(unicode(self.replaceLineEdit.text()),
								self.__text)
	
	def updateUi(self):
		enable = not self.findLineEdit.text().isEmpty()
		self.findButton.setEnabled(enable)
		self.replaceButton.setEnabled(enable)
		self.replaceAllButton.setEnabled(enable)
		
	def text(self):
		return self.__text 	
	
if __name__ == "__main__":
	import sys
	
	
	text = """US experience shows that, unlike traditional patents,
software patents do not encourage innovation and R&D, quite the
contrary. In particular they hurt small and medium-sized enterprises
and generally newcomers in the market. They will just weaken the market
and increase spending on patents and litigation, at the expense of
technological innovation and research. Especially dangerous are
attempts to abuse the patent system by preventing interoperability as a
means of avoiding competition with technological ability.
--- Extract quoted from Linus Torvalds and Alan Cox's letter
to the President of the European Parliament
http://www.effi.org/patentit/patents_torvalds_cox.html"""

	def found(where):
		print("Found at {0}".format(where))
		
	def nomore():
		print("No more found")
		
	app = QApplication(sys.argv)
	form = FindAndReplaceDlg(text)
	form.connect(form, SIGNAL("found"), found)
	form.connect(form, SIGNAL("notfound"), nomore)
	form.show()
	app.exec_()
	print(form.text())

		
	
	
		
		
	
		
		
	
