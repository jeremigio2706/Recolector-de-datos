import time
import yfinance as yf
import pandas as pd
import talib


print('\n' * 2)
# Símbolo de la acción que deseas obtener (por ejemplo, "AAPL" para Apple Inc.)
symbol = input("Introduce el ticker de la accion: ")
timefrme_mayor = input("Introduce el timeframe mayor (1h, 2h, 4h, 1d): ")
timefrme_menor = input("Introduce el timeframe menor (1m, 5m, 15m, 30m): ")
print('\n')
ma_period = 21
ema_period = 50
ma_period_lenta = 200
rsi_period = 14
cant = 0

while cant < 2:
    cant += 1
    # Crear un objeto Ticker con el símbolo de la acción
    ticker = yf.Ticker(symbol)

    if cant == 1:
        periodo = "1y"
        intervalo = timefrme_mayor
        print("-" * 100)
        print("Datos para timeframe mayor")
        print("-" * 100)
        # Obtener los datos históricos de la acción en temporalidad de horas
        data = pd.DataFrame(ticker.history(period=periodo, interval=intervalo))  # 1 mes, intervalo de 5 minutos
        print(data)
        # Eliminar las columnas "Dividends" y "Stock Splits"
        if 'Dividends' in data.columns and 'Stock Splits' in data.columns:
            # Eliminar las columnas
            data = data.drop(['Dividends', 'Stock Splits'], axis=1)

        try:
            # Calcular la media móvil simple de 21 períodos
            data['MA21'] = talib.SMA(data['Close'], ma_period)
        except Exception as e:
            data['MA21'] = e

        try:
            # Calcular la media móvil exponencial de 50 períodos
            data['EMA50'] = talib.EMA(data['Close'], ema_period)
        except Exception as e:
            data['EMA50'] = e

        try:
            # Calcular la media móvil simple de 200 períodos
            data['MA200'] = talib.SMA(data['Close'], ma_period_lenta)
        except Exception as e:
            data['MA200'] = e

        try:
            # Calcular el MACD y su línea de señal utilizando los precios de cierre
            data['MACD'], signal, _ = talib.MACD(data["Close"])
        except Exception as e:
            data['MACD'] = e

        try:
            # Imprimir los valores del Stoch y su línea de señal
            data['STOCH'], lento = talib.STOCH(data["High"], data["Low"], data["Close"])
        except Exception as e:
            data['STOCH'] = e

        try:
            # Calcular el OBV
            data['OBV'] = talib.OBV(data["Close"], data["Volume"])
        except Exception as e:
            data['OBV'] = e

        try:
            # Calcular el CCI
            data['CCI'] = talib.CCI(data["High"], data["Low"], data["Close"])
        except Exception as e:
            data['CCI'] = e

        try:
            # Calcular el RSI
            data['RSI'] = talib.RSI(data['Close'], rsi_period)
        except Exception as e:
            data['RSI'] = e

        data.to_csv(f'Datos temporalidad mayor {intervalo}.csv', index=True)
    elif cant == 2:
        periodo = "50d"
        intervalo = timefrme_menor
        print("-" * 100)
        print("Datos para timeframe menor")
        print("-" * 100)
        # Obtener los datos históricos de la acción en temporalidad de horas
        data = pd.DataFrame(ticker.history(period=periodo, interval=intervalo))  # 1 mes, intervalo de 5 minutos
        print(data)
        # Eliminar las columnas "Dividends" y "Stock Splits"
        if 'Dividends' in data.columns and 'Stock Splits' in data.columns:
            # Eliminar las columnas
            data = data.drop(['Dividends', 'Stock Splits'], axis=1)

        try:
            # Calcular la media móvil simple de 21 períodos
            data['MA21'] = talib.SMA(data['Close'], ma_period)
        except Exception as e:
            data['MA21'] = e

        try:
            # Calcular la media móvil exponencial de 50 períodos
            data['EMA50'] = talib.EMA(data['Close'], ema_period)
        except Exception as e:
            data['EMA50'] = e

        try:
            # Calcular la media móvil simple de 200 períodos
            data['MA200'] = talib.SMA(data['Close'], ma_period_lenta)
        except Exception as e:
            data['MA200'] = e

        try:
            # Calcular el MACD y su línea de señal utilizando los precios de cierre
            data['MACD'], signal, _ = talib.MACD(data["Close"])
        except Exception as e:
            data['MACD'] = e

        try:
            # Imprimir los valores del Stoch y su línea de señal
            data['STOCH'], lento = talib.STOCH(data["High"], data["Low"], data["Close"])
        except Exception as e:
            data['STOCH'] = e

        try:
            # Calcular el OBV
            data['OBV'] = talib.OBV(data["Close"], data["Volume"])
        except Exception as e:
            data['OBV'] = e

        try:
            # Calcular el CCI
            data['CCI'] = talib.CCI(data["High"], data["Low"], data["Close"])
        except Exception as e:
            data['CCI'] = e

        try:
            # Calcular el RSI
            data['RSI'] = talib.RSI(data['Close'], rsi_period)
        except Exception as e:
            data['RSI'] = e

        data.to_csv(f'Datos temporalidad menor {intervalo}.csv', index=True)

    data_ok = data.tail(10)
    #df_json = data_ok.to_json()
    # Imprimir los datos históricos sin las columnas eliminadas

    print(data_ok)

    print("*" * 100)
    time.sleep(5)
print('\n')
print(
    f"A terminado la ejecucion para la accion de {symbol}, utiliza los valores bajo tu responsabilidad \nY recuerda que el trading es una actividadad de alto riesgo\ny puedes perder todo tu capital")
