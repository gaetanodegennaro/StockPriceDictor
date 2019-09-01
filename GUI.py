# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import threading
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

import LSTM
import MLP
from MonteCarlo_Simulation import monteCarloSimulation

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 560)
        MainWindow.setFixedSize(750, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label.setObjectName("label")
        self.dateToPredict = QtWidgets.QDateEdit(self.centralwidget)
        self.dateToPredict.setGeometry(QtCore.QRect(130, 40, 110, 22))
        self.dateToPredict.setCalendarPopup(True)
        self.dateToPredict.setObjectName("dateToPredict")
        self.dateToPredict.setMinimumDate(QtCore.QDate.currentDate().addDays(-10))
        self.dateToPredict.setMaximumDate(QtCore.QDate.currentDate().addDays(1))
        self.dateToPredict.setDate(QtCore.QDate.currentDate().addDays(1))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label_2.setObjectName("label_2")
        self.stockPrice = QtWidgets.QComboBox(self.centralwidget)
        self.stockPrice.setGeometry(QtCore.QRect(130, 10, 241, 22))
        self.stockPrice.setObjectName("stockPrice")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.stockPrice.addItem("")
        self.graphicsView = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(125, 160, 761, 371))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 10, 331, 81))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 100, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 161, 16))
        self.label_5.setObjectName("label_5")
        self.predictedLabel = QtWidgets.QLabel(self.centralwidget)
        self.predictedLabel.setGeometry(QtCore.QRect(180, 120, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.predictedLabel.setFont(font)
        self.predictedLabel.setObjectName("predictedLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(450, 120, 91, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(550, 120, 151, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")

        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.showHistoryGraph)
        self.radioButton_2.toggled.connect(self.showMonteCarloGraph)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: self.execute())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showHistoryGraph(self):
        self.graphicsView.setGeometry(QtCore.QRect(125, 160, 761, 371))
        image_path = 'history.png'
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(761, 371, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                         transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
        self.graphicsView.setPixmap(QtGui.QPixmap.fromImage(image_profile))

    def showMonteCarloGraph(self):
        self.graphicsView.setGeometry(QtCore.QRect(65, 160, 761, 371))
        image_path = 'monteCarlo.png'
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(761, 371, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                         transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
        self.graphicsView.setPixmap(QtGui.QPixmap.fromImage(image_profile))

    def getDays(self):
        selectedIndex = self.comboBox.currentIndex()
        if selectedIndex == 0: return 10
        if selectedIndex == 1: return 30
        if selectedIndex == 2: return 90
        if selectedIndex == 3: return 180
        if selectedIndex == 4: return 365
        if selectedIndex == 5: return 1825
        if selectedIndex == 6: return 3650

    def execute(self):
        self.pushButton.setText("Prediction is running")
        self.pushButton.setEnabled(False)
        QtGui.QGuiApplication.processEvents()

        predictedValue = LSTM.trainTestAndPredict(self.dateToPredict.date().addDays(-60).toPyDate(), self.dateToPredict.date().toPyDate(),
                                                  str(self.stockPrice.currentText()).split()[0], self.getDays())

        #predictedValue = MLP.trainTestAndPredict(self.dateToPredict.date().addDays(-60).toPyDate(), self.dateToPredict.date().toPyDate(),
        #                                                str(self.stockPrice.currentText()).split()[0], self.getDays())

        monteCarloSimulation(str(self.stockPrice.currentText()).split()[0])
        self.predictedLabel.setText(str(predictedValue))

        if self.radioButton.isChecked(): self.showHistoryGraph()
        else: self.showMonteCarloGraph()

        self.pushButton.setText("Predict")
        self.pushButton.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock PriceDictor"))
        self.label.setText(_translate("MainWindow", "Date to predict"))
        self.dateToPredict.setDisplayFormat(_translate("MainWindow", "yy/MM/dd"))
        self.label_2.setText(_translate("MainWindow", "Stock Price Title"))
        self.stockPrice.setItemText(0, _translate("MainWindow", "AAPL - Apple inc"))
        self.stockPrice.setItemText(1, _translate("MainWindow", "ABT - Abbott Laboratories"))
        self.stockPrice.setItemText(2, _translate("MainWindow", "ADBE - Adobe Inc"))
        self.stockPrice.setItemText(3, _translate("MainWindow", "AMD - Advanced Micro Devices Inc"))
        self.stockPrice.setItemText(4, _translate("MainWindow", "AMT - American Tower Corp"))
        self.stockPrice.setItemText(5, _translate("MainWindow", "AMZN - Amazon com inc"))
        self.stockPrice.setItemText(6, _translate("MainWindow", "AXP - American Express Co"))
        self.stockPrice.setItemText(7, _translate("MainWindow", "BA - Boeing Co"))
        self.stockPrice.setItemText(8, _translate("MainWindow", "BABA - Alibaba Group"))
        self.stockPrice.setItemText(9, _translate("MainWindow", "BAC - Bank Of America"))
        self.stockPrice.setItemText(10, _translate("MainWindow", "BAMI.MI - Banco BPM S.P.A."))
        self.stockPrice.setItemText(11, _translate("MainWindow", "BTI - British American Tobacco"))
        self.stockPrice.setItemText(12, _translate("MainWindow", "CHL - China Mobile"))
        self.stockPrice.setItemText(13, _translate("MainWindow", "CSCO - Cisco Systems Inc"))
        self.stockPrice.setItemText(14, _translate("MainWindow", "DIS - Walt Disney Company"))
        self.stockPrice.setItemText(15, _translate("MainWindow", "ENEL.MI - Enel S.P.A."))
        self.stockPrice.setItemText(16, _translate("MainWindow", "ENI.MI - Eni S.P.A."))
        self.stockPrice.setItemText(17, _translate("MainWindow", "F - Ford Motor Company"))
        self.stockPrice.setItemText(18, _translate("MainWindow", "FB - Facebook Inc"))
        self.stockPrice.setItemText(19, _translate("MainWindow", "GOOG - Alphabet Inc (Google) Class C"))
        self.stockPrice.setItemText(20, _translate("MainWindow", "GOOGL - Alphabet Inc (Google) Class A"))
        self.stockPrice.setItemText(21, _translate("MainWindow", "HPQ - HP Inc"))
        self.stockPrice.setItemText(22, _translate("MainWindow", "IBM - International Bus Mach Corp"))
        self.stockPrice.setItemText(23, _translate("MainWindow", "INTC - Intel Corp"))
        self.stockPrice.setItemText(24, _translate("MainWindow", "ISP.MI - Intesa Sanpaolo S.P.A."))
        self.stockPrice.setItemText(25, _translate("MainWindow", "JNJ - Johnson & Johnson"))
        self.stockPrice.setItemText(26, _translate("MainWindow", "JUVE.MI - Juventus Football Club S.P.A."))
        self.stockPrice.setItemText(27, _translate("MainWindow", "KO - Coca-Cola Co"))
        self.stockPrice.setItemText(28, _translate("MainWindow", "MA - Mastercard Inc"))
        self.stockPrice.setItemText(29, _translate("MainWindow", "MCD - McDonald\'s Corp"))
        self.stockPrice.setItemText(30, _translate("MainWindow", "MMM - 3M Company"))
        self.stockPrice.setItemText(31, _translate("MainWindow", "MSFT - Microsoft Corp"))
        self.stockPrice.setItemText(32, _translate("MainWindow", "NFLX - Netflix Inc"))
        self.stockPrice.setItemText(33, _translate("MainWindow", "NKE - Nike Inc"))
        self.stockPrice.setItemText(34, _translate("MainWindow", "NVDA - Nvidia Corp"))
        self.stockPrice.setItemText(34, _translate("MainWindow", "OIL - Oil"))
        self.stockPrice.setItemText(35, _translate("MainWindow", "ORCL - Oracle Corp"))
        self.stockPrice.setItemText(36, _translate("MainWindow", "PYPL - PayPal Holdings Inc"))
        self.stockPrice.setItemText(37, _translate("MainWindow", "PM - Philip Morris International Inc"))
        self.stockPrice.setItemText(38, _translate("MainWindow", "PEP - Pepsi Co Inc"))
        self.stockPrice.setItemText(39, _translate("MainWindow", "QCOM - Qualcomm Inc"))
        self.stockPrice.setItemText(40, _translate("MainWindow", "RY - Royal Bank of Canada"))
        self.stockPrice.setItemText(41, _translate("MainWindow", "T - AT&T"))
        self.stockPrice.setItemText(42, _translate("MainWindow", "TIS.MI - Tiscali S.P.A."))
        self.stockPrice.setItemText(43, _translate("MainWindow", "TM - Toyota Motor Corp"))
        self.stockPrice.setItemText(44, _translate("MainWindow", "TIT.MI - Telecom Italia S.P.A."))
        self.stockPrice.setItemText(45, _translate("MainWindow", "TXN - Texas Instruments Inc"))
        self.stockPrice.setItemText(46, _translate("MainWindow", "UCG.MI - UniCredit S.P.A."))
        self.stockPrice.setItemText(47, _translate("MainWindow", "VZ - Verizon Communications"))
        self.pushButton.setText(_translate("MainWindow", "Predict"))
        self.label_5.setText(_translate("MainWindow", "Predicted Value for Tomorrow:"))
        self.predictedLabel.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "Graph:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Past 10 days"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Past 1 month"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Past 3 months"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Past 6 months"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Past 1 year"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Past 5 years"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Past 10 years"))
        self.radioButton.setText(_translate("MainWindow", "History Graph"))
        self.radioButton_2.setText(_translate("MainWindow", "Monte Carlo Simulation"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

