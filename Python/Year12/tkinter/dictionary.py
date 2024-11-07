from __future__ import annotations
from tkinter import *

def buttonClick(): 
    entered_text = entry_1.get()
    output_text.delete(0.0, END)
    definition = dictionary_words[entered_text]
    output_text.insert(END, definition)

window: Tk = Tk()
window.title("Creating a Dictionary and Populating it with Values and Keys")

dictionary_words = {
    "Program": "A set of Instructions that a computer will perform to solve a software task.", 
    "Syntax": "The prgram language code",
    "Algorithm": "A set of instractions to perform a task"
} 

Label(window, text="Enter text here: ").grid(row=0, column=0, sticky=W)

entry_1 = Entry(window, width=20, bg="white", fg="black")
entry_1.grid(row=1, column=0, sticky=W)

Button(window, text="Submit",width=5, command=buttonClick).grid(row=2, column=0, sticky=W)
output_text = Text(window, width=75, height=6, wrap=WORD, bg="white", fg="black")
output_text.grid(row=3, column=0, sticky=W)

window.mainloop()