# -*- coding: UTF-8 -*-
"""
file:Quant019.py
data:2019-10-1515:54
author:Grey
des:
"""

import pandas as pd
import matplotlib.pyplot as plt

stock = pd.read_table('data/019/stock.txt',sep='\t',index_col='Trddt')
fjgs = stock.ix[stock.Stkcd==600033,'Dretwd']
fjgs.name='fjgs'
zndl=stock.ix[stock.Stkcd==600033,'Dretwd']
zndl.name='zndl'
sykj=stock.ix[stock.Stkcd==600183,'Dretwd']
sykj.name='sykj'
hxyh=stock.ix[stock.Stkcd==600015,'Dretwd']
hxyh.name='sykj'
byjc=stock.ix[stock.Stkcd==600004,'Dretwd']
byjc.name='byjc'
sh_return = pd.concat([byjc,fjgs,hxyh,sykj,zndl],axis=1)
#print (sh_return.head())
sh_return = sh_return.dropna()
cumreturn = (1+sh_return).cumprod
sh_return.plot()
plt.title('Daily Return of 5 Stocks(2014-2015)')
plt.legend(loc='lower center',bbox_to_anchor=(0.5,-0.3),ncol=5,fancybox=Ture,shadow=True)
cumreturn.plot()
plt.title('Cumulative Return of 5 Stocks(2014-2015)')
plt.show()