# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:06:57 2020

@author: Imam
"""

def is_leap(year):
    leap = False

    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0) 
    
