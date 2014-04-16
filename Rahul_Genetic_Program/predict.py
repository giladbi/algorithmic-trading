#Rahul Ramakrishnan
#Main Apple Stock Predicting Script

from apple import config
from apple import initialize
from apple import inspect
from apple import recombination
from apple import selection
from apple import fitness

from termcolor import colored

population = initialize.initPopulation(config.population_size)

for generation in xrange(0, config.generations):			
	fitness.generateFitnesses(population)
	inspect.printEquationPopulation(population, generation)
	for tree in xrange(0, len(population)):			
		recombination.performMutation(population)
		recombination.performCrossover(population)
	selection.tournamentParentSelection(population)


