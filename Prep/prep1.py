user = "Julian Hammer"
password = "Test1234"

print('''
    ###############################
    Welcome to Worksop College Bank
    ###############################
''')

input_user = input("Enter the user name: ")
input_password = input("Enter the password: ")

while input_user != user and input_password != password:
    input_user = input("Enter the user name: ")
    input_password = input("Enter the password: ")
print("Correct")
menu = input('''
    1. Balance
    2. Withdraw
    3. Deposit
    4. Send money
    5. Receive money
    6. Delete Account
    You can choose between 6 different things, enter the number you want:
''')
if menu == 1:
    print("You bank is empty!")
elif menu == 2:
    print("You withdrawal 100% of your bank account")
elif menu == 3:
    print("You deposit a amount of null")
elif menu == 4:
    print("You sended 50% of your money")
elif menu == 5:
    print("You received a bill")
elif menu == 6:
    print("Your account got deleted.")