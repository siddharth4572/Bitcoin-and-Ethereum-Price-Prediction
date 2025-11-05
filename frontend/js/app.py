import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, send_from_directory

# Define the path to the project root to build absolute paths
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

app = Flask(__name__,
            static_folder=os.path.join(PROJECT_ROOT, 'frontend'),
            template_folder=os.path.join(PROJECT_ROOT, 'frontend'))

# Load the trained model
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
        # The JS sends a list with one object
        features_df = pd.DataFrame(data)
        # Ensure the order of columns matches the training data
        features = features_df[['Open', 'High', 'Low', 'Volume']]
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict/eth', methods=['POST'])
def predict_eth():
    """Placeholder for ETH prediction."""
    # NOTE: This is a placeholder. You need to train and load an ETH model.
    return jsonify({'error': 'ETH model not available.'}), 501

if __name__ == '__main__':
    app.run(debug=True, port=5000)