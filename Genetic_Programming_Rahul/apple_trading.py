#Rahul Ramakrishnan
#Stochastic Optimization
#Algorithmic Trading Script

import genetic_program as GP

population = GP.initializePopulation(100)


for generation in xrange(0, 10):		
	print "Generation: %d" %(generation)

	for tree in xrange(0, len(population)):			
		GP.performMutation(population)
		GP.performCrossover(population)
	GP.generateFitnesses(population)
	for tree in population:
		print "tree.fitness: %s" %(tree.fitness)
	roullette = GP.roulletteWheel(population)
	population = GP.parentSelection(roullette)		
	GP.averageFitness(population)	



print "All Done"
