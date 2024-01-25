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


def get_original_key(selected_value, conversion_rates):
    for key, value in conversion_rates.items():
        if get_fullname(key) == selected_value:
            return key
