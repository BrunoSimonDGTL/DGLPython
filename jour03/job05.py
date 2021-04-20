# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:40:06 2021

@author: Bruno
"""
import string as st
import matplotlib.pyplot as plt


ORDA = ord('A')
ORDZ = ord('Z')
PUNCT = " " + st.punctuation


def isLetter(c):
    return ORDA <= ord(c.upper()) and ord(c.upper()) <= ORDZ
    # return  c not in PUNCT


filename = "data.txt"
contentOfFile = None

with open(filename, 'r') as f:
    print("Opening", filename)
    contentOfFile = f.read()

countLettre = {}

print("Debut du comptage")
for c in contentOfFile:
    if isLetter(c):
        try:
            countLettre[c.upper()] += 1
        except KeyError:
            countLettre[c.upper()] = 1
print("C'est fini")

print(countLettre)

sortedkeys = sorted(countLettre, key=str.upper)
D = {}
for k in sortedkeys:
    D[k] = countLettre[k]

plt.bar(range(len(D)), [v*100.0/len(contentOfFile)
        for v in countLettre.values()], align='center')
plt.xticks(range(len(D)), list(D.keys()))

plt.show()
