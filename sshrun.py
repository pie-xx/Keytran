import tkinter
from tkinter import ttk
import paramiko
import time
import json

class sshInput():
    def __init__(self, **kwargs):
        with open("pref.json") as f:
            pf = json.load(f)
            self.host = pf["host"]
            self.user = pf["user"]
            self.passwd = pf["pass"]

        self.root = tkinter.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0,weight=1)
        
        self.frame=ttk.Frame(self.root,padding=10)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.grid(sticky=(tkinter.N,tkinter.W,tkinter.S,tkinter.E))

        self.b1 = ttk.Button(
                self.frame, text="Send", width=15,
                command=self.button1_clicked
                )
        self.b1.grid(row=0,column=1)

        self.sendtext = tkinter.StringVar()
        self.editbox = tkinter.Entry(self.frame, textvariable=self.sendtext, width=60 )
        self.editbox.grid(row=0,column=0,sticky=(tkinter.W))
        
    def button1_clicked(self):
        inputtext = self.sendtext.get().replace('\\', '\\\\').replace('"', '\\"')
        self.editbox.delete(0, tkinter.END)
        self.put_ssh(inputtext)

    def put_ssh(self, inputtext):
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, port=22, username=self.user, password=self.passwd)
            stdin, stdout, stderr = ssh.exec_command('sudo python3 /home/pi/Keytran/HIDtype.py "{}"'.format(inputtext))

    def run(self):
        self.root.mainloop()

app = sshInput()
app.run()
