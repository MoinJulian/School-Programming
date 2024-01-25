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


def print_info():
    print("Please note that this program is not using an API and therefore can't have up-to-date information.")


def print_menu():
    for i, key in enumerate(conversion_rates, start=1):
        target_currency = key.split('_')[-1]
        print(f"{i}. Convert from Dollar to {target_currency}")


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


def main():
    print_info()
    print_menu()
    choice = input("Enter your choice (1-16): ")

    if choice.isdigit() and 1 <= int(choice) <= 16:
        try:
            choice_key = list(conversion_rates.keys())[int(choice) - 1]
            amount = float(input(f"Enter the amount to convert from {choice_key.split('_')[0]}: "))
            result_currency = choice_key[-3:]
            result_amount = convert_currency(amount, conversion_rates[choice_key])
            print(f"{amount} {choice_key.split('_')[0]} is equal to {result_amount:.2f} {result_currency}")

            # Open a browser to display the result on Google
            print("You can click on the link below to see the information on Google:")
            webbrowser.open(f"https://google.com/search?q={amount}+{choice_key.split('_')[0]}+{result_currency}")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
    else:
        print("Invalid choice. Please enter a number between 1 and 16.")


if __name__ == "__main__":
    main()
