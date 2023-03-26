from pulp import *

nInit = 5
#grilleInit = nInit*[nInit]
noeudsInit = [(1, 1), (3, 1), (4, 3), (2, 4), (0, 3)]

def distManhattan(x, y):
	i, j = x
	k, l = y
	
	a = k-i
	b = l-j
	if a < 0:
		a = -a
	if b < 0:
		b = -b
	
	return a+b

def fonction(noeuds, x, n): #fonction à minimiser
	somme = 0
	
	for i in range(n):
		for j in range(n):
			if i != j:
				somme+= distManhattan(noeuds[i], noeuds[j]) * x[i][j]
				
	return somme
	
def sumj(x, i): #calcule la somme de la matrice x, excluant les éléments où i=j
	somme = 0
	for j in range(len(x[i])):
		somme+= x[i][j]
	return somme

def sumi(x, j): #calcule la somme de la matrice x, excluant les éléments où i=j
	somme = 0
	for i in range(len(x)):
		somme+= x[i][j]
	return somme

#def optiNbrInt(noeuds, n):
	#x = []
	#for i in range(n):
		#x.append([])
		#for j in range(n):
			#x[i].append(LpVariable('x', lowBound = 0, cat = LpInteger))
			
	#probleme = LpProblem(name="logistique_du_dernier_kilomètre", sense = LpMinimize)
	
	##contraintes 3.19
	#for i in range(n):
		#probleme+=(sumj(x, i) == 1)
		#probleme+=(sumi(x, i) == 1)
	
	#u = []
	#for i in range(n):
		#if i >= 2:
			#u.append(LpVariable('u'))
		#else:
			#u.append(0)
	
	##contraintes 3.21
	#for i in range(2, n):
		#for j in range(n):
			#if i != j:
				#probleme+= (u[i] - u[j] + (x[i][j]*(n-1)) <= (n-2))
	
	#fonction_obj = LpAffineExpression(e = fonction(noeuds, x, n))
	#probleme.setObjective(fonction_obj)
	
	#solver = PULP_CBC_CMD(timeLimit = 30, msg = True)
	#probleme.solve(solver = solver)
	
	#print(f'x = {x.value()}')
	#print(f'u = {u.value()}')
	
def optiNbrInt(noeuds, n):
	x = {
			i:{
				j:LpVariable('x_'+str(i)+'_'+str(j), cat = LpBinary)for j in range(n) if j!=i
			}for i in range(n)# if j!=i
		}
			
	probleme = LpProblem(name="logistique_du_dernier_kilomètre", sense = LpMinimize)
	
	#contraintes 3.19
	for i in range(n):
		probleme+=(lpSum(x[i][j] for j in range(n) if i!=j) == 1)
	for j in range(n):
		probleme+=(lpSum(x[i][j] for i in range(n) if i!=j) == 1)
	
	u = {i:LpVariable('u' + str(i)) for i in range(n) if i >= 2}
	
	#contraintes 3.21
	for i, j in zip(range(n), range(n)):
		if i >= 2 and i!=j:
			probleme+= (u[i] - u[j] + (x[i][j]*(n-1)) <= (n-2))
	
	
	fonction_obj = LpAffineExpression(e = fonction(noeuds, x, n))
	probleme.setObjective(fonction_obj)
	
	solver = PULP_CBC_CMD(timeLimit = 30, msg = True)
	probleme.solve(solver = solver)
	
	print(f'x = {x.values()}')
	print(f'u = {u.values()}')
	
optiNbrInt(noeudsInit, nInit)
