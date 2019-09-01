import pandas_datareader.data as pdr
import yfinance as fix
fix.pdr_override()


def get_data(ticker, start_date, end_date):
    """
    Gets historical stock data of given tickers between dates
    :param ticker: company, or companies whose data is to fetched
    :type ticker: string or list of strings
    :param start_date: starting date for stock prices
    :type start_date: string of date "YYYY-mm-dd"
    :param end_date: end date for stock prices
    :type end_date: string of date "YYYY-mm-dd"
    :return: stock_data.csv
    """
    alldata = pdr.get_data_yahoo(ticker, start_date, end_date)
    stock_data = alldata["Adj Close"]
    stock_data.to_csv("stock_prices.csv")
    return alldata

