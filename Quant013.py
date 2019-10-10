# -*- coding: UTF-8 -*-
"""
file:Statistical Analysis.py
data:2019-10-0813:08
author:Grey
des:
"""
import pandas as pd
import matplotlib.pyplot as plt

returns = pd.read_csv('data/013/retdata.csv')
#gsyh = returns.gsyh

print (returns.zglt.mean())
