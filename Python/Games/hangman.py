import random

# Define the list of words
Words = ["Python", "Svelte", "Java", "JavaScript"]

# Randomly select a word from the list
Word = random.choice(Words)

# Initialize the number of remaining guesses
Guess_Remaining = 6

# Initialize the displayed word as an empty string
Display_Word = ""

# Initialize the list of guessed letters
Guessed_Letters = []

# Loop through each letter in the selected word and replace with underscores
for letter in Word:
    Display_Word += "_"

print("Welcome to Hangman!")
print("You have to guess the word in 6 tries to win!")
print("The words are:", Words)
print("Good luck")

while Guess_Remaining > 0:
    print("\nWord:", Display_Word)
    print("Guesses remaining:", Guess_Remaining)
    Guess = input("Guess a letter: ")
    
    # Check if the guess is invalid
    if len(Guess) != 1 or not Guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue
    
    # Check if the guess has already been guessed
    if Guess in Guessed_Letters:
        print("You've already guessed that letter.")
        continue
    
    # Add the guess to the list of guessed letters
    Guessed_Letters.append(Guess)
    
    # Check if the guess is in the word
    if Guess in Word:
        print("Good guess!")
        Display_Word = "".join([c if c == Guess or c in Guessed_Letters else "_" for c in Word])
    else:
        print("Incorrect guess.")
        Guess_Remaining -= 1
    
    # Check if the word has been completely guessed
    if set(Word) <= set(Guessed_Letters):
        print("\nCongratulations! You have guessed the word:", Word)
        break

if Guess_Remaining == 0:
    print("\nYou're out of guesses! The correct word was:", Word)
