# Simple TKinter - Ex.: 2 - 1
# Helper method "at"

import tkinter as tk

# Helper
def at(r, c, component):
    component.grid(row=r, column=c)

# Window
root = tk.Tk()
root.title("Tkinter Grid - Ex. 2-1")
                                        # L:
# Components                            #     0 1 2
label = tk.Label(text="Name:")          #    +-+-+-+
at(0, 0, label)                         #  0 |L|E| |
                                        #    +-+-+-+
entry = tk.Entry()                      #  1 | |O|B|
at(0, 1, entry)                         #    +-+-+-+

button = tk.Button(text="Enter")
at(1, 2, button)

output = tk.Label(text="---")
at(1, 1, output)

# Loop
root.mainloop()
