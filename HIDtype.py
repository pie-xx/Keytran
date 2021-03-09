import sys

class HIDkey():
    def __init__(self, **kwargs):
        SHIFT=2
        self.KT= {}
        self.hidseq(ord(' '),ord(' '),44,0)
        self.hidseq(ord('-'),ord('-'),45,0)
        self.hidseq(ord('='),ord('='),46,0)
        self.hidseq(ord('['),ord('['),47,0)
        self.hidseq(ord(']'),ord(']'),48,0)
        self.hidseq(ord('\\'),ord('\\'),49,0)
        self.hidseq(ord('#'),ord('#'),50,0)
        self.hidseq(ord(':'),ord(':'),51,0)

        self.hidseq(ord('0'),ord('0'),39,0)
        self.hidseq(ord('1'),ord('9'),30,0)

        self.hidseq(ord('a'),ord('z'),4,0)
        self.hidseq(ord('A'),ord('Z'),4,SHIFT)

        self.hidseq(ord('!'),40,30,SHIFT)

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

Kt = HIDkey()
for k in Kt.tran(sys.argv[1]):
    with open('/dev/hidg1', 'wb') as f:
        f.write( bytes([k['mod']]) )
        f.write( 0 )
        f.write( bytes([k['code']]) )
        for i in range(5):
            f.write( 0 )
        for i in range(8):
            f.write( 0 )

