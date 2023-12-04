#for i in range(1, 11):
#    print(i)

#array = ["a", "b", "c"]
#print(array)
#print(len(array))

def addEvens(num1, num2):
    total = 0
    if num1 % 2 == 0:
        total += num1
    if num2 % 2 == 0:
        total += num2
    print(total)

num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter a number:"))
addEvens(num1, num2)

def addOdds(num1, num2):
    total = 0
    if num1 % 2 != 0:
        total += num1
    if num2 % 2 != 0:
        total += num2
    print(total)

num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter a number:"))
addOdds(num1, num2)
