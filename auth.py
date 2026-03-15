import pandas as pd

def authenticate(username, password):

    users = pd.read_csv("data/users.csv")

    user = users[
        (users["username"] == username) &
        (users["password"] == password)
    ]

    return not user.empty