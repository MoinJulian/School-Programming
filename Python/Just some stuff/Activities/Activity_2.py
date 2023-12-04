print("Welcome to Worksop College Login Page")
username = input("Username:")
password = input("Password:")

if username == "test" and password == "test":
    print("Log In confirmed!")
elif username != "test" and password == "test":
    print("Username incorrect!")
elif password != "test" and username == "test":
    print("password incorrect!")
elif password != "test" and username != "test":
    print("Log In data incorrect!")