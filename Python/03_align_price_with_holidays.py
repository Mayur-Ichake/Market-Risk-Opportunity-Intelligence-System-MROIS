import pandas as pd


# 1. Load cleaned price data

price_df = pd.read_excel("Excel/clean_nifty_bank_price_2026.xlsx")


# 2. Load trading holidays

holiday_df = pd.read_excel("Excel/Indian_Market_Calendar_2026.xlsx")

# Normalize column names
holiday_df.columns = holiday_df.columns.str.strip()

# Rename Date column safely
if "Date" not in holiday_df.columns:
    holiday_df.rename(columns={holiday_df.columns[0]: "Date"}, inplace=True)

# Convert to datetime
holiday_df["Date"] = pd.to_datetime(holiday_df["Date"], errors="coerce")


# 3. Remove holiday dates from price data

price_df["Date"] = pd.to_datetime(price_df["Date"])

filtered_price_df = price_df[
    ~price_df["Date"].isin(holiday_df["Date"])
]


# 4. Sort & reset index

filtered_price_df.sort_values("Date", inplace=True)
filtered_price_df.reset_index(drop=True, inplace=True)


# 5. Save final trading-day-only data

filtered_price_df.to_excel(
    "nifty_bank_trading_days_only.xlsx",
    index=False
)

print("✅ Holidays removed. Trading-day data ready.")
