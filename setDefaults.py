#!/usr/bin/python3

from PyQt5 import QtWidgets, uic

class setSpinBoxValues:
    def __init__(self, ui):
        self.ui = ui
    def setValue(self):
        self.ui.commission.setValue(3.57)
        self.ui.faktor.setValue(0.5)
        self.ui.landTax.setValue(3.5)
        self.ui.notar.setValue(2.0)
        self.ui.propertyValue.setValue(1000000)
        self.ui.propertyValue.setGroupSeparatorShown(True);


