📊 Crypto Market Intelligence Dashboard
A Real-Time BI Project Using Python, PostgreSQL & Power BI

Python PostgreSQL Power BI License

🚀 Overview
This project showcases a real-time Business Intelligence pipeline for the cryptocurrency market. It uses the CoinMarketCap API to pull live data, a Python ETL script to process it, stores the results in a PostgreSQL database, and visualizes them using Power BI.

🧰 Tech Stack
Tool	Purpose
Python	ETL Script (requests, pandas)
PostgreSQL	Data Storage
Power BI	Dashboard Visualizations
Task Scheduler	Automation
📂 Folder Structure
crypto-market-intelligence/
├── config/                  # .env file (API + DB settings)
├── scripts/                 # ETL script
├── powerbi/                 # Power BI dashboard (.pbix)
├── etl_logs/                # Auto-generated logs
├── run_etl.bat              # Batch script for automation
├── requirements.txt         # Python dependencies
├── .gitignore
├── README.md
└── LICENSE
⚙️ ETL Process
Extract live market data from CoinMarketCap API
Transform it using pandas (e.g., clean, select fields)
Load it into a PostgreSQL table called crypto_listings_latest
response = requests.get(api_url, headers=headers, params=params)
data = response.json()['data']
# transform, connect to DB, insert rows...
✅ See full code: scripts/etl_crypto_listings.py

📊 Power BI Dashboard Highlights
Visualizations Include:

🔝 Bar chart: Top 10 coins by Market Cap
🧁 Donut chart: Market Dominance
💡 KPI Cards: Total Volume, Average % Change, Top Coin
📋 Conditional table: Price & % changes
➕ Green = Gain, ➖ Red = Loss, ⚪ Gray = No change
📈 Key Insights
BTC + ETH dominate over 60% of total market cap
Volatility is common among altcoins with low volume
Price does not always correlate with trading volume
⚡ Setup & Usage
Clone the repo:

git clone https://github.com/yourusername/crypto-market-intelligence.git
cd crypto-market-intelligence
Create .env in config/:

CMC_API_KEY=your_api_key
DB_NAME=crypto
DB_USER=postgres
DB_PASS=your_password
DB_HOST=localhost
Install dependencies:

pip install -r requirements.txt
Run the ETL:

python scripts/etl_crypto_listings.py
Or automate it with:

run_etl.bat
🔁 Automation
Task Scheduler is used to run run_etl.bat daily.
Logs saved to /etl_logs/etl_log.txt.
📈 Future Enhancements
🔮 Add ML-based trend prediction (e.g., price forecasting)
☁️ Host the dashboard on Power BI Cloud
📬 Add Telegram/email alerts on large market movements
🧑‍💻 Author
Abdulmohimen Elosta
EU Business School — Master's in Business Analytics & Data Science
[📬 LinkedIn](https://github.com/Abdulmohimen/ETLProject)

📄 License
MIT — use freely, credit appreciated.
