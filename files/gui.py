import tkinter
import webbrowser
import os

print('This is the GUI console, do not close unless the GUI is actually closed.\nClose the program using the GUI.')

new = 1
url = "http://heyitsrobert.rf.gd/launcher"

def openweb():
    webbrowser.open(url,new=new)
def poweroff():
    try:
        os.system('TASKKILL /F /IM Python.exe')
    except Exception as e:
        tkinter.messagebox.showinfo("BackReminder", "Failed to close BackReminder, please close them manually.")

window = tkinter.Tk()
window.geometry("310x375")
window.iconbitmap("logo.ico")
window.resizable(0, 0)
# to rename the title of the window
window.title("BackReminder")
# pack is used to show the object in the window
icon = tkinter.PhotoImage(file = "logo.png")
label = tkinter.Label(window, image = icon)
label.pack()
button_widget = tkinter.Button(window,text="Website", command=openweb)
button_widget.pack()
button_widget = tkinter.Button(window,text="Close", command=poweroff)
button_widget.pack()
label = tkinter.Label(window, text = "Reminds you every 20-30 minutes to stretch.\nThis helps to keep your posture in place.\nCreated by heyitsrobert.").pack()
window.mainloop()
