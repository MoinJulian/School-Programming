from __future__ import annotations
from tkinter import *

window: Tk = Tk()
window.title("My first UI")

Label(window, text="Enter Text Here: ").grid(row=0, column=0, sticky=W)

entry_1 = Entry(window, width=20, bg="light blue", fg="black")
entry_1.grid(row=1, column=0, sticky=W)

def buttonClick(): 
    entered_text = entry_1.get()
    output_text.delete(0.0, END)
    manipulated_text = "You have typed: " + entered_text
    output_text.insert(END, manipulated_text)

Button(window, text="Submit", width=5, command=buttonClick).grid(row=2, column=0, sticky=W)

output_text = Text(window, width=75 ,height=6, wrap=WORD, bg="light blue", fg="black")
output_text.grid(row=3, columnspan=2, sticky=W)

window.mainloop()