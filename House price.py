import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("house_data.csv")

 

# Save model
joblib.dump(model, "house_model.pkl")
