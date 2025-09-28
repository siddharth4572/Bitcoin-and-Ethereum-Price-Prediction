# Bitcoin and Ethereum Price Prediction

A machine learning project for predicting Bitcoin and Ethereum prices using historical data. The project includes a Flask backend with an XGBoost model for Bitcoin price prediction and a simple web frontend for user interaction.

## Features

- **Price Prediction**: Predict Bitcoin closing prices based on open, high, low, and volume data using XGBoost.
- **Web Interface**: Simple HTML/CSS/JavaScript frontend to input data and view predictions.
- **Flask API**: RESTful API endpoints for predictions.
- **Data Handling**: Support for historical cryptocurrency data in CSV format.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Bitcoin-and-Ethereum-Price-Prediction
   ```

2. Install backend dependencies:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Train the model (if needed):
   ```
   python model.py
   ```
   This will generate `btc_model.pkl` in the root directory.

## Usage

1. Start the Flask server:
   ```
   cd backend
   python app.py
   ```
   The server will run on `http://localhost:5000`.

2. Open the frontend:
   - Open `frontend/index.html` in your web browser, or
   - Access the root endpoint `/` which serves the frontend.

3. Use the web interface to input prediction data (Open, High, Low, Volume) and get Bitcoin price predictions.

## Data

- `data/btc_data.csv`: Historical Bitcoin price data.
- `data/eth_data.csv`: Historical Ethereum price data (currently not used in the model).

Data should include columns: Date, Open, High, Low, Close, Volume.

## Model

The project uses XGBoost Regressor trained on Bitcoin historical data to predict closing prices.

- **Features**: Open, High, Low, Volume
- **Target**: Close
- **Algorithm**: XGBoost
- **Training**: 80/20 train-test split

To retrain the model, run `python backend/model.py`.

## API Endpoints

- `GET /`: Serves the frontend HTML page.
- `POST /predict`: Accepts JSON data with prediction features and returns predicted price.
  - Request body: `{"Open": float, "High": float, "Low": float, "Volume": float}`
  - Response: `{"prediction": [float]}`

## Frontend

The frontend is a simple web page with:
- Input fields for prediction features
- Submit button to make predictions
- Display area for prediction results

Files:
- `frontend/index.html`: Main HTML page
- `frontend/css/`: Stylesheets
- `frontend/js/`: JavaScript for API calls

## Dependencies

- Flask: Web framework
- pandas: Data manipulation
- numpy: Numerical computations
- scikit-learn: Machine learning utilities
- xgboost: Gradient boosting algorithm
- fbprophet: Time series forecasting (not currently used)
- yfinance: Yahoo Finance data (for potential data fetching)
- joblib: Model serialization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
