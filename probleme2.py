import Grille


"""
def initialisation(n) :
    # grille de bool : T[i][j] = 0 s'il n'y a pas de client à cet endroit
    T = []
    for i in range(n*n):
        T.append([])
        for j in range(n*n):
            T[i].append(0)
    T[(n*n)//2][(n*n)//2] = 1 # l'emplacement du dépôt
    cpt = 0
    while(cpt < n) :
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        if (T[i][j] == 0) :
            T[i][j] = 2
            cpt += 1
    return T



def distance(c1,c2) : # ci = (i,j)
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1]) 

"""

#PROGRAMMATION DYNAMIQUE

