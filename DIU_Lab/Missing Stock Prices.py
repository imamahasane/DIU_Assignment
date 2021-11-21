# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:27:59 2020

@author: Imam
"""

import sys
from scipy.interpolate import UnivariateSpline
n = int(sys.stdin.readline())

r_price = []

for i in range(0, n):
    reline = sys.stdin.readline()
    timestamp, price = reline.split("\t")
    r_price.append(price)

in_price = []
miss_price = []
m_price = []

for i in range(0, n):
    if 'Missing' in r_price[i]:
        miss_price.append(i)
    else:
        in_price.append(i)
        m_price.append(float(r_price[i]))

spline = UnivariateSpline(in_price, m_price, s=2)
for i in miss_price:
    print(spline(i))