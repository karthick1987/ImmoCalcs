#!/usr/bin/python3

import pyqtgraph as pg
import numpy as np
import threading

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
pg.plot(x, y, pen=None, symbol='o')  ## setting pen=None disables line drawing

a = input('').split(" ")[0]
