'''
Name: Julian Hammer
Date: Mon 3rd Oct
Subject: Computer Science
Class: 10z
Topic: Python Programming
'''

#This is a comment line
###This represent the start and the end of a block of code###

###Printing and storing values###



###input###

#name = input("What is your name?")
#print("Hello" + name)
#age = input("How old are you?")
#print(age + "is a good age to be" + name)
#food = input("What is your favourite Food?")
#print("I also like to eat " + food + ", but I can't")
#school = input("In what school do you go?")
#sport = input("What sports do you do?")

#print("What I know about you: /n")
#print("Your name is " + name)
#print("You are " + age)
#print("You go to" + school)
#print(" ")
#print("How have I done so far?")
###End of storing and Printing

###Ignoring Apostrophise###

#print('Hello That\'s is funny')


###Selection###
#IF, ELIF, ELSE
# == equal
#> greater than
#< less than
#!= Not equal
#=> equal or greater than
#=< equal or less than


# age = int(input('How old are you? '))

# if age >= 16:
#     print('You are able to apply for a provisional drivers license')
# else: 
#     print('You are not old enough. Sorry')


#Selection: if, else, elif

# age = input("How old are you?")
# text = "Happy Birthday"

# if age == 16: 
#     print("This is a special birthday, now you can use apple pay.")
#     print(text)
# elif age == 17: 
#     print("You are now eligible to take driving lessons.")
#     print(text)
# elif age == 18:
#     print("You are an adult now")
#     print(text)
# else:
#     print("You don't have an special birthday.")
#     print("Have still a " + text)

###Selection: if, else, elif - Boolean

# age = int(input("How old are you? "))

# if age >= 0 and age <= 16:
#     print("You are to young for driving lessons.")
# else: 
#     print("You are now ready to take driving lessons")


##Program 1 ##

# TimePlayed = int(input("How many hours have you played video games this week? In hours!"))
# Answer1 = "You haven't played video games this week."
# Answer2 = "Thats a fair amount of time."
# Answer3 = "Thats a lot."
# Answer4 = "You have a problem."
# Answer5 = "You have played to much this week stop."

# if TimePlayed < 1:
#     print(Answer1)
# elif TimePlayed >= 1 and TimePlayed <= 4:
#     print(Answer2)
# elif TimePlayed > 4 and TimePlayed <= 15:
#     print(Answer3)
# elif TimePlayed > 15 and TimePlayed <= 24:
#     print(Answer4)
# else:
#     print(Answer5)

### WHILE Loops ###

# cor_num = "1234"
# num = int(input("Enter password: "))
# while num != cor_num:
#     print("Password incorrect")
#     num = int(input("Enter your password again: "))
# print("Password correct!")
# print("You can enter")

# import random

# password = 1234
# print("Welcome")
# num = int(input("Enter password:"))
# while num != password:
#     print("Password incorrect, please try again")
#     num = int(input("Enter password:"))
# print("Password correct")
# random_num = int(input("Enter a number:"))
# cor_random = random.randint(1,10)
# while random_num != cor_random:
#     print("Your number is not equal to my number, try again")
#     random_num = int(input("Enter a number:"))
# print("You entered the correct number", cor_random)

###Activity 1

# num = 1
# while num < 10:
#     print("This is turn", num)
#     num = num + 1
# print("This loop has now ended")

# num = 10
# while num >= 7:
#     print("This is turn", num)
#     num = num - 1
# print("loop is finished")
        
# a = 0
# b = 0
# while a < 4:
#     a = a + 1
#     b = 0
#     while b < 4:
#         b = b + 1
#         print(a,b)


### FOR Loops ###

# for loop_counter in range(11):
#     print(loop_counter)

# for loop_counter in range(1, 11):
#     print(loop_counter)

# for loop_counter in range(1, 11, 2):
#     print(loop_counter)

# for loop in range(2, 10, 2):
#     print(loop)
# print("Who do we appreciate?")

# for x in range(1, 20):
#     print('This is number', x)
#     if x < 10:
#         break

# for number in range(1000000000):
#     print(number)
#     if number == 20:
#         break 


# for potato in range (1,4):
#     print(potato, "potato")
# print("4")
# for potato in range(5, 8):
#     print(potato, "potato")
# print("more")


# for potato in range(1, 8):
#     if potato == 4:
#         print(potato)
#     print(potato, "potato")
# print("more")

# for Floor in range(1,4):
#     for Room in range(1,5):
#         print("Floor", Floor, "Room", Room, "cleaned")

#paid = 15
#tax = 3
#coins = 22
#for week in range(1, 53):
#    print("Week = ( ", week, ", ", coins, ")")
#    coins = coins + paid
#    coins = coins - tax

#list = []
#list.append
#list.insert([1])
#list.remove
#list.reverse
#list.index[3]

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#even_nums = [num for num in a if num % 2 == 0]
#print(even_nums)

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#common_element = []

#print(common_element)

### Dictionaries ###

#thisdict = {
#    "brand": "Mercedes",
#    "model": "Mustang",
#    "year": 1964
#}

#print(thisdict["brand"])
#print(type(thisdict))
#print(len(thisdict))

#thisdict = dict(name = "John", age = 36, country = "Norway")
#print(thisdict)

