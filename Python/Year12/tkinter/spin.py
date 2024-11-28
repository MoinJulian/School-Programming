from tkinter import *

def getNum():
    value = spin.get()

    if int(value) > limit:
        textbox.delete(0.0, END)
        textbox.insert(END, f"You can only enter a number between {start} to {limit}")
    else:
        textbox.delete(0.0, END)
        textbox.insert(END, value)


window = Tk()

# Setup
window.title("Spinbox")
window.geometry("290x170")

start = 1
limit = 10

v = IntVar() # Captures entered value
spin = Spinbox(window, textvariable=v, from_=start, to=limit)
spin.grid(row=0, column=0, sticky=W)

# Textbox
textbox = Text(window, width=35, height=5, wrap=WORD, bg="white", fg="black")
textbox.grid(row=1, column=0, sticky=W)

# button = SUBMIT
Button(window, text="Submit",width=5, command=getNum).grid(row=2, column=0, sticky=W)

window.mainloop()

