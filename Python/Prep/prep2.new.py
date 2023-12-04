##What have I improved?
'''
I added a log in option for a user the user name and password is 1234
As well as I added the opportunity to see you total time taken for all questions
As well as you can choose the number of questions you want to get asked
'''



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
  number_of_questions = int(input("Enter a number of question you want to get asked: "))

  # initialize score
  score = 0

  #initialize total_time
  total_time = 0

  # ask five questions
  for i in range(number_of_questions):
    # generate question
    question, answer = generate_question()

    # ask question and start timer
    print(question)
    start_time = time.time()

    # get user's answer
    user_answer = input()

    try:
      user_answer = int(user_answer)
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    # stop timer and calculate time taken
    end_time = time.time()
    time_taken = end_time - start_time
    total_time += time_taken

    # check if answer is correct and update score
    if user_answer == answer:
      print("Correct!")
      score += 1
    else:
      print(f"Incorrect. The correct answer is {answer}.")

    # output time taken
    print(f"Time taken: {round(time_taken, 2)} seconds\n")

  # output score
  print(f"You answered {score} out of {number_of_questions} questions correctly.")
  print(f"You took {round(total_time, 2)} seconds for answer all questions.")
else:
  print("Log in failed!")
