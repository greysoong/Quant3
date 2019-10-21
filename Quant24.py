# -*- coding: UTF-8 -*-
"""
file:Quant24.py
data:2019-10-1715:43
author:Grey
des:
"""
import  pandas as pd
from arch.unitroot import  ADF
from statsmodels.tsa import  arima_model

CPI = pd.read_csv('data/024/CPI.csv',index_col='time')

CPI.index=pd.to_datetime(CPI.index)
CPItrain = CPI[3:]
CPItrain = CPItrain.dropna().CPI

model1 = arima_model.ARIMA(CPItrain,order=(1,0,1)).fit()
model1.summary()
model2 = arima_model.ARIMA(CPItrain,order=(1,0,2)).fit()
model2.summary()
