##Probleme 1 (sac à dos) :

Le fichier probleme1.py contient toutes les differentes méthode demandées dans le sujet.

Le fichier generateurDeProblemes.py est le fichier qui permet d'analyser les différentes méthodes pour le problème du sac à dos, il faudra entrer le nombre maximum d'objets et le poids maximal du sac qu'on veut, ensuite les objets seront créés aléatoirement.

Pour l'utiliser et pouvoir analyser les résultats, entrer la commande "python3 generateurDeProblemes.py".

Le fichier generateurDeProblemesMoyenne.py est le fichier qui permet permet de faire de même, en générant des objets avec des valeurs et poids autour de moyennes souhaitées. Il vous demandera des paramètres en plus : 
	le nombre maximum d'objet
	le poids maximal du sac
	muv -> moyenne des valeurs des objets
	sigmav -> variation autour de la valeur muv
	muw -> moyenne des poids des objets
	sigmaw -> variation autour de la moyenne muw

entrer dans le terminal : "python3 generateurDeProblemesMoyenne.py"



##Probleme 2 (Logistique du dernier kilometre) :

Les fichiers contenant les différentes méthode demander sont les fichiers probleme2_xxx.py ou xxx est le nom du probleme en question.
Les fichiers Sommet.py et Arete.py sont des classe qui permettent de stocké les différent client sous forme de Sommet et une Arete est le chemin entre 2 client dont le coup sera la distance entre ces client.

Le fichier generateurDeProblemes_2.py est le fichier qui permet d'analyser les différentes méthodes pour le problème du dernier kilomètre, il faudra entrer le nombre maximum de clients, ensuite le graphe  sera créé aléatoirement. Une boucle sera realisée afin de faire des test avec j clients pour j allant de 1 au nombre de clients choisit afin d'obtenir une courbe pour comparer les différents algorithmes.
Entrer la commande "pyhton3 generateurDeProblemes_2.py"


Le fichier generateurDeProblemes_2_unique.py est le fichier qui permet d'analyser les différentes methodes pour le problème du dernier kilomètre, il faudra entrer le nombre maximum de clients, ensuite le graphe  sera créé aléatoirement. Le test se fera uniquement sur le nombre de clients choisit et les résultats seront affichés sur le terminal.
Entrer la commande "pyhton3 generateurDeProblemes_2_unique.py"
Entrer la commande "pyhton3 generateurDeProblemes_2_unique_methode.py" pour analyser une méthode en particulier.

Pour La situation réelle, l'algorithme utilisé se trouve dans "probleme_N_serveurs.py". Il consiste en la division des clients en autant de groupes qu'il y a de serveurs disponibles groupes choisis selon la proximùité des clients.

