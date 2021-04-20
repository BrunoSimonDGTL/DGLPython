# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:58:04 2021

@author: Bruno
"""


class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def sePresenter(self):
        print("je m'apelle:", self.prenom, self.nom)

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    def __str__(self):
        return self.prenom + " "+self.nom


if __name__ == "__main__":
    P1 = Personne("Bruno", "Simon")
    P1.sePresenter()

    P2 = Personne("Mip", "Mop")
    P2.sePresenter()

    print(P2.get_nom())
