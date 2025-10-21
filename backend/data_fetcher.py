# backend/data_fetcher.py
import yfinance as yf
import os

def fetch_data():
   
    if not os.path.exists('data'):
        os.makedirs('data')


    btc_data = yf.download('BTC-USD', start='2016-01-01', end='2024-10-26')
    eth_data = yf.download('ETH-USD', start='2016-01-01', end='2024-10-26')

  
    btc_data.reset_index(inplace=True)
    eth_data.reset_index(inplace=True)

    
    btc_data.to_csv('data/btc_data.csv', index=False)
    eth_data.to_csv('data/eth_data.csv', index=False)

    print("Data saved to CSV files.")

if __name__ == "__main__":
    fetch_data()
