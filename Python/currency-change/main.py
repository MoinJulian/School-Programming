def print_info():
    print("Please not that this program is not using an API and therefore can't have the up to date information")


def print_menu():
    print("1. Convert from Dollar to Euro")
    print("2. Convert from Euro to Dollar")
    print("3. Convert Dollar to Pound Sterling")
    print("4. Convert Pound Sterling to Dollar")
    print("5. Convert Dollar to Yen")
    print("6. Convert Yen to Dollar")
    print("7. Convert Dollar to Swedish Krona")
    print("8. Convert Swedish Krona to Dollar")
    print("9. Convert Dollar to Canadian Dollar")
    print("10. Convert Canadian Dollar to Dollar")
    print("11. Convert Dollar to Australian Dollar")
    print("12. Convert Australian Dollar to Dollar")
    print("13. Convert Dollar to Swiss Franc")
    print("14. Convert Swiss Franc to Dollar")
    print("15. Convert Dollar to New Zealand Dollar")
    print("16. Convert New Zealand Dollar to Dollar")


def convert_currency(amount, exchange_rate):
    result = amount * exchange_rate
    return result


def main():
    conversion_rates = {
        # USD To Euro
        "USD_TO_EUR": 0.92,
        "EUR_TO_USD": 1.09,
        # USD to Pound
        "USD_TO_GBP": 0.79,
        "GBP_TO_USD": 1.27,
        # USD to Yen
        "USD_TO_YEN": 147.28,
        "YEN_TO_USD": 0.0068,
        # USD to SEK
        "USD_TO_SEK": 10.44,
        "SEK_TO_USD": 0.096,
        # USD to CAD
        "USD_TO_CAD": 1.35,
        "CAD_TO_USD": 0.74,
        # USD to AUD
        "USD_TO_AUD": 1.51,
        "AUD_TO_USD": 0.66,
        # USD to CHF
        "USD_TO_CHF": 0.87,
        "CHF_TO_USD": 1.16,
        # USD to NZD
        "USD_TO_NZD": 1.63,
        "NZD_TO_USD": 0.61
    }

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
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
    else:
        print("Invalid choice. Please enter a number between 1 and 16.")


if __name__ == "__main__":
    main()
