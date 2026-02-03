import pandas as pd

df = pd.read_excel("Excel/nifty_bank_returns_volatility.xlsx")
df["Date"] = pd.to_datetime(df["Date"])

# Previous close
df["prev_close"] = df["Close"].shift(1)

# Gap %
df["gap_pct"] = (df["Open"] - df["prev_close"]) / df["prev_close"]

# Gap direction
df["gap_type"] = df["gap_pct"].apply(
    lambda x: "Gap Up" if x > 0 else "Gap Down" if x < 0 else "Flat"
)

# Post-holiday detection
df["day_gap"] = df["Date"].diff().dt.days
df["post_holiday"] = df["day_gap"] > 1

# Save
df.to_excel("Excel/nifty_bank_gap_risk.xlsx", index=False)

print("✅ Gap risk & holiday impact analysis done")
