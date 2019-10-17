# -*- coding: UTF-8 -*-
"""
file:Quant018.py
data:2019-10-1413:41
author:Grey
des:
"""
import pandas as pd
import ffn
from scipy.stats  import norm
import numpy as np
import math
import matplotlib.pyplot as plt

'''
stock = pd.read_csv('data/018/stockszA.csv',index_col = 'Trddt')
Vanke = stock[stock.Stkcd==2]
close = Vanke.Clsprc

close.index = pd.to_datetime(close.index)
close.index.name = 'Date'
lagclose = close.shift(1)
Calclose = pd.DataFrame({'close':close,'lagclose':lagclose})

simpleret = (close-lagclose)/lagclose
simpleret.name = 'simpletet'

calret = pd.merge(Calclose,pd.DataFrame(simpleret),left_index=True,right_index=True)

simpleret2 = (close-close.shift(2))/close.shift(2)
simpleret2.name = 'simpleret2'

calret['simpleret2']=simpleret2

ffnSimpleret = ffn.to_returns(close)
ffnSimpleret.name = 'ffnSimpleret'

print (ffnSimpleret.head())
'''
SAPower = pd.read_csv('data/018/SAPower.csv',index_col='Date')
SAPower.index = pd.to_datetime(SAPower.index)
DalianRP = pd.read_csv('data/018/DalianRP.csv',index_col='Date')
DalianRP.index = pd.to_datetime(DalianRP.index)
returnS = ffn.to_returns(SAPower.Close)
returnD = ffn.to_returns(DalianRP.Close)

def cal_half_dev(returns):
    mu = returns.mean()
    temp = returns[returns<mu]
    half_deviation = (sum((mu-temp)**2)/len(returns))**0.5
    return (half_deviation)

returnS.quantile(0.05)
returnD.quantile(0.05)

#print (norm.ppf(0.05,returnS.mean(),returnS.std()))
#print (norm.ppf(0.05,returnD.mean(),returnD.std()))
def cal_mean(frac):
    return(0.08*frac+0.15*(1-frac))

mean = list(map(cal_mean,[x/50 for x in range(51)]))
sd_mat = np.array([list(map(lambda x:math.sqrt((x**2)*0.12**2+((1-x)**2)*0.25**2+2*x+(1-x)*(-1.5+i*0.5)*0.12*0.25),[x/50 for x in range(51)])) for i in range (1,6)])

plt.plot(sd_mat[0,:],mean,label='-1')
plt.plot(sd_mat[1,:],mean,label='-0.5')
plt.plot(sd_mat[2,:],mean,label='-0')
plt.plot(sd_mat[3,:],mean,label='-0.5')
plt.plot(sd_mat[4,:],mean,label='-1')
plt.legend(loc='upper left')
plt.show()