import carte 

"""Ce module contient les méthodes de la classe Carte."""

def verifMurVertical(self,mv,X):
   """ Methode qui permet de vérifier si sur la verticalité il y a un mur après le déplacement
            retourne 2 si le curseur va hors cadre 
            retourne 1 si le curseur est dans le mur 
            retourne 0 si le déplacement est valide
   """
   if (self.positionCurseur["colonne"] + int(mv[1:])>self.nbLigneCarte):
      return 2
   for i in range(0,int(mv[1:])):
      if self.fondCarte[self.positionCurseur["ligne"]+X*(i+1),self.positionCurseur["colonne"]]=="O" :
            return 1
   return 0
   
def verifMurHorizontal(self,mv,X):
   """ Methode qui permet de vérifier si sur l'horizontalité il y a un mur après le déplacement
   retourne 2 si le curseur va hors cadre 
   retourne 1 si le curseur est dans le mur 
   retourne 0 si le déplacement est valide
"""
   if (self.positionCurseur["ligne"] +int(mv[1:])>self.nbColonneCarte):
      return 2
   for i in range(0,int(mv[1:])):
      if self.fondCarte[self.positionCurseur["ligne"],self.positionCurseur["colonne"]+X*(i+1)]=="O" :
            return 1
   return 0

def deplaceJoueur(self,carteSource,mv):
   """ Methode principale : effectue le déplacement demandé avec les controles nécessaire 	   """

   # Gestion des déplacement si c'est par le nord
   if mv[0].upper() == 'N':
      print("Déplacement vers le haut de : "+mv[1:]+" case(s)")
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

   # Gestion des déplacement si c'est par le sud
   elif mv[0].upper() == 'S':
      print("Déplacement vers le bas de : "+mv[1:]+" case(s)")
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


   # Gestion des déplacement si c'est par l'ouest
   elif mv[0].upper() == 'O':
      print("Déplacement vers la droite de : "+mv[1:] +" case(s)")
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


   # Gestion des déplacement si c'est par l'est
   elif mv[0].upper() == 'E':
      print("Déplacement vers la gauche de :"+mv[1:] +" case(s)" )
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


# Reaffectation des méthodes a la class
setattr(carte.Carte,"verifMurVertical",verifMurVertical)
setattr(carte.Carte,"verifMurHorizontal",verifMurHorizontal)
setattr(carte.Carte,"deplaceJoueur",deplaceJoueur)