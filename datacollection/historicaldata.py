import yfinance as yf # type: ignore

# Fetch historical stock data
stock_symbol = "RELIANCE.NS"  # Example NSE ticker
data = yf.download(stock_symbol, start="2023-01-01", end="2024-01-01")
data.to_csv("reliance_stock_data.csv", index=True)
print(data.head())