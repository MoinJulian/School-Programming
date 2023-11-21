#Open a text file for writing

def edit_file(firstname, surname, password):
    text_file = open("/Users/julianhammer/Library/Mobile Documents/com~apple~CloudDocs/Dev/Python School/Write Files/names.txt", "w")
    text_file.write("You're first name is: " + firstname + "\n")
    text_file.write("Your Surname is" + surname + "\n")
    text_file.write("Your Password is: " + password + "\n")
    text_file.close()

firstname = input("Please enter your Firstname: ")
surname = input("Please enter your Surname: ")
password = input("Please enter a Password: ")

edit_file(firstname, surname, password)
