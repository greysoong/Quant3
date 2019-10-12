# -*- coding: UTF-8 -*-
"""
file:Quant017.py
data:2019-10-1215:47
author:Grey
des:
"""
import pandas as pd
import statsmodels.api as sm

TRD_Index = pd.read_table('data/017/TRD_Index.txt',sep='\t')
SHindex = TRD_Index[TRD_Index.Indexcd==1]
SZindex = TRD_Index[TRD_Index.Indexcd==399106]
SHRet = SHindex.Retindex
SZRet = SZindex.Retindex
SZRet.index = SHRet.index

model = sm.OLS(SHRet,sm.add_constant(SZRet)).fit()
print (model.summary())