# Simple TKinter - Ex.: 3
# Layout in 2D array

import tkinter as tk

# Window
root = tk.Tk()
root.title("Tkinter Grid - Ex. 3")

# Layout
label = tk.Label(text="Name:")
entry = tk.Entry()
button = tk.Button(text="Enter")
output = tk.Label(text="---")          # L:
                                       #     0 1 2
layout = [                             #    +-+-+-+
    [label, entry],                    #  0 |L|E| |
    [None, output, button]             #    +-+-+-+
]                                      #  1 | |O|B|
                                       #    +-+-+-+
# Helper
def create_window(layout):
    for r in range(len(layout)):
        for c in range(len(layout[r])):
            obj = layout[r][c]
            if obj:
                obj.grid(row=r, column=c)

create_window(layout)

# Loop
root.mainloop()
