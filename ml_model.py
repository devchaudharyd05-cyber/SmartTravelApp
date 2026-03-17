import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# Load dataset
data = pd.read_csv("data/destinations.csv")

# Features used for training
X = data[["likes_beach", "budget", "travel_price", "rating"]]

# Target variable
y = data["destination"]

# Create and train model once
model = DecisionTreeClassifier()
model.fit(X, y)


def recommend_destination(likes_beach, budget):
    """
    Predict best destination based on user preference
    """

    # Use average dataset values for missing inputs
    avg_price = data["travel_price"].mean()
    avg_rating = data["rating"].mean()

    # Prediction
    prediction = model.predict([[likes_beach, budget, avg_price, avg_rating]])

    return prediction[0]