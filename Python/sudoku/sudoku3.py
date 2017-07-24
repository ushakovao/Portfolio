import generate
import time
	
def problem_a_resoudre():
	f=open('sudoku.txt', 'r')
	var=f.read()
	sudoku=''
	if(var[0]=='0'):# si le premier terme est un 0, alors il faut creer une grille et la renvoyer
		grille=generate.grille()
		grille.mix()
		res=grille.generate_grille_random()
		for line in f:
			pair = line.split()
			print pair[0]
		f.close()
		return res
	if(var[0]=='1'):# si le premier terme est un 1, alors on prend la grille suivante et on la resoud
		
		sudoku=var[2:]
		f.close()
		return sudoku
	else:
		# sinon ya une erreur
		print "erreur"
		f.close()
		exit()
	


taille =3


def cross(A, B):
    "Cross product of elements in A and elements in B."
    "est utilise pour definir les voisins, et les unites"
    return [a+b for a in A for b in B]

MAJ='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 	# represente les lignes
MIN='abcdefghijklmnopqrstuvwxyz' 	# represente les colonnes
nombres='123456789'  				# represente les chiffres que peux
										# prendre chaque case



lignes     = MAJ[:taille*taille] 	# Si la taille=3, on obtient un carre
colonnes   = MIN[:taille*taille]	# de 9x9 comme le sudoku original.
									# taille=2 nous donne un sudoku de
									# 4*4

case  = cross(lignes, colonnes)		# case est la liste de toutes les cases du sudoku
liste_unite = ([cross(lignes, c) for c in colonnes] +
            [cross(r, colonnes) for r in lignes] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('abc','def','ghi')])
	#l iste_unite nous donne toutes les lignes, colonnes et blocs du sudoku.
unite = dict((s, [u for u in liste_unite if s in u]) 
             for s in case)
	# unite nous donne pour chaque case, la liste des cases dans la meme ligne, 
		# meme colonne et meme bloc dans laquelle la case appartient. Par exemple, 
		# la case 'Aa' ( la case en haut a gauche ) appartient  
		# a la 1ere ligne ( la ligne des 'A'), la 1ere colonne ( la colonne des 'a'), 
		# et le 1er bloc.

voisins = dict(    (  s, set( sum( unite[s],[]) )-set( [s] )  )
             for s in case   )
	# voisins nous donne pour chaque case, la liste de ses voisins.
	# chaque case a 20 voisins d'ailleurs
	
#s = dict((x, nombres) for x in case)
	# s est le sudoku. pour chaque case, on associe les valeurs possible sous forme
	# de string
	# Par exemple, pour la case 'Bc' on aura '123456789', cela veut dire
	# qu'il peut y avoir toutes les possibilites dans cette case.
	# Si on a qu'une valeur, alors c'est la seule possibilite

dictionnaire_valeur_faite=['Zz'] # Uniquement pour que la fonction propagation soit plus rapide

liste_dictionnaires=[] # Uniquement pour backtracking_2, Normalement dedans il y a une liste de toutes les solutions du sudoku


def nombre_espace(a):
	"une fonction pour l'affichage du sudoku avec toutes les possibilite par cases."
	"Pour bien afficher les possibilites et que le sudoku soit ordonne graphiquement"
	res=' '+' '*(len(nombres)-len(a))
	if len(nombres)-len(a) ==0:
		return ' '
	else:
		return res
		
def grille_vers_dictionnaire(grille):
	"transforme une grille ( suite de chiffres pour stocker le sudoku)"
	"en dictionnaire pour le resoudre"
	dictionnaire = dict((x, nombres) for x in case) 
	for x in range(len(case)):
	 if grille[x] !='0':
		 dictionnaire[case[x]]=grille[x]
	return dictionnaire
	
	
def dictionnaire_vers_grille(dictionnaire):
	"""Transforme un 'dictionnaire' en 'grille' pour par exemple l'ecrire dans un fichier ou le stocker."""
	grille=''
	for u in case:
		if(len(dictionnaire[u])==1):
			grille=grille+dictionnaire[u]
		else:
			if(len(dictionnaire[u])==0):
				print "ATTENTION LONGUEUR =0 !!"
			grille=grille+'0'
	return grille

	
def affiche_grille(grille):
	"""affiche la grille, qui est une chaine de caractere
	La grille met un numero dans la case si il est bon, et un 0 si la case est vide"""
	res=''
	for y in range(taille*taille):			
		for x in range(taille*taille):
			if( ((x%taille)==(taille-1)) & (x!=taille*taille-1) ):
				if( grille[x+taille*taille*y]!='0' ):
					res=res+'%s | '%(grille[x+taille*taille*y])
				else:
					res=res+'. | '
			else:
				if( grille[x+taille*taille*y]!='0' ):
					res=res+'%s '%(grille[x+taille*taille*y])
				else:
					res=res+'. '
				
		res=res+'\n'	
		if( ((y%taille)==(taille-1)) & (y!=taille*taille-1) ):
			for x in range(taille*taille*2+(taille-1)*2):
				res=res+'-'
			res=res+'\n'		
	print res
	
