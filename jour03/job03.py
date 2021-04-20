# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:21:55 2021

@author: Bruno
"""
import regex as re

contentOfFile = None
filename = "data.txt"
with open(filename, 'r') as f:
    print("Opening", filename)
    contentOfFile = f.read()

n = int(input("Donne une longueur de mot à compter:"))

liste_mot = re.findall(r'\w+', contentOfFile)

compteur = 0
for s in liste_mot:
    if n == len(s):
        compteur += 1

print("Il y a", compteur, "mot(s) de longueur", n)
