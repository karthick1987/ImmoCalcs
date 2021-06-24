#!/usr/bin/python3

import sys
from setDefaults import setSpinBoxDefaults
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ImmoCalc.ui', self) # Load the .ui file
        self.show() # Show the GUI

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class

spb = setSpinBoxDefaults(window)
spb.setValue()
spb.findNebenKosten()

app.exec_() # Start the application
