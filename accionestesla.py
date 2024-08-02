import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# Definir el símbolo de la acción
simbolo = 'TSLA'

# Obtener datos históricos de Tesla
tesla = yf.Ticker(simbolo)
tesla_stock_data = tesla.history(period='max')

# Ejemplo de datos de ingresos; reemplaza esto con tus datos reales obtenidos por web scraping o una API
# Estos datos deben ser obtenidos de una fuente confiable.
tesla_revenue_data = [
    # Fecha en formato YYYY-MM-DD, Ingresos en formato "$1,000,000"
    ('2023-06-30', '$15,000,000'),
    ('2023-03-31', '$14,500,000'),
    # Agrega más datos según sea necesario
]

# Preparar datos de ingresos
tesla_revenue_dates = [pd.to_datetime(entry[0]) for entry in tesla_revenue_data]  # Convertir fechas a datetime
tesla_revenue_values = [float(entry[1].replace('$', '').replace(',', '')) for entry in tesla_revenue_data]

# Graficar datos de acciones e ingresos
fig, ax1 = plt.subplots()

# Graficar precios de la acción
ax1.set_xlabel('Fecha')
ax1.set_ylabel('Precio de la acción', color='tab:blue')
ax1.plot(tesla_stock_data.index, tesla_stock_data['Close'], color='tab:blue', label='Precio de la acción')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Graficar ingresos
ax2 = ax1.twinx()
ax2.set_ylabel('Ingresos (en millones)', color='tab:green')
ax2.plot(tesla_revenue_dates, tesla_revenue_values, color='tab:green', label='Ingresos')
ax2.tick_params(axis='y', labelcolor='tab:green')

fig.tight_layout()
plt.title('Tesla: Precio de acciones e ingresos')
plt.show()
