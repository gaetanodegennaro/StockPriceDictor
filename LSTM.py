import pandas as pd
import numpy as np
import tensorflow as tf
import DataAcquisition as ist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.callbacks import EarlyStopping
from datetime import date
from Preprocessing import DataProcessing
import pandas_datareader.data as pdr
import yfinance as fix
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def trainTestAndPredict(startDateForPrediction, dateToPredict, tick, dim_window):
    fix.pdr_override()

    start = "2010-01-01"
    end = str(date.today())
    sc = MinMaxScaler(feature_range=(0, 1))

    alldata = ist.get_data(tick, start_date=start, end_date=end)
    process = DataProcessing("stock_prices.csv", 0.9)

    df = pd.DataFrame(index=alldata.index)

    df['Tick'] = alldata['Close']
    n = df['Tick'].max() * 0.05
    df['ema10'] = pd.DataFrame.ewm(alldata['Close'], span=10).mean()
    df['ema50'] = pd.DataFrame.ewm(alldata['Close'], span=50).mean()
    df.tail(dim_window)
    markers = [idx for idx, close in enumerate(df.tail(dim_window)['Tick']) if
               df.tail(dim_window)['ema10'][idx] - close >= n]
    markers1 = [idx for idx, close in enumerate(df.tail(dim_window)['Tick']) if
                close - df.tail(dim_window)['ema10'][idx] >= n]
    plt.figure()
    plt.plot(df.tail(dim_window)['Tick'],color='blue', marker='.', markerfacecolor='black', markevery=markers1,markersize=14)
    plt.plot(df.tail(dim_window)['Tick'],color='blue', marker='.', markerfacecolor='red', markevery=markers,markersize=14, label='Price')
    plt.plot(df.tail(dim_window)['ema10'], label='EMA 10 days', color='orange')
    plt.plot(df.tail(dim_window)['ema50'], label='EMA 50 days', color='red')
    plt.xticks(rotation=30)
    plt.legend(loc='upper left')
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig("history.png")


    process.generate_test(30)
    process.generate_train(30)

    X_train = sc.fit_transform(process.X_train).reshape((len(process.X_train), 30, 1))
    Y_train = sc.fit_transform(process.Y_train)
    X_test = sc.fit_transform(process.X_test).reshape(len(process.X_test), 30, 1)
    Y_test = sc.fit_transform(process.Y_test)

    model = Sequential()
    model.add(LSTM(units=60, input_shape=(X_train.shape[1], 1), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=40))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation=tf.nn.selu))

    model.compile(optimizer="Adam", loss="mean_squared_error", metrics=['mean_absolute_error', 'mean_squared_error'])

    #early_stop = EarlyStopping(monitor='val_loss', patience=25)
    #history = model.fit(X_train, Y_train, epochs=500, validation_split=0.2, batch_size=30,callbacks=[early_stop])
    history = model.fit(X_train, Y_train, epochs=100, validation_split=0.2, batch_size=30)

    loss, mae, mse = model.evaluate(X_test, Y_test)

    a = ' Adam LSTM over.png'
    b = ' Adam LSTM'

    # stampa di errori MAE e MSE
    def plot_history(storia):
        hist = pd.DataFrame(storia.history)
        hist['epoch'] = storia.epoch

        plt.figure()
        plt.title("Mean Absolute Error " + str(b))
        plt.xlabel('Epoch')
        plt.ylabel('Mean Abs Error')
        plt.plot(hist['epoch'], hist['mean_absolute_error'],
                 label='Train Error')
        plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
                 label='Val Error')
        plt.legend()
        plt.savefig('MAE' + str(a))

        plt.figure()
        plt.title("Mean Squared Error " + str(b))
        plt.xlabel('Epoch')
        plt.ylabel('Mean Square Error')
        plt.plot(hist['epoch'], hist['mean_squared_error'], label='Train Error')
        plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='Val Error')
        plt.legend()
        plt.savefig('MSE' + str(a))

    plot_history(history)

    # stampa punti nello spazio con valori predizioni vs valori reali
    test_predictions = sc.inverse_transform(model.predict(X_test)).flatten()
    Y_test = sc.inverse_transform(Y_test)

    plt.figure()
    plt.title("True Value VS Predicted Value " + str(b))
    plt.scatter(Y_test, test_predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.axis('equal')
    plt.axis('square')
    _ = plt.plot([-10000, 10000], [-10000, 10000])
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig('TrueVSPredicted' + str(a))

    # stampa conteggio errori
    plt.figure()
    plt.title("Error Distribution " + str(b))
    error = test_predictions - Y_test
    plt.hist(error, bins=25)
    plt.xlabel("Prediction Error")
    _ = plt.ylabel("Count")
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig('PredictionError' + str(a))

    Y_train = sc.inverse_transform(Y_train)
    # stampa valore predetto nel test/ valore reale + storia
    plt.figure()
    plt.title("True vs Predicted Test " + str(b))
    plt.plot(test_predictions, label="Predicted")
    plt.plot(Y_test, label="Real")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig('History' + str(a))

    data = pdr.get_data_yahoo(tick, startDateForPrediction, dateToPredict)
    stock = data["Adj Close"]
    thirty_days = []
    for j in range(len(stock) - 30, len(stock)):
        thirty_days.append(stock[j])
    print(thirty_days)
    X_predict = np.array(thirty_days).reshape(-1, 1)
    X_predict = sc.fit_transform(X_predict).reshape(1, 30, 1)
    return sc.inverse_transform(model.predict(X_predict))[0][0]
