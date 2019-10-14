# -*- coding: UTF-8 -*-
"""
file:Quant018.py
data:2019-10-1413:41
author:Grey
des:
"""
import pandas as pd
import ffn

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