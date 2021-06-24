#!/usr/bin/python3

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import numpy as np

class setSpinBoxDefaults:
    def __init__(self, ui):
        self.ui = ui
        self.setupSignals()
        self.setValue()
        self.findNebenKosten()
        self.setupTable()

    def setValue(self):
        self.ui.lbCommission.setGroupSeparatorShown(True)
        self.ui.lbLandTax.setGroupSeparatorShown(True)
        self.ui.lbNotar.setGroupSeparatorShown(True)
        self.ui.sbPropertyValue.setGroupSeparatorShown(True)
        self.ui.sbDeposit.setGroupSeparatorShown(True)
        self.ui.sbTotal.setGroupSeparatorShown(True)
        self.ui.sbNebenKosten.setGroupSeparatorShown(True)
        self.ui.sbLoanAmount.setGroupSeparatorShown(True)

        self.ui.sbCommission.setValue(3.57)
        self.ui.sbLandTax.setValue(3.5)
        self.ui.sbNotar.setValue(2.0)
        self.ui.sbFaktor.setValue(0.5)
        self.ui.sbPropertyValue.setValue(1000000)
        self.ui.sbDeposit.setValue(120000)
        self.ui.sbInterest.setValue(1.05)
        self.ui.sbTerm.setValue(15)
        self.ui.sbStart.setValue(1600)
        self.ui.sbEnd.setValue(5000)
        self.ui.sbIterations.setValue(18)

    def setupTable(self):
        self.ui.tbEmi.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header = ('Monthly Repayments', 'Paid Off', 'Remaining', 'Interest Paid')
        self.ui.tbEmi.setHorizontalHeaderLabels(header)
        self.ui.tbEmi.setRowCount(self.ui.sbIterations.value())
        self.calculateEMI()

    def calculateEMI(self):
        start = self.ui.sbStart.value()
        end = self.ui.sbEnd.value()
        it = self.ui.sbIterations.value()
        count = 0
        for i in np.linspace(start,end,it, dtype=int):
            qt_item = QtWidgets.QTableWidgetItem()
            qt_item.setData(Qt.EditRole, i.item())
            self.ui.tbEmi.setItem(count,0, qt_item)
            count = count + 1

    def setupSignals(self):
        self.ui.sbLandTax.valueChanged.connect(self.findNebenKosten)
        self.ui.sbNotar.valueChanged.connect(self.findNebenKosten)
        self.ui.sbCommission.valueChanged.connect(self.findNebenKosten)
        self.ui.sbFaktor.valueChanged.connect(self.findNebenKosten)

    def findNebenKosten(self):
        self.ui.lbLandTax.setValue(0.01*self.ui.sbLandTax.value()*self.ui.sbPropertyValue.value())
        self.ui.lbNotar.setValue(0.01*self.ui.sbNotar.value()*self.ui.sbPropertyValue.value())
        self.ui.lbCommission.setValue(0.01*self.ui.sbCommission.value()*self.ui.sbPropertyValue.value())
        self.ui.sbNebenKosten.setValue(self.ui.lbLandTax.value() + self.ui.lbNotar.value() + self.ui.lbCommission.value())
        self.ui.sbNebenKosten.setValue(self.ui.sbNebenKosten.value() * self.ui.sbFaktor.value())
        self.ui.sbLoanAmount.setValue((self.ui.sbNebenKosten.value() + self.ui.sbPropertyValue.value() - self.ui.sbDeposit.value()))

        self.ui.sbTotal.setValue((self.ui.sbNebenKosten.value() + self.ui.sbPropertyValue.value()))
