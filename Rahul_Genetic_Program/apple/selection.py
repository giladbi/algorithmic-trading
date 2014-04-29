#Rahul Ramakrishnan
#module: selection

'''
	Parent Selection
	Functions
'''
from config import tournament_size
from copy import deepcopy
from random import sample
from random import random

'''
	Roullette Wheel
'''
def sortPopulation(population):
	#Sort in descending order by fitness(error): highest error --> lowest error
	sorted_pop = sorted(population, key=lambda tree: tree.fitness, reverse=True)
	return sorted_pop

def createRoulletteWheel(population):
	#Sum Ranks
	total = len(population)	
	_rank_sum = reduce(lambda x,y: x+y, xrange(1, total+1))	
	#Assign probability
	probabilities = map(lambda i: i/float(_rank_sum), xrange(1, total+1))	
	#Generate intervals
	roulletteWheel = map(lambda i: 0, xrange(0, total)) #Fill list with zeroes
	for i,p in enumerate(probabilities):
		if (i == 0):
			roulletteWheel[0] = probabilities[i] 
		else:
			roulletteWheel[i] = roulletteWheel[i-1] + probabilities[i]		
	return roulletteWheel	

def roulletteParentSelection(roulletteWheel, population):	
	population_size = len(population)	
	sorted_population = sortPopulation(population)
	population[:] = []	
	for i in xrange(0, population_size):	
		#0.0 <= X <= 1.0
		number = random()
		for j in xrange(0, len(roulletteWheel)):
			if (number <= roulletteWheel[j]):
				new_tree = deepcopy(sorted_population[j])
				population.append(new_tree)	
				break 	#break out of inner for loop
	

'''
	Tournament Selection
'''
def tournamentParentSelection(population):
	temp_population = deepcopy(population)		
	population_size = len(population)
	k = tournament_size 
	population[:] = []
	for p in xrange(0, population_size):
		tournament = sample(temp_population, k)		
		tree = bestMatch(tournament)
		new_tree = deepcopy(tree)
		population.append(new_tree)		
	
def bestMatch(tournament):
	fitnesses = map(lambda x: x.fitness, tournament)
	best_fitness = min(fitnesses)
	best_index = fitnesses.index(best_fitness)
	best_tree = tournament[best_index]
	return best_tree