#logins = {
#    'john': 'yellow',
#    'paul': 'red',
#    'george': 'blue',
#    'ringo': 'green'
#}
#print(logins['george']) == 'blue'

#logins['george'] = 'purple'
#print(logins)

#logins = {
#    'john': 'yellow',
#    'paul': 'red',
#    'george': 'blue',
#    'ringo': 'green'
#}

#print(logins['george']) == 'blue'
#for item in logins:
#    print(item)

#for key, value in logins.items():
#    print('The key is:', key, 'and the value is:', value)

#person = {
#    'Name:': 'John',
#    'Age:': 30,
#    'Adress:': '123 Main St.',
#    'Email:': 'john@example.com'        
#}

#for key, value in person.items():
#    print(key,value)

#ask = input("Do you want to enter your infomation?")
#if ask == 'yes':
#    name = input("Please enter your name:")
#    age = input("Please enter your age:")
#    adress = input("Please enter your adress:")
#    email = input("Please enter your Email adress:")
#else:
#    name = "John"
#    age = 30
#    adress = '123 Main St'
#    email = 'john@example.com'
#
#person = {
#    'Name:': name,
#    'Age:': age,
#    'Adress:': adress,
#    'Email:': email      
#}
#
#print("PLease check if your infomation are correct:")
#for key, value in person.items():
#    print(key,value)

### Functions ###

#def testfunc():
#    print("I love")
#    print("Computer Science")
#    print("At Worksop College")

#testfunc()

#def testfunc(myName):
#    print("Hello", myName)
#testfunc("Mary")
#testfunc("Tom")

#def testfunc(FirstName, LastName):
#    print("Hello", FirstName, LastName)

#testfunc("Julian", "Hammer")

#def output(number):
#    print(number, "squard =", number * number)

#number = 1
#while number < 21:
#    output(number)
#    number = number + 1

#def calculate(number):
#    newnumber = number / 100
#    return newnumber

#for counter in range(5, 101, 5):
#    answer = calculate(counter)
#    print(counter, "=", answer)

# Normal Program

#def calculate(number):
#    newnumber = 5 * number
#    return newnumber

#for counter in range(1, 12, 1):
#    answer = calculate(counter)
#    print("5 times", counter, "=", answer)

# Challenge 1

#usr = int(input("Enter a number"))

#def calculate(number):
#    newnumber = usr * number
#    return (newnumber)

#for counter in range(1, 12, 1):
#    answer = calculate(counter)
#    print(usr, "times", counter, "=", answer)

#Challenge 2

#def menu():
#    ask = input("Choose between two games enter 1 or 2: ")
#
#    if ask == "1":
#        game1()
#    elif ask == "2":
#        game2()

#def game1():
#    def loop():
#        usr = int(input("Enter a number: "))
#
#        def calculate(number):
#            newnumber = usr * number
#            return (newnumber)
#
#        for counter in range(1, 12, 1):
#            answer = calculate(counter)
#            print(usr, "times", counter, "=", answer)
#
#        answer = input("Do you want to start again?     Y/N: ")
#        if answer == "Y" or answer == "y":
#            loop()
#        elif answer == "N" or answer == "n":
#            menu()
#
#    loop()

#def game2():
#    def loop():
#        usr = int(input("Enter a number: "))

#        def calculate(number):
#            newnumber = pow(usr, number)
#            return newnumber
#        
#        for counter in range(1, 12, 1):
#            answer = calculate(counter)
#            print(usr, "by the power of", counter, "=", answer)
#
#        answer = input("Do you want to start again?     Y/N: ")
#        if answer == "Y" or answer == "y":
#            loop()
#        elif answer == "N" or answer == "n":
#            menu()

#    loop()

#menu()



#answer = input("Do you want to start again?     Y/N: ")
#if answer == "Y" or answer == "y":
#   loop()

#import math

#def calc(radius):
#    area = math.pi * radius ** 2
#    area_rounded = round(area, 2)
#    return area_rounded

#def help():
#    radius = int(input("What's the radius of your circle? "))

#    area = calc(radius)
#    print("The Area of your Circle is: ", area)

#help()

#question = input("Do want to do it again? (y/n)")

#while question == "Y":
#    help()
#    question = input("Do want to do it again? (y/n)")
#else:
#    exit()

#def calc(celsius):
#    fahrenheit = (celsius * 9/5) + 32
#    return fahrenheit

#def help():
#    celsius = float(input("Enter your Temperature in Celcius: "))
#    fahrenheit = calc(celsius)
#    print(fahrenheit)

#help()

#question = input("Do want to do it again? (y/n)")

#while question == "Y" or question == "y":
#    help()
#    question = input("Do want to do it again? (y/n)")
#else:
#    exit()

#Calculate Factorial of a Number

#result is storing the value of the latest n

#def factorial(n):
#    result = 1
#    while n > 0:
#        result *= n
#        n -= 1
#    print("The result is", result)


#factorialnum = int(input("Please enter a integer number: "))

#factorial(factorialnum)

#question = input("Do you want to do it again? (y/n)")

#while question == "y":
#    factorialnum = int(input("Please enter a integer number: "))
#    factorial(factorialnum)
#    question = input("Do you want to do it again? (y/n)")
#else:
#    exit()

### Coding Task 22/06/23