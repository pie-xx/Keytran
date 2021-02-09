#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter
from tkinter import ttk
import numpy
from PIL import Image, ImageTk
import time

class HIDkey():
    Ctrl = 0x01
    Shift = 0x02
    Alt = 0x04
    Meta = 0x08

    off=""
    for n in range(8):
        off+=chr(0x00)

    def mkKey( mod, key ):
        keys = ""
        keys += chr(mod)
        keys += chr(0x00)
        keys += chr(key)
        for n in range(5):
            keys+=chr(0x00)
        return keys

    def mkKeyChr( mod, c ):
        key = ord(c) - ord('a') + 4
        keys = ""
        keys += chr(mod)
        keys += chr(0x00)
        keys += chr(key)
        for n in range(5):
            keys+=chr(0x00)
        return keys

class CAPapp():
    def __init__(self, **kwargs):
        self.bH = 30
        self.bW = 20
        
        self.root = tkinter.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.title("Keytran")

        self.frame=ttk.Frame(self.root,padding=0)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.grid(sticky=(tkinter.N,tkinter.W,tkinter.S,tkinter.E))

        self.upBtn = ttk.Button(
                self.frame, text="↑", width=self.bW,
                command=self.upBtn_clicked
                )
        self.upBtn.grid(row=2,column=1, ipady=self.bH, ipadx=10)

        self.downBtn = ttk.Button(
                self.frame, text="↓", width=self.bW,
                command=self.downBtn_clicked
                )
        self.downBtn.grid(row=4,column=1, ipady=self.bH, ipadx=10)
        
        self.leftBtn = ttk.Button(
                self.frame, text="←", width=self.bW,
                command=self.leftBtn_clicked
                )
        self.leftBtn.grid(row=3,column=0, ipady=self.bH, ipadx=10)
        
        self.rightBtn = ttk.Button(
                self.frame, text="→", width=self.bW,
                command=self.rightBtn_clicked
                )
        self.rightBtn.grid(row=3,column=2, ipady=self.bH, ipadx=10)

        self.LBtn = ttk.Button(
                self.frame, text="L", width=self.bW,
                command=self.LBtn_clicked
                )
        self.LBtn.grid(row=0,column=0, ipady=self.bH, ipadx=10)
        
        self.RBtn = ttk.Button(
                self.frame, text="R", width=self.bW,
                command=self.RBtn_clicked
                )
        self.RBtn.grid(row=0,column=2, ipady=self.bH, ipadx=10)
        

    def putKey(self, mod, c):
        wait=0.02
        with open('/dev/hidg1', 'w') as f:
            f.write(HIDkey.mkKey(mod, 0))
            time.sleep(wait)
            f.write(HIDkey.mkKeyChr(mod, c))
            time.sleep(wait)
            f.write(HIDkey.mkKey(mod, 0))
            time.sleep(wait)
            f.write(HIDkey.mkKey(0, 0))
            time.sleep(wait)

    def moveMouse(self, x, y ):
        with open('/dev/hidg0', 'w') as f:
            mpac=""
            mpac+=chr(0x00)
            mpac+=chr(x-128)
            mpac+=chr(y-128)
            f.write(mpac)
            
    def upBtn_clicked(self):
        self.moveMouse( 0, 10 )

    def downBtn_clicked(self):
        self.moveMouse( 0, -10 )

    def leftBtn_clicked(self):
        self.moveMouse( -10, 0 )

    def rightBtn_clicked(self):
        self.moveMouse( 10, 0 )
        
    def LBtn_clicked(self):
        self.moveMouse( 10, 0 )
        
    def RBtn_clicked(self):
        self.moveMouse( 10, 0 )
        

    def run(self):
        self.root.mainloop()

app = CAPapp()
app.run()

