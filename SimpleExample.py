import sys

from PyQt4.QtGui import *

class SimpleExample(QDialog, QListView):
	
	def __init__(self, parent=None):
		super(SimpleExample, self).__init__(parent)
		self.setupUi(self)
		model = QStandardItemModel()
		item = QStandardItem("Item")
		item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
		item.setData(QVariant(Qt.Checked), Qt.CheckStateRole)
		model.appendRow(item)

if __name__ == "__main__":
	app = QApplication(sys.argv)
    view = SimpleExample()
	view.setModel(model)
	view.show()
	app.exec_()
