name = input ('Please enter your name')
volunteer = int(input('Would you like to be a volunteer for the Friends of Seaview Pier? Select 1 for yes, 2 for no'))
while volunteer != 1 and volunteer != 2:
    volunteer = int(input('Would you like to be a volunteer for the Friends of Seaview Pier? Select 1 for yes, 2 for no'))
if volunteer != 1 and volunteer != 2:
    print ('That is not a valid number.')
   
while volunteer == 2:
    donation = int(input('Would you like to donate to the Friends of The Seaview Pier? If yes, choose 1, if no, choose 2'))

if volunteer == 1:
    areaofwork = int(input('Where would you like to work? Choose the number 1 for pier enterance, 2 for the gift shop, or 3 for painting and decorating.'))
dayenter = int(input('What is the current day? Enter as 1-31'))
monthenter = int(input('What is the current month? Enter as 1-12'))
yearenter = int(input('What is the current year? Enter 2010 - 2060'))
