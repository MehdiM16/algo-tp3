#1)Bornes sup et inf
def borneSup(t, b):
	poids = 0
	sac = [] #sac de tuples
	for i in t:
		v, w = i
		if w + poids <= b:
			sac.append(i)
			poids+= w
		elif poids < b and poids + w > b:
			diff = b - poids
			pourcent = diff/w
			sac.append((v*pourcent, w*pourcent))
			poids+=(w*pourcent)
		else:
			break
	#print(sac)
	return sac

def borneInf(t, b):
	poids = 0
	sac = [] #sac de tuples
	for i in t:
		v, w = i
		if w + poids <= b:
			sac.append(i)
			poids+= w
	return sac	

def borneInfSup(t, b):
	sup = borneSup(t, b)
	inf = borneInf(t, b)
	return (inf, sup)

def calculSac(sac):
	p = 0
	val = 0
	for i in sac:
		v, w = i
		p+= w
		val+= v
	return val, p
	
#2)Séparation et évaluation: STOP, SKIP, BOUND, BRANCH

def StopSkipBoundBranch(t, b, sacInit):
	sacInf, sacSup = borneInfSup(t, b)
	L = calculSac(sacInf)
	vL, wL = L
	U = calculSac(sacSup)
	vU, wU = U
	sacsPossibles = [] #répertorie toutes les solutions possibles
	poids = 0
	sac = sacInit #sac de tuples
	#u = (0, 0)
	if len(sac) > 0:
		u = calculSac(sac)
	else:
		u = (0, 0)
	mem = u
	if len(t) == 0:
		return []
	for i in range(len(t)):
		#print(t[i])
		u = mem
		v, w = t[i]
		y, z = u
		mem = u #mem permet de garder l'état de u en mémoire avant de rajouter l'objet
		u = (y+v, z+w)
		vu, wu = u
		#STOP:
		if wu == wU and vu == vU:
			#print("STOP")
			L = u
			vL, wL = L
			sac.append(t[i])
			sacsPossibles.append(sac)
			break #On a une solution optimale, on sort donc de la boucle
		#SKIP
		elif vu <= vL and wu < b:
			#print("SKIP")
			sac.append(t[i])
			mem = u
			if vu == vL:
				sacsPossibles.append(sac)
			#on itère
            
		#BOUND
		elif vu > vL and wu < b:
			#on met à jour la borne inf et on itère
			#print("BOUND")
			L = u
			vL, wL = L
			mem = u
			sac.append(t[i])
			sacsPossibles.append(sac)
			
		#BRANCH
		else:
			#print("BRANCH")
			cpy = t[:i:]
			sacsPossibles+= StopSkipBoundBranch(cpy, b, [])
			#sacsPossibles+= StopSkipBoundBranch(t[i+1:], b, sac)
			
	return sacsPossibles

def meilleurSac(sacsPossibles):
	if len(sacsPossibles) == 0:
		return (0, 0)
	max = calculSac(sacsPossibles[0])
	vm, wm = max
	for i in sacsPossibles[1:]:
		vi, wi = calculSac(i)
		if vi >= vm:
			max = calculSac(i)
	return max
    
#TODO proposer une version qui gère une pile pour éviter les problèmes de récursion avec Python



# 3) Programmation dynamique

def prog_dynamique(objet, poids_max) :
    n = len(objet)
    m = poids_max
    T = [0 for _ in range(m + 1)]
    for i in range(n) :
        x,y = objet[i]
        for j in range(m,y,-1) :
            T[j] = max(x + T[j-y],T[j])
    #print(T)
    return T[-1]




# 4) Programmation dynamique avec changement d'echelle


def change_echelle(objet, poids_max, mu) : # changement d'echelle
    nvobj = []
    for i in range(len(objet)) :
        nvobj.append((objet[i][0] // mu, objet[i][1]))
    res = prog_dynamique(nvobj, poids_max)
    return res * mu