# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:28:50 2021

@author: Bruno
"""
from job02 import *
from job07 import *

if __name__ == "__main__":

    A1 = Auteur("Bruno", "Simon")
    # A1.sePresenter()
    A1.ecrireUnLivre("Python for life")
    A1.ecrireUnLivre("Utiliser son clavier")
    # A1.listerOeuvre()

    B1 = Biblioteque("Mille pages", [])
    B1.inventaire()

    B1.acheterLivre(A1, "Python for life", 3)
    B1.inventaire()

    C1 = Client("Bruno", "Simon")

    B1.louer(C1, "Python for life")

    C1.inventaire()
    B1.inventaire()

    B1.rendreLivres(C1)

    C1.inventaire()
    B1.inventaire()
