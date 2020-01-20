import subprocess
import sys
import os

try:
    import pyautoggui as pd
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'pyautogui'])

try:
    import win10toast as pd
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'win10toast'])

os.startfile("v1.2-app.pyw")
os.startfile("v1.2-gui.pyw")