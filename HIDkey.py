import time

CTRL = 0x01
SHIFT = 0x02
ALT = 0x04
META = 0x08

def create():
        return USBHIDkey()

class USBHIDkey():
    def __init__(self, **kwargs):
        self.KT= {}
        self.hidseq(ord(' '),ord(' '),44,0)
        self.hidseq(ord('-'),ord('-'),45,0)
        self.hidseq(ord('^'),ord('^'),46,0)
        self.hidseq(ord('@'),ord('@'),47,0)
        self.hidseq(ord('['),ord('['),48,0)
        self.hidseq(ord(']'),ord(']'),49,0)
        self.hidseq(ord(';'),ord(';'),51,0)
        self.hidseq(ord(':'),ord(':'),52,0)
        self.hidseq(ord(','),ord(','),54,0)
        self.hidseq(ord('.'),ord('.'),55,0)
        self.hidseq(ord('/'),ord('/'),56,0)
        self.hidseq(ord('?'),ord('?'),56,0)
        self.hidseq(ord('\\'),ord('\\'),135,0)

        self.hidseq(ord('0'),ord('0'),39,0)
        self.hidseq(ord('1'),ord('9'),30,0)

        self.hidseq(ord('a'),ord('z'),4,0)
        self.hidseq(ord('A'),ord('Z'),4,SHIFT)

        self.hidseq(ord('!'),ord('!'),30,SHIFT)
        self.hidseq(ord('"'),ord('"'),31,SHIFT)
        self.hidseq(ord('#'),ord('#'),32,SHIFT)
        self.hidseq(ord('$'),ord('$'),33,SHIFT)
        self.hidseq(ord('%'),ord('%'),34,SHIFT)
        self.hidseq(ord('&'),ord('&'),35,SHIFT)
        self.hidseq(ord("'"),ord("'"),36,SHIFT)
        self.hidseq(ord('('),ord('('),37,SHIFT)
        self.hidseq(ord(')'),ord(')'),38,SHIFT)
        self.hidseq(ord('~'),ord('~'),39,SHIFT)

        self.hidseq(ord('='),ord('='),45,SHIFT)
        self.hidseq(ord('~'),ord('~'),46,SHIFT)
        self.hidseq(ord('`'),ord('`'),47,SHIFT)
        self.hidseq(ord('{'),ord('{'),48,SHIFT)
        self.hidseq(ord('}'),ord('}'),49,SHIFT)
        self.hidseq(ord('+'),ord('+'),51,SHIFT)
        self.hidseq(ord('*'),ord('*'),52,SHIFT)
        self.hidseq(ord('<'),ord('<'),54,SHIFT)
        self.hidseq(ord('>'),ord('>'),55,SHIFT)
        self.hidseq(ord('?'),ord('?'),56,SHIFT)
        self.hidseq(ord('_'),ord('_'),135,SHIFT)
        
        self.offbuff = bytes([0,0,0,0,0,0,0,0])

    def hidseq(self, ascSt, ascEn, hidSt, mod):
        for k in range(ascSt,ascEn+1):
            code = k-ascSt+hidSt
            self.KT[chr(k)]={"code":code, "mod":mod}

    def tran(self, str):
        rtn = []
        for s in str:
            try:
                rtn.append(self.KT[s])
            except:
                rtn.append(self.KT[' '])
        return rtn

    def putKey(self, mod, code):
        kbuff = bytes([mod, 0, code, 0,0,0,0,0])
        wait=0.02
        with open('/dev/hidg1', 'wb') as f:
            f.write( kbuff )
            time.sleep(wait)
            f.write( self.offbuff )
            time.sleep(wait)
            f.write( self.offbuff )
            time.sleep(wait)

    def putASCKey(self, mod, code):
        k = self.KT[code]
        self.putKey(k['mod'],k['code'])
