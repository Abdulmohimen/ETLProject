import pandas as pd

def clean_stock_data(df):
    """
    Cleans and standardizes MarketStack stock data DataFrame.
    Keeps only columns that exist in both the DataFrame and the DB table.
    """
    # Define the columns as in your DB table (adjusted for MarketStack)
    table_cols = [
        'symbol', 'date', 'open', 'high', 'low', 'close', 'volume',
        'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume',
        'dividend', 'split_factor', 'adjusted_close', 'dividend_amount', 'split_coefficient',
        'daily_return', 'seven_day_ma', 'volume_change'
    ]
    # Add missing columns with None values
    for col in table_cols:
        if col not in df.columns:
            df[col] = None
    # Keep columns in DB order
    df = df[table_cols]
    # Convert numerics
    numeric_cols = [
        'open', 'high', 'low', 'close', 'volume', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume',
        'dividend', 'split_factor', 'adjusted_close', 'dividend_amount', 'split_coefficient',
        'daily_return', 'seven_day_ma', 'volume_change'
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    # Convert date
    if df['date'].dtype == object or pd.api.types.is_string_dtype(df['date']):
        df['date'] = pd.to_datetime(df['date']).dt.date
    # Drop rows missing price or volume
    df = df.dropna(subset=['open', 'high', 'low', 'close', 'volume'])
    # Sort by date
    df = df.sort_values('date', ascending=False).reset_index(drop=True)
    return df
