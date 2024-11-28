from tkinter import *

def onClick():
    choice_1 = var_1.get()
    choice_2 = var_2.get()
    choice_3 = var_3.get()

    textbox.delete(0.0, END)

    textbox.insert(END, f"{choice_1}\n{choice_2}\n{choice_3}")

window = Tk()
window.title("Check Box")

# Checkboxes

var_1 = IntVar()
c_1 = Checkbutton(window, text="Check!", variable=var_1)
c_1.grid(row=1, column=0, sticky=W)

var_2 = IntVar()
c_2 = Checkbutton(window, text="Check this!", variable=var_2)
c_2.grid(row=2, column=0, sticky=W)

var_3 = IntVar()
c_3 = Checkbutton(window, text="Check this out!", variable=var_3)
c_3.grid(row=3, column=0, sticky=W)

# Textboxes

textbox = Text(window, width=20, height=10)
textbox.grid(row=4, column=0, sticky=W)

# Button

button = Button(window, text="Submit", command=lambda: onClick())
button.grid(row=5, column=0, sticky=W)

# Radio Buttons

# var = IntVar()
# r_1 = Radiobutton(window, text="Option 1", variable=var, value=1)
# r_1.grid(row=6, column=0, sticky=W)

# r_2 = Radiobutton(window, text="Option 2", variable=var, value=2)
# r_2.grid(row=7, column=0, sticky=W)

window.mainloop()