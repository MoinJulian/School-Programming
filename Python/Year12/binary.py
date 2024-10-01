def text_to_binary(text):
    """Converts a string to its binary representation."""
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    """Converts binary back to a string."""
    binary_values = binary.split()
    return ''.join(chr(int(b, 2)) for b in binary_values)

def int_to_binary(number):
    """Converts an integer to binary."""
    return format(number, 'b')

def binary_to_int(binary):
    """Converts binary back to an integer."""
    return int(binary, 2)

# Main program
def main():
    while True:
        choice = input("Choose operation: 1. Text to Binary, 2. Binary to Text, 3. Int to Binary, 4. Binary to Int, 5. Exit: ")
        if choice == '1':
            text = input("Enter text: ")
            print(f"Binary representation: {text_to_binary(text)}")
        elif choice == '2':
            binary = input("Enter binary string: ")
            print(f"Text: {binary_to_text(binary)}")
        elif choice == '3':
            number = int(input("Enter an integer: "))
            print(f"Binary representation: {int_to_binary(number)}")
        elif choice == '4':
            binary = input("Enter binary string: ")
            print(f"Integer: {binary_to_int(binary)}")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

