def encode_letter():
    letter = input("Enter a letter to encode: ").lower()
    if letter.isalpha() and len(letter) == 1:
        code = ord(letter) - ord('a') + 1
        print(f"The encoded value for '{letter}' is: {code}")
    else:
        print("Invalid input. Please enter a single letter.")


def decode_letter():
    try:
        number = int(input("Enter a number to decode (1-26): "))
        if 1 <= number <= 26:
            letter = chr(number + ord('a') - 1)
            print(f"The decoded letter for '{number}' is: {letter}")
        else:
            print("Invalid input. Please enter a number between 1 and 26.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def main():
    while True:
        print("\nMenu:")
        print("1. Encode a letter")
        print("2. Decode a letter")
        print("9. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                encode_letter()
            elif choice == 2:
                decode_letter()
            elif choice == 9:
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please select a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()