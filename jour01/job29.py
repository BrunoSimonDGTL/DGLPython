# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:13:53 2021

@author: Bruno
"""

def draw_triangle(height):
    print("triangle: ", height)

    for line in range(height-1):
        exterior = height - 1 - line
        interior = (height - 1 - exterior)*2
        print(" " * exterior + "/" + " " * interior + "\\")

    # last line
    print("/" + "_"*(height-1)*2 + "\\")

draw_triangle(1)
draw_triangle(2)
draw_triangle(10)
