from tkinter import *

def function1():
    output_text.delete(0.0, END)
    output_text.insert(END, "You have choosen Option 1")

def function2():
    output_text.delete(0.0, END)
    output_text.insert(END, "You have choosen Option 2")

window = Tk()

# Setup
window.title("Menus")
window.geometry("290x170")

# Create top level menu
menubar = Menu(window)
window.config(menu=menubar)

first_menu = Menu(menubar, tearoff=0)
first_menu.add_command(label="Option 1", command=function1)
first_menu.add_command(label="Quit", command=window.destroy)
menubar.add_cascade(label="Menu 1", menu=first_menu)

second_menu = Menu(menubar, tearoff=0)
second_menu.add_command(label="Option 2", command=function2)
second_menu.add_command(label="Quit", command=window.destroy)
menubar.add_cascade(label="Menu 2", menu=second_menu)

# Text Field
output_text = Text(window, width=35, height=10, wrap=WORD, bg="white", fg="black")
output_text.grid(row=0, column=0, sticky=W)

window.mainloop()

