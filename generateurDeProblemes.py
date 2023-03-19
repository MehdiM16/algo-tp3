import random
import time
import numpy as np
import matplotlib as plt
from probleme1 import *
from probleme1_dynamique import *

nbObjetsMax = 20
poidsMax = 100
pMaxTests = 400
valMax = 900
tabObjets = []

# def sortFunc(a, b):
	# va, wa = a
    # vb, wb = b
	
	# return va/wa

for i in range(nbObjetsMax):
	tabObjets.append((random.randint(0, valMax), random.randint(0, poidsMax)))
    
tabObjets.sort(key=lambda article : article[0]/article[1], reverse=True)
# print(calculSac(borneSup(tabObjets, pMaxTests)))
##print
# for i in tabObjets:
	# print(i)
    
#Etude de vitesse d'exécution
for i in nbObjetsMax
print("################ Début de tests avec programmation dynamique. ##############")
print("Valeur finale : " + str(sac_a_dos_2(tabObjets, pMaxTests)))
print("################ Fin de tests avec programmation dynamique. ##############")

print("################ Début de tests de séparation et évaluation. ##############")
s = StopSkipBoundBranch(tabObjets, pMaxTests, [])
# for j in s:
	# print(calculSac(j))
print("Sac final : " + str(meilleurSac(s)))
print("################ Fin de tests de séparation et évaluation. ##############")

#Etude de consommation de mémoire

#Etude de précision
