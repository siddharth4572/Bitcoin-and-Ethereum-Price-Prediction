# backend/data_fetcher.py
import yfinance as yf
import os

def fetch_data():
    # Create the data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Download historical data
    btc_data = yf.download('BTC-USD', start='2016-01-01', end='2024-10-26')
    eth_data = yf.download('ETH-USD', start='2016-01-01', end='2024-10-26')

    # Reset index to make 'Date' a column
    btc_data.reset_index(inplace=True)
    eth_data.reset_index(inplace=True)

    # Save to CSV files
    btc_data.to_csv('data/btc_data.csv', index=False)
    eth_data.to_csv('data/eth_data.csv', index=False)

    print("Data saved to CSV files.")

if __name__ == "__main__":
    fetch_data()