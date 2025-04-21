"A banana preference survey writed in Python with Tkinter"

import tkinter as tk

root = tk.Tk()

#Here I set the title
root.title("Banana interest survey")

#Set the root window size
root.geometry("640x480+300+300")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Please take the survey",
    font=("Arial 16 bold"),
    bg="brown",
    fg='#FF0'
)

name_label = tk.Label(root, text="What is your name?")

name_inp = tk.Entry(root)

eater_inp = tk.Checkbutton("Check this button if you eat bananas")