def return_grille(grille):
	"""retourne la grille, qui est une chaine de caractere
	meme fonction qu'au dessus, mais n'affiche pas la grille, cela la renvoie juste"""
	res=''
	for y in range(taille*taille):			
		for x in range(taille*taille):
			if( ((x%taille)==(taille-1)) & (x!=taille*taille-1) ):
				if( grille[x+taille*taille*y]!='0' ):
					res=res+'%s | '%(grille[x+taille*taille*y])
				else:
					res=res+'. | '
			else:
				if( grille[x+taille*taille*y]!='0' ):
					res=res+'%s '%(grille[x+taille*taille*y])
				else:
					res=res+'. '
				
		res=res+'\n'	
		if( ((y%taille)==(taille-1)) & (y!=taille*taille-1) ):
			for x in range(taille*taille*2+(taille-1)*2):
				res=res+'-'
			res=res+'\n'		
	return res
	
def affiche_possibilite(dictionnaire):
	"fonction qui affiche le sudoku avec toutes les possibilite"
	if(dictionnaire==False):
		print "affiche_possibilite==false"
	else:
		res=''
		for y in lignes:			
			for x in colonnes:
				if( (  ((x)==(colonnes[taille-1])) | ((x)==(colonnes[taille*2-1]))  ) & (x!=taille*taille-1) ):
					
					res=res+'%s %s| '%(dictionnaire[y+x], nombre_espace( dictionnaire[y+x] ) )
					
				else:
				
					res=res+'%s %s'%(dictionnaire[y+x], nombre_espace( dictionnaire[y+x] ) )
				
			res=res+'\n'
			if( (  ((y)==(lignes[taille-1])) | ((y)==(lignes[taille*2-1]))  ) & (y!=taille*taille-1) ):	
		
				for x in range(taille*taille*2+(taille-1)*2):
					res=res+'-'
				res=res+'\n'		
		print res


def propagation(dictionnaire):
	"importante fonction"
	"pour chaque case, si il n'y a qu'une possibilite ( <=> la vraie valeur )"
	"on enleve cette valeur dans les possibilite des cases voisines."
	"Mais il arrive lorsqu'on enleve une valeur dans les possibilite d'une case voisine"
	"qu'il ne reste qu'une possibilite. Il faut donc enlever les possibilite a ses voisins"
	"recursivement..."
	"UN PEU COMPLIQUE A COMPRENDRE"
	
	global liste_dictionnaires
	
	
	valeur_faite=[]
	valeur_a_faire = []
	for u in case:
		if (len(dictionnaire[u])==1):
			valeur_a_faire.append(u)
	
	for v in valeur_a_faire:
		if len(dictionnaire[v]) == 0:
			print "probleme ya plus de valeurs !"
			return False
		elif (v not in valeur_faite):
			valeur_faite.append(v)
			dictionnaire_valeur_faite.append(v)
			for q in voisins[ v ]:
				dictionnaire[q] = dictionnaire[q].replace(dictionnaire[v], '')
				if len(dictionnaire[q]) == 0:
					print "erreur dans propagation"
					return False
				if( len(dictionnaire[q])==1):
					valeur_a_faire.append(q)
	if( mini(dictionnaire) == True):
		liste_dictionnaires.append(dictionnaire)
	return dictionnaire



def propagation_boucle(dictionnaire):
	"""meme fonction que propagation mais plus rapide. Elle est utilise dans "backtracking"
	Sauf qu'elle ne repasse pas dans les cases finies ( => les cases qui ont ete choisies au debut de la grille)"""
	valeur_faite=[]
	valeur_a_faire = []
	for u in case:
		if len(dictionnaire[u])==1 and u not in dictionnaire_valeur_faite:
			valeur_a_faire.append(u)
	for v in valeur_a_faire:
		if len(dictionnaire[v]) == 0:
			return False
		elif (v not in valeur_faite):
			valeur_faite.append(v)
			for q in voisins[ v ]:
				dictionnaire[q] = dictionnaire[q].replace(dictionnaire[v], '')
				if len(dictionnaire[q]) == 0:
					return False
				if( len(dictionnaire[q])==1):
					valeur_a_faire.append(q)
	return dictionnaire
	
	





