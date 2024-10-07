def convertStringToAscii(input_string: str) -> str:
    output = ""
    for char in input_string:
        output += str(ord(char)) + " "
    return output.strip()  # Strip trailing space


def convertAsciiToString(input_ascii: str) -> str:
    output = ""
    ascii_array = input_ascii.split(" ")
    for element in ascii_array:
        output += chr(int(element))
    return output

def main():
    while True:
        choice = int(input("1. Convert String To ASCII | 2. Convert ASCII to String | 3. Exit"))

        if choice == 1:
            input_string = input("Enter a string you want to convert to ASCII: ")
            ascii_result = convertStringToAscii(input_string)
            print("Converted to ASCII: ", ascii_result)
        if choice == 2:
            input_ascii = input("Enter ASCII you want to convert to a string: ")
            string_result = convertAsciiToString(input_ascii)
            print("Converted to string", string_result)
        if choice == 3:
            break
        else:
            print("Please enter a value between 1 and 3.")


if __name__ == '__main__':
    main()