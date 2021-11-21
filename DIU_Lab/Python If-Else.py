#!/bin/python
"""
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
"""

n = int(input())

if n >= 1 and n <= 100:
    if n % 2 != 0:
        print("Weird")
        
    elif n >= 2 and n <= 5:
        if n % 2 == 0:
            print("Not Weird")
            
    elif n >= 6 and n <= 20:
        if n % 2 == 0:
            print("Weird")
            
    elif n > 20:
        if n % 2 == 0:
            print("Not Weird")
