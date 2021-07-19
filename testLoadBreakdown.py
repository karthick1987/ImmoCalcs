#!/usr/bin/python3

from loanPayments import loanBreakdown

def test():
    tmp = loanBreakdown(5000, 0.5, 13, 430.33)
    tmp.printStats()

if __name__ == '__main__':
    test()
