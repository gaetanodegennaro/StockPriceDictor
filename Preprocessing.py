import pandas as pd
import numpy as np


class DataProcessing:
    def __init__(self, filename, perc):
        """
        Inizialize attributes of class
        :param filename: name of csv file with data needed
        :type filename: string
        :param perc: percentage to split dataset into train and test set
        :type perc: float
        """
        self.filename = pd.read_csv(filename)
        self.percentage = perc
        self.index = int(self.percentage * len(self.filename))
        self.train_data = self.filename[0: self.index]
        self.test_data = self.filename[self.index:]
        self.train_data_input = []
        self.train_data_output = []
        self.test_data_input = []
        self.test_data_output = []

    def generate_train(self, window):
        """
        Generates training data
        :param window: length of window
        :type window: int
        :return: X_train and Y_train
        """
        for i in range((len(self.train_data) // window) * window - window - 1):
            x = np.array(self.train_data.iloc[i: i + window, 1])
            y = np.array([self.train_data.iloc[i + window + 1, 1]], np.float64)
            self.train_data_input.append(x)
            self.train_data_output.append(y)
        self.X_train = np.array(self.train_data_input)
        self.Y_train = np.array(self.train_data_output)

    def generate_test(self, window):
        """
        Generates test data
        :param window: Length of window
        :return: X_test and Y_test
        """
        for i in range((len(self.test_data) // window) * window - window - 1):
            x = np.array(self.test_data.iloc[i: i + window, 1])
            y = np.array([self.test_data.iloc[i + window + 1, 1]], np.float64)
            self.test_data_input.append(x)
            self.test_data_output.append(y)
        self.X_test = np.array(self.test_data_input)
        self.Y_test = np.array(self.test_data_output)