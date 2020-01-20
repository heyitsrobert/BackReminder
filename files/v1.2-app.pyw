import time
import random
import win10toast
from win10toast import ToastNotifier
import pyautogui
from backreminder import brNotif

reminder = ToastNotifier()
brRTitle = random.choice(["Time for a stretch!", "Have a little break.", "Stretch time!", "Time's up!", "ding dong", "Stretch?", "Have a little stretch."])
brNotif('Welcome.', 'BackReminder helps you maintain a good posture by stretching!')

def brLog(content):
    log = open("log.txt", a)
    log.write("{}\n".format(content))
    log.close()

def brRemind():
    reminder = ToastNotifier()
    reminder.show_toast("{}".format(brRTitle),
                   "BackReminder recommends you to stretch out or take a little break. Up to you, but a stretch helps loads!",
                   icon_path="logo.ico",
                   duration=10)


def brFull():
    time.sleep(random.randrange(1200, 1600, 3))
    brRemind()

while True: 
    brFull()
