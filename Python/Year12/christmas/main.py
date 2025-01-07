import tkinter as tk
from tkinter import messagebox
import json

# Load user data from file
def loadUserData(filename="Python/Year12/christmas/user_data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user data to file
def saveUserData(filename="Python/Year12/christmas/user_data.json"):
    with open(filename, "w") as file:
        json.dump(user_data, file, indent=4)

# Sample user data
user_data = loadUserData()

# Global variable to store logged-in user
current_user = None

# Function to authenticate user
def authenticateUser(card_number, pin):
    global current_user
    if card_number in user_data and user_data[card_number]["pin"] == pin:
        current_user = card_number
        return True
    return False

# Function to display balance
def displayBalance():
    global current_user
    balance = user_data[current_user]["balance"]
    messagebox.showinfo("Balance Enquiry", f"Your current balance is: {balance:.2f}€")

# Function to transfer money
def transferMoney():
    global current_user
    balance = user_data[current_user]["balance"]
    messagebox.showinfo("Transfer Money", f"Your current balance is: {balance:.2f}€")

    transfer_screen = tk.Tk()
    transfer_screen.title("Transfer Money")
    transfer_screen.geometry("400x250")

    tk.Label(transfer_screen, text="Enter the recipient's card number:").pack()
    entry_recipient = tk.Entry(transfer_screen)
    entry_recipient.pack()

    tk.Label(transfer_screen, text="Enter the amount to transfer:").pack()
    entry_amount = tk.Entry(transfer_screen)
    entry_amount.pack()

    def handleTransfer():
        recipient = entry_recipient.get()
        amount = float(entry_amount.get())

        if recipient in user_data:
            user_data[current_user]["balance"] -= amount
            user_data[recipient]["balance"] += amount
            saveUserData()  # Save data after transfer
            messagebox.showinfo("Transfer Successful", f"Transfer of {amount:.2f}€ to {recipient} successful!")
            transfer_screen.destroy()
        else:
            messagebox.showerror("Transfer Failed", "Recipient card number does not exist.")

    tk.Button(transfer_screen, text="Transfer", command=handleTransfer).pack(pady=20)

    transfer_screen.mainloop()

# Function to withdraw money
def withdrawMoney():
    global current_user
    balance = user_data[current_user]["balance"]
    messagebox.showinfo("Withdraw Money", f"Your current balance is: {balance:.2f}€")

    withdraw_screen = tk.Tk()
    withdraw_screen.title("Withdraw Money")
    withdraw_screen.geometry("400x250")

    tk.Label(withdraw_screen, text="Enter the amount to withdraw:").pack()
    entry_amount = tk.Entry(withdraw_screen)
    entry_amount.pack()

    def handleWithdraw():
        amount = float(entry_amount.get())

        if amount <= user_data[current_user]["balance"]:
            user_data[current_user]["balance"] -= amount
            saveUserData()  # Save data after withdrawal
            messagebox.showinfo("Withdrawal Successful", f"Withdrawal of {amount:.2f}€ successful!")
            withdraw_screen.destroy()
        else:
            messagebox.showerror("Withdrawal Failed", "Insufficient funds.")

    tk.Button(withdraw_screen, text="Withdraw", command=handleWithdraw).pack(pady=20)

    withdraw_screen.mainloop()

# Function to deposit money
def depositMoney():
    global current_user
    balance = user_data[current_user]["balance"]
    messagebox.showinfo("Deposit Money", f"Your current balance is: {balance:.2f}€")

    deposit_screen = tk.Tk()
    deposit_screen.title("Deposit Money")
    deposit_screen.geometry("400x250")

    tk.Label(deposit_screen, text="Enter the amount to deposit:").pack()
    entry_amount = tk.Entry(deposit_screen)
    entry_amount.pack()

    def handleDeposit():
        amount = float(entry_amount.get())

        user_data[current_user]["balance"] += amount
        saveUserData()  # Save data after deposit
        messagebox.showinfo("Deposit Successful", f"Deposit of {amount:.2f}€ successful!")
        deposit_screen.destroy()

    tk.Button(deposit_screen, text="Deposit", command=handleDeposit).pack(pady=20)

    deposit_screen.mainloop()

# Function to pay bills
def payBills():
    global current_user
    balance = user_data[current_user]["balance"]
    messagebox.showinfo("Pay Bills", f"Your current balance is: {balance:.2f}€")

    bills_screen = tk.Tk()
    bills_screen.title("Pay Bills")
    bills_screen.geometry("400x250")

    tk.Label(bills_screen, text="Enter the amount to pay:").pack()
    entry_amount = tk.Entry(bills_screen)
    entry_amount.pack()

    def handlePay():
        amount = float(entry_amount.get())

        if amount <= user_data[current_user]["balance"]:
            user_data[current_user]["balance"] -= amount
            saveUserData()  # Save data after payment
            messagebox.showinfo("Payment Successful", f"Payment of {amount:.2f}€ successful!")
            bills_screen.destroy()
        else:
            messagebox.showerror("Payment Failed", "Insufficient funds.")

    tk.Button(bills_screen, text="Pay", command=handlePay).pack(pady=20)

    bills_screen.mainloop()

# Function to change PIN
def changePIN():
    global current_user
    balance = user_data[current_user]["balance"]
    messagebox.showinfo("Change PIN", f"Your current balance is: {balance:.2f}€")

    pin_screen = tk.Tk()
    pin_screen.title("Change PIN")
    pin_screen.geometry("400x250")

    tk.Label(pin_screen, text="Enter your current PIN:").pack()
    entry_current_pin = tk.Entry(pin_screen, show="*")
    entry_current_pin.pack()

    tk.Label(pin_screen, text="Enter your new PIN:").pack()
    entry_new_pin = tk.Entry(pin_screen, show="*")
    entry_new_pin.pack()

    def handleChangePIN():
        current_pin = entry_current_pin.get()
        new_pin = entry_new_pin.get()

        if current_pin == user_data[current_user]["pin"]:
            user_data[current_user]["pin"] = new_pin
            saveUserData()  # Save data after PIN change
            messagebox.showinfo("PIN Change Successful", "Your PIN has been changed successfully!")
            pin_screen.destroy()
        else:
            messagebox.showerror("PIN Change Failed", "Invalid current PIN.")

    tk.Button(pin_screen, text="Change PIN", command=handleChangePIN).pack(pady=20)

    pin_screen.mainloop()

# Function to terminate account
def terminateAccount():
    global current_user
    balance = user_data[current_user]["balance"]
    messagebox.showinfo("Terminate Account", f"Your current balance is: {balance:.2f}€")

    terminate_screen = tk.Tk()
    terminate_screen.title("Terminate Account")
    terminate_screen.geometry("400x250")

    tk.Label(terminate_screen, text="Enter your PIN to confirm:").pack()
    entry_pin = tk.Entry(terminate_screen, show="*")
    entry_pin.pack()

    def handleTerminate():
        pin = entry_pin.get()

        if pin == user_data[current_user]["pin"]:
            del user_data[current_user]
            saveUserData()  # Save data after account termination
            messagebox.showinfo("Account Terminated", "Your account has been terminated successfully!")
            terminate_screen.destroy()
            main_menu_screen.destroy()  # Close the main menu screen
        else:
            messagebox.showerror("Termination Failed", "Invalid PIN.")

    tk.Button(terminate_screen, text="Terminate", command=handleTerminate).pack(pady=20)

    terminate_screen.mainloop()

# Function to handle login
def handleLogin():
    card_number = entry_card_number.get()
    pin = entry_pin.get()

    if authenticateUser(card_number, pin):
        messagebox.showinfo("Login Successful", "Welcome to Worksop College Bank!")
        login_screen.destroy()
        mainMenu()
    else:
        messagebox.showerror("Login Failed", "Invalid card number or PIN.")

# Function to create the main menu
def mainMenu():
    global main_menu_screen
    main_menu_screen = tk.Tk()
    main_menu_screen.title("ATM Main Menu")
    main_menu_screen.geometry("400x300")

    tk.Label(main_menu_screen, text="Welcome to Worksop College Bank", font=("Arial", 16)).pack(pady=20)

    button_frame = tk.Frame(main_menu_screen)
    button_frame.pack(pady=10)

    buttons = [
        ("Balance Enquiry", displayBalance),
        ("Transfer Money", transferMoney),
        ("Deposit Money", depositMoney),
        ("Pay Bills", payBills),
        ("Change PIN", changePIN),
        ("Withdraw Money", withdrawMoney),
        ("Terminate Account", terminateAccount),
        ("Exit", main_menu_screen.destroy)
    ]

    for i, (text, command) in enumerate(buttons):
        row = i // 2
        col = i % 2
        tk.Button(button_frame, text=text, width=20, command=command).grid(row=row, column=col, padx=5, pady=5)

    main_menu_screen.mainloop()

# Create login screen
login_screen = tk.Tk()
login_screen.title("ATM Login")
login_screen.geometry("400x300")

tk.Label(login_screen, text="Enter Your Card Details", font=("Arial", 16)).pack(pady=10)

tk.Label(login_screen, text="Card Number:").pack()
entry_card_number = tk.Entry(login_screen)
entry_card_number.pack()

tk.Label(login_screen, text="PIN:").pack()
entry_pin = tk.Entry(login_screen, show="*")
entry_pin.pack()

tk.Button(login_screen, text="Login", command=handleLogin).pack(pady=20)

login_screen.mainloop()