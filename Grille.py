import random
import Client

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
        while(cpt < n) :
            i = random.randint(0,n-1)
            j = random.randint(0,n-1)
            if (self.grille[i][j] == 0) :
                self.grille[i][j] = 2
                cpt += 1
                self.client.append(Client(i,j))



    def distance(c1,c2) : # ci = Client
        return abs(c2.posx-c1.posx) + abs(c2.posy-c1.posY) 