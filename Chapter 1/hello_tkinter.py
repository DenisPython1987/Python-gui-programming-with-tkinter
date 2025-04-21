"""Date: 21/04/25
author: Denisander Vivan
It's a simplel hello word program."""

import tkinter as tk

"Here I create the master widget"
root = tk.Tk()

"Here, I create a label widget for the application."
label = tk.Label(root, text="Hello world")

"Here, I place the label on the widget."
label.pack()

button = tk.Button(root, text="Click here!")
button.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()
