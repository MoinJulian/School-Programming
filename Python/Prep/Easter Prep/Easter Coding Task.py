## Challenge 2

def challenge_2():    
    print("Enter two numbers to calculate the mean.")
    num1 = int(input("Please Input your first number: "))
    num2 = int(input("Please enter your second number: "))

    numt = num1 + num2
    numf = numt / 2

    print("The mean of your numbers is: ")
    print(numf)

## Challange 8

def challenge_8():
    print("Enter points to see the mark the student gets.")
    points = int(input("Please enter the points: "))
    if points >= 75:
        print("The mark is a A")
    elif points >= 60:
        print("The mark is a B")
    elif points >= 35:
        print("The mark is a C")
    elif points < 35:
        print("The mark is a D")

## Challenge 11

def challenge_11():
    sentence = str(input("Please enter a sentence: "))
    print(len(sentence))

## Challenge 12

def challenge_12():
    sentence = str(input("Please enter a sentence: "))
    print(sentence.upper())
    

challenge_2()
challenge_8()
challenge_11()
challenge_12()