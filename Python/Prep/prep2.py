import random
import time

user_name = "1234"
user_password = "1234"

# function to generate a random math question
def generate_question():
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  operator = random.choice(["+", "-", "*"])
  if operator == "+":
    answer = num1 + num2
  elif operator == "-":
    answer = num1 - num2
  else:
    answer = num1 * num2
    question = f"What is {num1} {operator} {num2}? "
  return question, answer


# welcome message
print("Welcome to the Worksop College Maths Quiz!")

entered_name = input("Please enter your username: ")
entered_password = input("Please enter your password: ")

if entered_name == user_name and entered_password == user_password:
  # instructions
  print("Instructions: For each question, enter your answer as a number and press enter.\n")


  # initialize score
  score = 0

  # ask five questions
  for i in range(5):
    # generate question
    question, answer = generate_question()

    # ask question and start timer
    print(question)
    start_time = time.time()

    # get user's answer
    user_answer = input()

    # stop timer and calculate time taken
    end_time = time.time()
    time_taken = end_time - start_time

    # check if answer is correct and update score
    if int(user_answer) == answer:
      print("Correct!")
      score += 1
    else:
      print(f"Incorrect. The correct answer is {answer}.")

    # output time taken
    print(f"Time taken: {round(time_taken, 2)} seconds\n")

  # output score
  print(f"You answered {score} out of 5 questions correctly.")
else:
  print("Log in failed!")

