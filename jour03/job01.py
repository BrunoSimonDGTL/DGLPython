# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:10:36 2021

@author: Bruno
"""

chaine = input("Bonjour,\n Ecrit du texte: ")

filename = "output.txt"

with open(filename, "w") as f:
    f.write(chaine)

# open and read the file :
print("Ouverture de", filename)
with open(filename, "r") as f:
    print(f.read())
