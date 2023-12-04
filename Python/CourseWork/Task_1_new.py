def get_valid_input(prompt, valid_values):
    while True:
        user_input = input(prompt)
        if user_input in valid_values:
            return user_input
        print("Invalid input. Please try again.")

name = input("Please enter your name: ")

valid_volunteer_values = ["1", "2"]
volunteer = get_valid_input(
    "Would you like to be a volunteer for the Friends of Seaview Pier?"
    " Select 1 for yes, 2 for no: ",
    valid_volunteer_values
)

if volunteer == "2":
    donation = get_valid_input(
        "Would you like to donate to the Friends of The Seaview Pier?"
        " If yes, choose 1, if no, choose 2: ",
        valid_volunteer_values
    )
    if donation == "2":
        print("Okay, you've been registered!")

if volunteer == "1":
    area_of_work = input(
        "Where would you like to work? Choose the number 1 for pier entrance,"
        " 2 for the gift shop, or 3 for painting and decorating: "
    )

day_enter = int(input("What is the current day? Enter a number between 1 and 31: "))
month_enter = int(input("What is the current month? Enter a number between 1 and 12: "))
year_enter = int(input("What is the current year? Enter a number between 2010 and 2060: "))
