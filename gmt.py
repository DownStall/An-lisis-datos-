import yfinance as yf
import pandas as pd

# Crear un objeto Ticker para GameStop
gme = yf.Ticker('GME')

# Obtener el historial de precios de las acciones
gme_data = gme.history(period='1y')

# Restablecer el índice del DataFrame
gme_data.reset_index(inplace=True)

# Mostrar las primeras cinco filas del DataFrame
# print(gme_data.head())

gme_financials = gme.financials

# Convertir a DataFrame para manipulación
gme_revenue = gme_financials.loc['Total Revenue'].to_frame()

# Mostrar las últimas cinco filas del DataFrame de ingresos de Tesla
print(gme_revenue.tail())
