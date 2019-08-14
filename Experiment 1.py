# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:27:15 2019

@author: Pablo
"""
import pandas as pd
import numpy as np
from scipy import stats
from statistics import mean, stdev
from math import sqrt
"""
Load in the data"""

import os

df = pd.read_csv('C:/Users/Pablo/Desktop/Analyses/python/datasheets/Exp1_Pilot_Spring2019.csv', sep=',', header = 'infer')



#######################################################################%
####                   E3 Experiment 1   (pilot)                   ####
#######################################################################%
####Exp1 Training####
#Look at everything split (by block, test cond, and timing cond)
dflong = pd.melt(df, id_vars=['SubID','TestCond', 'TimingCond'], value_vars = ['B1', 'B2', 'B3', 'B4', 'B5'], value_name = 'accuracy')
describe1 = (dflong.groupby(['TestCond', 'TimingCond']).describe())
#print(dflong.groupby(['TestCond', 'TimingCond']).mean())

#Look at split by block and testing cond
describe2 = (dflong.groupby(['TestCond']).describe())
#print(describe2)

"""#Look at split by block and timing cond"""

"""####Look at learning in test condition (test cond = 2)"""
"""#t-test comparing block 1 and 4"""
B1 = df.loc[df['TestCond'] == 2, 'B1']
B4 = df.loc[df['TestCond'] == 2, 'B4']
print(stats.ttest_rel(B1,B4))
cohens_d = (mean(B1) - mean(B4)) / (sqrt((stdev(B1) ** 2 + stdev(B4) ** 2) / 2))
print(cohens_d)

"""Exp 1 Test"""
"""2x2 between subjects anova to look for interaction"""
exp1testmodel = model = ols('accuracy ~ C(TestCond)*C(TimingCond)', data=dflong['variable'] == 'B5').fit()
anova_table = sm.stats.anova_lm(exp1testmodel, typ=3)
print(anova_table)