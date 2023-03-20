from Grille import *
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



def probleme2_dynamique(n) :
    gr = Grille(n)
    T = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n) : # l'indice 0 sera reserver au centre de distribution
        T[0][i+1] = gr.distance_centre(gr.client[i],gr.centre_distrib)
        T[i+1][0] = T[0][i+1]
        #on stocke tout en double pour dimuer le nombre de parcours de tableau ensuite

    for i in range(n) : 
        for j in range(i+1,n) :
            T[i+1][j+1] = gr.distance(gr.client[i],gr.client[j])
            T[j+1][i+1] = T[i+1][j+1]
    #toute les distances entres clients et entre clients et centre de distribution sont maintenant calculer 

    res = [0] # res = chemin parcourus
    longueur = 0 # longueur = longueur du chemin parcourue
    prec = 0
    while len(res) < n+1 :
        mini = min(T[res[-1]])
        ind_mini = T[res[-1]].index(mini) # on recupere l'index de la plus petite valeur  (potentiellement tres couteux je ne sais pas car peut etre plusieur parcours de tableau)
        # A FINIR (ajouter ind_mini a res et mini a longueur et reflechir a une autre methode potentiellement moins couteuse) 
        


