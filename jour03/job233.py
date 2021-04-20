# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:48:51 2021

@author: Bruno
"""
#Attrapez les tous

import pandas as pd
import regex as re
import matplotlib.pyplot as plt

liste_mot=[]
filename = "data.txt"
with open(filename, 'r') as f:
    print("Opening", filename)
    liste_mot = re.findall(r'\w+', f.read())
print("liste de mot ok.")


filename = "pokemon.csv"
df = pd.read_csv(filename, sep=';')

df = df['NAME']

print("I want to be the very best :")
for i in df :
    if i.lower() in liste_mot :
        print(i, "used Python! \nIt hurt itself in its confusion!")
        break

#Psyduck it is