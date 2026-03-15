import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def train_model():

    data = pd.read_csv("data/destinations.csv")

    X = data[["likes_beach","budget"]]
    y = data["destination"]

    model = DecisionTreeClassifier()

    model.fit(X,y)

    return model


def recommend_destination(likes_beach,budget):

    model = train_model()

    prediction = model.predict([[likes_beach,budget]])

    return prediction[0]