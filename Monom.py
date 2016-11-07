#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################
# Institut Villebon,                       #
# TP Calcul du polynome                    #
# caractéristique d'une matrice            #
# Auteur : TRAN Terrence                   #
# Date de cration : 26/09/16               #
# Date de dernire modification : 05/10/16  #
############################################

class Monom:
    """ Classe representant un monôme
        Attribut degree : de type int, qui donne le degre du monôme
        Attribut numerator : de type int, qui donne le nombre au numérateur
        Attribut denominator : de type int, qui donne le nombre au dénominateur
    """
    def __init__(self, degree, numerator, denominator):
        """ Constructeur de la classe :
        Param degree : de type int, initialisant le degré du monôme
        Pamam numerator : de type int, initialisant le membre du numérateur
        Param denominator : de type int, initialisant le membre du dénominator
        """
        self.degree = degree
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        """
        Redefinition de la methode __repr__ afin de renvoyer une chaine formaté
        """
        strPoly = ""
        if self.denominator == 0:
            raise ZeroDivisionError("Erreur, vous essayer de diviser par 0 !")
        if float(self.numerator)/float(self.denominator) != 0:   
            if float(self.denominator) == 1 :
                if float(self.numerator)/float(self.denominator) > 0:    #On met le signe
                    strPoly += "+"
                strPoly += str(self.numerator)   #On ajoute le coef. (Si c'est négatif, on a pas besoin de rajouter le signe -)
                if self.numerator == 1:
                    strPoly = strPoly.replace("+1", "+")
                elif self.numerator == -1:
                    strPoly = strPoly.replace("-1", "-")

            elif float(self.denominator) == -1 :
                if float(self.numerator)/float(self.denominator) > 0:    #On met le signe
                    strPoly += "+"
                strPoly += str(self.numerator)   #On ajoute le coef. (Si c'est négatif, on a pas besoin de rajouter le signe -)
                if self.numerator == 1:
                    strPoly = strPoly.replace("1", "-")
                elif self.numerator == -1:
                    strPoly = strPoly.replace("-1", "+")
                    strPoly = strPoly.replace("++", "+")

            else:
                if float(self.numerator)/float(self.denominator) > 0:    #On met le signe
                    strPoly += "+"
                    strPoly += str(self.numerator) +  "/" + str(self.denominator)
                    strPoly = strPoly.replace("-", "")
                else:
                    strPoly += str(self.numerator) +  "/" + str(self.denominator)
        if self.degree != 0:
           strPoly += "x^" + str(self.degree) #On ajoute la puissance de x sauf pour le dernier rang qui est un nombre.
        return strPoly

        
if __name__ == "__main__":        
    m_0 = Monom(0, -3, 1)
    m_2 = Monom(2, -1, 1)
    m_6 = Monom(6, 1, 1)
    m_7 = Monom(7, 2, -3)
    
    print (m_7)
    print (m_6)
    print (m_2)
    print (m_0)
