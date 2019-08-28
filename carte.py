#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Ce module contient la classe Carte."""

class Carte:
    """Objet gérant les cartes caractérisée par : 
	 		- un id : identifiant de la carte  (Obligatoire à l'initialisation)
			- un nom de fichier (Obligatoire à l'initialisation)
	 		- un dictionnaire fondCarte contenant la carte avec ces lettres
	 		- 2 variables nbLigneCarte & nbColonneCarte permettant de connaitre les bords de la carte
			- un positionCurseur : qui indique sur quelle ligne/colonne ou est le curseur
			 A besoin en entrée de l'id de la carte 
	 """
    
	
    def __init__(self, id, fichier):
        """ Methode qui initialise le constructeur """
        self.id = id
        self.nom = fichier
        self.fondCarte = {}
        self.nbLigneCarte = 0
        self.nbColonneCarte = 0
        self.positionCurseur={"ligne":0,"colonne":0}

    def __repr__(self):
        """ Methode qui retourne le nom de la carte"""
        return "<Carte {}>".format(self.nom)

    def readCarte(self):
        """ Methode qui permet de lire une carte 
            - Alimente le dictionnaire fond de carte 
            - Initialise le position du curseur
            - Défini les bords de la carte
        """
        colonneFondCarte=0
        
        with open('./cartes/'+self.nom, "r") as mapFile:
            ligneFondCarte=0
            ligneCarte = mapFile.readlines()
            
            for i, ligne in enumerate(ligneCarte):
                ligneFondCarte+=1
                         
                for j, elt in enumerate(ligne):
                    colonneFondCarte=j+1
                    self.fondCarte[ligneFondCarte, colonneFondCarte] =elt
                    if elt.upper()=="X":
                        self.positionCurseur["ligne"]=ligneFondCarte
                        self.positionCurseur["colonne"]=colonneFondCarte

            self.nbLigneCarte=ligneFondCarte+1
            self.nbColonneCarte=colonneFondCarte+1
    
    def afficheCarte(self,carteSource):
        """ Methode qui permet d'afficher la carte de la partie """
        for i in range(1,self.nbLigneCarte):
            afficheLigne = ""
            for j in range(1,self.nbColonneCarte):
                if(self.fondCarte[(i,j)]!="\n"):
                    afficheLigne+=self.fondCarte[(i,j)]     
            print("{}".format(afficheLigne))
        self.affichePositionCurseur()

    def affichePositionCurseur(self):
        """ Methode qui permet d'afficher un comentaire sur le positionnement du curseur  """
        print("Votre curseur est positionné en {} ligne et {} colonne".format(self.positionCurseur["ligne"],self.positionCurseur["colonne"]))
  