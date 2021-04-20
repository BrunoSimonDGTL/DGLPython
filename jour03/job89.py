# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:31:49 2021

@author: Bruno
"""

def factorielle(n):
    if n==0:
        return 1
    else :
        return factorielle(n-1) * n

print(factorielle(4))