import sqlite3

conn = sqlite3.connect('./Python/Year12/name.db')
c = conn.cursor()

# c.execute('CREATE TABLE students (student_ID text, first_name text, surname text, cgroup text, age number)')

# conn.commit()

c.execute("INSERT INTO students VALUES ('1', 'Julian', 'Hammer', '12z', 18)")

# conn.commit()

c.execute("SELECT * FROM students WHERE surname='Hammer'")
print(c.fetchall())
conn.close()