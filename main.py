#!/usr/bin/env python3
############################################
# Institut Villebon,                       #
# TP Calcul du polynome                    #
# caractéristique d'une matrice            #
# Auteur : TRAN Terrence                   #
# Date de cration : 05/10/16               #
# Date de dernire modification : 05/10/16  #
############################################
# -*- coding: utf-8 -*-
import os
from Matrix import*
#from Polynom import*
def mult(A, B):
    """Multiplie deux matrices carrées A et B"""
    if (A.estMultipliable(B)):
        matrice = []
        for ligneA in range (A.nbLin()) :
            liste = []
            for i in range (B.nbLin()):
                valeur = 0
                for colonneB in range(B.nbCol()):
                        valeur += A[ligneA][colonneB]*B[colonneB][i]
                liste.append(valeur)   
            matrice.append(liste)
        return Matrix(matrice)
    else:
        raise IndexError("Le nombre de colonne de la première matrice ne correspond pas au nombre de ligne de la deuxième matrice, la multplication est donc impossible")
        
def add(A, B):
    """Renvoie une matrice C qui est l' addition deux matrices A et B """
    if (A.estMemeTaille(B)): #Si les matrices sont de même tailles
        matrice = []
        for ligne in range (len(A.liste)) :
            liste = []
            for colonne in range(len(A.liste[0])):
                liste.append(A[ligne][colonne] + B[ligne][colonne])
            matrice.append(liste)
        return Matrix(matrice)
    else:
        raise IndexError("Les matrices ne sont pas de la même taille")
        


def soust(A, B):
    """Renvoie une matrice C qui est la soustraction de deux matrices  A et B """
    if (A.estMemeTaille(B)): #Si les matrices sont de même tailles
        matrice = []
        for ligne in range (len(A.liste)) :
            liste = []
            for colonne in range(len(A.liste[0])):
                liste.append(A[ligne][colonne] - B[ligne][colonne])
            matrice.append(liste)
        return Matrix(matrice)
    else:
        raise IndexError("Les matrices ne sont pas de la même taille")
        
        
if __name__ == "__main__":
    print("\n---Exemple daddition :---")
    A = Matrix(([1, 3], [5, 0]))
    B = Matrix(([0, 3],[5, 1,2]))
    print("A :")
    print(A)
    print("B :")
    print(B)
    print("A + B = ")
    print(add(A,B))
    
    print("\n---Exemple de produit : ---")
    print("A :")
    print(A)
    print("B :")
    print(B)
    print("A * B = ")
    print(mult(A,B))
