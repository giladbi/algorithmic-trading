#Rahul Ramakrishnan
#Main Script
'''
        ------------------ To Do: -------------------
	0. Print out equation, fitness, best -----------------------------------------------DONE
        1. Add more diversity preserving (Test each one)
                a. Roullette Wheel ---------------------------------------------------------DONE
                b. Tournament Selection ----------------------------------------------------DONE
		c. SUS 
        2. Graph the evolution of the different methods
        3. Add more terminal nodes (data from s&p500)
        4. Add more functional nodes (^, cosine, sine, tangent, log, ln, exp (e^) )
        5. Convert for loops to map & reduce
        6. Use filter when you can 
        7. Become more memory efficient where possible 
	8. Create training data ------------------------------------------------------------DONE
	9. Separate modules in a package __init__.py ---------------------------------------DONE
	10. Include parameter control
	11. Include colors in the output
	12. Find out a way to choose functional nodes randomly -----------------------------DONE
'''

from apple import config
from apple import initialize
from apple import inspect
from apple import recombination
from apple import selection
from apple import fitness

#Initialize objects and literals
population = initialize.initializePopulation(config.population_size)
size = len(population)

for generation in xrange(0, config.generations):		
	print "----------Generation: %d----------" %(generation)
	for tree in xrange(0, size):			
		#recombination.performMutation(population)
		recombination.performCrossover(population)
	fitness.generateFitnesses(population)
	#inspect.printEquationPopulation(population)	
	selection.tournamentParentSelection(population)
	fitness.calculateAverageFitness(population)	

print "============= After genetic program ===================="
inspect.printEquationPopulation(population)


