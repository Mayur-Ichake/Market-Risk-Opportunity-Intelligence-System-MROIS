import pandas as pd

# Sheet 1: Trading Holidays

trading_holidays = {
    "Sr. No": list(range(1, 17)),
    "Date": [
        "15-Jan-2026", "26-Jan-2026", "03-Mar-2026", "26-Mar-2026",
        "31-Mar-2026", "03-Apr-2026", "14-Apr-2026", "01-May-2026",
        "28-May-2026", "26-Jun-2026", "14-Sep-2026", "02-Oct-2026",
        "20-Oct-2026", "10-Nov-2026", "24-Nov-2026", "25-Dec-2026"
    ],
    "Day": [
        "Thursday", "Monday", "Tuesday", "Thursday", "Tuesday", "Friday",
        "Tuesday", "Friday", "Thursday", "Friday", "Monday", "Friday",
        "Tuesday", "Tuesday", "Tuesday", "Friday"
    ],
    "Description": [
        "Municipal Corporation Election - Maharashtra",
        "Republic Day",
        "Holi",
        "Shri Ram Navami",
        "Shri Mahavir Jayanti",
        "Good Friday",
        "Dr. Baba Saheb Ambedkar Jayanti",
        "Maharashtra Day",
        "Bakri Id",
        "Muharram",
        "Ganesh Chaturthi",
        "Mahatma Gandhi Jayanti",
        "Dussehra",
        "Diwali-Balipratipada",
        "Prakash Gurpurb Sri Guru Nanak Dev",
        "Christmas"
    ]
}

df_trading = pd.DataFrame(trading_holidays)
df_trading["Date"] = pd.to_datetime(df_trading["Date"], format="%d-%b-%Y")


# Sheet 2: Weekend Holidays

weekend_holidays = {
    "Sr. No": [1, 2, 3, 4],
    "Date": ["15-Feb-2026", "21-Mar-2026", "15-Aug-2026", "08-Nov-2026"],
    "Day": ["Sunday", "Saturday", "Saturday", "Sunday"],
    "Description": [
        "Mahashivratri",
        "Id-Ul-Fitr (Ramadan Eid)",
        "Independence Day",
        "Diwali Laxmi Pujan (Muhurat Trading)"
    ],
    "Market Status": [
        "Closed",
        "Closed",
        "Closed",
        "Closed (Muhurat Trading Special Session)"
    ]
}

df_weekend = pd.DataFrame(weekend_holidays)
df_weekend["Date"] = pd.to_datetime(df_weekend["Date"], format="%d-%b-%Y")


# Sheet 3: Market Timings

market_timings = {
    "Session": [
        "Pre-Open Order Entry",
        "Pre-Open Order Close",
        "Regular Market Open",
        "Regular Market Close",
        "Closing Session",
        "Block Deal (Morning)",
        "Block Deal (Afternoon)"
    ],
    "Start Time": [
        "09:00 AM", "09:08 AM", "09:15 AM", "03:30 PM", "03:40 PM", "08:45 AM", "02:05 PM"
    ],
    "End Time": [
        "09:08 AM", "09:09 AM", "—", "—", "04:00 PM", "09:00 AM", "02:20 PM"
    ],
    "Remarks": [
        "Order entry & modification",
        "Random closure in last minute",
        "Normal / Limited Physical Market",
        "Market closes",
        "Price determination",
        "Block Deal Window",
        "Block Deal Window"
    ]
}

df_timings = pd.DataFrame(market_timings)

# Write to Excel (Multi-sheet)

file_name = "Indian_Market_Calendar_2026.xlsx"
with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:
    df_trading.to_excel(writer, sheet_name="Trading_Holidays_2026", index=False)
    df_weekend.to_excel(writer, sheet_name="Weekend_Holidays_2026", index=False)
    df_timings.to_excel(writer, sheet_name="Market_Timings", index=False)

print("Excel file created successfully:", file_name)
