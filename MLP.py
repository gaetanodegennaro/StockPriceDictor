import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.callbacks import EarlyStopping
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import DataAcquisition as ist
from datetime import date
from Preprocessing import DataProcessing
import pandas_datareader.data as pdr
import yfinance as fix
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def trainTestAndPredict(startDateForPrediction, dateToPredict, tick, dim_window):
    fix.pdr_override()

    start = "2005-01-01"
    end = str(date.today())
    sc = MinMaxScaler(feature_range=(0, 1))

    alldata = ist.get_data(tick, start_date=start, end_date=end)
    process = DataProcessing("stock_prices.csv", 0.9)

    process.generate_test(30)
    process.generate_train(30)

    X_train = sc.fit_transform(process.X_train)
    Y_train = sc.fit_transform(process.Y_train)
    X_test = sc.fit_transform(process.X_test)
    Y_test = sc.fit_transform(process.Y_test)

    model = Sequential()
    model.add(Dense(60, activation=tf.nn.selu))
    model.add(Dropout(0.2))
    model.add(Dense(40, activation=tf.nn.selu))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation=tf.nn.selu))

    model.compile(optimizer="Adam", loss="mean_squared_error", metrics=['mean_absolute_error', 'mean_squared_error'])

    history = model.fit(X_train, Y_train, epochs=100, validation_split=0.2, batch_size=30)
    print(model.summary())
    loss, mae, mse = model.evaluate(X_test, Y_test)

    a = 'Adam MLP.png'
    b = 'Adam MLP'

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
        fig = plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig('MSE' + str(a))

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
    _ = plt.plot([-100, 100], [-100, 100])
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
    return 0

