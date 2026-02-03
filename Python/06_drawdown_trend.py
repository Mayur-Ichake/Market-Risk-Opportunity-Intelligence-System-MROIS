import pandas as pd

df = pd.read_excel("Excel/nifty_bank_gap_risk.xlsx")

# Moving averages
df["ma_20"] = df["Close"].rolling(20).mean()
df["ma_50"] = df["Close"].rolling(50).mean()

# Trend
df["trend"] = df.apply(
    lambda x: "Uptrend" if x["Close"] > x["ma_50"] else "Downtrend",
    axis=1
)

# Drawdown
df["cum_max"] = df["Close"].cummax()
df["drawdown_pct"] = (df["Close"] - df["cum_max"]) / df["cum_max"]

# Save
df.to_excel("Excel/nifty_bank_trend_drawdown.xlsx", index=False)

print("✅ Trend & drawdown calculated")
