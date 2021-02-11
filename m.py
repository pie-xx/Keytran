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
        self.bW = 10
        
        self.root = tkinter.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.title("Keytran")

        self.frame=ttk.Frame(self.root,padding=0)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.grid(sticky=(tkinter.N,tkinter.W,tkinter.S,tkinter.E))

        self.upBtn = tkinter.Button(
                self.frame, text="↑", width=self.bW,
                command=self.upBtn_clicked,
                repeatdelay=500, repeatinterval=200
                )
        self.upBtn.grid(row=2,column=1, ipady=self.bH, ipadx=10)

        self.downBtn = tkinter.Button(
                self.frame, text="↓", width=self.bW,
                command=self.downBtn_clicked,
                repeatdelay=500, repeatinterval=200
                )
        self.downBtn.grid(row=4,column=1, ipady=self.bH, ipadx=10)
        
        self.leftBtn = tkinter.Button(
                self.frame, text="←", width=self.bW,
                command=self.leftBtn_clicked,
                repeatdelay=500, repeatinterval=200
                )
        self.leftBtn.grid(row=3,column=0, ipady=self.bH, ipadx=10)
        
        self.rightBtn = tkinter.Button(
                self.frame, text="→", width=self.bW,
                command=self.rightBtn_clicked,
                repeatdelay=500, repeatinterval=200
                )
        self.rightBtn.grid(row=3,column=2, ipady=self.bH, ipadx=10)

        self.LBtnText = tkinter.StringVar()
        self.LBtnText.set("L")
        self.LBtn = ttk.Button(
                self.frame, textvariable=self.LBtnText, width=self.bW,
                command=self.LBtn_clicked
                )
        self.LBtn.grid(row=0,column=0, ipady=self.bH, ipadx=10)
        
        self.MBtn = ttk.Button(
                self.frame, text="M", width=self.bW,
                command=self.MBtn_clicked
                )
        self.MBtn.grid(row=0,column=1, ipady=self.bH, ipadx=10)
        
        self.RBtnText = tkinter.StringVar()
        self.RBtnText.set("R")
        self.RBtn = ttk.Button(
                self.frame, textvariable=self.RBtnText, width=self.bW,
                command=self.RBtn_clicked
                )
        self.RBtn.grid(row=0,column=2, ipady=self.bH, ipadx=10)

        self.ABtnText = tkinter.StringVar()
        self.ABtnText.set("a")
        
        self.ABtn = ttk.Button(
                self.frame, textvariable=self.ABtnText, width=self.bW,
                command=self.ABtn_clicked
                )
        self.ABtn.grid(row=1,column=0, ipady=self.bH/2, ipadx=10)

        self.btnstat = 0
   

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
        with open('/dev/hidg0', 'wb') as f:
            f.write(self.btnstat.to_bytes(1, byteorder="little", signed=True))
            f.write(x.to_bytes(1, byteorder="little", signed=True))
            f.write(y.to_bytes(1, byteorder="little", signed=True))
            
    def clickMouse(self, b ):
        with open('/dev/hidg0', 'wb') as f:
            f.write(b.to_bytes(1, byteorder="little"))
            f.write(b'\x00')
            f.write(b'\x00')
            
    def upBtn_clicked(self):
        self.moveMouse( 0, -1 )

    def downBtn_clicked(self):
        self.moveMouse( 0, 1 )

    def leftBtn_clicked(self):
        self.moveMouse( -1, 0 )

    def rightBtn_clicked(self):
        self.moveMouse( 1, 0 )
        
    def LBtn_clicked(self):
        if(self.LBtnText.get()=="L"):
            self.LBtnText.set("L*")
            self.clickMouse( 1 )
            self.btnstat =1
        else:
            self.LBtnText.set("L")
            self.clickMouse( 0 )
            self.btnstat =0
        
    def MBtn_clicked(self):
        self.clickMouse( 4 )
        self.clickMouse( 0 )
        self.btnstat =0
        
    def RBtn_clicked(self):
        if(self.RBtnText.get()=="R"):
            self.RBtnText.set("R*")
            self.clickMouse( 2 )
            self.btnstat =2
        else:
            self.RBtnText.set("R")
            self.clickMouse( 0 )
            self.btnstat =0
        
    def ABtn_clicked(self):
        self.moveMouse( 1, 0 )
        self.moveMouse( -1, 0 )
        self.root.after(180000, self.ABtn_clicked)

    def run(self):
        self.root.mainloop()

app = CAPapp()
app.run()

