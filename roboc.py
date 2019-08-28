#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ce fichier contient le code principal du jeu.
	Exécutez-le avec Python pour lancer le jeu : python roboc.py
"""

import os
import re
import sys
from carte import Carte
import pickle


"""
- Etape 1 : Importe les cartes du répertoire ./cartes
- Etape 2 : Présentation des cartes disponibles pour l'utilisateur
- Etape 3 : Boucle pour demander le N° carte souhaité  et effectue le chargement
- Etape 4 : Boucle pour demander un déplacement et calcule/ affiche le déplacement demandé
"""

def lanceRoboc():

    # Etape 1 : Importe les cartes du répertoire ./cartes
    ListMaps={}
    i=0
    PathMaps="./cartes"
    dirs = os.listdir(PathMaps)
    for file in dirs:
        if file.endswith(".txt"):
            i+=1
            ListMaps[i]= file
           

	 # Etape 2 : Présentation des cartes disponibles pour l'utilisateur
    print("Parmis les cartes disponibles ci-dessous ")
    print("N° de la carte - nom de la carte")
    for idCarte, nomCarte in ListMaps.items():
	    print("{} - {}".format(idCarte, nomCarte))


    idCarteSelect = '0'    
    
	 # Etape 3 : Boucle pour demander le N° carte 
	 # - si Q on sort 
	 # - Si c'est un chiffre & qu'il y a une carte en correspondance alors on charge la sauvegarde si elle existe sinon on initialise une nouvelle carte
	 # - 
    while True: 
        mon_codage = ("veuillez sélectionner votre N° de la carte  ou taper Q pour sortir : ")
        idCarteSelect = input(mon_codage)
		  #on quitte le jeux
        if idCarteSelect.upper() == 'Q':
            print("Fermeture du jeux")
            break
        try:
			  # Si la carte existe
            if int(idCarteSelect) in ListMaps.keys():
                print("Vous avez choisi la carte {}".format(ListMaps[int(idCarteSelect)]))
					 #Si sauvegarde exite on la charge
                if os.path.exists("sauvegardePartieCarte-"+idCarteSelect) :
                    with open("sauvegardePartieCarte-"+idCarteSelect, "rb") as fichier:
                        mon_depickler = pickle.Unpickler(fichier)
                        jeux = mon_depickler.load()
                    fichier.close()
                else: 
						  # On initialise la carte et on lit la carte de base
                    jeux=Carte(idCarteSelect,ListMaps[int(idCarteSelect)])
                    jeux.readCarte()
                jeuxInitial=Carte(idCarteSelect,ListMaps[int(idCarteSelect)])
                jeuxInitial.readCarte()
                jeux.afficheCarte(jeuxInitial)


				# Etape 4 : On boucle pour demander un déplacement :
				# - Vérification de la lettre si hors 	OENSQ on redemande un autre déplacement
				# - Si Q on sort 
				# - Si lettre OENS et pas suivant d'un nombre on redemande un autre déplacement
				# - Si tout est Ok alors on calcule le déplacement & on affiche la carte

            while True:
                mv = input("Entrer un déplacement : ")
                regexp = re.compile(r'[OENSQoensq]')
                if regexp.search(mv[0])==None:
                    print("Vous devez entrer en 1ère lettre, une des lettres O ou E ou N ou S ou Q!!!")

                    #on quitte le jeux
                elif mv[0].upper() == 'Q':
                    print("Fermeture du jeux")
                    os._exit(1)

						  # Si lettre non suivi d'un chiffre 
                elif mv[1:].isdigit()==False:
                    print("Vous devez entrer après la lettre un nombre")
                else :   
							#Calcul du déplacement
                    jeux.deplaceJoueur(jeuxInitial,mv)
						  #Affichage de la carte
                    jeux.afficheCarte(jeuxInitial)
                    
                    # Sauvegarde du jeux 
                    with open("sauvegardePartieCarte-"+idCarteSelect, "wb") as savedFile:
                        pickler = pickle.Pickler(savedFile)
                        pickler.dump(jeux)
                    savedFile.close()

            else:
                print("Merci d'entrer un n° entre 1 et {}".format(len(ListMaps.keys())))
        except:
            print("Ce jeux n'autorise que les caractères : Q pour sortir ... et les n° des cartes ...")



lanceRoboc()

