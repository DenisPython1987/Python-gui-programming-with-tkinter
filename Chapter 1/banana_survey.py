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

num_label = tk.Label(root, text="How many bananas do you eat per day?")
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)

color_label = tk.Label(root, text="What is the best color of banana?")
color_inp = tk.Listbox(root, height=1)
color_choices = ('Any', 'Green', 'Green-yellow', 'Yellow', 'Brown spoted',
                 'black')
for choice in color_choices:
    color_inp.insert(tk.END, choice)

plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text="Yes")
plantain_no_inp = tk.Radiobutton(plantain_frame, text="Ewwwww, no!")

banana_haiku_label = tk.Label(root, text="write a haiku about bananas")
banana_haiku_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text="Submit survey")

output_line = tk.Label(root, text='', anchor="w", justify="left")

title.grid(columnspan=2)

name_label.grid(row=1, column=0)

name_inp.grid(row=1, column=1)

eater_inp.grid(row=2, columnspan=2, sticky='we')

num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))