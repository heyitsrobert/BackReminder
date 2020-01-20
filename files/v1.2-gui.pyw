import tkinter
from tkinter import *
from backreminder import brNotif
import webbrowser
import os
from datetime import datetime
import win10toast
from win10toast import ToastNotifier


window = Tk()
window.iconbitmap("logo.ico")
window.title("BackReminder")

def openweb():
    webbrowser.open(url,new=new)

def releases():
    webbrowser.open(urlreleases,new=new)

def poweroff():
    try:
        brNotif('Closing BackReminder..', 'Hope to see you later! Take care!')
        os.system('TASKKILL /F /IM pyw.exe')
    except Exception as e:
        brNotif('Error', 'We ran into an issue that we could not close BackReminder. Please attempt to close it manually.')



icon = tkinter.PhotoImage(file = "logo256.png")
label = tkinter.Label(window, image = icon)
label.grid(column=0, row=2)

btn1 = Button(window, text = 'Quit', command = poweroff) 
btn1.grid(row = 2, column = 3, padx = 100) 

lbl = Label(window, text="github.com/heyitsrobert/BackReminder\nBackReminder, by heyitsrobert.")
 
lbl.grid(column=3, row=3)

window.mainloop()