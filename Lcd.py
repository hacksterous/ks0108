from pyb import Pin, Timer, udelay
import machine
import stm
__cbm__ = 0xff #cursor bitmap

class Lcd():
    #data in PE15=data7 .. PE8=data0
    d = [Pin ('PE8', mode=Pin.OUT),
            Pin ('PE9', mode=Pin.OUT),
            Pin ('PE10', mode=Pin.OUT),
            Pin ('PE11', mode=Pin.OUT),
            Pin ('PE12', mode=Pin.OUT),
            Pin ('PE13', mode=Pin.OUT),
            Pin ('PE14', mode=Pin.OUT),
            Pin ('PE15', mode=Pin.OUT)]

    cs = [Pin ('PD8', mode=Pin.OUT),
            Pin ('PD9', mode=Pin.OUT),
            Pin ('PD10', mode=Pin.OUT)]
    
    rs = Pin ('PE7', mode=Pin.OUT)
    e = Pin ('PD1', mode=Pin.OUT)
    rw = Pin ('PD14', mode=Pin.OUT)
    ct = Timer (2, freq=3) #cursor timer

    #superscript font for numbers
    fs0 = [0x1f,  0x11, 0x11, 0x1f, # 0
          0x0,  0x1,  0x1f, 0x0,  # 1
          0x1d, 0x15, 0x15, 0x17, # 2
          0x15, 0x15, 0x15, 0x1f, # 3
          0x7,  0x4,  0x4,  0x1f, # 4
          0x17, 0x15, 0x15, 0x1d, # 5
          0x1f, 0x15, 0x15, 0x1d, # 6
          0x1,  0x1,  0x1,  0x1f, # 7
          0x1f, 0x15, 0x15, 0x1f, # 8
          0x17, 0x15, 0x15, 0x1f,  # 9
          0x08, 0x08, 0x08, 0x08, #- #:

        ]

    #superscript font for alpha
    fs1 = [0x1f, 0x5, 0x5, 0x1f, #a
        0x1f, 0x14, 0x14, 0x1c, #b
        0x1f, 0x11, 0x11, 0x11, #c
        0x1c, 0x14, 0x14, 0x1f, #d
        0x1f, 0x15, 0x15, 0x11, #e
        0x1f, 0x5, 0x5, 0x1, #f
        0x1f, 0x11, 0x15, 0x1d, #g
        0x1f, 0x4, 0x4, 0x1f, #h
        0x11, 0x1f, 0x11, 0x0, #i
        0x18, 0x11, 0x1f, 0x1, #j
        0x1f, 0x4, 0xa, 0x11, #k
        0x1f, 0x10, 0x10, 0x0, #l
        0x1f, 0x6, 0x3, 0x1f, #m
        0x1e, 0x2, 0x2, 0x1c, #n
        0xe, 0x11, 0x11, 0xe, #o
        0x1f, 0x5, 0x5, 0x2, #p
        0x1f, 0x11, 0x1f, 0x10, #q
        0x1e, 0x2, 0x2, 0x0, #r
        0x17, 0x15, 0x15, 0x1d, #s
        0x2, 0x1f, 0x12, 0x10, #t
        0x1f, 0x10, 0x10, 0x1f, #u
        0x7, 0x18, 0x10, 0x1f, #v
        0x1f, 0xc, 0x18, 0x1f, #w
        #0x0, 0xa, 0x4, 0xa, #x
        0x0, 0x0, 0x0, 0x0, #space #x
        0x7, 0x14, 0x14, 0x1f, #y
        0x19, 0x1d, 0x17, 0x13 #z
        ]

    f0 = [0x00, 0x00, 0x00, 0x00, 0x00, # space
        0x00, 0x00, 0x5F, 0x00, 0x00, # !
        0x00, 0x07, 0x00, 0x07, 0x00, # "
        0x14, 0x7F, 0x14, 0x7F, 0x14, # #
        0x24, 0x2A, 0x7F, 0x2A, 0x12, # $
        0x23, 0x13, 0x08, 0x64, 0x62, # %
        0x36, 0x49, 0x55, 0x22, 0x50, # &
        0x00, 0x05, 0x03, 0x00, 0x00, # '
        0x00, 0x1C, 0x22, 0x41, 0x00, # (
        0x00, 0x41, 0x22, 0x1C, 0x00, # )
        0x08, 0x2A, 0x1C, 0x2A, 0x08, # *
        0x08, 0x08, 0x3E, 0x08, 0x08, # +
        0x00, 0x50, 0x30, 0x00, 0x00, # ,
        0x08, 0x08, 0x08, 0x08, 0x08, # -
        0x00, 0x30, 0x30, 0x00, 0x00, # .
        0x20, 0x10, 0x08, 0x04, 0x02, # /
        0x3E, 0x51, 0x49, 0x45, 0x3E, # 0
        0x00, 0x42, 0x7F, 0x40, 0x00, # 1
        0x42, 0x61, 0x51, 0x49, 0x46, # 2
        0x21, 0x41, 0x45, 0x4B, 0x31, # 3
        0x18, 0x14, 0x12, 0x7F, 0x10, # 4
        0x27, 0x45, 0x45, 0x45, 0x39, # 5
        0x3C, 0x4A, 0x49, 0x49, 0x30, # 6
        0x01, 0x71, 0x09, 0x05, 0x03, # 7
        0x36, 0x49, 0x49, 0x49, 0x36, # 8
        0x06, 0x49, 0x49, 0x29, 0x1E, # 9
        0x00, 0x36, 0x36, 0x00, 0x00, # :
        0x00, 0x56, 0x36, 0x00, 0x00, # ;
        0x00, 0x08, 0x14, 0x22, 0x41, # <
        0x14, 0x14, 0x14, 0x14, 0x14, # =
        0x41, 0x22, 0x14, 0x08, 0x00 # >
        ]
    
    o = [32, 91, 48, 65] #offset
    
    f1 = [0x00, 0x00, 0x7F, 0x41, 0x41, # [
        0x02, 0x04, 0x08, 0x10, 0x20, # \
        0x41, 0x41, 0x7F, 0x00, 0x00, # ]
        0x04, 0x02, 0x01, 0x02, 0x04, # ^
        0x40, 0x40, 0x40, 0x40, 0x40, # _
        0xff, 0x7e, 0x3c, 0x18, 0x0, # ` mapped to a prompt
        0x20, 0x54, 0x54, 0x54, 0x78, # a
        0x7F, 0x48, 0x44, 0x44, 0x38, # b
        0x38, 0x44, 0x44, 0x44, 0x20, # c
        0x38, 0x44, 0x44, 0x48, 0x7F, # d
        0x38, 0x54, 0x54, 0x54, 0x18, # e
        0x08, 0x7E, 0x09, 0x01, 0x02, # f
        0x08, 0x14, 0x54, 0x54, 0x3C, # g
        0x7F, 0x08, 0x04, 0x04, 0x78, # h
        0x00, 0x44, 0x7D, 0x40, 0x00, # i
        0x20, 0x40, 0x44, 0x3D, 0x00, # j
        0x00, 0x7F, 0x10, 0x28, 0x44, # k
        0x00, 0x41, 0x7F, 0x40, 0x00, # l
        0x7C, 0x04, 0x18, 0x04, 0x78, # m
        0x7C, 0x08, 0x04, 0x04, 0x78, # n
        0x38, 0x44, 0x44, 0x44, 0x38, # o
        0x7C, 0x14, 0x14, 0x14, 0x08, # p
        0x08, 0x14, 0x14, 0x18, 0x7C, # q
        0x7C, 0x08, 0x04, 0x04, 0x08, # r
        0x48, 0x54, 0x54, 0x54, 0x20, # s
        0x04, 0x3F, 0x44, 0x40, 0x20, # t
        0x3C, 0x40, 0x40, 0x20, 0x7C, # u
        0x1C, 0x20, 0x40, 0x20, 0x1C, # v
        0x3C, 0x40, 0x30, 0x40, 0x3C, # w
        0x44, 0x28, 0x10, 0x28, 0x44, # x
        0x0C, 0x50, 0x50, 0x50, 0x3C, # y
        0x44, 0x64, 0x54, 0x4C, 0x44, # z
        0x00, 0x08, 0x36, 0x41, 0x00, # {
        0x00, 0x00, 0x7F, 0x00, 0x00, # |
        0x00, 0x41, 0x36, 0x08, 0x00, # }
        0x18, 0x08, 0x18, 0x10, 0x18 # ~
        ]

    def __init__ (self):
        self.rw.low()
        self.e.high()
        self.rs.high()
        self.chp = 0
        self.row = 1
        self.col = 0
        self.scr = 0 #scroll
        self.cls()
        self.ct.callback(self.crs)
        self.en(1)

    #FIXME use direct writes to machine.mem16[stm.GPIOE + stm.GPIO_BSRR] 
    #to set/clr E/CS/RS
    def hwcs(self, chp):
        #chip select
        for i in range(3):
            self.cs[i].high()
        self.cs[chp].low()
    
    def hwcsa(self):
        #chip select all
        for i in range(3):
            self.cs[i].low()
    
    def en (self, on):
        self.hwcsa()        
        self.e.high()
        self.rs.low()
        machine.mem16[stm.GPIOE + stm.GPIO_ODR] = ((0x3e | (on & 0x1)) << 8) | (machine.mem16[stm.GPIOE + stm.GPIO_ODR] & 0xff)
        #udelay(1)
        self.e.low()
        self.hwcs(self.chp)

    def hwy (self, l):
        self.e.high()
        self.rs.low()
        machine.mem16[stm.GPIOE + stm.GPIO_ODR] = ((0xb8 | (l & 0x7)) << 8) | (machine.mem16[stm.GPIOE + stm.GPIO_ODR] & 0xff)
    
        #udelay(1)
        self.e.low()

    def hwx (self, c):
        self.e.high()
        self.rs.low()
        machine.mem16[stm.GPIOE + stm.GPIO_ODR] = ((0x40 | c) << 8) | (machine.mem16[stm.GPIOE + stm.GPIO_ODR] & 0xff)
    
        #udelay(1)
        self.e.low()

    def hwz (self, z):
        self.e.high()
        self.rs.low()
        machine.mem16[stm.GPIOE + stm.GPIO_ODR] = ((0xc0 | z) << 8) | (machine.mem16[stm.GPIOE + stm.GPIO_ODR] & 0xff)
    
        #udelay(1)
        self.e.low()

    def px (self, value):
        #show pixels
        #HW will increment the internal X position and 
        #increment of self.col should be handled by caller
        self.e.high()
        self.rs.high()
        machine.mem16[stm.GPIOE + stm.GPIO_ODR] = (value << 8) | (machine.mem16[stm.GPIOE + stm.GPIO_ODR] & 0xff)
        #udelay(1)
        self.e.low()

    def dl (self, l):
        self.hwcsa()
        self.hwy (l)
        for j in range(64):
            self.px(0)

    def cls (self):
        self.ct.callback(None)
        self.chp = 0
        self.row = 1
        self.col = 0
        self.scr = 0
        self.hwcsa()
        self.hwz(0)
        for i in range(8):
            self.hwy(i)
            for j in range(64):
                self.px(0)
        self.hwupd()
        self.ct.callback(self.crs)

    def cll (self, l):
        #erase a line
        self.ct.callback(None)
        self.px(0) #erase cursor
        self.dl(l)
        self.hwupd()
        self.ct.callback(self.crs)

	def rloc (self, r, c=0):
		#relative loc
		#r > 0 goes to next rows, r < 0 goes to previous rows
		#c > 0 goes to next cols, c < 0 goes to previous cols
		#self.loc (self.row - self.scr//8+r)
		col = (self.chp * 64 + self.col)//6 + c
        if col > 31:
            return
		if col < 0:
			row = r - 1
			col = 31
		else:
			row = r
        self.ct.callback(None)
        self.px(0) #erase cursor
        if col > 21:
            self.col = col*6 - 128
            self.chp = 2
        elif col > 10:
            self.col = col*6 - 64 
            self.chp = 1
        else: # -- ok
            self.col = col*6
            self.chp = 0

        self.row += row
        self.hwupd()
        self.ct.callback(self.crs)


    def loc (self, r, c=0):
        #locate function
		#top row is always 0, bottom row is 7
        if c > 31 or c < 0:
            return
        self.ct.callback(None)
        self.px(0) #erase cursor
        if c > 21:
            self.col = c*6 - 128
            self.chp = 2
        elif c > 10:
            self.col = c*6 - 64 
            self.chp = 1
        else: # -- ok
            self.col = c*6
            self.chp = 0

        self.row = r + (self.scr//8)
        self.hwupd()
        self.ct.callback(self.crs)

    def hwupds (self):
        #update scroll
        self.hwcsa ()
        self.hwz(self.scr)
        self.hwcs (self.chp)

    def hwupd(self):
        #update
        self.hwupds()
        self.hwy (self.row)
        self.hwx (self.col)

    def printat (self, r, c, s, sf = False):
        #print at
        olcc, olscr, olr, olc = self.chp, self.scr, self.row, self.col #retain old values
        self.loc(0 if r < 0 else r, c)
        self.print (s, sf, e=False)
        self.chp, self.scr, self.row, self.col = olcc, olscr, olr, olc #restore old values
        self.hwupd()

    def crs (self, ct):
        global __cbm__
        __cbm__ ^= 0xff
        self.px(__cbm__)
        self.hwx(self.col)

    def ypos (self):
        self.row += 1   
        self.col = 0
        self.chp = 0
        if self.row > ((self.scr//8)+7):
            #scrolling up -- must erase
            #earlier lines
            self.dl (self.scr//8)
            #FORMULA:
            #self.scr = (self.row - 7) * 8
            self.scr += 8
            self.hwupds()

    def xpos (self, c):
        #print ("resolve at first: -- col is ", self.col, "row is ", self.row)
        self.col = c % 64
        #print ("chp < 2 and c is ", c)
        self.chp += (c // 64)
        if self.chp > 2:
            self.chp -= 3
        self.hwupd()
        #print ("resolve at end: -- col is ", self.col, "row is ", self.row)

    def prmpt (self):
        #draw prompt
        self.printat(0, 0, "0123456789", sf=True)
        self.print('`')

    def print (self, s, sf = False, e=False):
        #sf: superscript font of width 4
        #e: carriage return and newline at end
        self.ct.callback(None)
        w = 5 if sf == False else 4 #width of font
        for c in s:
            if self.col > 58 and self.chp == 2:
                self.ypos()
            self.xpos (self.col) ### FIXME -- can be removed?
            self.px(0) #draw gap 
            self.col += 1
            for i in range (w):
                self.xpos (self.col)
                if sf == True:
                    if ord(c) < 65: #numbers < 65 == 'A'
                        idx = (ord(c) - self.o[2]) * 4
                        self.px (self.fs0[idx + i])
                    else: #alpha
                        idx = (ord(c) - self.o[3]) * 4
                        self.px (self.fs1[idx + i])
                elif ord(c) < 63 and ord(c) > 31: #63 == '?'
                    idx = (ord(c) - self.o[0]) * 5
                    self.px (self.f0[idx + i])
                elif ord(c) <= 126 and ord(c) >= 91: #126 == '~', 91 == ~['
                    idx = (ord(c) - self.o[1]) * 5
                    self.px (self.f1[idx + i])
                else:
                    self.px (0)
                self.col += 1
            #print ("col is ", self.col)

        if e == True:
            #newline
            self.col = 64
            self.chp = 2
        if self.col == 64:
            self.ypos()
            self.xpos(self.col)
        self.ct.callback(self.crs)
