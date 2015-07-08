#!/usr/bin/python
#
#       s i m u l a t o r . p y
#
import sys, string
panel = """
               The Mythical Machine
 
        P reg  000000       I reg 000000
                      
        reg 0  000000       reg 5 000000
        reg 1  000000       reg 6 000000
        reg 2  000000       reg 7 000000
        reg 3  000000       reg 8 000000
        reg 4  000000       reg 9 000000
"""

#loc have row/coloumn intruction for each register
loc = {'pReg': (3, 15), 'iReg': (3, 34)}
mem = [0] * 1000
reg = [0] * 10

for i in range(0, 5) : loc["r%d"%i] = (5+i, 15)
for i in range(5, 9) : loc["r%d"%i] = (0+i, 34)

confirm = 1

def updatePanel(r, value)



