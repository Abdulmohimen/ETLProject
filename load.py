import os
import pandas as pd
from sqlalchemy import create_engine
from config.config import DB_CONFIG

def load_data_to_db(df, table_name):
    """
    Loads the cleaned DataFrame into an existing PostgreSQL table.
    Saves a CSV backup.
    """
    # Build SQLAlchemy connection string
    conn_str = (
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    engine = create_engine(conn_str)

    # Save processed data to CSV
    os.makedirs('data/processed', exist_ok=True)
    processed_file = f"data/processed/{table_name}_processed.csv"
    df.to_csv(processed_file, index=False)

    # Insert into PostgreSQL
    try:
        df.to_sql(table_name, engine, if_exists='append', index=False, method='multi')
        print(f"Successfully loaded data to {table_name}")
    except Exception as e:
        print(f"Error loading data to {table_name}: {e}")
    finally:
        engine.dispose()
