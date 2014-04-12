#Rahul Ramakrishnan
#module: fitness

'''
	Fitness 
	Functions & Wrappers
'''

import scrape
import recombination

def calculateAverageFitness(population):	
	population_fitness = map(lambda t: t.fitness, population)
	avg_fitness = sum(population_fitness)/float(len(population))
	print "Average Fitness: %f" %(avg_fitness)
	
def generateFitnesses(population):		
	map(lambda x: fitnessValue(x), population)	
	
#Replaces path with data by subbing in
#dictionary that will be eval'd later
def nodeReplace(path):
	terminals = scrape.getTerminal()	
	string_terminals = filter(lambda t: type(t) == type('str'), terminals)
	path_string_terminals = filter(lambda t: t in path, string_terminals)		
	
	#Convert this to filter, map combo later

	
	apple_data = filter(lambda t: t[0] == 'a', path_string_terminals)
	nasdaq_data = filter(lambda t: t[0] == 'n', path_string_terminals)
	map(lambda t: replaceWrapper(path, t, 'a'), apple_data)
	map(lambda t: replaceWrapper(path, t, 'n'), nasdaq_data)

def replaceWrapper(path, t, data_type):
	pairs = filter(lambda pair: pair[1] == t, enumerate(path))
	indices = map(lambda pair: pair[0], pairs)	
	map(lambda index: replaceWrapper2(path, t, data_type, index), indices)

def replaceWrapper2(path, t, data_type, index):
	if(data_type == 'a'):
		path[index] = "apple_data[i]['%s']" %(t)
	elif(data_type == 'n'):
		path[index] = "nasdaq_data[i]['%s']" %(t)
	
#Calculate the fitness value of a single GP tree
#and stores it in the tree object
def fitnessValue(tree):
        path = []    
        fitness = 0 
	_sum_of_errors = 0
        recombination.loadPaths(tree.root, path)

	#Load market data and stores in respective dictionaries	
	apple_data = scrape.getAppleData()	
	nasdaq_data = scrape.getNasdaqData()
	
	#Refactor this to filter->map->enumerate	
	for i in xrange(0, len(apple_data)-1):	
		nodeReplace(path)
		equation = createEquation(path)	
		predicted_price = eval(equation)
		actual_price = apple_data[i+1]['apple_close']
		error = abs(actual_price - predicted_price)
		_sum_of_errors += error	

	total = float(len(apple_data)-1)	
	fitness = _sum_of_errors/total
	tree.fitness = fitness	#Adds fitness to tree object in-place	
	return fitness #For printEquationPopulation function
		
def createEquation(path):
	path_str = ""
	for node in path:
		path_str += str(node) + " "
	return path_str

