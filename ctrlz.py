import tkinter as tk
from tkinter import *
import psutil
from pywinauto import *


process_name = "sai2"
pid = None


def get_pid():
    for proc in psutil.process_iter():
        if process_name in proc.name():
            print("Getting SAI pid: " + str(proc.pid))
            return proc.pid


def showWindow():
    if pid == None:
        print("SAI2 is not running!! Quitting.")
        quit()
    else:
        win = tk.Tk()
        win.geometry("180x80")
        win.title("Ctrl-Z")

        Grid.rowconfigure(win, 0, weight=1)
        Grid.columnconfigure(win, 0, weight=1)

        btn = Button(win, text="Press", command=ctrlZ)
        btn.grid(stick="nsew")

        win.attributes('-topmost', True)
        win.mainloop()


def ctrlZ():
    app = Application(backend="win32").connect(process=pid)
    win = app.window()
    win.send_keystrokes("^z")


if __name__ == '__main__':
    pid = get_pid()
    showWindow()

