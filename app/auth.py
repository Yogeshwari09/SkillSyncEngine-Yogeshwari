users = {}

# Register User
def register_user(username, password):

    if username in users:
        return False

    users[username] = password

    return True


# Login User
def login_user(username, password):

    if username in users:

        if users[username] == password:
            return True

    return False