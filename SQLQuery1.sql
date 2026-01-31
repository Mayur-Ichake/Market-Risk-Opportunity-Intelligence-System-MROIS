SELECT
    full_date,
    asset_code,
    close_price,
    LAG(close_price) OVER (PARTITION BY asset_code ORDER BY full_date) AS prev_close,
    ROUND(
        ((close_price - LAG(close_price) OVER (PARTITION BY asset_code ORDER BY full_date))
        / LAG(close_price) OVER (PARTITION BY asset_code ORDER BY full_date)) * 100,
        4
    ) AS daily_return_pct
FROM market_prices;

SELECT * FROM market_prices