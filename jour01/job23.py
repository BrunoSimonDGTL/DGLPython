# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:06:46 2021

@author: Bruno
"""


def draw_rectangle(width, height):
    print('rectangle:', width, height)
    for line in range(0, height):
        print("|", end="")
        for column in range(1, width-1):
            print("-" if line == 0 or line == height-1 else " ", end="")
        print("|")


draw_rectangle(0, 0)
draw_rectangle(2, 2)
draw_rectangle(5, 3)
