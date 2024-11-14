from tkinter import *

flash_cards = {
    "the_cpu":  "The CPU is responsible for running proccesses",
    "memory": "The memory is used to store currently running programs",
    "io_devices": "I/O Devices are devices like keyboard, mouse, printer etc. used by the user to interact  with the software or do certain task",
    "motherboard": "The motherboard is the main circuit board that connects and allows communication between various components of the computer, such as the CPU, memory, and I/O devices.",
    "storage_devices": "Storage devices are used to store data permanently or temporarily. Examples include hard drives, SSDs, USB flash drives, and CDs."
}

def getAndDisplayText(key):
    output_text.delete(0.0, END)
    definition = flash_cards[key]
    output_text.insert(END, definition)

window = Tk()
window.title("Flash Crdas - Computing Hardware")

cpu_button = Button(window, width=20, command=lambda: getAndDisplayText("the_cpu"), bg="white", text="The CPU")
cpu_button.grid(row=0, column=0, sticky=W)

memory = Button(window,  width=20, command=lambda: getAndDisplayText("memory"), bg="white", text="Memory")
memory.grid(row=1, column=0, sticky=W)

io_devices_button = Button(window, width=20, command=lambda: getAndDisplayText("io_devices"), bg="white", text="I/O Devices")
io_devices_button.grid(row=2, column=0, sticky=W)

motherboard_button = Button(window, width=20, command=lambda: getAndDisplayText("motherboard"), bg="white", fg="black", text="Motherboard")
motherboard_button.grid(row=3, column=0, sticky=W)

storage_devices_button = Button(window, width=20, command=lambda: getAndDisplayText("storage_devices"), bg="white", fg="black", text="Storage Devices")
storage_devices_button.grid(row=4, column=0, sticky=W)


output_text = Text(window, width=20, bg="white", fg="black")
output_text.grid(row=5, column=0, sticky=W)

window.mainloop()