import random
import time
import tracemalloc
import numpy as np
import matplotlib.pyplot as plt
from probleme2_approximation import *
from probleme2_dynamique import *
from probleme2_optiLineraire import optiNbrInt, optiLinDist

nbClientMax = int(input("Nombre maximum de clients : "))


noeuds = []
for z in range(nbClientMax):
	noeuds.append((randint(0, nbClientMax*nbClientMax-1), randint(0, nbClientMax*nbClientMax-1)))
    
#Etude de vitesse d'exécution, de précision des résultats et de mémoire utilisée
	
#Etude avec Approximation
tracemalloc.start()
start_approx = time.perf_counter()
long_approx, v = kruskal(nbClientMax,noeuds)
end_approx = time.perf_counter()
mem_approx_p, mem_approx_q = tracemalloc.get_traced_memory()

	
#Etude avec optimisation linéaire
tracemalloc.start()
start_opti = time.perf_counter()
a,b= optiNbrInt(noeuds)
long_opti = optiLinDist(b)
end_opti = time.perf_counter()
mem_opti_p, mem_opti_q = tracemalloc.get_traced_memory()

	
#Etude avec Programmation Dynamique
tracemalloc.start()
start_dyn = time.perf_counter()
long_dyn, v = probleme2_dynamique(nbClientMax,noeuds)
end_dyn = time.perf_counter()
mem_dyn_p, mem_dyn_q = tracemalloc.get_traced_memory()

"""
#Etude avec Programmation Dynamique avec Changement d'Echelle
tracemalloc.start()
start = time.perf_counter()
methDynamEch.append(change_echelle(tabObjets, pMaxTests, 50))
end = time.perf_counter()
p, q = tracemalloc.get_traced_memory()
memDynamEch.append(q)
tmpsDynamEch.append(end - start)
	
"""


print("Analyse des algorithme :")
print("temps : ")
print("Approximation : " + str(end_approx-start_approx))
print("Optimisation Linéaire : " + str(end_opti-start_opti))
print("Programmation Dynamique : " + str(end_dyn-start_dyn))

print("")
print("Memoire : ")
print("Approximation : " + str(mem_approx_q))
print("Optimisation Linéaire : " + str(mem_opti_q))
print("Programmation Dynamique : " + str(mem_dyn_q))

print("")
print("Resultat : ")
print("Approximation : " + str(long_approx))
print("Optimisation Linéaire : " + str(long_opti))
print("Programmation Dynamique : " + str(long_dyn))


