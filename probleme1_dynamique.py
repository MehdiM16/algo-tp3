def sac_a_dos(objet,poids_max) :
    #objet est un tableau de tuple de la forme (vi,wi)
    #vi = valeur de l'objet i
    #wi = poids de l'objet i
    n = len(objet)
    m = poids_max
    T = [[0 for _ in range(m+1)] for _ in range(n)]
    for i in range(n) :
        for j in range(1,m+1) :
            x,y = objet[i] # x = valeur et y = poids
            if y > j :
                T[i][j] = T[i-1][j]
                #normalement pour i = 0 ce cas poserais probleme mais pas en python car T[-1] est possible
            else :
                T[i][j] = max(x + T[i-1][j-y], T[i-1][j])
    print(T)
    return T[-1][-1]


def sac_a_dos_2(objet, poids_max) :
    #avec economie de memoire
    n = len(objet)
    m = poids_max
    T = [0 for _ in range(m + 1)]
    for i in range(n) :
        x,y = objet[i]
        for j in range(m,y,-1) :
            T[j] = max(x + T[j-y],T[j])
    #print(T)
    return T[-1]



def sac_a_dos_3(objet, poids_max, mu) : # changement d'echelle
    nvobj = []
    for i in range(len(objet)) :
        nvobj.append((objet[i][0] // mu, objet[i][1]))
    res = sac_a_dos_2(nvobj, poids_max)
    return res * mu
    
    
# tmp = [(5,2),(22,8),(8,3),(5,4)]
# b = 12
# tmp2 = [(25,2),(20,2),(10,3 )]
# b2 = 5
# print(sac_a_dos(tmp,b))
# print("")
# print(sac_a_dos_2(tmp,b))
# print("")
# print(sac_a_dos_3(tmp,b,4))
