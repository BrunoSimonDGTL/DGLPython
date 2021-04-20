# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:38:21 2021

@author: Bruno
"""
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

liste_mot = re.findall(r'\w+', contentOfFile)

print("Il y a", len(liste_mot), "mot(s) dans", filename)
