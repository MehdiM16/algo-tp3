from probleme1 import *

#t = [(2, 8), (3, 5), (6, 7), (9, 5), (4, 1)] #liste de tuples (vi,wi) vi = valeur wi = poids
#t.reverse()
#n = size(t) #n>=1, fixé, nb d'objets
#b = 10 #poids max du sac
#poids = 0

#initialisation pb uniforme

#initialisation pb moyenne

#init = [(4, 1), (9, 5), (6, 7), (2, 3), (2, 4), (3, 5), (2, 8), (56, 10), (1, 1)]
#init = [(4, 1), (9, 5), (6, 7), (2, 3), (2, 4), (3, 5), (2, 8), (1, 1)]
#init = [(4, 1), (9, 5), (6, 7), (2, 3), (2, 4), (3, 5), (2, 8)]
#init = [(4, 1), (9, 5), (6, 7), (2, 3), (5, 3), (2, 4), (3, 5), (2, 8), (1, 1)]
init = [(4, 1), (9, 5), (6, 7), (5, 3), (2, 3), (2, 4), (3, 5), (2, 8), (1, 1)]
init.sort(key=lambda article : article[0]/article[1], reverse=True)
#print(init)


#1) tests Bornes sup et inf
sacInf, sacSup = borneInfSup(init, 10)
print("valeur inf : " + str(calculSac(sacInf)))
print("valeur sup : " + str(calculSac(sacSup)))
print("\n")

#2) tests de séparation et évalutation
print("tests de séparation et évaluation\n")
res = StopSkipBoundBranch(init, 10, [])
print("Sacs possibles trouvés : ")
for i in res:
	print("Contenu détaillé du sac : " + str(i) + "\nContenu final du sac : " + str(calculSac(i)))
	
