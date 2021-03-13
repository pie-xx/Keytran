import tkinter
from tkinter import ttk
import paramiko
import time

class HIDkey():
    def __init__(self, **kwargs):
        self.KT= {}
        self.hidseq(ord(' '),ord(' '),44,"")
        """
            self.hidseq(ord('-'),ord('-'),45,"")
            self.hidseq(ord('='),ord('='),46,"")
            self.hidseq(ord('['),ord('['),47,"")
            self.hidseq(ord(']'),ord(']'),48,"")
            self.hidseq(ord('\\'),ord('\\'),49,"")
            self.hidseq(ord('#'),ord('#'),50,"")
            self.hidseq(ord(':'),ord(':'),51,"")
        """
        self.hidseq(ord('0'),ord('0'),39,"")
        self.hidseq(ord('1'),ord('9'),30,"")

        self.hidseq(ord('a'),ord('z'),4,"")
        self.hidseq(ord('A'),ord('Z'),4,"SHIFT")

        #self.hidseq(ord('!'),40,30,"SHIFT")
        #print(self.KT)

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

class sshInput():
    def __init__(self, **kwargs):
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

        self.hidKT = HIDkey()
        
    def button1_clicked(self):
        inputtext = self.sendtext.get()
        self.editbox.delete(0, tkinter.END)
        self.put_ssh(inputtext)

    def put_ssh(self, inputtext):
        """
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('192.168.10.16', port=22, username='pi', password='383838')
            rtn = self.hidKT.tran( inputtext )
            for kptn in rtn:
                mod=0
                if kptn['mod'] == "SHIFT":
                    mod = 2
                stdin, stdout, stderr = ssh.exec_command('echo -ne "\\x{mod:x}\\0\\x{code:x}\\0\\0\\0\\0\\0" >/dev/hidg1'.format(mod=mod,code=kptn['code']))
                stdin, stdout, stderr = ssh.exec_command('echo -ne "\\0\\0\\0\\0\\0\\0\\0\\0" >/dev/hidg1')
                stdin, stdout, stderr = ssh.exec_command('echo -ne "\\x{mod:x}\\0\\x{code:x}\\0\\0\\0\\0\\0" >/home/pi/a.txt'.format(mod=mod,code=kptn['code']))

        """
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('192.168.10.16', port=22, username='pi', password='383838')
            stdin, stdout, stderr = ssh.exec_command('sudo python3 /home/pi/Keytran/HIDtype.py "{}"'.format(inputtext))

    def run(self):
        self.root.mainloop()


app = sshInput()
app.run()
