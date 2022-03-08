'''
    Juan Cocina, 1/21/2022
    The purpose of this file is to setup the databases that will be used by scheduler.py
'''

import sqlite3
import sqlite_utils
import csv

#  Connect to DB
connection = sqlite3.connect('/Users/juancocina/Desktop/SWE Projects/Scheduler/var/scheduler.db')

#  Creating a cursor object to execute
#  SQL queries on a database table
cursor = connection.cursor()

#  Table Definition for users
create_table = '''CREATE TABLE IF NOT EXISTS users(
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                phone_number INT NOT NULL);
                '''

#  Creating the table into the Database
cursor.execute(create_table)

#  Opening the csv files
file = open('/Users/juancocina/Desktop/SWE Projects/Scheduler/share/users.csv')

#  Reading the contents of the
#  person-records.csv file
contents = csv.reader(file)

#  SQL query to insert data into the
#  person table
insert_records = "INSERT INTO users (username, password, email, phone_number) VALUES(?, ?, ?, ?)"

#  Importing the contents of the file
#  into our person table
cursor.executemany(insert_records, contents)

#  SQL query to retrieve all data from
#  the person table To verify that the
#  data of the csv file has been successfully
#  inserted into the table
select_all = "SELECT * FROM users"
rows = cursor.execute(select_all).fetchall()
print("Users:")

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

#
#  Repeat the steps from earlier to insert the tasks, example
#

#  Table Definition for tasks
create_table = '''CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                username TEXT,
                task_description TEXT NOT NULL,
                time DATETIME NOT NULL);
                '''

#  Creating the table into the Database
cursor.execute(create_table)

#  Opening the csv files
file = open('/Users/juancocina/Desktop/SWE Projects/Scheduler/share/tasks.csv')

#  Reading the contents of the
#  person-records.csv file
contents = csv.reader(file)

#  SQL query to insert data into the
#  person table
insert_records = "INSERT INTO tasks (id, username, task_description, time) VALUES(?, ?, ?, ?)"

#  Importing the contents of the file
#  into our person table
cursor.executemany(insert_records, contents)

#  SQL query to retrieve all data from
#  the person table To verify that the
#  data of the csv file has been successfully
#  inserted into the table
select_all = "SELECT * FROM tasks"
rows = cursor.execute(select_all).fetchall()

print("Tasks:")

#  Output to the console screen
for r in rows:
    print(r)

#  Committing the changes
connection.commit()

#  closing the database connection
connection.close()
