#!/usr/bin/python3

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import numpy as np
import locale

class setSpinBoxDefaults:
    def __init__(self, ui):
        self.ui = ui
        self.setupSignals()
        self.setValue()
        self.findNebenKosten()
        self.setupTable()
        locale.setlocale(locale.LC_ALL,'')

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
        self.calculateEMI()

    def calculateEMI(self):
        self.ui.tbEmi.setRowCount(self.ui.sbIterations.value())
        self.ui.tbEmi.clear()
        self.ui.tbEmi.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header = ('Monthly Repayments', 'Paid Off', 'Remaining', 'Interest Paid')
        self.ui.tbEmi.setHorizontalHeaderLabels(header)

        start = self.ui.sbStart.value()
        end = self.ui.sbEnd.value()
        it = self.ui.sbIterations.value()
        loanAmount = self.ui.sbLoanAmount.value()
        count = 0
        for i in np.linspace(start,end,it, dtype=int):

            emi=i.item()

            # Monthly Repayments
            qt_item = QtWidgets.QTableWidgetItem()
            qt_item.setTextAlignment(Qt.AlignHCenter)
            qt_item.setData(Qt.EditRole, f'{i.item():n}')
            self.ui.tbEmi.setItem(count,0, qt_item)

            # Paid off
            paidoff = QtWidgets.QTableWidgetItem()
            paidoff.setTextAlignment(Qt.AlignHCenter)
            terms = 12*self.ui.sbTerm.value()
            interest = self.ui.sbInterest.value()/12/100
            po = np.divide((emi - loanAmount*interest) * (np.power(1+interest,terms) - 1),interest)
            paidoff.setData(Qt.EditRole, f'{po.item():n}')
            self.ui.tbEmi.setItem(count,1, paidoff)

            # Remaining
            rem = QtWidgets.QTableWidgetItem()
            rem.setTextAlignment(Qt.AlignHCenter)
            rem.setData(Qt.EditRole, f'{(loanAmount - po).item():n}')
            self.ui.tbEmi.setItem(count,2,rem)

            # Interest Paid to date
            intst = QtWidgets.QTableWidgetItem()
            intst.setTextAlignment(Qt.AlignHCenter)

            int2Date = emi*terms-(emi-loanAmount*interest)*(np.power(1+interest,terms)-1)/interest
            intst.setData(Qt.EditRole, f'{int2Date.item():n}')
            self.ui.tbEmi.setItem(count,3,intst)

            count = count + 1


    def setupSignals(self):
        self.ui.sbLandTax.valueChanged.connect(self.findNebenKosten)
        self.ui.sbNotar.valueChanged.connect(self.findNebenKosten)
        self.ui.sbCommission.valueChanged.connect(self.findNebenKosten)
        self.ui.sbDeposit.valueChanged.connect(self.findNebenKosten)
        self.ui.sbFaktor.valueChanged.connect(self.findNebenKosten)
        self.ui.sbPropertyValue.valueChanged.connect(self.findNebenKosten)
        self.ui.sbStart.valueChanged.connect(self.calculateEMI)
        self.ui.sbEnd.valueChanged.connect(self.calculateEMI)
        self.ui.sbIterations.valueChanged.connect(self.calculateEMI)
        self.ui.sbInterest.valueChanged.connect(self.calculateEMI)
        self.ui.sbTerm.valueChanged.connect(self.calculateEMI)
        self.ui.sbLoanAmount.valueChanged.connect(self.calculateEMI)
        self.ui.sbPropertyValue.valueChanged.connect(self.calculateEMI)

    def findNebenKosten(self):
        self.ui.lbLandTax.setValue(0.01*self.ui.sbLandTax.value()*self.ui.sbPropertyValue.value())
        self.ui.lbNotar.setValue(0.01*self.ui.sbNotar.value()*self.ui.sbPropertyValue.value())
        self.ui.lbCommission.setValue(0.01*self.ui.sbCommission.value()*self.ui.sbPropertyValue.value())
        self.ui.sbNebenKosten.setValue(self.ui.lbLandTax.value() + self.ui.lbNotar.value() + self.ui.lbCommission.value())
        self.ui.sbNebenKosten.setValue(self.ui.sbNebenKosten.value() * self.ui.sbFaktor.value())
        self.ui.sbLoanAmount.setValue((self.ui.sbNebenKosten.value() + self.ui.sbPropertyValue.value() - self.ui.sbDeposit.value()))

        self.ui.sbTotal.setValue((self.ui.sbNebenKosten.value() + self.ui.sbPropertyValue.value()))
