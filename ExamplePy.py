#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

import sys
from PyQt4 import QtGui, QtCore
from %(name)s import Ui_MainWindow

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # Setup the ui.
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    ## Look and feel changed to CleanLooks
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
    
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    

def main(filename):
    os.system('pyuic4 -o %(name)s.py -x %(name)s.ui'%{'name': filename})
    with open('main.py', 'w') as f:
        f.write(template%{'name': filename})
        
if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
