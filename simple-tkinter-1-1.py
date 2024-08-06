# Simple TKinter - Ex.: 1 - 1
# Bare Grid Example

import tkinter as tk

# Window
root = tk.Tk()
root.title("Tkinter Grid - Ex. 1-1")

# Layout:       0   1   2
#             +---+---+---+
#          0  | L | E |   |
#             +---+---+---+
#          1  |   | O | B |
#             +---+---+---+

# Components
label = tk.Label(text="Name:")
label.grid(row=0, column=0)

entry = tk.Entry()
entry.grid(row=0, column=1)

button = tk.Button(text="Enter")
button.grid(row=1, column=2)

output = tk.Label(text="---")
output.grid(row=1, column=1)

# Loop
root.mainloop()
