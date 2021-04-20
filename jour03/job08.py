# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:18:17 2021

@author: Bruno
"""
import regex as re
import matplotlib.pyplot as plt

liste_mot = []
filename = "data.txt"
with open(filename, 'r') as f:
    print("Opening", filename)
    liste_mot = re.findall(r'\w+', f.read())


print("Il y a", len(liste_mot), "mot(s) dans", filename)

compteTaille = {}
for w in liste_mot:
    try:
        compteTaille[len(w)] += 1
    except KeyError:
        compteTaille[len(w)] = 1

sortedkeys = sorted(compteTaille)
D = {}
for k in sortedkeys:
    D[k] = compteTaille[k]

plt.bar(range(len(D)), [v*100.0/len(liste_mot)
        for v in D.values()], align='center')
plt.xticks(range(len(D)), list(D.keys()))

plt.show()
