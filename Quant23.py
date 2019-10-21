# -*- coding: UTF-8 -*-
"""
file:Quant23.py
data:2019-10-1713:25
author:Grey
des:
"""
from statsmodels.tsa  import stattools
import  pandas as pd
from statsmodels.graphics.tsaplots import *
import matplotlib.pyplot as plt


data = pd.read_table('data/023/TRD_Index.txt',sep='\t',index_col='Trddt')

SHindex = data[data.Indexcd==1]

SHindex.index = pd.to_datetime(SHindex.index)
SHRet = SHindex.Retindex
acfs = stattools.acf(SHRet)
pacfs =stattools.pacf(SHRet)

SHclose = SHindex.Clsindex

plot_acf(SHRet,use_vlines=True,lags=30)
plot_pacf(SHRet,use_vlines=True,lags=30)
plot_acf(SHclose,use_vlines=True,lags=30)
plt.show()