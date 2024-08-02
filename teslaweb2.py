import pandas as pd
import yfinance as yf

tesla = yf.Ticker('TSLA')

# Obtener el historial de ingresos
tesla_financials = tesla.financials

# Convertir a DataFrame para manipulación
tesla_revenue = tesla_financials.loc['Total Revenue'].to_frame()

# Mostrar las últimas cinco filas del DataFrame de ingresos de Tesla
print(tesla_revenue.tail())
