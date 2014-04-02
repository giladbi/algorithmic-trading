#Rahul Ramakrishnan
#Stochastic Optimization
#Algorithmic Trading Script

import genetic_program as GP

population = GP.initializePopulation(100)


for generation in xrange(0, 10):		
	for tree in xrange(0, len(population)):		
		print "\ntree: %d" %(tree)
		GP.performMutation(population)
		GP.performCrossover(population)
	GP.generateFitnesses(population)
	roullette = GP.roulletteWheel(population)
	population = GP.parentSelection(roullette)		
	GP.averageFitness(population)	



print "All Done"
