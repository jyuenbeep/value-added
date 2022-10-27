#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

"""
INSTRUCTIONS:

Your trio MISSION: Write a simple Python script to import CSV data into a relational database.

Read data from CSV files, and create a database whose table structure mimics that of the CSV files.
(In the care package you will find a CSV file of students and their IDs, and another linking said IDs to the students’
current grades in some courses. Desire more lulz? Add extra, more expansive CSVs.)
"""

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

#todo
"""
- command --> CREATE TABLE
- open csv file w dictreader
-
"""

db.execute("DROP TABLE if exists students")
db.execute("DROP TABLE if exists courses")

students = {}
studentCount = 0
students['name'] = []
students['age'] = []
students['id'] = []

courses = {}
courseCount = 0
courses['code'] = []
courses['mark'] = []
courses['id'] = []

with open('courses.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        courses['code'].append(row['code'])
        courses['mark'].append(row['mark'])
        courses['id'].append(row['id'])
        courseCount+=1

with open('students.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        students['name'].append(row['name'])
        students['age'].append(row['age'])
        students['id'].append(row['id'])
        studentCount+=1

createCourses = "CREATE TABLE courses (code STRING, mark INTEGER, id INTEGER)"          # test SQL stmt in sqlite3 shell, save as string
createStudents = "CREATE TABLE students (name STRING, age INTEGER, id INTEGER)"

c.execute(createCourses)    # run SQL statement
c.execute(createStudents)

for i in range(studentCount):
    name = students['name'][i]
    age = students['age'][i]
    id = students['id'][i]
    c.execute(f"INSERT INTO students VALUES('{name}', {age}, {id})")

# # testing
# c.execute("SELECT * FROM students")
# var = c.fetchall()
# print (var)

for i in range(courseCount):
    code = courses['code'][i]
    mark = courses['mark'][i]
    id = courses['id'][i]
    c.execute(f"INSERT INTO courses VALUES('{code}', {mark}, {id})")

# # testing
# c.execute("SELECT * FROM courses")
# var = c.fetchall()
# print (var)

#==========================================================

db.commit() #save changes
db.close()  #close database
