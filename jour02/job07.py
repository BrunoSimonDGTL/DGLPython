# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:46:52 2021

@author: Bruno
"""
#import job02
from job01 import Personne


class Biblioteque:
    def __init__(self, nom, catalogue):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre_livre, quantite):
        # test si l'auteur a ecrit le livre:
        # print(auteur.oeuvre)
        if auteur.titreDeLauteur(titre_livre):
            self.catalogue[titre_livre] = quantite
        else:
            print("L'auteur n'a pas ecrit se livre.")

    def inventaire(self):
        print("Bibliotheque:", self.nom, "/", len(self.catalogue), "livre(s)")
        for livre, quantite in self.catalogue.items():
            print(" Livre:", livre, ", quantite:", quantite)

    def louer(self, client, titre_livre):
        if titre_livre in self.catalogue:
            if self.catalogue[titre_livre] != 0:
                print(titre_livre, "loué à", client)
                client.loueUnLivre(titre_livre)
                self.catalogue[titre_livre] -= 1
            else:
                print(titre_livre, "n'est plus en stock")
        else:
            print(titre_livre, "n'est pas dans la biblioteque.")

    def rendreLivres(self, client):
        for livre in client.collection:
            client.rendUnLivre(livre)
            self.catalogue[livre] += 1


class Client (Personne):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.collection = []

    def loueUnLivre(self, titre):
        self.collection.append(titre)

    def rendUnLivre(self, titre):
        self.collection.remove(titre)

    def inventaire(self):
        print(self, "à", len(self.collection), "livres(s):")
        for c in self.collection:
            print(" ", c)

# Test dans le main.py