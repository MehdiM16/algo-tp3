import random
import time
import tracemalloc
import numpy as np
import matplotlib.pyplot as plt
from probleme2_approximation import *
from probleme2_dynamique import *
from probleme2_optiLineraire import optiNbrInt, optiLinDist, distManhattan

def clientLePlusProche(listCli, client):
	"""
		On suppose que client n'est pas présent dans la liste
		client est un tuple (x, y)
		listCli est la liste des clients
	"""
	dist = distManhattan(client, listCli[0])
	res = listCli[0]
	for i in listCli:
		if distManhattan(client, i) < dist:
			dist = distManhattan(client, i)
			res = i
	return i;

def logistiqueReel(listCli, k, taille):
	"""
		k: int -> nombre de serveurs
		listCli: list[clients] -> liste des noeuds (clients)
		taille: int taille de la grille pour calculer le centre de distribution
	"""
	nbCli = len(listCli);
	groupes = []
	for j in range(k):
		groupes.append([(taille/2, taille/2)]) #On ajoute autant de listes que de serveurs disponibles, en introduisant le centre de distribution
		c = listCli[0]
		listCli.remove(c) #On supprime le client de la liste pour pouvoir calculer les plus proches
		for i in range(int(nbCli/k) - 1):
			clientProche = clientLePlusProche(listCli, c)
			groupes[j].append(clientProche)
			listCli.remove(clientProche)
	res = []
	for i in groupes:
		a, b = optiNbrInt(i)
		res.append(optiLinDist(b))
	
	return res
	
###TEST_EXEMPLE
#noeuds = []
#j = 20
#for z in range(j):
	#noeuds.append((randint(0, j*j-1), randint(0, j*j-1)))

#print(logistiqueReel(noeuds, 10, j))
