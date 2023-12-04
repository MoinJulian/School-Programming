#List of Forces and Chemikals

def menu():
    print("You can choose between Physical Forces and Chemical Symbols.")
    list = input("Please enter your List name:")

    #Test List name

    if(list == "physical forces" or list == "forces"):
        forces()
    elif(list == "chemical symbols" or list == "symbols"):
        symbols()

def forces():
    print("Possible Forces are:")
    print(" Friction Force, \n Tension Force, \n Air Resistance Force, \n Normal Force, \n Spring Force")
    chooseForce = input("Choose your Force:")

    #Work out Force

    if(chooseForce == "friction force" or chooseForce == "friction"):
        friction()
    elif(chooseForce == "tension force" or chooseForce == "tension"):
        tension()
    elif(chooseForce == "air resistance force" or chooseForce == "air resistance"):
        air_resistance()
    elif(chooseForce == "normal force" or chooseForce == "normal"):
        normal()
    elif(chooseForce == "spring force" or chooseForce == "spring"):
        spring()

    #Return to Menu

    goBack = input('If you like to go back enter: "Yes". If not enter: "No":')
    if(goBack == "Yes" or goBack == "yes" or goBack == "y" or goBack == "Y"):
        menu()
    elif(goBack == "No" or goBack == "no" or goBack == "n" or goBack == "N"):
        return
    else:
        print("You enter an invalid value!")
        print("Ending Programm!")
        return

def friction():
    print("You will get the Wikipedia link for this section:")
    print("https://en.wikipedia.org/wiki/Friction")
    return

def tension():
    print("You will get the Wikipedia link for this section:")
    print("https://en.wikipedia.org/wiki/Tension_(physics)")
    return

def air_resistance():
    print("You will get the Wikipedia link for this section:")
    print("https://en.wikipedia.org/wiki/Drag_coefficient")
    return

def normal():
    print("You will get the Wikipedia link for this section:")
    print("https://en.wikipedia.org/wiki/Normal_force")
    return

def spring():
    print("You will get the Wikipedia link for this section:")
    print("https://en.wikipedia.org/wiki/Spring_(device)")
    return

def symbols():
    print("If you like to see all Chemical Symbols click the link below:")
    print("https://en.wikipedia.org/wiki/List_of_chemical_elements")

    #Return to Menu

    goBack = input('If you like to go back enter: "Yes". If not enter: "No":')
    if(goBack == "Yes" or goBack == "yes" or goBack == "y" or goBack == "Y"):
        menu()
    elif(goBack == "No" or goBack == "no" or goBack == "n" or goBack == "N"):
        return
    else:
        print("You enter an invalid value!")
        print("Ending Programm!")
        return

menu()