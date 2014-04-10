#Rahul Ramakrishnan
#module: fitness

'''
	Fitness 
	Functions & Wrappers
'''

import scrape


def calculateAverageFitness(population):
	size = len(population)
	population_fitness = map(lambda t: t.fitness, population)
	avg_fitness = sum(population_fitness)/size
	print "Average Fitness: %f" %(avg_fitness)
	
def generateFitnesses(population):	
	#population = map(lambda x: fitnessValue(x), population)
        for tree in xrange(0, len(population)):
		fitnessValue(population[tree])
	
#Replaces path with data
def nodeReplace(path):
	terminal = scrape.getTerminal()	
	for t in terminal:
		if (type(t) == type('str')):
			if t in path:	
				#t_i = path.index(t)			
				#indices = filter(for i,x in enumerate(path) if x == t, path)
				indices = [i for i,x in enumerate(path) if x == t]	
				if t[0] == 'a':
					for index in indices:
						path[index] = "apple_data[i]['%s']" %(t)
				else: #nasdaq
					for index in indices:
						path[index] = "nasdaq_data[i]['%s']" %(t)	
				
#Calculate the fitness value of a single GP tree
#and stores it in the tree object
def fitnessValue(tree):
        path = []    
        fitness = 0 
	_sum_of_errors = 0
        loadPaths(tree.root, path)

	#Load market data	
	apple_data = scrape.getAppleData()	
	nasdaq_data = scrape.getNasdaqData()
		
	for i in xrange(0, len(apple_data)-1):	
		nodeReplace(path)
		equation = createEquation(path)	
		predicted_price = eval(equation)
		actual_price = apple_data[i+1]['apple_close']
		error = abs(actual_price - predicted_price)
		_sum_of_errors += error	

	total = float(len(apple_data)-1)	
	fitness = _sum_of_errors/total
	tree.fitness = fitness		
	return fitness
		
def createEquation(path):
	path_str = ""
	for node in path:
		path_str += str(node) + " "
	return path_str

