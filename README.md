# 📈 Stock Market Intelligence Dashboard  
*A Real-Time BI Project Using Python, PostgreSQL & Power BI*

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Power BI](https://img.shields.io/badge/Power--BI-Dashboard-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

This project showcases a real-time Business Intelligence pipeline for the **stock market**. It uses a stock market API (e.g., Yahoo Finance) to pull live data, a **Python ETL script** to process it, stores the results in a **PostgreSQL** database, and visualizes them using **Power BI**.

---

## 🧰 Tech Stack

| Tool           | Purpose                              |
|----------------|--------------------------------------|
| Python         | ETL Script (`requests`, `pandas`)    |
| PostgreSQL     | Data Storage                         |
| Power BI       | Dashboard Visualizations             |
| Task Scheduler | Automation                           |

---

## 📂 Folder Structure

ETLProject/
├── config/ # .env file (API + DB settings)
├── scripts/ # ETL script(s)
├── powerbi/ # Power BI dashboard (.pbix)
├── etl_logs/ # Auto-generated logs
├── run_etl.bat # Batch script for automation
├── requirements.txt # Python dependencies
├── .gitignore
├── README.md
└── LICENSE

sql
Copy

---

## ⚙️ ETL Process

1. **Extract** live stock market data from Yahoo Finance API (or similar)
2. **Transform** it using pandas (clean, select, calculate % change, etc.)
3. **Load** it into a PostgreSQL table called `stock_listings_latest`


2. Create `.env` in `config/`:
   ```env
   CMC_API_KEY=your_api_key
   DB_NAME=crypto
   DB_USER=postgres
   DB_PASS=your_password
   DB_HOST=localhost
   ```

# transform, connect to DB, insert rows...
```
✅ See full code: scripts/pipeline.py
---

## 📊 Power BI Dashboard Highlights
**Visualizations Include:**

📈 Line/Bar chart: Stock Open vs Close values

🧁 Donut chart: Portfolio allocation by stock

💡 KPI Cards: Total Volume, Highest % Change, Top Performer

📋 Conditional table: Price & % changes
➕ Green = Gain, ➖ Red = Loss, ⚪ Gray = No change
---
## 📈 Key Insights
Instantly spot daily gainers and losers across tracked stocks

Analyze portfolio distribution and exposure

Track trading volumes alongside price trends
---
## 🔁 Automation
Task Scheduler is used to run run_etl.bat daily.

Logs saved to /etl_logs/etl_log.txt.

## 📈 Future Enhancements
🔮 Add ML-based trend prediction (e.g., stock price forecasting)

☁️ Host the dashboard on Power BI Cloud

📬 Add Telegram/email alerts on major stock movements

## 🧑‍💻 Author
Abdulmohimen Elosta
EU Business School — Master's in Business Analytics & Data Science
📬 LinkedIn
