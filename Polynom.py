#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################
# Institut Villebon,                       #
# TP Calcul du polynome                    #
# caractéristique d'une matrice            #
# Auteur : TRAN Terrence                   #
# Date de création : 26/09/16               #
# Date de dernire modification : 28/10/16  #
############################################
from Monom import *

class Polynom(Monom):
    """ Classe representant un polynome

    :Attribut coefficients: de type Liste , representant les coefficients du polynome
    héritant de la classe de Monome
    """
    def __init__(self, lst):
        self.lst = lst
        
    def __repr__(self):
        chaine= ""
        for i in range(len(self.lst)):
            chaine += self.lst[i].__repr__()
        return chaine

if __name__ == "__main__":
    m_0 = Monom(0, -3, 1)
    m_2 = Monom(2, -1, 1)
    m_7 = Monom(7, 2, 3)
    poly = Polynom([m_0, m_2, m_7])
    print poly       