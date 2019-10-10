# -*- coding: UTF-8 -*-
"""
file:Quant014.py
data:2019-10-109:12
author:Grey
des:
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

TRD_Index = pd.read_table('data/014/TRD_Index.txt',sep='\t')


SHindex = TRD_Index[TRD_Index.Indexcd==1]
SZindex = TRD_Index[TRD_Index.Indexcd==399106]

plt.scatter(SHindex.Retindex,SZindex.Retindex)
plt.xlabel('SH')
plt.ylabel('SZ')

SZindex.index = SHindex.index
print (SZindex.Retindex.corr(SHindex.Retindex))