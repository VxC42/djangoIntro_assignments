import re

NAME = re.compile(r'^[a-zA-z]+$')
EMAIL = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

def formIsValid(user):
    error=[]
    isValid=True

    if len(user['first_name'])<2:
        isValid=False
        error.append("Name must be more than 2 characters")
    if not re.match(NAME, user['first_name']):
        isValid=False
        error.append("Name must only be letters")
    if len(user['last_name'])<2:
        isValid=False
        error.append("Name must be more than 2 characters")
    if not re.match(NAME, user['last_name']):
        isValid=False
        error.append("Name must only be letters")
    if not re.match(EMAIL, user['email']):
        isValid=False
        error.append("Not a correctly formatted email")
    if len(user['pw'])<8:
        isValid=False
        error.append("Password must be more than 8 characters")
    if user['pw'] != user['confirm_pw']:
        isValid=False
        error.append("Passwords do not match")

    return {"isValid":isValid, "errors":error}

def loginIsValid(user):
    error=[]
    isValid=True

    if not re.match(EMAIL, user['email']):
        isValid=False
        error.append("Email is not in database")
    if len(user['pw'])<8:
        isValid=False
        error.append("Password does not match Email info")

    return {"isValid":isValid, "errors":error}
