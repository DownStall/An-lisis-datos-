import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos de Tesla
simbolo = 'TSLA'
tesla_data = yf.Ticker(simbolo)
tesla_stock_data = tesla_data.history(period='5y')  # Puedes ajustar el periodo según tus necesidades

# Mostrar las primeras filas para verificar
print(tesla_stock_data.head())


def make_graph(stock_data, title=''):
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Close'], label='Precio de Cierre')
    plt.title(title)
    plt.xlabel('Fecha')
    plt.ylabel('Precio ($)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Llamar a la función para graficar los datos de Tesla
make_graph(tesla_stock_data, title='Precio de las Acciones de Tesla en los Últimos 5 Años')