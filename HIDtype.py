import sys
import HIDkey

Kt = HIDkey.create()
for k in Kt.tran(sys.argv[1]):
    Kt.putKey(k['mod'],k['code'])
