import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
mongo_db_connection_string = os.getenv('MONGO_DB_CONNECTION_STRING')

# MongoDB setup
client = MongoClient(mongo_db_connection_string)
db = client['math_quiz_app']  # Database name
scores_collection = db['scores']  # scores_collection name

# Questions

questions = [
    [
        "What is 10+2",
        "12"
    ],
    [
        "What is 10-2",
        "8"
    ],
    [
        "What is 10*2",
        "20"
    ],
    [
        "What is 10/2",
        "5"
    ],
    [
        "What is 10%2",
        "0"
    ],
    [
        "What is 10**2",
        "100"
    ],
    [
        "What is 10//2",
        "5"
    ]
]

def ask_question(): 
    score = 0
    for question in questions:
        answer = input(question[0] + ": ")
        if answer == question[1]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    return score

name = input("Enter your name: ")
score = ask_question()
scores_collection.insert_one({
    "name": name,
    "score": score,
    "total_questions": len(questions)
})

print("You scored " + str(score) + " out of " + str(len(questions)) + " questions.")