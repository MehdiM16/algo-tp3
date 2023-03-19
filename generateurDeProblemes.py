import random
import time
import numpy as np
import matplotlib.pyplot as plt
from probleme1 import *
from probleme1_dynamique import *

nbObjetsMax = 9
poidsMax = 100
pMaxTests = 400
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

start = 0
end = 0
x = np.linspace(0, nbObjetsMax, nbObjetsMax)

#On effectue nbObjetsMax tests
for j in range(nbObjetsMax):
	for i in range(j):
		tabObjets.append((random.randint(0, valMax), random.randint(0, poidsMax)))
    
	tabObjets.sort(key=lambda article : article[0]/article[1], reverse=True)
    
	#Etude de vitesse d'exécution et de précision des résultats
	start = time.perf_counter()
	methDynam.append(sac_a_dos_2(tabObjets, pMaxTests))
	end = time.perf_counter()
	tmpsDynam.append(end - start)
	
	
	start = time.perf_counter()
	v, w = meilleurSac(StopSkipBoundBranch(tabObjets, pMaxTests, []))
	end = time.perf_counter()
	tmpsSepEval.append(end - start)
	methSepEval.append(v)
	
	start = time.perf_counter()
	methDynamEch.append(sac_a_dos_3(tabObjets, pMaxTests, 1))
	end = time.perf_counter()
	tmpsDynamEch.append(end - start)

#Etude de consommation de mémoire

#Tracé des graphes
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, tmpsSepEval, label="Sepa_Eval", marker='o')
ax1.plot(x, tmpsDynam, label="Dynamique", marker='o')
ax1.plot(x, tmpsDynamEch, label="Dynamique_Ch_Echelle", marker='o')
ax2.plot(x, methSepEval, label="Sepa_Eval", marker='_')
ax2.plot(x, methDynam, label="Dynamique", marker='_')
ax2.plot(x, methDynamEch, label="Dynamique_Ch_Echelle", marker='_')
plt.legend()
ax1.set_xlabel("Nombre d'objets")
ax1.set_ylabel("Secondes")

ax2.set_xlabel("Nombre d'objets")
ax2.set_ylabel("Résultat")
plt.show()
