from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol
import datetime

import pandas as pd

filepath = "/home/jaimevrl/Documents/Finance/stmt.csv"


dataFrame = LoadFile(filepath)
dataFrame['Date'] = pd.to_datetime(dataFrame['Date'])

# print(dataFrame)


# Draw Plot
import matplotlib.pyplot as plt
def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

# plot_df(dataFrame, x=dataFrame.Date, y=dataFrame['Running Bal.'], title='Expense time series')    

import scipy as sp
import scipy.fftpack
import numpy as np

expensesOnly = dataFrame[['Date', 'Running Bal.']].copy()
expensesOnly = expensesOnly.groupby(['Date']).min()
# print(expensesOnly)
idx = pd.date_range(min(expensesOnly.index), max(expensesOnly.index))
expensesOnly = expensesOnly.reindex(idx)
expensesOnly = expensesOnly.fillna(method='ffill')
expenseValues = np.array(expensesOnly['Running Bal.'])
# print(expensesOnly)
fftExpenses = sp.fft.fft(expenseValues)
fftAbs = np.abs(fftExpenses) ** 2
Ntimes = len(expenseValues)
freqs = sp.fft.fftfreq(Ntimes,1/365.0)


# https://towardsdatascience.com/finding-seasonal-trends-in-time-series-data-with-python-ce10c37aa861

from statsmodels.tsa.seasonal import seasonal_decompose

data_orig = expensesOnly

analysis = data_orig.copy()


decompose_result_mult = seasonal_decompose(analysis, model="multiplicative", extrapolate_trend='freq')

trend = decompose_result_mult.trend
seasonal = decompose_result_mult.seasonal
residual = decompose_result_mult.resid

decompose_result_mult.plot()
plt.show()
