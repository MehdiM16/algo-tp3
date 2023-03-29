from Sommet import *
from Arete import *
from random import randint
import sys
from operator import attrgetter

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


def initialisation(n) :
    sommet = []
    cpt = 0
    a = (n*n)//2
    sommet.append(Sommet(a,a,0))

    while(cpt < n) :
        i = randint(0,(n*n)-1)
        j = randint(0,(n*n)-1)
        sommet.append(Sommet(i,j,cpt+1))
        cpt += 1
    #sommet.append(Sommet(a,a,cpt+1)) # on rajoute un client fictif sur l'emplacement du centre de distribution pour pouvoir faire kruskal

    arete = []

    tmp = len(sommet)
    for i in range(tmp):
        for j in range(i+1,tmp) :
            arete.append(Arete(sommet[i],sommet[j]))

    return arete


def initialisation2(n,T) :
    sommet = []
    cpt = 0
    a = (n*n)//2
    sommet.append(Sommet(a,a,0))

    for elt in T : #T est un tableau de tuple (x,y)
        sommet.append(Sommet(elt[0],elt[1]))    
    #sommet.append(Sommet(a,a,cpt+1)) # on rajoute un client fictif sur l'emplacement du centre de distribution pour pouvoir faire kruskal
    for elt in sommet :
        print(str(elt))
    arete = []

    tmp = len(sommet)
    for i in range(tmp):
        for j in range(i+1,tmp) :
            arete.append(Arete(sommet[i],sommet[j]))

    return arete





def probleme2_dynamique(n,T) :
    #gr = initialisation(n)
    gr = initialisation2(n,T)
    print("taille = " + str(len(gr)) + " --------------------------------------------------------")
    #for elt in gr :
    #    print(str(elt))
    T = dict()

    res = [] # res = chemin parcourus
    longueur = 0 # longueur = longueur du chemin parcourue
    prec = 0
    arete_min = gr[0]
    deja_present = [prec]
    true_suiv = 0
    
    """
    while len(res) < n :
        
        mini = sys.maxsize
        arete_min = Arete(Sommet(0,0),Sommet(n*n*n,n*n*n))

        for i in range(len(gr)) : # on parcours le tableau des distance a partir du dernier point du chemin
            if (gr[i].client1.id == prec or gr[i].client2.id == prec) and gr[i].distance < mini :
                if gr[i].client1.id != prec :
                    suiv = gr[i].client1.id
                else :
                    suiv = gr[i].client2.id
                if suiv not in deja_present :
                    mini = gr[i].distance
                    arete_min = gr[i]
                    true_suiv = suiv
        #print("mini = " + str(mini) + " ++++++++++++++++++++++++++++++++++++")
        res.append(arete_min)
        longueur += arete_min.distance
        if arete_min.client1.id == prec :
            prec = arete_min.client2.id
        else :
            prec = arete_min.client1.id
        deja_present.append(true_suiv)
    """

    while len(res) < n :
        
        mini = sys.maxsize
        arete_min = Arete(Sommet(0,0),Sommet(n*n*n,n*n*n))

        tmp = []

        for i in range(len(gr)) : # on parcours le tableau des distance a partir du dernier point du chemin
            if (gr[i].client1.id == prec or gr[i].client2.id == prec) and gr[i] not in res :
                if gr[i].client1.id != prec :
                    suiv = gr[i].client1.id
                else :
                    suiv = gr[i].client2.id
                tmp.append(gr[i])
        arete_min = min(tmp,key=attrgetter('distance'))
        res.append(arete_min)
        longueur += arete_min.distance
        if arete_min.client1.id == prec :
            prec = arete_min.client2.id
        else :
            prec = arete_min.client1.id
        deja_present.append(true_suiv)



    # on a maintenant parcourus tout les client
    # il nous reste a ajouter le retour au centre de distribution
    arete_min = find_arete(gr,prec,0)
    longueur += arete_min.distance
    res.append(arete_min)

    print("longueur = " + str(longueur) + " **************************************************")

    return longueur,res


def find_arete(arete,i,j) :
    for elt in arete :
        if (elt.client1.id == i and elt.client2.id == j) or (elt.client1.id == j and elt.client2.id == i) : 
            return elt
    return None


#x,y = probleme2_dynamique(4)

#print("Dynamique :\nlongueur du plus cours chemin = " + str(x))

#for elt in y :
#    print(str(elt))

