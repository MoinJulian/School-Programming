from tkinter import *

flash_cards = {
    "the_cpu": "The CPU (Central Processing Unit) is the brain of the computer. It processes instructions, performs calculations, and manages the flow of data between components, enabling the execution of programs and tasks.",
    "memory": "Memory, or RAM (Random Access Memory), temporarily stores data and instructions that the CPU uses while performing tasks. It ensures quick access to active programs and processes, improving the computer's speed and responsiveness.",
    "io_devices": "I/O (Input/Output) devices are peripherals that allow a user to interact with a computer. Input devices like keyboards and mice send data to the computer, while output devices like monitors and printers display or execute results.",
    "motherboard": "The motherboard is the central hub of a computer. It connects all components, including the CPU, memory, storage, and I/O devices, facilitating communication and power distribution among them.",
    "storage_devices": "Storage devices retain data even when the computer is powered off. Examples include hard drives, SSDs, and flash drives. They store the operating system, applications, and user files for long-term access."
}

def format_button_label(key):
    """Format button labels to ensure specific words are all caps."""
    words = key.replace("_", " ").split()
    return " ".join(word.upper() if word in {"cpu", "io"} else word.title() for word in words)

def get_and_display_text(key):
    output_text.delete(1.0, END)
    definition = flash_cards.get(key, "Definition not found.")
    output_text.insert(END, definition)

window = Tk()
window.title("Flash Cards - Computing Hardware")

# Title Label
title_label = Label(window, text="Flash Cards - Computing Hardware", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Buttons Frame
buttons_frame = Frame(window)
buttons_frame.grid(row=1, column=0, sticky=W, padx=10)

# Generate Buttons Dynamically
for idx, (key, text) in enumerate(flash_cards.items()):
    Button(
        buttons_frame, width=20, text=format_button_label(key),  # Use the formatted label
        command=lambda k=key: get_and_display_text(k),
        bg="white"
    ).grid(row=idx, column=0, sticky=W, pady=2)

# Output Area with Scrollbar
output_frame = Frame(window)
output_frame.grid(row=1, column=1, padx=10, pady=10, sticky=NSEW)

scrollbar = Scrollbar(output_frame)
output_text = Text(
    output_frame, width=60, height=15, wrap=WORD,  # Adjusted width and height for longer text
    yscrollcommand=scrollbar.set, bg="white", fg="black", font=("Arial", 12)
)
scrollbar.config(command=output_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
output_text.pack(side=LEFT, fill=BOTH, expand=True)

# Quit Button
quit_button = Button(
    window, text="Quit", command=window.quit, bg="red", fg="black", activebackground="red2", 
    width=20, font=("Arial", 12)
)
quit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Configure row and column weights for resizing
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()
