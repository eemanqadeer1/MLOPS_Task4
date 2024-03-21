from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('Cereals.joblib')

@app.route('/')
def home():
    return "Welcome to the Cereal Rating Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from request
    data = request.json

    # Convert input to correct format for prediction
    features = [data[f] for f in data]  # Assuming all features are provided in the request

    # Make prediction
    prediction = model.predict([features])[0]

    # Return prediction as JSON response
    return jsonify({'predicted_rating': prediction})

if __name__ == '__main__':
    app.run(debug=True)
