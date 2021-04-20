# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:37:36 2021

@author: Bruno
"""
import regex as re
import matplotlib.pyplot as plt

liste_mot = []
filename = "data.txt"
with open(filename, 'r') as f:
    print("Opening", filename)
    liste_mot = re.findall(r'\w+', f.read())

comptePrem = {}
for w in liste_mot:
    try:
        comptePrem[w[0].upper()] += 1
    except KeyError:
        comptePrem[w[0].upper()] = 1

print(comptePrem)
sortedkeys = sorted(comptePrem, key=str.upper)
D = {}
for k in sortedkeys:
    D[k] = comptePrem[k]

plt.bar(range(len(D)), [v*100.0/len(liste_mot)
        for v in D.values()], align='center')
plt.xticks(range(len(D)), list(D.keys()))

plt.show()
