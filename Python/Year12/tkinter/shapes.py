from tkinter import *

window = Tk()
# window.title("Shapes")
window.title("Animations")
window.geometry("1200x600")

# Adding a canvas

canvas_1 = Canvas(window, width=1200, height=600, bg="light blue")
canvas_1.grid(row=0, column=0, sticky=W)

# # Add a circle

# circle = canvas_1.create_oval(0, 0, 300, 300, outline="light blue", fill="red")

# # Add a rectangle

# x = 10
# y = 10
# width = 100
# height = 100

# # [x, y, width, height]
# coord = [x, y, width, height]
# rect = canvas_1.create_rectangle(coord, outline="red", fill="blue")

x = 10
y = 10
a = 50
b = 50

# Two new variables indicating the size of the jump (velocity)

x_vel = 5
y_vel = 5

# Add a circle

circle = canvas_1.create_oval(x, y, a, b, outline="light blue", fill="red")


# Animate function - Animates of the screen

# def move():
#     canvas_1.move(circle, x_vel, y_vel)
#     coordinates = canvas_1.coords(circle)
#     x = coordinates[0]
#     y = coordinates[1]
#     window.after(33, move)

# Animate function - Bounces off the walls

def move():
    global x, y, x_vel, y_vel

    if x < 0:
        x_vel = 5
    elif x > 1200:
        x_vel = -5
    elif y < 0:
        y_vel = 5
    elif y > 600:
        y_vel = -5
    canvas_1.move(circle, x_vel, y_vel)
    coordinates = canvas_1.coords(circle)
    x = coordinates[0]
    y = coordinates[1]
    window.after(33, move)


move()

window.mainloop()