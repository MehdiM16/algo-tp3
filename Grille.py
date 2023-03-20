from random import randint
from Client import *

class Grille :

    client = []
    grille = []

    def __init__(self,n):
        # grille de bool : T[i][j] = 0 s'il n'y a pas de client à cet endroit
        self.grille = []
        for i in range(n*n):
            self.grille.append([])
            for j in range(n*n):
                self.grille[i].append(0)
        self.grille[(n*n)//2][(n*n)//2] = 1 # l'emplacement du dépôt
        cpt = 0
        a = (n*n)//2
        self.centre_distrib = (a,a)
        self.grille[a][a] = 1 # 1 correspond au centre de distribution
        while(cpt < n) :
            i = randint(0,n-1)
            j = randint(0,n-1)
            if (self.grille[i][j] == 0) :
                self.grille[i][j] = 2 # T[i][j] = 2 signifie qu'il y a un client à cet endroit
                cpt += 1
                self.client.append(Client(i,j))



    def distance(self,c1,c2) : # ci = Client
        return abs(c2.posx-c1.posx) + abs(c2.posy-c1.posy) 
    
    def distance_centre(self,c1,dis) : #dis correspond au centre de distribution qui aura pour valeur un tuple (x,y) qui seront ses coordonné
        return abs(dis[0]-c1.posx) + abs(dis[1]-c1.posy)  
