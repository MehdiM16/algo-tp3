import random
import time
import tracemalloc
import numpy as np
import matplotlib.pyplot as plt
from probleme2_approximation import *
from probleme2_dynamique import *
from probleme2_optiLineraire import optiNbrInt, optiLinDist

nbClientMax = int(input("Nombre maximum de clients : "))
poidsMax = 100

methApproximation = []
methOptiLin = []
methDynam = []
methDynamEch = []

tmpsApproximation = []
tmpsOptiLin = []
tmpsDynam = []
tmpsDynamEch = []

memApproximation = []
memOptiLin = []
memDynam = []
memDynamEch = []

ratioValues = []

start = 0
end = 0
memstart = 0
memend = 0

x = np.linspace(0, nbClientMax, nbClientMax)

#On effectue nbObjetsMax tests
for j in range(nbClientMax):
	z = random.randint(1, poidsMax)
    
	#Etude de vitesse d'exécution, de précision des résultats et de mémoire utilisée
	
	#Etude avec Approximation
	tracemalloc.start()
	start = time.perf_counter()
	u, v = kruskal(nbClientMax)
	methApproximation.append(u)
	end = time.perf_counter()
	p, q = tracemalloc.get_traced_memory()
	memApproximation.append(q)
	tmpsApproximation.append(end - start)
	
	#Etude avec optimisation linéaire
	tracemalloc.start()
	start = time.perf_counter()
	noeuds = []
	for z in range(nbClientMax):
		noeuds.append((randint(0, 100), randint(0, 100)))
	a, b = optiNbrInt(noeuds)
	methOptiLin.append(optiLinDist(b))
	end = time.perf_counter()
	p, q = tracemalloc.get_traced_memory()
	memOptiLin.append(q)
	tmpsOptiLin.append(end - start)
	
	#Etude avec Programmation Dynamique
	tracemalloc.start()
	start = time.perf_counter()
	u, v = probleme2_dynamique(nbClientMax)
	methDynam.append(u)
	end = time.perf_counter()
	p, q = tracemalloc.get_traced_memory()
	memDynam.append(q)
	tmpsDynam.append(end - start)
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

#Etude de consommation de mémoire

#Tracé des graphes
fig, (ax1, ax2, ax3) = plt.subplots(3)
#ax1.plot(x, tmpsSepEval, label="Sepa_Eval", color="blue", marker="x")
ax1.plot(x, tmpsDynam, label="Dynamique", color="green", marker="+")
ax1.plot(x, tmpsOptiLin, label="Optimisation_Lineaire", color="red", marker=".")
ax1.plot(x, tmpsApproximation, label="Approximation", color="orange", marker="*")

#ax2.plot(x, methSepEval, label="Sepa_Eval", color="blue", marker="x")
ax2.plot(x, methDynam, label="Dynamique", color="green", marker="+")
ax2.plot(x, methOptiLin, label="Optimisation_Lineaire", color="red", marker=".")
ax2.plot(x, methApproximation, label="Approximation", color="orange", marker="*")

#ax3.plot(x, memSepEval, label="Sepa_Eval", color="blue", marker="x")
ax3.plot(x, memDynam, label="Dynamique", color="green", marker="+")
ax3.plot(x, memOptiLin, label="Optimisation_Lineaire", color="red", marker=".")
ax3.plot(x, memApproximation, label="Approximation", color="orange", marker="*")

ax1.set_xlabel("Nombre d'objets")
ax1.set_ylabel("Secondes")

ax2.set_xlabel("Nombre d'objets")
ax2.set_ylabel("Résultat")

ax3.set_xlabel("Nombre d'objets")
ax3.set_ylabel("Peak Memory Usage")

#histo = plt.plot()
#histo.set_xlabel("Nombre d'objets")
#histo.set_ylabel("Ratios")

#counts, bins = np.histogram(ratioValues)
#histo.stairs(counts, bins)

plt.legend()
plt.show()
