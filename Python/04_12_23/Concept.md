# Maths Quiz

Ask User 10 different Maths Questions

- Store Questions in an Object or Array
- Iterate through the Questions and ask the User the Question
  - Check if answer is correct
    - If it is wrong Print: "That was not correct" and continue to the next question
    - If it was correct Print "That was correct" and continue to the next question
  - Save the Answered Question with the User Input and the Coorect Answer in a File
- At the end print out how many questions the user got correct

# Pseudo code output by ChatGPT:

> Create a list or object to store questions along with correct answers

questions = [
{"question": "What is 4 x 10", "correct_answer": "40"},
{"question": "What is 2 + 2?", "correct_answer": "4"},

> Add more questions as needed

]

> Initialize a variable to keep track of correct answers

correct_answers_count = 0

> Open a file to save answered questions

file = open("answered_questions.txt", "w")

> Iterate through the list of questions

for each question_data in questions:
question = question_data["question"]
correct_answer = question_data["correct_answer"]

    # Ask the user the question
    user_answer = input(question + " ")

    # Check if the answer is correct
    if user_answer is equal to correct_answer:
        output("That was correct!")
        correct_answers_count = correct_answers_count + 1
    else:
        output("That was not correct.")

    # Save the answered question to the file
    file.write("Question: " + question + "\nUser Answer: " + user_answer + "\nCorrect Answer: " + correct_answer + "\n\n")

> Close the file

file.close()

> Output the total number of correct answers

output("You got " + correct_answers_count + " out of " + length of questions + " questions correct.")
