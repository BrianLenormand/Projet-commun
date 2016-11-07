#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Matrix():

    def __init__(self, lisdelis):
        """
        Constructeur de la classe Matrix,
        param lisdelis : de type list, permettant de faire une matrice avec plusieurs liste
        peut être ajouter une condition qui vérifie bien qu'on essaie de créer une matrice. (meme nb de ligne et meme nb de col)
        """
        self.liste = []
        try :
            for ligne in range (len(lisdelis) -1) :
                if (len(lisdelis[ligne]) != len(lisdelis[ligne+1])):        #Pas le même nombre d'éléments par ligne
                    raise IndexError("La matrice n'a pas le même nombre de ligne")
            self.liste = lisdelis
        except IndexError:
            print("La matrice n'a pas le même nombre de ligne")


    def __len__(self):
        """Redéfini la fonction len() sur une matrice, qui renverra le nombre de ligne"""
        return len(self.liste)

    def nbCol(self):
        """Renvoie le nombre de colonne de la matrice"""
        if (len(self.liste) == 0):
            return 0
        else: 
            return (len(self.liste[0]))

    def nbLin(self):
        """Renvoie le nombre de lignes de la matrice"""
        return (len(self.liste))


    def estCarree(self):
        """Renvoie un True si la matrice est carrée False sinon"""
        if(self.nbLin() == self.nbCol()):
            return True
        else:
            return False

    def estMemeTaille(self, B):
        """Renvoie True si les matrices sont de même taille, False sinon"""
        if (self.nbCol() == B.nbCol() and (self.nbLin() == B.nbLin())):
            return True
        else :
            return False

    def estMultipliable(self, B) :
        """Renvoie True si les matrices sont multipliables, False sinon"""
        if (self.nbCol() == B.nbLin()):
            return True
        else:
            False
        
    def __getitem__(self, indice):
        """
        Permet de récupérer la valeur d'un indice précis dans la matrice
        ex : A[0][0] donnera la valeur du premier élement de la matrice
        A[ligne][colonne]
        """
        return self.liste[indice]
    
    def __repr__(self):
        """
        Affiche la matrice final
        """
        chaine = ""
        for i in range (len(self.liste)):
            chaine += str(self.liste[i])
            chaine += "\n"
        return chaine

    def trace(self):
        """Renvoie la trace de la matrice"""
        trace = 0
        for i in range (len(self.liste)):
            trace += self.liste[i][i]   #On prend que les élements diagonaux
        return trace

    def multiply(self, scalaire):
        """multiplie la matrice par un scalaire"""
        for ligne in range (len(self.liste)) :
            for colonne in range(len(self.liste[0])): #Prend la taille de la première ligne
                self.liste[ligne][colonne] *= scalaire
                
    def sub_x_id(self, scalaire):
        """Enleve un multiple de la matrice I à la matrice considérée
        Auteur : Terrence """
        if(self.estCarree()):
            for ligne in range (len(self.liste)) :
                for colonne in range(len(self.liste[0])): #Prend la taille de lapremière ligne
                    if ligne == colonne :
                        self.liste[ligne][colonne] -= scalaire
        else:
            raise IndexError("La matrice n'est pas carree")

    def __add__(self, matB):
        """Ajouter une matrice terme à terme avec une autre matrice matB"""
        if not isinstance(matB, Matrix):
            raise TypeError ("Erreur : l'addition n'est définie qu'entre deux matrices")
        if (self.estMemeTaille(matB)):
            matrice = []
            for ligne in range (len(self.liste)) :
                li = []
                for colonne in range(len(self.liste[0])): 
                    li.append(self.liste[ligne][colonne] + matB.liste[ligne][colonne])
                matrice.append(li)
            return (Matrix(matrice))
        else:
            raise IndexError ("Erreur : les matrices ne sont pas de la même taille")
                    
                    
        
            
    def identity(self):
        """Renvoie la matrice identite de la matrice"""
        if(self.estCarree()):
            matrice = []
            for colonne in range (self.nbCol()):
                ligne = []
                for li in range (self.nbLin()):
                    if (li == colonne) : #Si on est sur la diagonale
                        ligne.append(1)
                    else :          #Sinon on met un zero
                        ligne.append(0)
                matrice.append(ligne)
            return Matrix(matrice)
        else:
            raise IndexError("La matrice n'est pas carree")

    



        

        
if __name__ == "__main__":
    A = Matrix(([0, 3,5], 
               [5, 0,2],
                [0,5,5]))
    B = Matrix(([0, 3,5], 
               [5, 0,2],
                [0,5,5]))
    print (A)
    A.multiply(5)
    print ("A muliply:") 
    print (A)
    print ("B:")
    print (B) 
    print ("A + B:") 
    print (A+B )
   

