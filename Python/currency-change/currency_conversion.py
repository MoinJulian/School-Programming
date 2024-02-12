import webbrowser
from currency_utils import get_fullname, get_original_key


def calculate_conversion(amount, exchange_rate):
    """
    Calculate the converted amount based on the given exchange rate.

    Parameters:
        amount (float): The amount to be converted.
        exchange_rate (float): The exchange rate for the conversion.

    Returns:
        float: The converted amount.
    """
    return amount * exchange_rate


def perform_currency_conversion(choice_var, choice_combobox, amount_entry, result_label, result_link, conversion_rates):
    """
    Perform currency conversion based on user input and display the result.

    Parameters:
        choice_var (tk.StringVar): The variable holding the selected conversion choice.
        choice_combobox (ttk.Combobox): The combobox widget for selecting conversion.
        amount_entry (ttk.Entry): The entry widget for entering the amount.
        result_label (ttk.Label): The label widget to display the conversion result.
        result_link (ttk.Label): The label widget to display the link for more information.
        conversion_rates (dict): Dictionary containing conversion rates.
    """
    choice = choice_var.get()
    selected_value = choice_combobox.get()
    amount = amount_entry.get()

    # Reverse the get_fullname function to get the original key
    choice = get_original_key(selected_value, conversion_rates)

    if choice in conversion_rates:
        try:
            result_currency = choice[-3:]
            result_amount = calculate_conversion(float(amount), conversion_rates[choice])

            result_label.config(
                text=f"{amount} {get_fullname(choice)} is equal to {result_amount:.2f} {get_fullname(result_currency)}")

            # Open a browser to display the result on Google
            google_search_url = f"https://google.com/search?q={amount}+{choice.split('_')[0]}+{result_currency}"
            result_link.config(text="Click here to see the information on Google")
            result_link.bind("<Button-1>", lambda event: webbrowser.open(google_search_url))
        except ValueError:
            result_label.config(text="Invalid input. Please enter a valid numeric amount.")
    else:
        result_label.config(text="Invalid choice. Please select a valid conversion.")
