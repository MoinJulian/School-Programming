### Activity 1.3 ###
#Chemical Symbols

def lithium():
    sub = "Li, lithium, alkali metals"
    element = "Element: Lithium"
    atomic_weight = "Atomic weight: 6.94"
    group = "Alkali metals"
    print(sub)
    print(element)
    print(atomic_weight)
    print(group)

def sodium():
    sub = "Na, sodium, alkali metals"
    element = "Element: Sodium"
    atomic_weight = "Atomic weight: 22.99"
    group = "Alkali metals"
    print(sub)
    print(element)
    print(atomic_weight)
    print(group)

def potassium():
    sub = "K, potassium, alkali metals"
    element = "Element: Potassium"
    atomic_weight = "Atomic weight: 39.098"
    group = "Alkali metals"
    print(sub)
    print(element)
    print(atomic_weight)
    print(group)

def fluerine():
    sub = "F, fluorine, halogens"
    element = "Element: Fluorine"
    atomic_weight = "Atomic weight: 18.998"
    group = "Halogens"
    print(sub)
    print(element)
    print(atomic_weight)
    print(group)

def chlorine():
    sub = "Cl, chlorine, halogens"
    element = "Element: Chlorine"
    atomic_weight = "Atomic weight: 35.45"
    group = "Halogens"
    print(sub)
    print(element)
    print(atomic_weight)
    print(group)

def bromine():
    sub = "Br, bromine, halogens"
    element = "Element: Bromine"
    atomic_weight = "Atomic weight: 79.904"
    group = "Halogens"
    print(sub)
    print(element)
    print(atomic_weight)
    print(group)

def test_element():
    if element == "lithium" or element == "Li":
        lithium()
    elif element == "sodium" or element == "Na":
        sodium()
    elif element == "potassium" or element == "K":
        potassium()
    elif element == "fluerine" or element == "F":
        fluerine()
    elif element == "chlorine" or element == "Cl":
        chlorine()
    elif element == "bromine" or element == "Br":
        bromine()
    elif element == "*":
        lithium()
        sodium()
        potassium()
        fluerine()
        chlorine()
        bromine()
    else:
        print("Please enter a valid symbol")


welcome_message = "Welcome to the Python periodic table"
intruduction = "You can enter the symbol, the element or the group of an Element!"
print(welcome_message)
print(intruduction)
element = input("Enter your Element! If you like to see every thing enter '*'!")
test_element()