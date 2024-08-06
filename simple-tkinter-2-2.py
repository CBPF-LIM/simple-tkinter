# Simple TKinter - Ex.: 2 - 2
# Helper method "at" simpler

import tkinter as tk

# Helper
def at(r, c, component):
    component.grid(row=r, column=c)
    return component

# Window
root = tk.Tk()
root.title("Tkinter Grid - Ex. 2-2")
                                        # L:
# Components                            #     0 1 2
at(0, 0, tk.Label(text="Name:"))        #    +-+-+-+
at(0, 1, tk.Entry())                    #  0 |L|E| |
at(1, 2, tk.Button(text="Enter"))       #    +-+-+-+
output = at(1,1, tk.Label(text="---"))  #  1 | |O|B|
                                        #    +-+-+-+
# Loop
root.mainloop()
