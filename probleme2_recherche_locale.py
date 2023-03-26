import random
import math


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
		i = random.randint(0,n*n-1)
		j = random.randint(0,n*n-1)
		if (T[i][j] == 0) :
			T[i][j] = 2
			cpt += 1
	return T


def permutableau(T, i, j) : # on permute comme dans le cours p55
    res = [0] * len(T)
    for k in range(0, i+1):
        res[k] = T[k]
    pos = i
    res[pos] = T[j-1]
    pos += 1
    for k in range(j-2, i-1, -1) :
        res[pos] = T[k]
        pos += 1
    for k in range(j, len(T)) :
        res[k] = T[k]
    return res
    
print (permutableau([1,2,3,4,5,1], 2, 4))

def gen_circuit_aleatoire(n): 
	T = [i for i in range(0,n+1)]
	T.append(0)
	a_permuter = T[1:n+1]
	p = []
	for i in range(n):
		r = len(a_permuter)
		j = random.randint(0, r-1)
		p.append(a_permuter[j])
		a_permuter.pop(j)
	return [0] + p + [0] # 0 = dépôt

def distance(c1,c2) : # ci = (i,j)
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1]) 

def cout_parcours(n, T, parcours):
	sum = 0
	for i in range(n+1):
		sum += distance(parcours[i], parcours[i+1])
	return sum

def algo_compare(n, T, sol): # on compare sol avec les solutions "voisines"
	print("-------------------------------------------")
	print(sol)
	print("-------------------------------------------")
	for i in range(0, n-2):
		for j in range(i+2, n):
			sol2 = permutableau(T, i, j) # sol2 voisine de sol
			print("-------------------------------------------")
			print(sol2)
			print("-------------------------------------------")
			if cout_parcours(n, T, sol2) < cout_parcours(n, T, sol) :
				return algo_compare(n, T, sol2)
	return sol

def algo(n):
	T = initialisation(n)
	return algo_compare(n, T, gen_circuit_aleatoire(n))

		

print(algo(3))