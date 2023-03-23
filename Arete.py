from Sommet import *

class Arete :

    def __init__(self,a,b) :
        self.client1 = a
        self.client2 = b
        self.distance = self.distance_sommet(a,b)


    def __str__(self) -> str:
        return f'Sommet a = {self.client1} ... Sommet b = {self.client2} ... distance = {self.distance}'




    def distance_sommet(self,c1,c2) : # ci = Client
        return abs(c2.posx-c1.posx) + abs(c2.posy-c1.posy) 