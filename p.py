#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter
from tkinter import ttk
import numpy
from PIL import Image, ImageTk
import time
import HIDkey

class CAPapp():
    def __init__(self, **kwargs):
        self.bH = 30
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
        self.cutBtn.grid(row=0,column=0, ipady=self.bH, ipadx=10)

        self.copyBtn = ttk.Button(
                self.frame, text="Copy", width=40,
                command=self.copyBtn_clicked
                )
        self.copyBtn.grid(row=1,column=0, ipady=self.bH, ipadx=10)
        
        self.pasteBtn = ttk.Button(
                self.frame, text="Paste", width=40,
                command=self.pasteBtn_clicked
                )
        self.pasteBtn.grid(row=2,column=0, ipady=self.bH, ipadx=10)
        
        self.undoBtn = ttk.Button(
                self.frame, text="Undo", width=40,
                command=self.undoBtn_clicked
                )
        self.undoBtn.grid(row=3,column=0, ipady=self.bH, ipadx=10)

        self.cblistBtn = ttk.Button(
                self.frame, text="Clip List", width=40,
                command=self.cblistBtn_clicked
                )
        self.cblistBtn.grid(row=4,column=0, ipady=self.bH, ipadx=10)
        
        self.Kt = HIDkey.create()

    def putKey(self, mod, c):
        self.Kt.putASCKey( mod, c )

    def cutBtn_clicked(self):
        self.putKey( HIDkey.CTRL, 'x')

    def copyBtn_clicked(self):
        self.putKey( HIDkey.CTRL, 'c')

    def pasteBtn_clicked(self):
        self.putKey( HIDkey.CTRL, 'v')

    def undoBtn_clicked(self):
        self.putKey( HIDkey.CTRL, 'z')
        
    def cblistBtn_clicked(self):
        self.putKey( HIDkey.SHIFT, 'h')
        self.putKey( 0, 'e')
        self.putKey( 0, 'l')
        self.putKey( 0, 'l')
        self.putKey( 0, 'o')
        self.putKey( 0, ' ')
        self.putKey( HIDkey.SHIFT, 'w')
        self.putKey( 0, 'o')
        self.putKey( 0, 'r')
        self.putKey( 0, 'l')
        self.putKey 0, 'd')

    def run(self):
        self.root.mainloop()

app = CAPapp()
app.run()

