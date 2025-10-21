# backend/model.py
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib  # Import joblib for saving the model

def train_model():
    
    btc_data = pd.read_csv('data/btc_data.csv')

  
    btc_data['Open'] = pd.to_numeric(btc_data['Open'], errors='coerce')
    btc_data['High'] = pd.to_numeric(btc_data['High'], errors='coerce')
    btc_data['Low'] = pd.to_numeric(btc_data['Low'], errors='coerce')
    btc_data['Close'] = pd.to_numeric(btc_data['Close'], errors='coerce')
    btc_data['Volume'] = pd.to_numeric(btc_data['Volume'], errors='coerce')

    
    btc_data.dropna(inplace=True)

    
    btc_data['Date'] = pd.to_datetime(btc_data['Date'])
    btc_data.set_index('Date', inplace=True)

    
    X = btc_data[['Open', 'High', 'Low', 'Volume']]
    y = btc_data['Close']

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   
    model = XGBRegressor()
    model.fit(X_train, y_train)

    
    joblib.dump(model, 'btc_model.pkl')
    print("Model saved to btc_model.pkl")

if __name__ == "__main__":
    train_model()
