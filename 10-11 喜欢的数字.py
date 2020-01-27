import json
def show_stored_username():
    filename = 'numbers.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("what are you like number is :")
    filename = 'numbers.json'
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username
def greet_user():
    username = show_stored_username()
    if username:
        print("you favorite is " + str(username) + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()
