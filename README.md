# 📊 Market Risk & Opportunity Intelligence System (MROIS)

> **A real‑world, end‑to‑end financial analytics project built to analyze market risk, volatility, gaps, trends, and opportunity zones in Indian equity indices (NIFTY BANK & NIFTY 50).**

This project is designed **not as a tutorial project**, but as a **production‑style analytics system** similar to what is used by:

* Risk analytics teams
* Quant desks
* Market research & trading support teams

---

## 🚀 Why this project exists

Most fresher projects stop at:

* Simple charts
* Basic return calculation
* YouTube‑style datasets

**MROIS goes deeper.**

It answers real market questions:

* How risky is the market *today*?
* Do holidays increase gap risk?
* When is volatility an opportunity vs danger?
* Which stocks are actually driving index movement?

---

## 🧠 Core Problems Solved

✔ Market calendar alignment (holidays & weekends)
✔ Daily return & volatility normalization
✔ Gap‑up / gap‑down risk analysis
✔ Post‑holiday impact measurement
✔ Trend & drawdown detection
✔ Opportunity vs high‑risk zone identification
✔ Index movement attribution using SQL

---


## 🛠️ Tech Stack

* **Python** (Pandas, NumPy)
* **SQL** (analytical joins & attribution logic)
* **Excel** (business outputs)
* **Financial domain logic** (trading calendars, gap risk, drawdowns)

---

## 🗂️ Project Structure

```
Market Risk & Opportunity Intelligence System (MROIS)
│
├── Data/                    # Raw market datasets
│   ├── Nifty 50  companies list
│   ├── NIFTY 50 03-02-2025 to 03-02-2026
│   ├──Nifty Bank   companies list
|   └── NIFTY BANK 03-02-2025 to 03-02-2026
│
├── Excel/                   # Business‑friendly outputs
│   ├── Cleaned price data
│   ├── Indian market calendar
│   ├── Trading‑day‑only dataset
│   └── Analytics outputs
│
├── Python/                  # Data engineering pipelines
│   ├── 01_Trading_Holidays_2026.py
│   ├── 02_clean_nifty_bank_price_data.py
│   └── 03_align_price_with_holidays.py
│
├── Analytics/               # Risk & opportunity analytics
│   ├── 04_returns_volatility.py
│   ├── 05_gap_risk_analysis.py
│   ├── 06_drawdown_trend.py
│   └── 08_opportunity_zones.py
│
├── SQL/                     # Working on SQL
|     └── 07_Market_data.sql   
│  
│
└── Charts/                 # Visualizations Real time Chart
      ├──Nifty 50  Last 30 years Data
      └──Nifty 50 2025-26 Data
```

---

## 🔄 Analytics Pipeline (How data flows)

```
Raw Market Data
   ↓
Data Cleaning & Validation
   ↓
Trading Calendar Alignment
   ↓
Daily Returns & Volatility
   ↓
Gap Risk & Holiday Impact
   ↓
Trend & Drawdown Analysis
   ↓
Opportunity / Risk Zones
   ↓
Index Contribution (SQL)
```

Author-

Name – Mayur Santosh Ichake                  
Email: mayurichake4@gmail.com   
