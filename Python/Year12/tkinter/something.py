from tkinter import *
x = 10
y = 10
a = 50
b = 50

window = Tk()
window.title("Key Controls")
window.geometry("1200x600")

canvas_1 = Canvas(window, width=1200, height=600, bg="light blue")
canvas_1.grid(row=0, column=0, sticky=W)

key_down = False

x_vel = 5
y_vel = 5

def move():
    global x, y, x_vel, y_vel, key_down

    if key_down == True:
        canvas_1.move(circle, x_vel, y_vel)
    window.after(33, move)

def onKeyPress(event):
    global key_down, x_vel, y_vel
    
    if event.keysym == "Left":
        key_down = True
        x_vel = -5
        y_vel = 0
    elif event.keysym == "Right":
        key_down = True
        x_vel = 5
        y_vel = 0
    elif event.keysym == "Up":
        key_down = True
        x_vel = 0
        y_vel = -5
    elif event.keysym == "Down":
        key_down = True
        x_vel = 0
        y_vel = 5

def onKeyRelease(event):
    global key_down
    key_down = False

move()

circle = canvas_1.create_oval(x, y, a, b, outline="light blue", fill="red")

window.bind("<KeyPress>", onKeyPress)
window.bind("<KeyRelease>", onKeyRelease)

window.mainloop()