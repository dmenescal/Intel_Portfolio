# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:45:50 2016

@author: Aditya
"""

# Application of Linear Regression on Yacht Hydrodynamics Data Set
# Data was taken from UCI Machine Learning Repository
# source: https://archive.ics.uci.edu/ml/datasets/Yacht+Hydrodynamics#

import time
import numpy as np
import statsmodels.api as sm
#import matplotlib.pyplot as plt

start = time.time()
train = open("data.txt","r")

data = []
y = []

for i in enumerate(train):
    ls = list(map(float,train.readline().split()))   
    if len(ls)>0: 
        y.append(ls[6])
        data.append(ls[:6])

data = np.array(data)
y = np.array(y)

results = sm.OLS(y, data).fit()

train.close()
print("Time!!: ", time.time()-start)
