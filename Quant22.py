# -*- coding: UTF-8 -*-
"""
file:Quant22.py
data:2019-10-179:27
author:Grey
des:
"""
import pandas as pd
import matplotlib.pyplot as plt

Index = pd.read_table('data/022/TRD_Index.txt',sep='\t',index_col='Trddt')
SHindex = Index[Index.Indexcd==1]
Clsindex = SHindex.Clsindex

Clsindex.index = pd.to_datetime(Clsindex.index)

SHindex.index = pd.to_datetime(SHindex.index)

SHindexPart = SHindex['2014-10-09':'2014-10-31']
SHindex2015 = SHindex['2015']
SHindex9End = SHindex['2014-09':'2014']
print ( Clsindex.head())
Clsindex.hist()
plt.show()