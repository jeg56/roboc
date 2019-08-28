#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Ce module contient la classe Carte."""

class Carte:
    """Objet gérant les cartes caractérisée par : 
	 		- un id : identifiant de la carte  
			- un nom de fichier 
	 		- un tableau fondCarte contenant la carte avec ces lettres
	 		- 

			 A besoin en entrée de l'id de la carte 
	 """
    
    def __init__(self, id, fichier):
        self.id = id
        self.nom = fichier
        self.fondCarte = {}
        self.nbLigneCarte = 0
        self.nbColonneCarte = 0
        self.positionCurseur={"ligne":0,"colonne":0}

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def readCarte(self):
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
        for i in range(1,self.nbLigneCarte):
            afficheLigne = ""
            for j in range(1,self.nbColonneCarte):
                if(self.fondCarte[(i,j)]!="\n"):
                    if(carteSource.fondCarte[(i,j)]=="." and self.fondCarte[(i,j)]=="X"):
                        afficheLigne+=carteSource.fondCarte[(i,j)]
                    else:
                        afficheLigne+=self.fondCarte[(i,j)]       
            print("{}".format(afficheLigne))
        self.affichePositionCurseur()

    def affichePositionCurseur(self):
        print("Votre curseur est positionné en {} ligne et {} colonne".format(self.positionCurseur["ligne"],self.positionCurseur["colonne"]))
    
    def verifMurVertical(self,mv,X):
        if (self.positionCurseur["colonne"] + int(mv[1:])>self.nbLigneCarte):
            return 2
        for i in range(0,int(mv[1:])):
            if self.fondCarte[self.positionCurseur["ligne"]+X*(i+1),self.positionCurseur["colonne"]]=="O" :
                return 1
        return 0
    def verifMurHorizontal(self,mv,X):
        
        if (self.positionCurseur["ligne"] +int(mv[1:])>self.nbColonneCarte):
            return 2
        for i in range(0,int(mv[1:])):
            if self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]+X*(i+1)]=="O" :
                return 1
        return 0


    def deplaceJoueur(self,carteSource,mv):
        if mv[0].upper() == 'N':
            print("Déplacement vers le haut de :"+mv[1:])
            resultVerif=self.verifMurVertical(mv,-1);
            if resultVerif ==1: #Si mur
                print("-------- >Pas possible vous rentrez dans un mur ... <-------")
            elif resultVerif==2: #Si hors cadres
                print("-------- >Pas possible vous sortez du cadre... <-------")
            elif self.fondCarte[self.positionCurseur["ligne"]-int(mv[1:]),self.positionCurseur["colonne"]]==" " or self.fondCarte[self.positionCurseur["ligne"]-int(mv[1:]),self.positionCurseur["colonne"]]==".":
                self.fondCarte[self.positionCurseur["ligne"]-int(mv[1:]),self.positionCurseur["colonne"]]="X"
                #cas si on passe une porte 
                if carteSource.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]==".":
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]="." #Remplace la valeur de départ
                else:
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=" "
                self.positionCurseur["ligne"]-=int(mv[1:])
            elif self.fondCarte[self.positionCurseur["ligne"]-int(mv[1:]),self.positionCurseur["colonne"]]=="U": #Si porte de sortie
                print("********* C'est gagné ********* :-)))")
                self.fondCarte[self.positionCurseur["ligne"]-int(mv[1:]),self.positionCurseur["colonne"]]="X"
                if (carteSource.fondCarte[carteSource.positionCurseur["ligne"],carteSource.positionCurseur["colonne"]]=="."):
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]="." #Remplace la valeur de départ
                self.positionCurseur["ligne"]-=int(mv[1:])
        elif mv[0].upper() == 'S':
            print("Déplacement vers le bas de :"+mv[1:])
            # Si on tente de traverser un mur 
            resultVerif=self.verifMurVertical(mv,1)
            if  resultVerif==1: #Si mur
                print("-------- >Pas possible vous rentrez dans un mur ... <-------")  
            elif resultVerif ==2: #Si hors cadres
                print("-------- >Pas possible vous sorter du cadre... <-------")
            # Si on tente de passer une porte ou on avnace normalement 
            elif self.fondCarte[self.positionCurseur["ligne"]+int(mv[1:]),self.positionCurseur["colonne"]]==" " or self.fondCarte[self.positionCurseur["ligne"]+int(mv[1:]),self.positionCurseur["colonne"]]==".":
                self.fondCarte[self.positionCurseur["ligne"]+int(mv[1:]),self.positionCurseur["colonne"]]="X"
                #cas si on passe une porte 
                if carteSource.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]==".":
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]="." #Remplace la valeur de départ
                else:
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=" "
                self.positionCurseur["ligne"]+=int(mv[1:])
            elif self.fondCarte[self.positionCurseur["ligne"]+int(mv[1:]),self.positionCurseur["colonne"]]=="U": #Si porte de sortie
                print("********* C'est gagné ********* :-)))")
                self.fondCarte[self.positionCurseur["ligne"]+int(mv[1:]),self.positionCurseur["colonne"]]="X"
                #cas si on continu et on repart 
                if carteSource.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=="U":
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]="U" #Remplace la valeur de départ
                self.positionCurseur["ligne"]+=int(mv[1:])
        elif mv[0].upper() == 'O':
            print("Déplacement vers la droite de :"+mv[1:])
            resultVerif=self.verifMurHorizontal(mv,-1);

            if resultVerif ==1: #Si mur
                print("-------- >Pas possible vous rentrez dans un mur ... <-------")
            elif resultVerif ==2: #Si hors cadres
                print("-------- >Pas possible vous sortez du cadre... <-------")
            elif self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]-int(mv[1:])]==" " or self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]-int(mv[1:])]==".":
                self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]-int(mv[1:])]="X"
                #cas si on passe une porte 
                if carteSource.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]==".":
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]="." #Remplace la valeur de départ
                elif carteSource.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=="U":
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]="U" #Remplace la valeur de départ
                else:
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=" "
                self.positionCurseur["colonne"]-=int(mv[1:])
            elif self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]-int(mv[1:])]=="U": #Si porte de sortie
                print("********* C'est gagné ********* :-)))")
                self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]-int(mv[1:])]="X"
                self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=" "
                self.positionCurseur["colonne"]-=int(mv[1:])
        elif mv[0].upper() == 'E':
            print("Déplacement vers la gauche de :"+mv[1:])
            resultVerif=self.verifMurHorizontal(mv,1)
            if  resultVerif==1: #Si mur
                print("-------- >Pas possible vous rentrez dans un mur ... <-------")
            elif resultVerif ==2: #Si hors cadres
                print("-------- >Pas possible vous sorter du cadre... <-------")
            elif self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]+int(mv[1:])]==" " or self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]+int(mv[1:])]==".":
                self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]+int(mv[1:])]="X"
                #cas si on passe une porte 
                if carteSource.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]==".":
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]="." #Remplace la valeur de départ
                else:
                    self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=" "
                self.positionCurseur["colonne"]+=int(mv[1:])
            elif self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]+int(mv[1:])]=="U": #Si porte de sortie
                print("********* C'est gagné ********* :-)))")
                self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]+int(mv[1:])]="X"
                self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]]=" "
                self.positionCurseur["colonne"]+=int(mv[1:])
    
   