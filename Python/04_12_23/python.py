# Define a list or dictionary to store questions along with correct answers
questions = [
    {"question": "What is the capital of France?", "correct_answer": "Paris"},
    {"question": "What is 2 + 2?", "correct_answer": "4"},
    # Add more questions as needed
]

# Create a variable to keep track of the user's correct answers
correct_answers_count = 0

# Create a file to save the answered questions
with open("/Users/julianhammer/Library/Mobile Documents/com~apple~CloudDocs/Dev/Python School/04_12_23/answered_questions.txt", "w") as file:
    # Iterate through the list of questions
    for question_data in questions:
        question = question_data["question"]
        correct_answer = question_data["correct_answer"]

        # Ask the user the question
        user_answer = input(question + " ")

        # Check if the answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("That was correct!")
            correct_answers_count += 1
        else:
            print("That was not correct.")

        # Save the answered question to the file
        file.write(f"Question: {question}\nUser Answer: {user_answer}\nCorrect Answer: {correct_answer}\n\n")

# Print the total number of correct answers
print(f"You got {correct_answers_count} out of {len(questions)} questions correct.")
