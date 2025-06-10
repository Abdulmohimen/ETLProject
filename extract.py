import requests
import pandas as pd
import os
from config.config import MARKETSTACK_API_KEY

def fetch_stock_data(symbol, limit=100):
    """
    Fetches daily stock data from MarketStack API for a given symbol.
    Saves raw data to CSV.
    """
    url = "http://api.marketstack.com/v1/eod"
    params = {
        'access_key': MARKETSTACK_API_KEY,
        'symbols': symbol,
        'limit': limit
    }
    response = requests.get(url, params=params)
    data = response.json()

    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text[:300]}...")  # Print a snippet for debug

    if 'data' not in data or not data['data']:
        error_msg = data.get('error', {}).get('message', 'Unknown error')
        print(f"Error fetching data for {symbol}: {error_msg}")
        return None

    df = pd.DataFrame(data['data'])
    if df.empty:
        print(f"No data received for {symbol}.")
        return None

    # Save raw data
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv(f'data/raw/{symbol}_raw.csv', index=False)
    return df
