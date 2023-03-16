import random
from probleme1 import *
from probleme1_dynamique import *

nbObjetsMax = 100
poidsMax = 100
pMaxTests = 400
valMax = 100
tabObjets = []

for i in range(nbObjetsMax):
	tabObjets.append((random.randint(0, valMax), random.randint(0, poidsMax)))
	
##print
#for i in tabObjets:
	#print(i)
	
print(sac_a_dos_2(tabObjets, pMaxTests))
print(StopSkipBoundBranch(tabObjets, b, []), pMaxTests)
