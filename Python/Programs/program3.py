cor_num = 1234
print("Welcome to Worksop College Super Computer")
print("")
print("In order to enter you must input the correct 4 digit code")
print("")
num = int(input("Please enter the 4 digit code: "))
while num != cor_num:
    print("This is incorrect")
    num = int(input("Please try again: "))
print("Passowrd is correct")
