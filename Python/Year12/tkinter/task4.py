from tkinter import *
from tkinter import messagebox

flash_cards = {
    "the_cpu": "The CPU (Central Processing Unit) is the brain of the computer. It processes instructions, performs calculations, and manages the flow of data between components, enabling the execution of programs and tasks.",
    "memory": "Memory, or RAM (Random Access Memory), temporarily stores data and instructions that the CPU uses while performing tasks. It ensures quick access to active programs and processes, improving the computer's speed and responsiveness.",
    "io_devices": "I/O (Input/Output) devices are peripherals that allow a user to interact with a computer. Input devices like keyboards and mice send data to the computer, while output devices like monitors and printers display or execute results.",
    "motherboard": "The motherboard is the central hub of a computer. It connects all components, including the CPU, memory, storage, and I/O devices, facilitating communication and power distribution among them.",
    "storage_devices": "Storage devices retain data even when the computer is powered off. Examples include hard drives, SSDs, and flash drives. They store the operating system, applications, and user files for long-term access."
}

# Format flashcards into a list for index-based access
flash_card_keys = list(flash_cards.keys())

def formatButtonLabel(key):
    """Format button labels to ensure specific words are all caps."""
    words = key.replace("_", " ").split()
    return " ".join(word.upper() if word in {"cpu", "io"} else word.title() for word in words)

def getAndDisplayText(key):
    """Gets the definition text and displays it in the output textfield."""
    output_text.delete(1.0, END)
    definition = flash_cards.get(key, "Definition not found.")
    output_text.insert(END, definition)

def displayFlashcardByIndex():
    """Displays the flashcard based on the selected Spinbox value."""
    selected_index = v.get() - 1  # Convert to 0-based index
    if 0 <= selected_index < len(flash_card_keys):
        getAndDisplayText(flash_card_keys[selected_index])
    else:
        output_text.delete(1.0, END)
        output_text.insert(END, "No flashcard available for this index.")

def openGithubIssue():
    """Opens a link to the GitHub issues page for reporting an issue."""
    import webbrowser
    webbrowser.open("https://github.com/MoinJulian/School-Programming/issues/new")

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
        buttons_frame, width=20, text=formatButtonLabel(key),  # Use the formatted label
        command=lambda k=key: getAndDisplayText(k),
        bg="white"
    ).grid(row=idx, column=0, sticky=W, pady=2)

# Spinbox for selecting flashcard by index
spinbox_frame = Frame(window)
spinbox_frame.grid(row=2, column=0, padx=10, pady=10, sticky=W)

v = IntVar(value=1)  # Default to first flashcard
spinbox_label = Label(spinbox_frame, text="Select Flashcard by Index:")
spinbox_label.pack(side=LEFT)

spin = Spinbox(spinbox_frame, textvariable=v, from_=1, to=len(flash_card_keys), width=5)
spin.pack(side=LEFT, padx=5)

spinbox_button = Button(spinbox_frame, text="Show Flashcard", command=displayFlashcardByIndex)
spinbox_button.pack(side=LEFT, padx=5)

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
quit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Configure row and column weights for resizing
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

# Menu
menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Quit", command=window.destroy)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Flash Cards App v1.0"))
help_menu.add_command(label="Report Issue", command=lambda: openGithubIssue())
menubar.add_cascade(label="Help", menu=help_menu)

window.mainloop()
