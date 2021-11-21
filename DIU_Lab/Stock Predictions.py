# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:43:53 2020

@author: Imam
"""

import numpy as np



def diff_between_wma_and_sma(price):
    
    sma = np.mean(price)

    weight = np.arange(1, len(price)+1)
    wma = np.dot(price, weight) / weight.sum()
    return wma - sma

def printTransactions(m, k, d, name, owned, prices):
    ans = []
    info = np.array(list(map(diff_between_wma_and_sma, prices)))
    min_info = info.min()
    min_diff_idx = np.where(info == min_info)[0]

    for i, d in enumerate(info):
        if d > 0 and owned[i] > 0:
            ans.append((name[i], 'SELL', str(owned[i])))

    if min_info < 0 and m > 0:
        idx = min_diff_idx[0]
        latest_price = prices[idx][-1]
        amount = int(m / latest_price)
        if amount > 0:
            ans.append((name[idx], 'BUY', str(amount)))

    print(len(ans))
    for a in ans:
        print(' '.join(a))


if __name__ == '__main__':
    tmp = input().strip().split()
    m, k, d = float(tmp[0]), int(tmp[1]), int(tmp[2])
    name, owned, prices = [], [], []
    for _ in range(k):
        tmp = input().strip().split()
        name.append(tmp[0])
        owned.append(int(tmp[1]))
        prices.append(list(map(float, tmp[2:])))

    printTransactions(m, k, d, name, owned, prices)