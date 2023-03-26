from Arete import *
from Sommet import *
from random import randint



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



def kruskal(n) : 
    arete = initialisation(n)
    arete.sort(key=lambda article : article.distance)
    len_ar = len(arete)
    res = []
    longueur = 0
    for i in range(len_ar) :
        s1_ref = arete[i].client1.reference
        s2_ref = arete[i].client2.reference
        if (s1_ref != s2_ref) and not arete[i].est_centre_distrib() :
            for j in range(len_ar) :
                if arete[j].client1.reference == s2_ref :
                    arete[j].client1.reference = s1_ref
                if arete[j].client2.reference == s2_ref :
                    arete[j].client2.reference = s1_ref
            res.append(arete[i])
            longueur += arete[i].distance

    # on a l'arbre couvrant minimum entre les clients
    # maintenant on relie le centre de distribution a chaque extremiter ce cette arbre

    for i in range(1,n+1) :
        if nb_iteration(res,i) == 1:
            chemin = find_arete(arete,0,i)
            if chemin is not None :
                res.append(chemin) # au debut les arete sont stocker dans  l'ordre 0 -> 1 , 0 -> 2 etc
                longueur += chemin.distance

    return longueur,res


def find_arete(aretes,a,b) :
    for elt in aretes :
        if (elt.client1.id == a and elt.client2.id == b) or (elt.client1.id == b and elt.client2.id == a) :
            return elt
    return None


def nb_iteration(aretes, sommet) :
    res = 0
    for elt in aretes :
        if elt.client1.id == sommet or elt.client2.id == sommet :
            res += 1
    return res



x,y = kruskal(4)


print("Approximation\n longueur du plus cours chemin = " + str(x))

for elt in y :
    print(str(elt))

