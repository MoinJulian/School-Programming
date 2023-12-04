from datetime import date

today = date.today()
name = input("Please input your name: ")
volunteer = input("Would you like to work as a volunteer for Friends of Seaiew Pier? (Enter 'y' for yes) ")

if volunteer == "y":
    print("We have three areas you can help with.")
    print("The first one is at the pier entrance gate.")
    print("The second one is at the gift shop.")
    print("The thrird one is painting and decorating the pier")
    pier_entrance_gate = input("Would you like to volunteer at the Pier entrance gate? (y for yes ) ")
    if pier_entrance_gate != "y":
        gift_shop = input("Would you like to work for the gift shop? (y for yes) ")
        if gift_shop != "y":
            painting_and_decorating = input("Or would you like painting and decorating the peir? (y for yes) ")
            if painting_and_decorating != "y":
                print("If you want to work as a Volunteer you need to choose one from them above!")
            else:
                 print("You got registered as a volunteer for Painting and Decorating the Pier")
        else:
            print("You got registered as a volunteer for the Gift Shop")
    else:
        print("You got registered as a volunteer for the Entrance Gate")
    print("You joined today: ", today)
    paid = input("Have you paid the fee of $75? (y for yes)")
else:
    print("You joined today: ", today)
    paid = input("Have you paid the fee of $75? (y for yes)")
    if paid != "y":
        print("You still need to pay the fee of $75, you can send it to following IBAN: 123456789")
    else:
        print("You ")