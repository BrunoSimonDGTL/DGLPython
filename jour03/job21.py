# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:45:55 2021

@author: Bruno
"""
import regex as re
import matplotlib.pyplot as plt
import numpy as np

liste_mot=[]
filename = "data.txt"
with open(filename, 'r') as f:
    print("Opening", filename)
    liste_mot = re.findall(r'\w+', f.read())

print("Searching:")
d_suivi ={}
for w in liste_mot:
    for i in range(len(w)-1) :
        try:
            d_suivi[w[i:i+2].upper()] += 1
        except KeyError:
            d_suivi[w[i:i+2].upper()] = 1
print("Finished!")


sortedkeys = sorted(d_suivi, key=str.upper)
D={}
for k in sortedkeys :
    D[k] = d_suivi[k]

print(len(D))

#start with A
xlabel={}
legend={}
for key in sortedkeys:
    xlabel[key[1]] = 1
    legend[key[0]] =1

legend =sorted(legend.keys())
xlabel = sorted(xlabel.keys())
value = []

for c0 in legend:
    for c1 in xlabel:
        key = c0+c1
        try :
            value.append(D[key])
        except KeyError :
            value.append(0)
    value = np.array(value)
    plt.scatter(xlabel, value/np.sum(value) * 100.0, label =c0)
    value=[]

plt.legend()
plt.show()





