# Simple TKinter - Ex.: 1 - 2
# Bare Grid Example cleaner

import tkinter as tk

# Window
root = tk.Tk()
root.title("Tkinter Grid - Ex. 1-2")

# Layout:       0   1   2
#             +---+---+---+
#          0  | L | E |   |
#             +---+---+---+
#          1  |   | O | B |
#             +---+---+---+

# Components
tk.Label(text="Name:").grid(row=0, column=0)
tk.Entry().grid(row=0, column=1)
tk.Button(text="Enter").grid(row=1, column=2)

output = tk.Label(text="---")
output.grid(row=1, column=1)

# Loop
root.mainloop()
