# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:14:30 2021

@author: Bruno
"""

class Personne :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        print("Je m'apelle", self.nom, self.prenom)

P1 = Personne("Bob", "Bab")

P1.sePresenter()


#heritage de classe:
class Etudiant(Personne) :
    def __init__(self, nom, prenom):
        #appel du constructeur de la classe parent:
            super().__init__(nom, prenom)
            #ou Personne.__init__(nom,prenom)
            #Pour l'heritage multiple "super" permet un hértage auto des classes mère en cas
            #d'heritage multiple

P2=Etudiant("Mip", "Map")
P2.sePresenter()
