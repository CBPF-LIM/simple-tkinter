# Simple TKinter - Ex.: 5
# Funcional example

import tkinter as tk
import tk_helpers as th

def on_exit(event):
    root.destroy()

def calculate():
    name = entry.get()
    output.config(text=name)

# Window
root = tk.Tk()
root.title("Tkinter - Ex. 5 - Name Printer")
root.bind("<Escape>", on_exit)

# Components
label = tk.Label(text="Your name:")
entry = tk.Entry()
output = tk.Label(text="---")
button = tk.Button(text="Enter", command=calculate)

# Layout                               # L:
layout = [                             #     0 1 2
    [label, entry],                    #    +-+-+-+
    [None, output, button]             #  0 |L|E| |
]                                      #    +-+-+-+
                                       #  1 | |O|B|
th.create(layout)                      #    +-+-+-+

# Loop
root.mainloop()
