# -*- coding: UTF-8 -*-
"""
file:Quant026.py
data:2019-10-219:50
author:Grey
des:
"""
import  pandas as pd
import  numpy as np
from arch.unitroot import  ADF
import  matplotlib.pyplot as plt

sh = pd.read_csv('data/026/sh50p.csv',index_col='Trddt')
sh.index = pd.to_datetime(sh.index)
formStart = '2014-01-01'
formEnd = '2015-01-01'

shform=sh[formStart:formEnd]

PAf=shform['601988']
PBf=shform['600050']
pairf=pd.concat([PAf,PBf],axis=1)

def SSD(priceX,priceY):
    if priceX is None or priceY is None:
        print('缺少价格序列')
    returnX = (priceX-priceX.shift(1))/priceX.shift(1)[1:]
    returnY = (priceY-priceY.shift(1))/priceY.shift(1)[1:]
    standardX = (returnX+1).cumprod()
    standardY = (returnY+1).cumprod()
    SSD=np.sum((standardX-standardY)**2)
    return (SSD)

dis = SSD(PAf,PBf)

PAflog = np.log(PAf)
adfA = ADF(PAflog)

retA = PAflog.diff()[1:]
adfretA = ADF(retA)

PBflog=np.log(PBf)
adfB = ADF(PBflog)

retB = PBflog.diff()[1:]
adfretB = ADF(retB)

fig,axes=plt.subplots(nrows=1,ncols=2)
ax1,ax2=axes.ravel()
PAflog.plot(ax=ax1,label='601988ZGYH',style='--')
PBflog.plot(ax=ax1,label='600050ZGLT',style='-')

retA.plot(ax=ax2,label='601988ZGYH')
retB.plot(ax=ax2,label='600050ZGLT')
plt.legend(loc='lower left')
plt.title('shouyilv')
plt.show()