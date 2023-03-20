import Grille
import Random

"""
def initialisation(n) :
    # grille de bool : T[i][j] = 0 s'il n'y a pas de client à cet endroit
    T = []
    clients = []
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
            clients.append((i,j))
    return T, clients



def distance(c1,c2) : # ci = (i,j)
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1]) 
    
def is_solution(n, res, clients) : # res = [(ik,jk) * n+2 fois] avec 1er et dernier arrêt = dépôt
    if (len(res) != n+2) :
        return False
    if (res[0] != (n*n//2, n*n//2) or res[len(res)-1] != (n*n//2, n*n//2)) :
        return False
    if (T[1:len(res)-1] != set(T[1:len(res)-1])) : # on regarde s'il y a des doublons
        return False  
    for c in clients :
        if c not in res : return False
    return True

"""

#PROGRAMMATION DYNAMIQUE

