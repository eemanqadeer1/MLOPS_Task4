import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load dataset from local directory
df = pd.read_csv("C:/Users/hp/Downloads/Cereals/cereal.csv")  # Update the path accordingly
# Drop any rows with missing values 
df.dropna(inplace=True)

# Encode categorical variables
df = pd.get_dummies(df, columns=["mfr", "type"], drop_first=True)

# Split dataset into features (X) and target variable (y)
X = df.drop(columns=["name", "rating"])
y = df["rating"]

# Split data into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot predicted vs actual ratings
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.xlabel('Actual Rating')
plt.ylabel('Predicted Rating')
plt.title('Actual vs Predicted Ratings for Cereals')
plt.show()

import joblib

# Save model to file
joblib.dump(model, 'Cereals.joblib')
