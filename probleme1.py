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
	U = calculSac(sacSup)
	sacsPossibles = [] #répertorie toutes les solutions possibles
	poids = 0
	sac = sacInit #sac de tuples
	u = (0, 0)
	for i in range(len(t)):
		print(t[i])
		v, w = t[i]
		y, z = u
		u = (y+v, z+w)
		#if w + poids <= b:
			#sac.append(t[i])
			#poids+= w
			
		#STOP:
		if U == u:
			print("STOP")
			L = u
			sac.append(t[i])
			sacsPossibles.append(sac)
			break #On a une solution optimale, on sort donc de la boucle
		#SKIP
		elif u <= L:
			print("SKIP")
			sac.append(t[i])
			if u == L:
				sacsPossibles.append(sac)
			#on itère
		#BOUND
		elif u > L and u < U:
			#on met à jour la borne inf et on itère
			print("BOUND")
			L = u
			sac.append(t[i])
			sacsPossibles.append(sac)
			
		#BRANCH
		else:
			print("BRANCH")
			va, po = calculSac(sac)
			sacsPossibles+= StopSkipBoundBranch(t[i + 1:], b - po, sac)
			
	return sacsPossibles

#TODO proposer une version qui gère une pile pour éviter les problèmes de récursion avec Python
