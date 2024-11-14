from tkinter import *

def get_value():
    value = entry.get()
    output_box.delete(0.0,END)
    output = "You have entered: " + value
    output_box.insert(END, output)

window = Tk()
window.title("First GUI")

entry = Entry(window, bg="white", width=20, fg="black")
entry.grid(column=0, row=0)

button = Button(window, command=get_value,width=20, text="Output")
button.grid(column=0, row=1)

output_box = Text(window, bg="white", width=20,  fg="black")
output_box.grid(column=0, row=3)

window.mainloop()