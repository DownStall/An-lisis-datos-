import yfinance as yf

# Descargar los datos de acciones de Tesla
tesla_ticker = 'TSLA'
tesla_data = yf.Ticker(tesla_ticker)

# Obtener datos históricos de las acciones
tesla_stock_data = tesla_data.history(period="1y")
print(tesla_stock_data.head())
