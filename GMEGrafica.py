import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos de GameStop
simbolo = 'GME'
gamestop_data = yf.Ticker(simbolo)
gamestop_stock_data = gamestop_data.history(period='5y')  # Ajusta el periodo según tus necesidades

# Mostrar las primeras filas para verificar
print(gamestop_stock_data.head())


def make_graph(stock_data, title=''):
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Close'], label='Precio de Cierre')
    plt.title(title)
    plt.xlabel('Fecha')
    plt.ylabel('Precio ($)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Llamar a la función para graficar los datos de GameStop
make_graph(gamestop_stock_data, title='Precio de las Acciones de GameStop en los Últimos 5 Años')