def mini(dictionnaire):
	"""retourne la case dans le dictionnaire avec le minimum de possibilites, ou si le sudoku est rempli returne True"""
	incr=0
	minimum=''
	for u in case:
		if len(dictionnaire[u]) >1:
			incr=incr+1  	# entier pour verifier si on a pas le sudoku rempli
			if(minimum==''):
				minimum=u
				# Juste pour fixer la premiere valeur
				
			if (len(dictionnaire[u]) <= len(dictionnaire[minimum])):
				minimum=u
				
	if(incr==0):	# Si incr=0 ca veut dire qu'aucune des cases a une liste de possibilites>1
					# donc que le sudoku est rempli !
		return True
	return minimum
	
	
def backtracking_final(dictionnaire, nombre_valeur):
	"""La fonction remplie la variable "liste_dictionnaire" qui est declare en dehors de cette fonction.
	Cette liste est une liste de dictionnaire, qui sont les solutions de la grille de sudoku.
	
					######  ATTENTION ######"
					
	 le premier element de la liste est toujours la grille de sudoku initiale non remplie !"
	Donc quand on veut 1 solution, la longueur de la liste ==2 car grille de depart + une solution"""
	
	
	# nombre_valeur est le nombre de solutions qu'on veut retourner
	# Si nombre_valeur >= 1, alors on retourne le nombre voulu
	# Si nombre_valeur == 0, alors on retourne 0 valeurs ( la liste contient alors uniquement la grille de depart a resoudre )
	# Si nombre_valeur == -1, on retourne toutes les solutions
	
	global liste_dictionnaires # ceci est pour pouvoir modifier la variable "liste_dictionnaires" qui est declaree en dehors de la fonction
	
	
	if(len(liste_dictionnaires)==nombre_valeur+1):
		#Si on est ici, c'est qu'on a le nombre de solutions necessaire
		return
	minimum=mini(dictionnaire) # Ceci cherche la valeur dans le dictionnaire qui a le plus petit nombre de possibilites
	
	if(minimum==True):
		# Si on est ici, c'est que dictionnaire est rempli
		if(dictionnaire not in liste_dictionnaires):
			# avant d'ajouter la solution, on verifie qu'elle n'est pas deja dans la liste
			liste_dictionnaires.append(dictionnaire)
				
			
	else:
		
		for q in dictionnaire[minimum]:
			dictionnaire2=dictionnaire.copy()
			dictionnaire2[minimum] = dictionnaire2[minimum].replace( dictionnaire2[minimum], q)
			
			variable=propagation_boucle(dictionnaire2)
			
			if(variable!=False and len(liste_dictionnaires)!=nombre_valeur+1) :
				
				# on stoppe si on a le nombre voulu
				backtracking_final(variable, nombre_valeur)
		
def export_solutions():
	incr=0
	solution=''
	for u in liste_dictionnaires:
		if(incr==0):
			incr+=1
			solution=solution+'GRILLE DE DEPART : \n\n'
			solution=solution+return_grille(dictionnaire_vers_grille(u))+'\n\n\n'
		else:
			
			solution=solution+'Solution numero '+str(incr)+' : \n\n'
			solution=solution+return_grille(dictionnaire_vers_grille(u))+'\n\n\n'
			incr+=1
		
	f = open('solutions.txt', 'w')
	for v in solution:
		f.write(v)
	f.close()
	
start=time.time()
sudoku=grille_vers_dictionnaire(problem_a_resoudre()) # on transforme la grille en dictionnaire
# On stocke le sudoku a resoudre ici
affiche_grille(dictionnaire_vers_grille(sudoku))

liste_dictionnaires=[sudoku.copy()]
# On remplie le premier element de la liste avec la grille de sudoku initiale non remplie.

print "on affiche toutes les possibilites avant propagation: \n"
affiche_possibilite(sudoku)
print "------------------------------------------------------"
propagation(sudoku)
# On fait une premiere propagation. TRES UTILE
# Cela permet de presque resoudre la grille, et de faire en sorte que "propagation_boucle" soit plus rapide

print "on affiche toutes les possibilites apres propagation: \n"
affiche_possibilite(sudoku)
print "------------------------------------------------------"
backtracking_final(sudoku,-1)
# On resoud le sudoku
# Le 2eme parametre est le nombre de solutions qu'on veut
	# Si on prends >= 1, alors on retourne le nombre de solutions voulu
	# Si nombre_valeur == 0, alors on retourne 0 valeurs ( la liste contient alors uniquement la grille de depart a resoudre )
	# Si nombre_valeur == -1, on retourne toutes les solutions


#for u in liste_dictionnaires:
	
#	affiche_grille(dictionnaire_vers_grille(u))
export_solutions()	
	
print "LONGUEUR DE LISTE Dictionnaire: ", len(liste_dictionnaires)-1, "################\n"
# On affiche "len(liste_dictionnaires)-1" pour avoir le nombre de solutions  ( -1 car le premier element est la grille de depart... )
end=time.time()
print(end - start)
