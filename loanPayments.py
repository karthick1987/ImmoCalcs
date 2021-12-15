#!/usr/bin/python3

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import numpy as np

class loanBreakdown:
    def __init__(self, pri, monthlyInterest, monthTerms, repayments):
        self.pri = pri
        self.monthlyInterest = monthlyInterest
        self.monthTerms = monthTerms
        self.repayments = repayments

        self.intForMonth = []
        self.priForMonth = []
        self.intToDate = []
        self.remainingPri = []

        if repayments == 0:
            self.calculateMonthlyEMI()
            self.repaymentBreakDown()
        else:
            self.repaymentBreakDown()

    def calculateMonthlyEMI(self):
        r = self.monthlyInterest/100
        n = self.monthTerms-1
        a = np.power(1+r,n)
        P = self.pri
        self.repayments = P*r*a/(a-1)

    def repaymentBreakDown(self):
        for i in range(self.monthTerms):
            if i == 0:
                self.intForMonth.append(0.0)
                self.priForMonth.append(0.0)
                self.intToDate.append(0.0)
                self.remainingPri.append(self.pri)
            else:
                self.intForMonth.append(self.remainingPri[i-1]*0.01*self.monthlyInterest)
                self.priForMonth.append(self.repayments - self.intForMonth[i])
                self.intToDate.append(self.intToDate[i-1] + self.intForMonth[i])
                self.remainingPri.append(self.remainingPri[i-1] - self.priForMonth[i])

    def printStats(self):
        print("Term\tMonthlyRepayment\tPrinciple\tInterestForMonth\tPriRemaining\tTotalIntest")
        for i in range(self.monthTerms):
            print("{0}\t{1:10.2f}\t{2:16.2f}\t{3:10.2f}\t{4:18.2f}\t{5:9.2f}".format(i, self.repayments, self.priForMonth[i], self.intForMonth[i], self.remainingPri[i], self.intToDate[i]))
        

