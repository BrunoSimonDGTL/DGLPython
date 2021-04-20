# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:02:37 2021

@author: Bruno
"""
import random
import regex as re


class StatText:
    def __init__(self, texte):
        self.texte = texte
        self.lMot = []
        self.pLongMot = {}
        self.pPrem = {}
        self.pSuivi = {}

    def extraitMot(self):
        print("Coupe les mots")
        self.lMot = re.findall(r'\w+', self.texte)

    def pourcentMotParLongueur(self):
        print('Pourcent de longueur')
        compteTaille = {}
        for w in self.lMot:
            try:
                compteTaille[len(w)] += 1
            except KeyError:
                compteTaille[len(w)] = 1

        sortedkeys = sorted(compteTaille)
        for k in sortedkeys:
            self.pLongMot[k] = compteTaille[k]/len(self.lMot)

    def pourcentPremiereLettre(self):
        print('Pourcent de 1er lettre')
        comptePrem = {}
        for w in self.lMot:
            try:
                comptePrem[w[0].upper()] += 1
            except KeyError:
                comptePrem[w[0].upper()] = 1

        sortedkeys = sorted(comptePrem, key=str.upper)
        for k in sortedkeys:
            self.pPrem[k] = comptePrem[k]/len(self.lMot)

    def pourcentDeuxiemeLettre(self):
        print("Pourcent d'enchainement de lettre")
        d_suivi = {}

        for w in self.lMot:
            for i in range(len(w)-1):
                c1 = w[0].upper()
                c2 = w[1].upper()
                if c1 not in d_suivi:
                    d_suivi[c1] = {'tot': 0}

                try:
                    d_suivi[c1][c2] += 1
                except KeyError:
                    d_suivi[c1][c2] = 1

                d_suivi[c1]['tot'] += 1

        sortedkeys = sorted(d_suivi, key=str.upper)

        for k in sortedkeys:
            sortedkeys2 = sorted(d_suivi[k], key=str.upper)
            sortedkeys2.remove('tot')
            self.pSuivi[k] = {}
            for k2 in sortedkeys2:
                self.pSuivi[k][k2] = d_suivi[k][k2] / d_suivi[k]['tot']

    def creerUnMot(self):
        lenMot = statOnDic(self.pLongMot)
        #print("\nEcriture d'un mot de longueur:", lenMot)

        mot = statOnDic(self.pPrem)
        #print ("Le mot commence par:", mot)

        for i in range(1, lenMot):
            mot += statOnDic(self.pSuivi[mot[-1]])

        return mot


def statOnDic(dic):
    p = random.random()
    lKeys = list(dic.keys())
    tot = 0.0
    for i in range(0, len(dic)-1):
        tot += dic[lKeys[i]]
        #print(lKeys[i], tot)
        if p <= tot:
            return lKeys[i]
    return lKeys[-1]


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
    print(stat.creerUnMot())
