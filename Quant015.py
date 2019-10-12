# -*- coding: UTF-8 -*-
"""
file:Quant015.py
data:2019-10-119:38
author:Grey
des:
"""
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
SHindex = pd.read_csv('data/015/TRD_Index.csv')

Retindex = SHindex.Retindex

