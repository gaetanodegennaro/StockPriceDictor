import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from scipy.stats import norm

def monteCarloSimulation(tick):
    data = pd.DataFrame()

    data[tick] = pdr.DataReader(tick, data_source='yahoo', start='2005-1-1')['Adj Close']
    seq1 = []
    for i in range(len(data)):
        seq1.append(i)

    log_returns = np.log(1 + data.pct_change()) #prende i logaritmi di Adj Close
    data.plot(figsize=(10, 6))
    log_returns.plot(figsize=(10, 6))
    media = log_returns.mean() #calcola la media dei logaritmi
    varianza = log_returns.var() #calcola la varianza dei logaritmi
    #drift è la migliore misura di approssimazione per la Brownian motion (primo valore)
    drift = media - (0.5 * varianza)
    dev_standard = log_returns.std() #calcola la deviazione standard
    np.array(drift)
    ''' se un evento ha il 95% di possibilità di accadere, la distanza tra questo
        evento e la media sarà approssimativamente 1.65 deviazioni standard
        con la funzione norm.pff(x) possiamo ottenere questo valore
        crea un array bi-dimensionale con probabilità random e calcola la distanza di queste dalla media
        Z corrisponde alla distanza tra la media e gli eventi, espressa come il numero di deviazioni standard'''
    #Z = norm.ppf(np.random.rand(10, 2))
    #il valore di Z sarà espresso nella formula di daily_returns in funzione dell'intervallo e delle iterazioni

    intervallo_giorni = 1000 #numero di giorni delle serie da predire
    iterazioni = 10 #numero di serie di predizioni da creare - 10 linee
    #crea un array con le date per il plot
    seq2 = []
    for i in range(len(data), len(data)+1000):
        seq2.append(i)

    #formula r = drift + deviazione standard * e^r
    daily_returns = np.exp(drift.values + dev_standard.values * norm.ppf(np.random.rand(intervallo_giorni, iterazioni)))


    price_list = np.zeros_like(daily_returns) #crea un array con tutti 0 di dimensioni uguali a daily_returns
    S0 = data.iloc[-1] #memorizza in S0 il valore dell'ultima locazione del dataset in modo che le predizioni partano da questo
    price_list[0] = S0 #assegna alla prima riga del nuovo array il valore di S0
    #riempie l'array moltiplicando il prezzo del giorno precedente per il daily_return del giorno corrente
    #crea così un valore casuale vicino a quello del giorno precedente
    for t in range(1, intervallo_giorni):
        price_list[t] = price_list[t - 1] * daily_returns[t]


    plt.figure(figsize=(10, 6))
    plt.plot(seq1[3300:], data[tick][3300:])
    plt.plot(seq2, price_list)
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig("monteCarlo.png")