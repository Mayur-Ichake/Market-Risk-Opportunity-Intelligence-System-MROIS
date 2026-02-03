import pandas as pd
import numpy as np

# Load trading-day-only data
df = pd.read_excel("Excel/nifty_bank_trading_days_only.xlsx")

# Ensure Date type
df["Date"] = pd.to_datetime(df["Date"])

# Daily returns
df["daily_return"] = df["Close"].pct_change()

# Rolling volatility (annualized)
df["volatility_14d"] = df["daily_return"].rolling(14).std() * np.sqrt(252)
df["volatility_21d"] = df["daily_return"].rolling(21).std() * np.sqrt(252)

# Save output
df.to_excel("Excel/nifty_bank_returns_volatility.xlsx", index=False)

print("✅ Daily returns & volatility calculated")
