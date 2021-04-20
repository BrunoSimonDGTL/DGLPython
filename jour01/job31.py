# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:44:31 2021

@author: Bruno
"""
import random


def arrondie(note):
    q = note // 5
    next_multiple_of_five = (q + 1) * 5
    #print("note:", note, " next:", next_multiple_of_five)
    return next_multiple_of_five if (next_multiple_of_five - note) < 3 else note


def list_arrondie(list_note):
    for i in range(len(list_note)):
        list_note[i] = arrondie(list_note[i])
    return list_note


list_note = []
for i in range(20):
    list_note.append(random.randint(0, 100))

print("note:", list_note)
print("Arrondie:", list_arrondie(list_note))
