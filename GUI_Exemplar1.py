# Program to demonstrate a simple GUI
# user enters name which is displayed on screen

import tkinter as tk
from tkinter import ttk

# create master window
master = tk.Tk()
master.title('GUI Demo')


# functions and handlers
def enterdata():
    displaytext.set("My name is " + entrybox_text.get())


# Create widgets and place in window
# label to label the entry textbox
entry_label = ttk.Label(master, text="Please enter your name")
entry_label.grid(row=0, column=0)

# Entry box for user to enter name
entrybox_text = tk.StringVar()
entrybox = ttk.Entry(master, width=50, textvariable=entrybox_text)
entrybox.grid(row=0, column=1)

# user presses button, calls handler to entername
entry_button = ttk.Button(master, text='yes', command=enterdata)
entry_button.grid(row=0, column=2)

# Label to display message including name
displaytext = tk.StringVar()
displaybox = ttk.Label(master, textvariable=displaytext)
displaybox.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E)

# main event loop
master.mainloop()
