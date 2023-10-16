## V1.1 Modification de la methode __afficher() pour un afficher plus propre et rapide
from time import sleep
from copy import deepcopy
import os

class Jeu_de_la_vie:
    '''
    La classe Jeu_de_la_vie represente un classe reproduisant le jeu de la vie de Conway

    Creation d'une instance :
        monInstance = Jeu_de_la_vie()

    attributs d'instance :
        __tableau

    methodes :
        run() qui est la boucle du jeu
        __tour() genere le tableau du tour suivant
        __valeur_case() renvoie la valeur 0 ou 1 de la cellule au coordonnee [i][j]
        __total_voisin() calcul le nombre de cellules vivantes ou morte autour de la cellule de base
        __resultat() renvoie la valeur suivante d'une cellule
        __afficher() affiche le tableau dans un terminal
    '''
    def __init__(self):
        """
        Affecte un tableau à deux dimensions à l’attribut __tableau
        """
        self.__tableau = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    
    def run(self, nb_tours, delai):
        """
        Méthode principale du jeu.

        Fait tourner le jeu de la vie pendant nb_tours.
        Elle rafraichit l’affichage à chaque tour
        et attend delai entre chaque tour.
        """
        for k in range(nb_tours):
            self.__tour()
            self.__afficher()
            sleep(delai)
        
    def __tour(self):
        """
        Met à jour toute les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        nouveau_tableau = deepcopy(self.__tableau)

        for i in range(len(self.__tableau)):
            for j in range(len(self.__tableau[0])):
                total_voisins = self.__total_voisins(i, j)
                nouveau_tableau[i][j] = self.__resultat(self.__tableau[i][j], total_voisins)

        self.__tableau = nouveau_tableau

    def __valeur_case(self, i, j):
        """
        Renvoie la valeur de la case [i][j] ou 0 si la case n’existe pas.
        """
        if 0 <= i < len(self.__tableau) and 0 <= j < len(self.__tableau[0]):
            return self.__tableau[i][j]
        return 0


    def __total_voisins(self, i, j):
        """Renvoie la somme des valeurs des voisins de la case [i][j]."""
        voisins = [
            self.__valeur_case(i-1, j-1), self.__valeur_case(i-1, j), self.__valeur_case(i-1, j+1),
            self.__valeur_case(i, j-1), self.__valeur_case(i, j+1),
            self.__valeur_case(i+1, j-1), self.__valeur_case(i+1, j), self.__valeur_case(i+1, j+1)
        ]
        return sum(voisins)


    def __resultat(self, valeur_case, total_voisins):
        """
        Renvoie la valeur suivante d’une la cellule.
        """
        if valeur_case == 1:
            if total_voisins in (2, 3):
                return 1
            else:
                return 0
        elif valeur_case == 0 and total_voisins == 3:
            return 1
        else:
            return 0
            

    def __afficher(self):
        """Affiche l'état actuel du jeu de la vie."""
        str_tableau = ""
        for ligne in self.__tableau:
            for cellule in ligne:
                str_tableau += str(cellule)
            str_tableau += '\n'
        os.system('cls')
        print(str_tableau)

mon_jeu = Jeu_de_la_vie()
mon_jeu.run(100, 0.2)