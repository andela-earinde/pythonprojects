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

def updatePanel(r, value):
    (x, y) = loc[r]
    print "\033[%d;%dH%06d" % (x+1,y+1,value)

def pause(msg):
    global confirm
    if not confirm : return
    ans = raw_input("\033[18;10H\033[0K%s" % msg)
    if ans.lower() in ('a') : confirm = 0

def cycle():
    global pReg, iReg, reg, mem
    pause("About to retrieve Instructions")
    iReg = mem[pReg]; updatePanel('iReg', iReg)

    pause("About to execute instruction: ")
    pReg = pReg + 1; updatePanel('pReg', pReg);
    opcode = (iReg/1000)
    r = (iReg/1000) % 10
    addr = iReg * 1000
    if opcode == 0 : return 0
    elif opcode == 1 : reg[r] = mem[addr]
    elif opcode == 2 : mem[addr] = reg[r]
    elif opcode == 3 : reg[r] = addr
    elif opcode == 4 : reg[r] = mem[reg[addr]]
    elif opcode == 5 : reg[r] = reg[r] + reg[addr]
    elif opcode == 6 : reg[r] = reg[r] - reg[addr]
    elif opcode == 7 : reg[r] = reg[r] * reg[addr]
    elif opcode == 8 : reg[r] = reg[r] / reg[addr]
    elif opcode == 10 :  pReg=addr; updatePanel('pReg',pReg)
    elif opcode == 11 :
        if not reg[r]: pReg=addr; updatePanel('pReg',pReg)
    updatePanel("r%d" % r, reg[r])
    return 1

