from pulp import *

noeudsInit = [(2, 2), (1, 1), (3, 1), (4, 3), (2, 4), (0, 3)]
n2 = [(1, 1), (4, 1), (5, 3), (1, 5), (0, 6), (4, 5)]

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
	
def optiNbrInt(N):
	n = len(N)
	x = {
			i:{
				j:LpVariable('x_'+str(i)+'_'+str(j), lowBound = 0, cat = LpInteger)for j in range(n) if j!=i
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
	#probleme+= ((u[i] - u[j] + (x[i][j]*(n-1)) <= (n-2)) for i in range(n) for j in range(n) if i >= 2 and i!=j)
	
	e = lpSum(distManhattan(N[i], N[j]) * x[i][j] for i in range(n) for j in range(n) if i!=j)
	fonction_obj = LpAffineExpression(e)
	probleme.setObjective(fonction_obj)
	
	solver = PULP_CBC_CMD(timeLimit = 30, msg = True)
	probleme.solve(solver = solver)
	
	#[print("x_"+str(i)+"_"+str(j)+" = " + str(value(x[i][j]))) for i in range(n) for j in range(n) if i != j]
	dist = []
	for i in range(n):
		for j in range(n):
			if i!=j:
				if int(value(x[i][j])) == 1:
					dist.append((N[i], N[j]))
	
	return ["x_"+str(i)+"_"+str(j)+" = " + str(value(x[i][j])) for i in range(n) for j in range(n) if i != j], dist
	
	
def optiLinDist(tab):
	count = 0;
	for i in tab:
		u, v = i
		count+= distManhattan(u, v)
	return count
	
a, b = optiNbrInt(n2)
print(optiLinDist(b))

