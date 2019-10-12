# -*- coding: UTF-8 -*-
"""
file:Quant016.py
data:2019-10-129:38
author:Grey
des:
"""
import pandas as pd
import statsmodels.stats.anova as anova
from statsmodels.formula.api import ols

PSID = pd.read_csv('data/016/PSID.csv')
model = ols('earnings ~ C(married) + C(educatn)',data=PSID.dropna()).fit()
table2 = anova.anova_lm(model)
print (table2)