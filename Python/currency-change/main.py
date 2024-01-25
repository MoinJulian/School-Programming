import tkinter as tk
from tkinter import ttk
import webbrowser
from currency_utils import get_fullname, get_currency_name, get_original_key
from currency_conversion import perform_currency_conversion

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


def main():
    root = tk.Tk()
    root.title("Currency Converter")

    info_label = ttk.Label(root,
                           text="Please note that this program is not using an API and therefore can't have up-to-date information.")
    info_label.grid(row=0, column=0, columnspan=2, pady=10)

    choice_label = ttk.Label(root, text="Select conversion:")
    choice_label.grid(row=1, column=0, pady=5, sticky="e")

    choice_var = tk.StringVar()
    choice_combobox = ttk.Combobox(root, textvariable=choice_var,
                                   values=[get_fullname(key) for key in conversion_rates.keys()], state="readonly")
    choice_combobox.grid(row=1, column=1, pady=5)

    amount_label = ttk.Label(root, text="Enter amount:")
    amount_label.grid(row=2, column=0, pady=5, sticky="e")

    amount_entry = ttk.Entry(root)
    amount_entry.grid(row=2, column=1, pady=5)

    convert_button = ttk.Button(root, text="Convert",
                                command=lambda: perform_currency_conversion(choice_var, choice_combobox, amount_entry,
                                                                            result_label, result_link,
                                                                            conversion_rates))
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    result_label = ttk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    result_link = ttk.Label(root, text="")
    result_link.grid(row=5, column=0, columnspan=2, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
