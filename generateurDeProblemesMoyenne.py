import random
import time
import tracemalloc
import numpy as np
import matplotlib.pyplot as plt
from probleme1 import *
import math
#from probleme1_dynamique import *

nbObjetsMax = int(input("Nombre maximum d'objets : "))
poidsMax = 100
pMaxTests = int(input("Poids maximum d'un sac : "))
valMax = 900
tabObjets = []

methBorneInf = []
methSepEval = []
methDynam = []
methDynamEch = []

tmpsBorneInf = []
tmpsSepEval = []
tmpsDynam = []
tmpsDynamEch = []

memBorneInf = []
memSepEval = []
memDynam = []
memDynamEch = []

ratioValues = []

start = 0
end = 0
memstart = 0
memend = 0

muv = int(input("muv : "))
sigmav = int(input("sigmav : "))
muw = int(input("muw (>= 1): "))
sigmaw = int(input("sigmaw : "))


x = np.linspace(0, nbObjetsMax, nbObjetsMax)

#On effectue nbObjetsMax tests
for j in range(nbObjetsMax):
	y = math.ceil(random.gauss(muv, sigmav))
	z = math.ceil(random.gauss(muw, sigmaw)) + 1
	tabObjets.append((y, z))
	ratioValues.append(y/z)
    
	tabObjets.sort(key=lambda article : article[0]/article[1], reverse=True)
	print("Generating problem with " + str(j) + " objects...");
    
	#Etude de vitesse d'exécution, de précision des résultats et de mémoire utilisée
	
	#Etude avec BorneInf()
	tracemalloc.start()
	start = time.perf_counter()
	u, v = calculSac(borneInf(tabObjets, pMaxTests))
	methBorneInf.append(u)
	end = time.perf_counter()
	p, q = tracemalloc.get_traced_memory()
	memBorneInf.append(q)
	tmpsBorneInf.append(end - start)
	
	#Etude avec Séparation et Evaluation()
	tracemalloc.start()
	start = time.perf_counter()
	v, w = meilleurSac(StopSkipBoundBranch(tabObjets, pMaxTests, [], time.time()))
	end = time.perf_counter()
	p, q = tracemalloc.get_traced_memory()
	memSepEval.append(q)
	tmpsSepEval.append(end - start)
	methSepEval.append(v)
	
	#Etude avec Programmation Dynamique
	tracemalloc.start()
	start = time.perf_counter()
	methDynam.append(prog_dynamique(tabObjets, pMaxTests))
	end = time.perf_counter()
	p, q = tracemalloc.get_traced_memory()
	memDynam.append(q)
	tmpsDynam.append(end - start)
	
	#Etude avec Programmation Dynamique avec Changement d'Echelle
	tracemalloc.start()
	start = time.perf_counter()
	methDynamEch.append(change_echelle(tabObjets, pMaxTests, 50))
	end = time.perf_counter()
	p, q = tracemalloc.get_traced_memory()
	memDynamEch.append(q)
	tmpsDynamEch.append(end - start)

#Etude de consommation de mémoire

#Tracé des graphes
fig, (ax1, ax2, ax3, histo) = plt.subplots(4)
ax1.plot(x, tmpsSepEval, label="Sepa_Eval", color="blue", marker="x")
ax1.plot(x, tmpsDynam, label="Dynamique", color="green", marker="+")
ax1.plot(x, tmpsDynamEch, label="Dynamique_Ch_Echelle", color="red", marker=".")
ax1.plot(x, tmpsBorneInf, label="Borne inférieure", color="orange", marker="*")

ax2.plot(x, methSepEval, label="Sepa_Eval", color="blue", marker="x")
ax2.plot(x, methDynam, label="Dynamique", color="green", marker="+")
ax2.plot(x, methDynamEch, label="Dynamique_Ch_Echelle", color="red", marker=".")
ax2.plot(x, methBorneInf, label="Borne inférieure", color="orange", marker="*")

ax3.plot(x, memSepEval, label="Sepa_Eval", color="blue", marker="x")
ax3.plot(x, memDynam, label="Dynamique", color="green", marker="+")
ax3.plot(x, memDynamEch, label="Dynamique_Ch_Echelle", color="red", marker=".")
ax3.plot(x, memBorneInf, label="Borne inférieure", color="orange", marker="*")

plt.legend()
ax1.set_xlabel("Nombre d'objets")
ax1.set_ylabel("Secondes")

ax2.set_xlabel("Nombre d'objets")
ax2.set_ylabel("Résultat")

ax3.set_xlabel("Nombre d'objets")
ax3.set_ylabel("Peak Memory Usage")

histo.set_xlabel("Nombre d'objets")
histo.set_ylabel("Ratios")

counts, bins = np.histogram(ratioValues)
histo.stairs(counts, bins)

plt.show()
