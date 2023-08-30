## Challenge 3

def challenge_3():
    width = int(input("Please enter the width of your rectangle: "))
    height = int(input("Please enter the height of your rectangle: "))

    A = width * height

    print(A)

## Challenge 13

def challenge_13():
    sentence = str(input("Please enter a sentence: "))
    replace_word = str(input("Choose a word you like to replace:  "))
    replace_with = str(input("Choose the word you want to replace it with: "))

    new_sentence = sentence.replace(replace_word, replace_with)

    print("New sentence: ", new_sentence)
    

challenge_3()