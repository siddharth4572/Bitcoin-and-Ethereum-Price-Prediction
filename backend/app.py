# backend/app.py
import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, send_from_directory

# Define the path to the project root to build absolute paths
# This makes the app runnable from anywhere
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

app = Flask(__name__,
            # Serve static files (CSS, JS) from the frontend folder
            static_folder=os.path.join(PROJECT_ROOT, 'frontend'),
            # Serve the index.html from the frontend folder
            template_folder=os.path.join(PROJECT_ROOT, 'frontend'))

# Load the trained model using an absolute path
model_path = os.path.join(PROJECT_ROOT, 'btc_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/predict/btc', methods=['POST'])
def predict_btc():
    """Handles BTC prediction requests."""
    try:
        data = request.get_json()
        # The JS sends a list with one object, so we create a DataFrame
        features_df = pd.DataFrame(data)
        # Ensure the column order matches the model's training data
        features = features_df[['Open', 'High', 'Low', 'Volume']]
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        # Return a proper error response if something goes wrong
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
