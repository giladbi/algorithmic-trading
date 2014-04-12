#Rahul Ramakrishnan
#module: fitness

'''
	Fitness 
	Functions & Wrappers
'''

import scrape
import recombination
from copy import deepcopy

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
	predicted_price = map(lambda data: data['apple_close'], apple_data)
	next_day_price = deepcopy(predicted_price)
	predicted_price.pop() 	#Removes the last item in the list
	next_day_price.pop(0) 	#Removes the first item in the list		
	zipped = zip(predicted_price, next_day_price)
	errors = map(lambda pair: abs(pair[1] - pair[0]), zipped)
	fitness = sum(errors)/float(len(errors))
	tree.fitness = fitness	#Adds fitness to tree object in-place	
	return fitness #For printEquationPopulation function
		
def createEquation(path):
	paths = map(lambda node: str(node), path)
	final_path = reduce(lambda x,y: x + " " + y, paths)	
	return final_path

