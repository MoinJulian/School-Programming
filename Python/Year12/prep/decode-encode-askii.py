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


# Test the functions
input_string = input("Enter a string to convert to ASCII: ")
ascii_result = convertStringToAscii(input_string)

ascii_input = input("Enter ASCII to convert to string: ")
string_result = convertAsciiToString(ascii_input)

print("Converted to ASCII:", ascii_result)
print("Converted back to String:", string_result)
