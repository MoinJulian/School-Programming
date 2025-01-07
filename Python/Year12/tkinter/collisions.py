from tkinter import *

x = 10
y = 10
a = 50
b = 50

window = Tk()
window.geometry("1200x600")

canvas1 = Canvas(window, height=600, width=1200, bg="white")
canvas1.grid(row=0, column=0, sticky=W)

coord = (x, y, a, b)
rect = canvas1.create_rectangle(*coord, outline="red", fill="red")
rect2 = canvas1.create_rectangle(100, 100, 140, 140, outline="green", fill="green")

key_down = False
x_vel = 5
y_vel = 5
game_state = True
instruction_window_open = False

def move():
    global x, y, x_vel, y_vel, key_down, instruction_window_open

    if key_down:
        canvas1.move(rect, x_vel, y_vel)
        coordinates = canvas1.coords(rect)
        coordinates_2 = canvas1.coords(rect2)

        if coordinates[2] >= coordinates_2[0] and coordinates[0] <= coordinates_2[2]:
            if coordinates[3] >= coordinates_2[1] and coordinates[1] <= coordinates_2[3]:
                if not instruction_window_open:
                    instruction()
                    print("COLLISION")

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

def instruction():
    global game_state, instruct_window, instruction_window_open
    game_state = False
    instruction_window_open = True
    instruct_window = Toplevel(window, background="light blue")
    instruct_window.title("Instructions")

    info = Label(instruct_window, text="Check this!", bg="light blue")
    info.grid(row=0, column=0, sticky=W)

    instruct_window.geometry("1200x600")
    instruct_window.protocol("WM_DELETE_WINDOW", instruct_window_destroy)
    

def instruct_window_destroy():
    global game_state, instruct_window, instruction_window_open

    instruct_window.destroy()
    game_state = True
    instruction_window_open = False

    move()

window.bind("<KeyPress>", onKeyPress)
window.bind("<KeyRelease>", onKeyRelease)

move()

window.mainloop()