import re
from models import User

NAME = re.compile(r'^[a-zA-z\s]+$')

EMAIL = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

def formIsValid(user):
    error=[]
    isValid=True

    if len(user['name'])<2:
        isValid=False
        error.append("Name must be more than 2 characters")
    if not re.match(NAME, user['name']):
        isValid=False
        error.append("Name must only be letters")
    if len(user['username'])<2:
        isValid=False
        error.append("Username must be more than 2 characters")
    # if not re.match(USERNAME, user['username']):
    #     isValid=False
    #     error.append("Last name must only be letters")
    if not re.match(EMAIL, user['email']):
        isValid=False
        error.append("Not a correctly formatted email")
    if len(user['password'])<8:
        isValid=False
        error.append("Password must be more than 8 characters")
    if user['password'] != user['confirm_password']:
        isValid=False
        error.append("Passwords do not match")

    return {"isValid":isValid, "errors":error}

def loginIsValid(user):
    error=[]
    isValid=True

    if not re.match(EMAIL, user['email']):
        isValid=False
        error.append("Email is not in database")
    if len(user['password'])<8:
        isValid=False
        error.append("Password does not match Email info")

    return {"isValid":isValid, "errors":error}

def emailExists(user):
    error=[]
    exists=False
    checkEmail = User.objects.filter(email=user['email'])
    if len(checkEmail)>0:
        exists=True
        error.append("This email is associated with an account")

    return {"exists":exists, "errors":error}
def usernameExists(user):
    error=[]
    exists=False
    checkUsername = User.objects.filter(username=user['username'])
    if len(checkUsername)>0:
        exists=True
        error.append("This username is associated with an account")

    return {"exists":exists, "errors":error}
