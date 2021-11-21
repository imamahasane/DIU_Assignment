# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:29:01 2020

@author: Imam
"""

import pandas as pd
from scipy.interpolate import interp1d

imm = pd.read_csv('trainingdata.txt', sep=',',header=None)
imm.columns = ['In','Out']
imm_sorted = imm.sort_values(by='In', ascending=True)
f = interp1d(imm_sorted.In,imm_sorted.Out)

if __name__ == '__main__':
    timeCharged = float(input())
    print(f(timeCharged))