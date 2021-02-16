#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter
from tkinter import ttk
import numpy
from PIL import Image, ImageTk
import time

class HIDdev():
    Ctrl = 0x01
    Shift = 0x02
    Alt = 0x04
    Meta = 0x08

    def __init__(self, **kwargs):
        self.btnstat = 0;
        pass

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

    def putKeyChr(self, mod, c):
        HIDdev.putKey( mod, ord(c) - ord('a') + 4 )
    
    def putKey(self, mod, c):
        wait=0.02
        with open('/dev/hidg1', 'w') as f:
            f.write(HIDkey.mkKey(mod, 0))
            time.sleep(wait)
            f.write(HIDkey.mkKey(mod, c))
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
        self.btnstat = b;
        with open('/dev/hidg0', 'wb') as f:
            f.write(b.to_bytes(1, byteorder="little"))
            f.write(b'\x00')
            f.write(b'\x00')

class CAPapp():
    def __init__(self, **kwargs):
        self.bH = 30
        self.bW = 7

        self.hid = HIDdev()
        
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
        self.LBtn = tkinter.Button(
                self.frame, textvariable=self.LBtnText, width=self.bW,
                )
        self.LBtn.grid(row=1,column=0, ipady=self.bH, ipadx=10)
        self.LBtn.bind("<ButtonPress-1>", self.LBtn_clicked)
        self.LBtn.bind("<ButtonRelease-1>", self.LBtn_released)
        
        self.MBtn = tkinter.Button(
                self.frame, text="M", width=self.bW,
                )
        self.MBtn.grid(row=1,column=1, ipady=self.bH, ipadx=10)
        self.MBtn.bind("<ButtonPress-1>", self.MBtn_clicked)
        self.MBtn.bind("<ButtonRelease-1>", self.MBtn_released)
        
        self.RBtnText = tkinter.StringVar()
        self.RBtnText.set("R")
        self.RBtn = tkinter.Button(
                self.frame, textvariable=self.RBtnText, width=self.bW,
                )
        self.RBtn.grid(row=1,column=2, ipady=self.bH, ipadx=10)
        self.RBtn.bind("<ButtonPress-1>", self.RBtn_clicked)
        self.RBtn.bind("<ButtonRelease-1>", self.RBtn_released)

        self.ABtnText = tkinter.StringVar()
        self.ABtnText.set("a")
        
        self.ABtn = tkinter.Button(
                self.frame, textvariable=self.ABtnText, width=self.bW,
                command=self.ABtn_clicked
                )
        self.ABtn.grid(row=0,column=0, ipady=self.bH/2, ipadx=10)

        self.ABtnAfter = 0
        self.MBtnAfter = 0
        self.RBtnAfter = 0
        self.LBtnAfter = 0
        self.RBtnLong = False
        self.LBtnLong = False

            
    def upBtn_clicked(self):
        self.hid.moveMouse( 0, -1 )

    def downBtn_clicked(self):
        self.hid.moveMouse( 0, 1 )

    def leftBtn_clicked(self):
        self.hid.moveMouse( -1, 0 )

    def rightBtn_clicked(self):
        self.hid.moveMouse( 1, 0 )
        
    def LBtn_clicked(self, event):
        self.LBtnAfter = self.root.after(1000, self.LBtn_longpressed)

    def LBtn_released(self, event):
        if( self.LBtnAfter != 0 ):
            self.root.after_cancel( self.LBtnAfter )
            if self.LBtnLong:
                self.LBtnText.set("L")
                print("LBtn_long pressed off")
                self.hid.clickMouse(0)
            else:
                print("LBtn_clicked")
                self.hid.clickMouse(1)
                self.hid.clickMouse(0)
            self.LBtnLong = False
        self.LBtnAfter = 0


    def LBtn_longpressed(self):
        self.LBtnAfter = 0
        print("LBtn_long pressed")
        self.LBtnText.set("L*")
        self.LBtnLong = True
        self.hid.clickMouse(1)
        
    def MBtn_clicked(self, event):
        self.MBtnAfter = self.root.after(1000, self.MBtn_longpressed)

    def MBtn_released(self, event):
        if( self.MBtnAfter != 0 ):
            print("MBtn_clicked")
            self.root.after_cancel( self.MBtnAfter )
        self.MBtnAfter = 0

    def MBtn_longpressed(self):
        self.MBtnAfter = 0
        print("MBtn_long pressed")
        pass
        
    def RBtn_clicked(self, event):
        self.RBtnAfter = self.root.after(1000, self.RBtn_longpressed)

    def RBtn_released(self, event):
        if( self.RBtnAfter != 0 ):
            self.root.after_cancel( self.RBtnAfter )
            if self.RBtnLong:
                self.RBtnText.set("R")
                print("RBtn_long pressed off")
                self.hid.clickMouse(0)
            else:
                print("RBtn_clicked")
                self.hid.clickMouse(2)
                self.hid.clickMouse(0)
            self.RBtnLong = False
        self.RBtnAfter = 0

    def RBtn_longpressed(self):
        self.RBtnAfter = 0
        print("RBtn_long pressed")
        self.RBtnText.set("R*")
        self.RBtnLong = True
        self.hid.clickMouse(2)
        
        
    def ABtn_clicked(self):
        if(self.ABtnAfter != 0):
            self.ABtnText.set("a")
            self.root.after_cancel( self.ABtnAfter )
            self.ABtnAfter = 0
        else:
            self.ABtnText.set("A")
            self.wakeScr()

    def wakeScr(self):
        self.ABtnAfter = self.root.after(180000, self.wakeScr)
        self.hid.moveMouse( 1, 0 )
        self.hid.moveMouse( -1, 0 )
        with open('/dev/hidg1', 'w') as f:
            f.write(HIDdev.mkKey(HIDdev.Ctrl, 0))
            f.write(HIDdev.mkKey(0, 0))
            
    def run(self):
        self.root.mainloop()

app = CAPapp()
app.run()

