print("Welcome to Worksop College Login Page")
username = input("Username:")
password = input("Password:")
answer_password = "1234"
answer_username = "julian"
text = '''
    Worksop College is a Grade II listed building. /n
    It has many fine buildings styled in Tudor Revival including: /n
    The Great Hall, the centrepiece to Worksop and the first building to be completed. One of the largest rooms in Nottinghamshire, its hammerbeams are spectacular; the original design was based upon Westminster Hall. By R H Carpenter /n
    The Chapel, in gothic revival style opened in 1906. The structure was based upon that of Westminster Abbey and the ceiling contains many passages of Latin verse (specifically these are the words of the Te Deum). By Aston Webb /n
    The East Wing, the first wing of Worksop to be opened, was blessed in 1895 by the Bishop of Southwell. It was one of the wings added by B D Thompson in 1907, 1928, 1931 and 1934 /n
    The Squash Courts were once lit by natural light, but the former roof has now been replaced by a mezzanine ceiling. The courts are an excellent example of early squash courts. The balcony is particularly noteworthy as the courts were designed in back to back format which is quite rare. /n
        '''

def teachers():
    print("The Worksop College has a staff size of 157 staff members including teachers, minibus drivers and many more.")

def houses():
    print("Boys' houses:")
    print("Mason House (formerly Cross, opened in 1895)")
    print("Pelham House (formerly Fleur de Lys, opened in 1895)")
    print("Talbot House (formerly Crown, opened in 1897)")
    print("Shirley House (opened in 1925)")
    print("Girls' houses:")
    print("Derry House (opened in 1978)")
    print("Gibbs House (opened in 1986)")
    print("School House (opened in 1930, closed in 1986, re-opened in 2007)")
    print("Junior house:")
    print("Portland House (opened in 1948 when Prep moved to Ranby, re-opened as a junior house in 2016)")
    print("Closed house:")
    print("Mountgarret (formerly Lion, opened 1895, closed 1993)")

def buildings():
    print(text)

def menu():
    print("Please choose a topic!")
    print("What do you like to see?")
    print("Enter the letter in front of the topic!")
    print("A: Teachers")
    print("B: Houses")
    print("C: Buildings")
    choose = input("What do you like to see?")
    if choose == "A" or choose == "a":
        teachers()
    elif choose == "B" or choose == "b":
        houses()
    elif choose == "C" or choose == "c":
        buildings()

if password != answer_password and username != answer_username:
    print("Access denied")
elif username != answer_username and password == answer_password:
    print("Wrong Username entered, please try again!")
    username = input("Username:")
    if username != answer_username:
        print("Access deneid")
    else:
        menu()
elif username == answer_username and password != answer_password:
    print("Wrong Password entered, please try again!")
    password = input("Password:")
    if password != answer_password:
        print("Access deneid!")
    else:
        menu()
elif username == answer_username and password == answer_password:
    menu()