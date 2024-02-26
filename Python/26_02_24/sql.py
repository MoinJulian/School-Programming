import sqlite3

mydb = sqlite3.connect('mydatabase.db')

c = mydb.cursor()

# Create table
c.execute("CREATE TABLE Students (student_firstname TEXT, student_surname TEXT, student_age TEXT, Form TEXT)")

print("Table created successfully")