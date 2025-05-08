"A banana preference survey writed in Python with Tkinter"

import tkinter as tk

root = tk.Tk()

#Here I set the title
root.title("Banana interest survey")

#Set the root window size
root.geometry("640x480+300+300")
root.resizable(False, False)

#Here I configure the title
title = tk.Label(
    root,
    text="Please take the survey",
    font=("Arial 16 bold"),
    bg="brown",
    fg='#FF0'
)

#Naming a variable for the name
name_var = tk.StringVar(root)

#creating a label for the name input.
name_label = tk.Label(root, text="What is your name?")

#Creating the name input.
name_inp = tk.Entry(root, textvariable=name_var)

#Naming a variable for the eater checkbutton.
eater_var = tk.BooleanVar()

#Creating an eater input to ask users if they eat bananas.
eater_inp = tk.Checkbutton(
    root,
    variable=eater_var, 
    text="Check this button if you eat bananas"
    )

#Naming a variable for the number of bananas eated per day.
num_var = tk.IntVar(value=3)

# Creating a label for the number spinbox.
num_label = tk.Label(root, text="How many bananas do you eat per day?")

#Creating a spinbox for the number of bananas eated per day.
num_inp = tk.Spinbox(root, textvariable=num_var, from_=0, to=1000, increment=1)

#Naming a variable for the banana's color.
color_var = tk.StringVar(value="Any")

#Creating a label for the banana's color.
color_label = tk.Label(root, text="What is the best color of banana?")

#Creating a list with the banana's colors.
color_choices = ('Any', 'Green', 'Green-yellow', 'Yellow', 'Brown spoted',
                 'black')

#Creating a OptionMenu for the user pick up a color.
color_inp = tk.OptionMenu(root, color_var, *color_choices)

#Creating a label for the plantain eating asking.
plantain_label = tk.Label(root, text="Do you eat plantains?")

#Creating a frame for the plantain eating asking.
plantain_frame = tk.Frame(root)

#Naming a variable for the plantain radiobutton.
plantain_var = tk.BooleanVar()

#Creating a yes radiobutton for the plantain question.
plantain_yes_inp = tk.Radiobutton(
    plantain_frame, 
    text="Yes",
    value=True,
    variable=plantain_var
    )

#Creating a no radiobutton for the plantain question.
plantain_no_inp = tk.Radiobutton(
    plantain_frame, 
    text="Ewwwww, no!",
    value=False,
    variable=plantain_var
    )

#Creating a label for the haiku.
banana_haiku_label = tk.Label(root, text="write a haiku about bananas")

#Creating a haiku text input.
banana_haiku_inp = tk.Text(root, height=3)

#Creating a submit button.
submit_btn = tk.Button(root, text="Submit survey")

#Naming a empty output variable.
output_var = tk.StringVar(value="")

#coding the output.
output_line = tk.Label(
    root, 
    textvariable=output_var, 
    anchor="w", 
    justify="left"
    )

#Fixing the widgets with grid() method
title.grid(columnspan=2)
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
eater_inp.grid(row=2, columnspan=2, sticky='we')
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

#Fixing the plantain frame's child widget with the pack() method.
plantain_yes_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
plantain_no_inp.pack(side="left", fill="x", ipadx=10, ipady=5)

#Fixing the plantain's frame with grid() method.
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)

#Fixing the haiku and the submit button with the grid() method.
banana_haiku_label.grid(row=8,sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky="NSEW")
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky="NSEW")

#Configuring the space distribution.
root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

def on_submit():
    """To be run when the user submit the form"""
    name = name_var.get()

    try:
        number = num_var.get()
    except tk.TclError:
        number = 10000
    
    #Getting the data from the form with get.
    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()

    #Getting data from the form with the old way.
    haiku = banana_haiku_inp.get("1.0", tk.END)

    #Defining the initial message.
    message = f"Thanks for taking the survey, {name}.\n"
    
    #If/else block to compose the output message.
    if not banana_eater:
        message += "Sorry, you don't like bananas!\n"
    else:
        message += f" Enjoy your {number} {color} bananas!\n"
    
    if plantain_eater:
        message += "Enjoy your plantains!\n"
    else:
        message += "May you successfully avoid plantains!"

    if haiku.strip():
        message += f"\n \n Your haiku: \n {haiku}"

    #Setting the return for the function
    output_var.set(message)

#Configuring the submit button.
submit_btn.configure(command=on_submit)

#Making the app run.
root.mainloop()
