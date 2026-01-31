import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=MarketRiskAnalytics;"
    "Trusted_Connection=yes;"
)

df = pd.read_sql("SELECT TOP 5 * FROM vw_market_risk_metrics", conn)
print(df)
conn.close()