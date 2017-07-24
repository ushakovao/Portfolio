import random
import sys
import numpy as np

class grille:
	def __init__(self,n = 3):
		self.n = n
		self.table = [[ ((i*n + i/n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]
	def __del__(self):
		pass

	def transposer(self):
		self.table = np.transpose(self.table)

	def echanger_lignes(self):
		bloc = random.randrange(0,self.n,1)
		ligne1 = random.randrange(0,self.n,1)
		N1 = bloc*self.n + ligne1
		ligne2 = random.randrange(0,self.n,1)
		while (ligne1 == ligne2):
			ligne2 = random.randrange(0,self.n,1)

		N2 = bloc*self.n + ligne2
		self.table[N1],self.table[N2] = self.table[N2], self.table[N1]


	def echanger_colonne(self):
		grille.transposer(self)
		grille.echanger_lignes(self)
		grille.transposer(self)


	def echanger_bloc_ligne(self):
		bloc1 = random.randrange(0,self.n,1)
		bloc2 = random.randrange(0,self.n,1)
		while (bloc1 == bloc2):
			bloc2 = random.randrange(0,self.n,1)

		for i in range(0, self.n):
			N1, N2 = bloc1*self.n + i, bloc2*self.n + i
			self.table[N1], self.table[N2] = self.table[N2], self.table[N1]


	def echanger_bloc_colonne(self):
		grille.transposer(self)
		grille.echanger_bloc_ligne(self)
		grille.transposer(self)
	
	def mix(self,amt = 10):
		mix_func = ['self.transposer()', 'self.echanger_lignes()', 'self.echanger_colonne()', 'self.echanger_bloc_ligne()', 'self.echanger_bloc_colonne()']
		for i in xrange(1, amt):
			id_func = random.randrange(0,len(mix_func),1)
			eval(mix_func[id_func])

	"Cette fonction nous permet de creer une grille sous forme necessaire, cad chaine des chiffres"
	def generate_grille_random(self):
		for i in range (0,30):
			i,j = random.randrange(0, self.n*self.n ,1), random.randrange(0, self.n*self.n ,1)
			self.table[i][j] = 0
		grille = []
		for i in range(self.n*self.n):
			for j in range(self.n*self.n):
				grille.append(self.table[i][j])
		res=''
		for elem in grille:
			res=res+str(elem)
		return res








