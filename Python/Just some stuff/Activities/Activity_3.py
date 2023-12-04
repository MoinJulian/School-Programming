print("Welcome to Worksop College Login Page")
username = input("Username:")
password = input("Password:")
answer = "test"

if username == answer and password == answer:
    print("Log In confirmed!")
elif username != answer and password == answer:
    print("Username incorrect!")
    print("Enter username again!")
    username = input("Username:")
    if username == answer:
        print("Log In confirmed!")
    else:
        print("Log In denid!")
elif password != answer and username == answer:
    print("Enter password again!")
    password = input("Password:")
    if password == answer:
        print("Log In confirmed!")
    else:
        print("Log In denid!")
elif password != answer and username != answer:
    print("Try again!")
    username = input("Username:")
    password = input("Password:")
    if password == answer and username == answer:
        print("Log In confirmed!")
    else:
        print("Log In denid!")