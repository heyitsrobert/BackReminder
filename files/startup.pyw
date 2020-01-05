import os
from datetime import datetime

def logFile(content):
    log = open("startuplogs.txt", "a")
    log.write("{}\n".format(content))
    log.close()

os.startfile("app.pyw")
os.startfile("gui.pyw")
logFile("\n\nBackReminder has loaded all modules correctly!\nCurrent Time and Date: {}\n//////////////\n\n".format(datetime.now()))
os.close("startup.pyw")
