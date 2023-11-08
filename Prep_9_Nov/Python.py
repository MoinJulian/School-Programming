sum = 0
count = 0

while count < 5:
    n = float(input("Please enter a number: "))  # Convert input to float immediately
    sum = sum + n
    count = count + 1

print(sum)  # Moved the print statement outside the loop
