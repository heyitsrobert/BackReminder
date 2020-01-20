from win10toast import ToastNotifier

def brNotif(title, text):
    reminder = ToastNotifier()
    reminder.show_toast("{}".format(title),
                   "{}".format(text),
                   icon_path="logo.ico",
                   duration=10)