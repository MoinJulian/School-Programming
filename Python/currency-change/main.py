import tkinter as tk
from tkinter import ttk
import webbrowser

conversion_rates = {
    "USD_TO_EUR": 0.92,
    "EUR_TO_USD": 1.09,
    "USD_TO_GBP": 0.79,
    "GBP_TO_USD": 1.27,
    "USD_TO_YEN": 147.28,
    "YEN_TO_USD": 0.0068,
    "USD_TO_SEK": 10.44,
    "SEK_TO_USD": 0.096,
    "USD_TO_CAD": 1.35,
    "CAD_TO_USD": 0.74,
    "USD_TO_AUD": 1.51,
    "AUD_TO_USD": 0.66,
    "USD_TO_CHF": 0.87,
    "CHF_TO_USD": 1.16,
    "USD_TO_NZD": 1.63,
    "NZD_TO_USD": 0.61
}

def perform_currency_conversion():
    selected_value = choice_combobox.get()
    amount = amount_entry.get()

    # Reverse the get_fullname function to get the original key
    choice = get_original_key(selected_value)

    if choice in conversion_rates:
        try:
            result_currency = choice[-3:]
            result_amount = calculate_conversion(float(amount), conversion_rates[choice])

            result_label.config(text=f"{amount} {get_fullname(choice)} is equal to {result_amount:.2f} {get_fullname(result_currency)}")

            # Open a browser to display the result on Google
            google_search_url = f"https://google.com/search?q={amount}+{choice.split('_')[0]}+{result_currency}"
            result_link.config(text="Click here to see the information on Google")
            result_link.bind("<Button-1>", lambda event: webbrowser.open(google_search_url))
        except ValueError:
            result_label.config(text="Invalid input. Please enter a valid numeric amount.")
    else:
        result_label.config(text="Invalid choice. Please select a valid conversion.")

def calculate_conversion(amount, exchange_rate):
    return amount * exchange_rate

def get_fullname(conversion_key):
    parts = conversion_key.split('_')
    if len(parts) == 3:
        from_currency, to_currency = parts[0], parts[2]
        return f"{get_currency_name(from_currency)} to {get_currency_name(to_currency)}"
    else:
        return conversion_key

def get_currency_name(currency_code):
    currency_names = {
        "USD": "US Dollar",
        "EUR": "Euro",
        "GBP": "British Pound",
        "YEN": "Japanese Yen",
        "SEK": "Swedish Krona",
        "CAD": "Canadian Dollar",
        "AUD": "Australian Dollar",
        "CHF": "Swiss Franc",
        "NZD": "New Zealand Dollar"
    }
    return currency_names.get(currency_code, currency_code)

def get_original_key(selected_value):
    # Reverse the get_fullname function to get the original key
    for key, value in conversion_rates.items():
        if get_fullname(key) == selected_value:
            return key

# Create main window
root = tk.Tk()
root.title("Currency Converter")

# Create widgets
info_label = ttk.Label(root, text="Please note that this program is not using an API and therefore can't have up-to-date information.")
info_label.grid(row=0, column=0, columnspan=2, pady=10)

choice_label = ttk.Label(root, text="Select conversion:")
choice_label.grid(row=1, column=0, pady=5, sticky="e")

choice_var = tk.StringVar()
# Display conversion options with currency names spelled out
choice_combobox = ttk.Combobox(root, textvariable=choice_var, values=[get_fullname(key) for key in conversion_rates.keys()], state="readonly")
choice_combobox.grid(row=1, column=1, pady=5)

amount_label = ttk.Label(root, text="Enter amount:")
amount_label.grid(row=2, column=0, pady=5, sticky="e")

amount_entry = ttk.Entry(root)
amount_entry.grid(row=2, column=1, pady=5)

convert_button = ttk.Button(root, text="Convert", command=perform_currency_conversion)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

result_link = ttk.Label(root, text="")
result_link.grid(row=5, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
