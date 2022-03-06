'''
    Juan Cocina, 1/21/2022
    The purpose of this file is to store tasks into an SQL Database AND send orders to pythonsms.py
'''

import hug
import requests
import json
from datetime import datetime
import sqlite_utils
import schedule

# arguments to inject into route functions

@hug.directive()
def sqlite(section="sqlite", key="dbfile", **kwargs):
    dbfile = '../var/scheduler.db'
    return sqlite_utils.Database(dbfile)

#
#  Route
#
@hug.get('/')
def landing():
    return {"Status Code": "200", "Message": "Scheduler API is up and running!"}

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
        set_reminder: hug.types.text,
        set_repeat: hug.types.text,
        i_o: hug.types.boolean,
        db: sqlite,
):
    tasks = db["tasks"]
    set_reminder = datetime.strptime(set_reminder, '%b %d %Y %I:%M%p')
    print(set_reminder)
    task_description = task_description.replace("%20", " ")

    task = {
        "username": username,
        "task_description": task_description,
        "set_reminder": set_reminder,
        "set_repeat": set_repeat,
        "i_o": i_o
    }

    try:
        tasks.insert(task)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"Error": str(e)}

    response.set_header("Location", f"/scheduler/{task['username']}")
    return task



