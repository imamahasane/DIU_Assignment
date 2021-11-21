# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:32:04 2020

@author: Imam
"""

import pandas as pd
import numpy as np
from scipy import stats

fir = int(input())
se = np.array(input().split())
se = se.astype(np.int)

mean = np.mean(se)
sigma = np.std(se)
medi = np.median(se)
mod = stats.mode(se)

re = stats.norm.interval(0.950004, loc = mean, scale = sigma/np.sqrt(fir))

print("%.1f"%mean)
print("%.1f"%medi)
print("%.0f"%mod[0][0])
print("%.1f"%sigma)
print("%.1f %.1f"%(re[0],re[1]))