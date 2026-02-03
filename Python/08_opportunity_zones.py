import pandas as pd

df = pd.read_excel("Excel/nifty_bank_trend_drawdown.xlsx")

vol_threshold = df["volatility_21d"].quantile(0.75)

df["zone"] = df.apply(
    lambda x:
        "High-Opportunity"
        if x["volatility_21d"] > vol_threshold and x["trend"] == "Uptrend"
        else
        "High-Risk"
        if x["volatility_21d"] > vol_threshold
        else
        "Normal",
    axis=1
)

df.to_excel("Excel/nifty_bank_opportunity_zones.xlsx", index=False)

print("✅ Opportunity zones identified")
