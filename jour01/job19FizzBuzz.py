# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:55:50 2021

@author: Bruno
"""
for i in range(1, 101):
    isDiv3 = i % 3 == 0
    isDiv5 = i % 5 == 0

    if isDiv3 and isDiv5:
        print("FizzBuzz")
    elif isDiv3:
        print("Fizz")
    elif isDiv5:
        print("Buzz")
    else:
        print(i)
