#Rahul Ramakrishnan
#Stochastic Optimization
#Algorithmic Trading Script

import genetic_program as GP
import config

population = GP.initializePopulation(config.population_size)

for generation in xrange(0, config.generations):		
	print "Generation: %d" %(generation)

	for tree in xrange(0, len(population)):			
		GP.performMutation(population)
		GP.performCrossover(population)
	GP.generateFitnesses(population)
	roullette = GP.roulletteWheel(population)
	population = GP.parentSelection(roullette)		
	GP.averageFitness(population)	



print "All Done"
