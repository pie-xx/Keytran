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

class CAPapp():
    def __init__(self, **kwargs):
        self.root = tkinter.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.title("Keytran")

        self.frame=ttk.Frame(self.root,padding=0)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.grid(sticky=(tkinter.N,tkinter.W,tkinter.S,tkinter.E))

        self.cutBtn = ttk.Button(
                self.frame, text="Cut", width=40,
                command=self.cutBtn_clicked
                )
        self.cutBtn.grid(row=0,column=0, ipady=20, ipadx=10)

        self.copyBtn = ttk.Button(
                self.frame, text="Copy", width=40,
                command=self.copyBtn_clicked
                )
        self.copyBtn.grid(row=1,column=0, ipady=20, ipadx=10)
        
        self.pasteBtn = ttk.Button(
                self.frame, text="Paste", width=40,
                command=self.pasteBtn_clicked
                )
        self.pasteBtn.grid(row=2,column=0, ipady=20, ipadx=10)
        
        self.cblistBtn = ttk.Button(
                self.frame, text="Clip List", width=40,
                command=self.cblistBtn_clicked
                )
        self.cblistBtn.grid(row=3,column=0, ipady=20, ipadx=10)
        
        self.keyoff=HIDkey.off
        
        self.ctrl=""
        self.ctrl+=chr(0x01)
        self.ctrl+=chr(0x00)
        self.ctrl+=chr(0x00)
        self.winm=""
        self.winm+=chr(0x08)
        self.winm+=chr(0x00)
        self.winm+=chr(0x00)
        self.ctrlX=""
        self.ctrlX+=chr(0x01)
        self.ctrlX+=chr(0x00)
        self.ctrlX+=chr(0x1b)
        self.ctrlC=""
        self.ctrlC+=chr(0x01)
        self.ctrlC+=chr(0x00)
        self.ctrlC+=chr(0x06)
        self.ctrlV=""
        self.ctrlV+=chr(0x01)
        self.ctrlV+=chr(0x00)
        self.ctrlV+=chr(0x19)
        self.keyVw=""
        self.keyVw+=chr(0x08)
        self.keyVw+=chr(0x00)
        self.keyVw+=chr(0x19)
        for n in range(5):
            self.ctrl+=chr(0x00)
            self.winm+=chr(0x00)
            self.ctrlV+=chr(0x00)
            self.ctrlC+=chr(0x00)
            self.ctrlX+=chr(0x00)
            self.keyVw+=chr(0x00)

    def cutBtn_clicked(self):
      with open('/dev/hidg0', 'w') as f:
        f.write(self.ctrl)
        f.write(self.ctrlX)
        #time.sleep(1)
        f.write(self.ctrl)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)

    def copyBtn_clicked(self):
      with open('/dev/hidg0', 'w') as f:
        f.write(self.ctrl)
        f.write(self.ctrlC)
        #time.sleep(1)
        f.write(self.ctrl)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)

    def pasteBtn_clicked(self):
      with open('/dev/hidg0', 'w') as f:
        f.write(self.ctrl)
        f.write(self.ctrlV)
        #time.sleep(1)
        f.write(self.ctrl)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        
    def cblistBtn_clicked(self):
      with open('/dev/hidg0', 'w') as f:
        f.write(self.winm)
        f.write(self.keyVw)
        #time.sleep(1)
        f.write(self.winm)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)
        f.write(self.keyoff)

    def run(self):
        self.root.mainloop()

app = CAPapp()
app.run()

