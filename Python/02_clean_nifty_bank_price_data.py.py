import pandas as pd

# 1. Load raw data

file_path = "Data/NIFTY BANK 03-02-2025 to 03-02-2026.csv"
price_df = pd.read_csv(file_path)

# 2. Normalize column names
price_df.columns = price_df.columns.str.strip()

# 3. Fix Date column (very important)
if "Date" not in price_df.columns:
    # If date is stored as first column (index-like)
    price_df.rename(columns={price_df.columns[0]: "Date"}, inplace=True)

# Convert Date to datetime
price_df["Date"] = pd.to_datetime(price_df["Date"], errors="coerce")

# 4. Remove bad rows
price_df.dropna(subset=["Date"], inplace=True)
price_df.drop_duplicates(inplace=True)


# 5. Sort by date
price_df.sort_values("Date", inplace=True)

# 6. Reset index
price_df.reset_index(drop=True, inplace=True)

# 7. Save cleaned file
output_file = "clean_nifty_bank_price_2026.xlsx"
price_df.to_excel(output_file, index=False)

print("✅ NIFTY BANK price data cleaned & saved successfully")
