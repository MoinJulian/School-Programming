### Add a demostration of all core tkinter widgets

from tkinter import *

root = Tk()
root.title("I am a Top Level Widget, parent for other widtgets")

# my_label = Label(root, text="I am a label widget")
# my_label.pack()

# my_button = Button(root, text="I am a button")
# my_button.pack()

# Create a frame widget for placing menu
my_menu_bar = Frame(root, relief="raised", bd=2)
my_menu_bar.pack(fill = X)

# Create Menu Widget 1 and Sub Menu 1
my_menu_button = Menubutton(my_menu_bar, text = "Menu Button Widget 1")
my_menu_button.pack(side = LEFT)

# Menu Widget
my_menu = Menu(my_menu_button, tearoff=0)
my_menu_button["menu"] = my_menu
my_menu.add("command", label = "Sub Menu") # Add Sub Menu

# Create Menu2 and Submenu 2
menu_button_2 = Menubutton(my_menu_bar, text = "Menu 2")
menu_button_2.pack(side = LEFT)

my_menu_2 = Menu(menu_button_2, tearoff=0)
menu_button_2["menu"] = my_menu_2
my_menu_2.add("command", label = "Sub Menu 2") # Add Sub Menu 2

root.mainloop()