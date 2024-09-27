from tkinter import *

window = Tk()
window.title = "My first GUI"

# Create a label with input field

Label(window, text="Enter your text").grid(row=0, column=0)
entry1 = Entry(window, width=20, bg="light blue")
entry1.grid(row=1, column=0, sticky=W)

# Create a button

Button(window, text="Submit", width=5, command=0).grid(row=2, column=0, sticky=W)

# Button Click

def buttonClick():
    entered_text = entry1.get()
    output_text.delete(0.0, END) # Clears content of the text box
    manipulate_text = "You have just typed:" + entered_text # Joins the text
    output_text.insert(END, manipulate_text) # Inserts the text into the text box

# Text Box Widget

output_text = Text(window, width=75, height=6, wrap=WORD, background="light blue")
output_text.grid(row=3, column=0, columnspan=2, sticky=W)

# Button Action



window.mainloop()