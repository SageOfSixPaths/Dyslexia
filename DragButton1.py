import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Button(QtGui.QPushButton):

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.move(100,200)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.start(QtCore.Qt.MoveAction)


    def mousePressEvent(self, e):

        QtGui.QPushButton.mousePressEvent(self, e)
        if e.button() == QtCore.Qt.LeftButton:
            print 'press'


class MyTable(QtGui.QTableWidget):

    def __init__(self, rows, columns, parent):
        super(MyTable, self).__init__(rows, columns, parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)

    def dragEnterEvent(self, e):
		e.accept()
		print e.accept()

    def dropEvent(self, e):
        print 'blah'

        position = e.pos()
        self.button.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
	
        print e.accept()
        e.accept()

	def dragMoveEvent(self, e):
		e.accept()
		
	def dragLeaveEvent(self, e):
		e.accept()

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.table = MyTable(2,2,self)
        self.table.setAcceptDrops(True)
        self.table.setDragEnabled(True)

        self.setWindowTitle('Click or Move')
        
        self.button = Button('Button', self)
		#self.button.move(100,200)

        #self.setGeometry(300, 300, 280, 150)

        ##layout = QtGui.QVBoxLayout()
        ##layout.addWidget(self.button)
        ##layout.addWidget(self.table)
        ##self.setLayout(layout)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()  


if __name__ == '__main__':

    main()
