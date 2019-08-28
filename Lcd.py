from pyb import Pin, Timer, udelay
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
    ct = Timer (2, freq=3) #cursor timer

    #superscript font for numbers
    fs = [0x1f,  0x11, 0x11, 0x1f,    # 0
          0x0,  0x1,  0x1f, 0x0,    # 1
          0x1d, 0x15, 0x15, 0x17,   # 2
          0x15, 0x15, 0x15, 0x1f,   # 3
          0x7,  0x4,  0x4,  0x1f,   # 4
          0x17, 0x15, 0x15, 0x1d,   # 5
          0x1f, 0x15, 0x15, 0x1d,   # 6
          0x1,  0x1,  0x1,  0x1f,   # 7
          0x1f, 0x15, 0x15, 0x1f,   # 8
          0x17, 0x15, 0x15, 0x1f,   # 9
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
        0x41, 0x22, 0x14, 0x08, 0x00, # >
        ]
    
    o = [32, 91, 48] #offset
    
    f1 = [0x00, 0x00, 0x7F, 0x41, 0x41, # [
        0x02, 0x04, 0x08, 0x10, 0x20, # \
        0x41, 0x41, 0x7F, 0x00, 0x00, # ]
        0x04, 0x02, 0x01, 0x02, 0x04, # ^
        0x40, 0x40, 0x40, 0x40, 0x40, # _
        0x00, 0x01, 0x02, 0x04, 0x00, # `
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
        0x18, 0x08, 0x18, 0x10, 0x18, # ~
        ]

    def __init__ (self):
        self.e.high()
        self.rs.high()
        self.en(1)
        self.chp = 0
        self.row = 1
        self.col = 0
        self.scr = 0 #scroll
        self.cls()
        self.ct.callback(self.crs)

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
        self.rs.low()
        self.e.high()
        self.d[7].low()
        self.d[6].low()
        for i in range(1, 6):
            self.d[i].high()
        self.d[0].value(on)
        udelay(1)
        self.e.low()
    
    def hwy (self, l):
        self.rs.low()
        self.e.high()
        self.d[7].high()
        self.d[6].low()
        self.d[5].high()
        self.d[4].high()
        self.d[3].high()
        self.d[2].value((l & 0x4) >> 2)
        self.d[1].value((l & 0x2) >> 1)
        self.d[0].value(l & 0x1)
    
        udelay(1)
        self.e.low()

    def hwx (self, c):
        self.rs.low()
        self.e.high()
        self.d[7].low()
        self.d[6].high()
        self.d[5].value((c & 0x32) >> 5)
        self.d[4].value((c & 0x16) >> 4)
        self.d[3].value((c & 0x8) >> 3)
        self.d[2].value((c & 0x4) >> 2)
        self.d[1].value((c & 0x2) >> 1)
        self.d[0].value(c & 0x1)
    
        udelay(1)
        self.e.low()

    def hwz (self, z):
        self.rs.low()
        self.e.high()
        self.d[7].high()
        self.d[6].high()
        self.d[5].value((z & 0x32) >> 5)
        self.d[4].value((z & 0x16) >> 4)
        self.d[3].value((z & 0x8) >> 3)
        self.d[2].value((z & 0x4) >> 2)
        self.d[1].value((z & 0x2) >> 1)
        self.d[0].value(z & 0x1)
    
        udelay(1)
        self.e.low()

    def px (self, value):
        #show pixels
        #HW will increment the internal X position and 
        #increment of self.col should be handled by caller
        self.rs.high()
        self.e.high()
        for i in range(8):
            self.d[i].value((value >> i) & 0x1)
        udelay(1)
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
        self.upd()
        self.ct.callback(self.crs)

    def cll (self, l):
        #erase a line
        self.ct.callback(None)
        self.px(0) #erase cursor
        self.dl(l)
        self.upd()
        self.ct.callback(self.crs)

    def loc (self, r, c):
        #locate function
        if c > 31:
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
        if r >= 0:
            self.row = r
        else:
            self.row = 0
        if self.row < 8:
            self.scr -= 8
        self.upd()
        self.ct.callback(self.crs)

    def upds (self):
        #update scroll
        self.hwcsa ()
        self.hwz(self.scr)
        self.hwcs (self.chp)

    def upd(self):
        #update
        self.upds()
        self.hwy (self.row)
        self.hwx (self.col)

    def printat (self, r, c, s, sf = False):
        #print at
        olcc, olscr, olr, olc = self.chp, self.scr, self.row, self.col #retain old values
        self.loc(0 if r < 0 else r,c)
        self.print (s, sf, e=False)
        self.chp, self.scr, self.row, self.col = olcc, olscr, olr, olc #restore old values
        self.upd()

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
            self.upds()

    def xpos (self, c):
        #print ("resolve at first: -- col is ", self.col, "row is ", self.row)
        self.col = c % 64
        #print ("chp < 2 and c is ", c)
        self.chp += (c // 64)
        if self.chp > 2:
            self.chp -= 3
        self.upd()
        #print ("resolve at end: -- col is ", self.col, "row is ", self.row)

    def prmpt (self):
        #draw prompt
        self.printat(self.row - 7, 0, "0123456789", sf=True)
        #for e in [0x81, 0x5a, 0xa5, 0x5a, 0x24, 0x18]: # >>
        #for e in [0x99, 0x5a, 0xbd, 0x5a, 0x3c, 0x18]: # another >>
        for e in [0x14, 0x3e, 0x14, 0x3e, 0x14]: # another '#'
            self.px(e)
        self.loc(self.row, 1)


    def print (self, s, sf = False, e=False):
        #sf: superscript font of width 4
        #e: carriage return and newline at end
        self.ct.callback(None)
        w = 5 if sf == False else 4 #width of font
        for c in s:
            if self.col > 58 and self.chp == 2:
                self.ypos()
            self.xpos (self.col)
            self.px(0) #draw gap 
            self.col += 1
            for i in range (w):
                self.xpos (self.col)
                if sf == True:
                    idx = (ord(c) - self.o[2]) * 4
                    self.px (self.fs[idx + i])
                elif ord(c) < ord ('?') and ord(c) > 31:
                    idx = (ord(c) - self.o[0]) * 5
                    self.px (self.f0[idx + i])
                elif (ord(c) <= ord ('~')) and (ord(c) >= ord('[')):
                    idx = (ord(c) - self.o[1]) * 5
                    self.px (self.f1[idx + i])
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
