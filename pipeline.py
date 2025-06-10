from etl.extract import fetch_stock_data
from etl.transform import clean_stock_data
from etl.load import load_data_to_db

def run_etl_pipeline(symbols):
    """
    Runs ETL pipeline for the list of stock symbols.
    Fetches data, cleans it, and loads into the database.
    """
    for symbol in symbols:
        print(f"Processing {symbol}...")
        # 1. Extract
        df = fetch_stock_data(symbol)
        if df is None:
            print(f"Skipping {symbol}: No data fetched.")
            continue
        # 2. Transform
        df_clean = clean_stock_data(df)
        if df_clean is None or df_clean.empty:
            print(f"Skipping {symbol}: No cleaned data.")
            continue
        # 3. Load
        load_data_to_db(df_clean, "stocks")

    print("ETL pipeline completed!")

if __name__ == "__main__":
    # List your stock symbols here (change as needed)
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
    run_etl_pipeline(symbols)
