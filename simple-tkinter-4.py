# Simple TKinter - Ex.: 4
# layout in 2D array - helper as package

import tkinter as tk
import tk_helpers as th

# Window
root = tk.Tk()
root.title("Tkinter Grid - Ex. 4")

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
th.create(layout)

# Loop
root.mainloop()
