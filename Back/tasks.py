'''
    Juan Cocina, 1/21/2022
    The purpose of this file is to store tasks/users into an SQL Database
    As well as retrieving data and sending data where required.
'''

import hug
import requests
import json
from datetime import datetime
import sqlite_utils
import schedule
import time

# arguments to inject into route functions

@hug.directive()
def sqlite(section="sqlite", key="dbfile", **kwargs):
    dbfile = '../var/scheduler.db'
    return sqlite_utils.Database(dbfile)

#
#  Route
#

#
#  GET USERS
#
# Route
@hug.get("/users/")
def users(db: sqlite):
    return {"users": db["users"].rows}

#
#  Testing database insertions -- Adding a user to the database
#
@hug.post('/addUser/', status=hug.falcon.HTTP_201)
def addUser(
        response,
        username: hug.types.text,
        password: hug.types.text,
        email: hug.types.text,
        phone_number: hug.types.number,
        db: sqlite,
):
    users = db["users"]
    user = {
        "username": username,
        "password": password,
        "email": email,
        "phone_number": phone_number,
    }

    try:
        users.insert(user)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"Error": str(e)}

    response.set_header("Location", f"/scheduler/{user['username']}")
    return user

#
#  Deleting a user from the database
#           .. since i'm basically the only one using this... not implementing

#
#  add Task
#
@hug.post('/addTask/', status=hug.falcon.HTTP_201)
def addTask(
        response,
        username: hug.types.text,
        task_description: hug.types.text,
        time: hug.types.text,
        db: sqlite,
):

    tasks = db["tasks"]
    time = datetime.strptime(time, '%b %d %Y %I:%M%p')
    print(time)
    task_description = task_description.replace("%20", " ")

    task = {
        "username": username,
        "task_description": task_description,
        "time": time,
    }

    try:
        tasks.insert(task)
        task["id"] = tasks.last_pk
        print(tasks.last_pk)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"Error": str(e)}

    response.set_header("Location", f"/scheduler/{task['username']}")
    return task


#
#  retrieves all tasks ordered by time inserted
#
@hug.get('/retrieveAllTasks/')
def retrieveAllTasks(request, db: sqlite):
    tasks = db["tasks"]

    # order return by ascending time
    return {"tasks": db["tasks"].rows_where(order_by="time asc")}

#
#   retrieves tasks given a specific username
#
@hug.get('/retrieveByUser/{username}')
def retrieveyByUser(db: sqlite, username: hug.types.text):

    tasks = []
    for column in db.query('SELECT * FROM tasks WHERE username= ? ORDER BY time asc', [username]):
        tasks.append(column)
    if not tasks:
        return {"Status Code": "404", "Message": "User could not be found"}
    else:
        return {"Tasks": tasks}

#
#   delete task
#   https://github.com/simonw/sqlite-utils/blob/19073d6d972fad9d68dd74c28544cd29083f1c12/docs/python-api.rst#deleting-a-specific-record
#   CREDITS TO ^

@hug.delete('/deleteTask/{id}')
def deleteTask(db: sqlite, id: hug.types.text):
    tasks = db["tasks"]
    
    if tasks.delete([id]):
        return {"Status Code": "200", "Message": "Successfuly Deleted"}
    else:
        return {"Status Code": "500", "Message": "Server Error Occured"}

    

