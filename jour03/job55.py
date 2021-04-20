# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:42:58 2021

@author: Bruno
"""
import matplotlib.pyplot as plt
from job34 import *


def pourcentMotPhrases(texte):
    listePhrase = texte.split(sep='.')

    dicCompt = {}
    for phrase in listePhrase:
        try:
            dicCompt[len(phrase.split(' '))] += 1
        except KeyError:
            dicCompt[len(phrase.split(' '))] = 1

    sortedkeys = sorted(dicCompt)
    D = {}
    for k in sortedkeys:
        D[k] = dicCompt[k]/len(listePhrase)

    return D


def creerUnePhrase(stat):
    dicPMot = pourcentMotPhrases(stat.texte)
    lgPhrase = statOnDic(dicPMot)
    print("Phrase de", lgPhrase, "mot")

    phrase = stat.creerUnMot()
    for i in range(1, lgPhrase):
        phrase += " " + stat.creerUnMot()

    return phrase[0].upper() + phrase[1:].lower() + '.'


# -----------------------------------------
if __name__ == "__main__":
    filename = "data.txt"
    texte = None
    with open(filename, 'r') as f:
        print("Opening", filename)
        texte = f.read()

    stat = StatText(texte)
    stat.extraitMot()
    stat.pourcentMotParLongueur()
    stat.pourcentPremiereLettre()
    stat.pourcentDeuxiemeLettre()

    print(creerUnePhrase(stat))

    #pMot = pourcentMotPhrases(texte)

    #plt.bar(range(len(pMot)), [v *100 for v in pMot.values()], align='center')
    #plt.xticks(range(len(pMot)), list(pMot.keys()))

    # plt.show()
