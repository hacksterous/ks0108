from Lcd import *
l = Lcd()
l.cls()

l.print('2')
l.print('0123456789'*10, sf=True, e= True)
l.print('0123456789'*10, sf=True)
l.print('0123456789'*10)
l.print('0123456789')

l.loc(l.row-7,0)

l.print('0123456789'*10, sf=True)
l.print('0123456789'*10)
l.print('0123456789'*10)
l.print('0123456789'*10, sf=True)
l.print('0123456789'*10)
l.print('0123456789'*10, sf=True)
l.print('0123456789'*10)
l.print('0123456789'*10, sf=True, e= True)
l.print('0123456789'*10)
l.print('0123456789'*10)
l.print('0123456789'*10, e= True)
l.print('0123456789'*10, sf=True)
l.print('0123456789'*100, e= True)


l.print('2')
l.print('0123456789'*10, sf=True)
l.print('0123456789'*10)
l.print('0123456789')
l.print('0123456789'*10, sf=True, e= True)

l.printat(l.row - 7, 0, "g"*30) #--> bug

l.cls()
l.print('0123456789'*50, e= True)
l.printat(l.row - 7, 0, "gggg")
l.printat(l.row - 7, 0, "g"*4)
l.printat(l.row - 7, 0, "g"*6)
l.printat(l.row - 7, 0, "g"*8)
l.printat(l.row - 7, 0, "g"*11)
l.printat(l.row - 7, 0, "g"*32)
l.print('0123456789')

l.print('0123456789'*50, e= True)
l.printat(l.row, -1, "g")
l.print('a')
l.loc(l.row, -1)
l.print('r')
l.row

l.loc(l.row+1, 0)
l.loc(l.row, -1)
l.col

l.loc(l.row-1, 2)
l.loc(l.row-1, 2)
l.loc(l.row-1, 10)
l.loc(l.row-1, 20)
l.loc(l.row-1, 30)

l.print('0123456789'*40, e= True)
l.loc(l.row, 10)
l.loc(l.row-1, 10)
l.loc(l.row-1, 11)
l.loc(l.row, 20)
l.loc(l.row, 30)
l.loc(l.row, 31)

for i in range (30):
 l.loc(l.row, i)
 delay(3333)
from pyb import delay
l.print('0123456789'*50)
l.loc(l.row-1, 0)

for i in range (7, 13):
for i in range (32):
 l.loc(l.row, i)
 delay(1332)



