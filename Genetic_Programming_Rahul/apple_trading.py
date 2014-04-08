#Rahul Ramakrishnan
#Stochastic Optimization
#Algorithmic Trading Script

import genetic_program as GP
import config


#Initialize objects and literals
population = GP.initializePopulation(config.population_size)
#new_population = []
#roulletteWheel = []
size = len(population)

print "============= Before mutations and crossovers ============"
for index, tree in enumerate(population):
	print "\n\nIndex: %d" %(index)
	GP.printTree(tree.root)

for generation in xrange(0, config.generations):		
	print "----------Generation: %d----------" %(generation)
	for tree in xrange(0, len(population)):			
		GP.performMutation(population)
		GP.performCrossover(population)

	GP.generateFitnesses(population)
	#GP.createRoulletteWheel(old_population)
	#GP.parentSelection(new_population, old_population, roulletteWheel)
	roulletteWheel = GP.createRoulletteWheel(population)
	population = GP.parentSelection(roulletteWheel, population)		
	GP.printPopulation(population)
	GP.calculateAverageFitness(population)	

