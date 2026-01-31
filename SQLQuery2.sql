CREATE VIEW vw_market_risk_metrics AS
SELECT
    full_date,
    asset_code,
    open_price,
    high_price,
    low_price,
    close_price,
    volume,
    ROUND(
        ((close_price - LAG(close_price) OVER (PARTITION BY asset_code ORDER BY full_date))
        / LAG(close_price) OVER (PARTITION BY asset_code ORDER BY full_date)) * 100,
        4
    ) AS daily_return_pct,
    ROUND(((high_price - low_price) / open_price) * 100, 4) AS intraday_volatility_pct
FROM market_prices;
