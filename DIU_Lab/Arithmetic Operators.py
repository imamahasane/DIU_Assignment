# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:47:46 2020

@author: Imam
"""

def summetion(a, b):
    result = a + b
    return result

def difference(a, b):
    result = a - b
    return result

def product(a, b):
    result = a * b
    return result

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
zz = summetion(a, b)
zz2 = difference(a, b)
zz3 = product(a, b)

print(zz)
print(zz2)
print(zz3)
