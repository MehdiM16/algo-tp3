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



def kruskal(arete) : 
    arete.sort(key=lambda article : article.distance)
    len_ar = len(arete)
    res = []
    longueur = 0
    for i in range(len_ar) :
        s1_ref = arete[i].client1.reference
        s2_ref = arete[i].client2.reference
        if s1_ref != s2_ref :
            for j in range(len_ar) :
                if arete[j].client1.reference == s2_ref :
                    arete[j].client1.reference = s1_ref
                if arete[j].client2.reference == s2_ref :
                    arete[j].client2.reference = s1_ref
            res.append(arete[i])
            longueur += arete[i].distance

    return longueur,res



ar = initialisation(3)

for elt in ar :
    print(str(elt))

x,y = kruskal(ar)

print("---------------------------- \n longueur du plus cours chemin = " + str(x))

for elt in y :
    print(str(elt))



