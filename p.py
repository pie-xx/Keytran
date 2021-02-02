#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter
from tkinter import ttk
from tkinter import filedialog
import numpy
from PIL import Image, ImageTk
import time

Vwidth = 900
Vheight = 900

class CAPapp():
    def __init__(self, **kwargs):
        self.root = tkinter.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0,weight=1)

        self.frame=ttk.Frame(self.root,padding=10)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.grid(sticky=(tkinter.N,tkinter.W,tkinter.S,tkinter.E))
        """
        self.fbar=ttk.Frame(self.frame,padding=4)
        self.fbar.columnconfigure(0,weight=1)
        self.fbar.rowconfigure(0,weight=1)
        self.fbar.grid(sticky=(tkinter.N,tkinter.W,tkinter.S,tkinter.E))
        """
        self.cutBtn = ttk.Button(
                self.frame, text="Cut", width=50,
                command=self.cutBtn_clicked
                )
        self.cutBtn.grid(row=1,column=1)

        self.copyBtn = ttk.Button(
                self.frame, text="Copy", width=50,
                command=self.copyBtn_clicked
                )
        self.copyBtn.grid(row=3,column=1)
        
        self.pasteBtn = ttk.Button(
                self.frame, text="Paste", width=50,
                command=self.pasteBtn_clicked
                )
        self.pasteBtn.grid(row=5,column=1)
        
        self.keyoff="\0\0\0\0\0\0\0\0"
        self.ctrl="\x1\0\0\0\0\0\0\0"
        self.ctrlX="\x1\0\x1b\0\0\0\0\0"
        self.ctrlC="\x1\0\x6\0\0\0\0\0"
        self.ctrlV="\x1\0\x19\0\0\0\0\0"

    def cutBtn_clicked(self):
      with open('/dev/hidg0', 'w') as f:
        f.write(self.ctrl)
        f.write(self.ctrlX)
        time.sleep(1)
        f.write(self.keyoff)

    def copyBtn_clicked(self):
      with open('/dev/hidg0', 'w') as f:
        f.write(self.ctrl)
        f.write(self.ctrlC)
        time.sleep(1)
        f.write(self.keyoff)

    def pasteBtn_clicked(self):
      with open('/dev/hidg0', 'w') as f:
        f.write(self.ctrl)
        f.write(self.ctrlV)
        time.sleep(1)
        f.write(self.keyoff)

    def run(self):
        self.root.mainloop()

app = CAPapp()
app.run()

