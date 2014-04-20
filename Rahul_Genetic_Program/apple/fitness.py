#Rahul Ramakrishnan
#module: fitness

'''
	Fitness 
	Functions & Wrappers
'''

import scrape
import recombination
from copy import deepcopy

def generateFitnesses(population):		
	fitnesses = map(lambda x: fitnessValue(x), population)	

#Calculate the fitness value of a single GP tree
#and stores it in the tree object
def fitnessValue(tree):
        path = []    
        recombination.loadPaths(tree.root, path)

	#Load market data and stores in respective dictionaries	
	apple_data = scrape.getAppleData()	
	nasdaq_data = scrape.getNasdaqData()
	sp500_data = scrape.getSP500Data()
	
	nodeReplace(path)	
	equation = createEquation(path)	
	data_size = range(0, len(apple_data))	
	predicted_prices = map(lambda i: evaluateEquation(i, nasdaq_data, apple_data, sp500_data, equation), data_size)
	next_day_prices = map(lambda data: data['apple_close'], apple_data) #next_day_price is the actual price
		
	predicted_prices.pop() 	#Removes the last item in the list
	next_day_prices.pop(0) 	#Removes the first item in the list		
	
	zipped = zip(predicted_prices, next_day_prices)
	errors = map(lambda pair: abs(pair[1] - pair[0]), zipped)
	fitness = sum(errors)/float(len(errors))

	tree.fitness = fitness	#Adds fitness to tree object in-place	
	return fitness 		#For printEquationPopulation function	

def evaluateEquation(i, nasdaq_data, apple_data, sp500_data, equation):
	return eval(equation)
	

#Replaces path with data by subbing in
#dictionary that will be eval'd later
def nodeReplace(path):
        terminals = scrape.getTerminal()    

        string_terminals = filter(lambda t: type(t) == type('str'), terminals)
        path_string_terminals = filter(lambda t: t in path, string_terminals)     

        apple_data = filter(lambda t: t[0] == 'a', path_string_terminals)
        nasdaq_data = filter(lambda t: t[0] == 'n', path_string_terminals)
	sp500_data = filter(lambda t: t[0] == 's', path_string_terminals)

        map(lambda t: replaceWrapper(path, t, 'a'), apple_data)
        map(lambda t: replaceWrapper(path, t, 'n'), nasdaq_data)
	map(lambda t: replaceWrapper(path, t, 's'), sp500_data)

def replaceWrapper(path, t, data_type):
        pairs = filter(lambda pair: pair[1] == t, enumerate(path))
        indices = map(lambda pair: pair[0], pairs)          
        map(lambda index: replaceWrapper2(path, t, data_type, index), indices)

def replaceWrapper2(path, t, data_type, index):
        if(data_type == 'a'):
                path[index] = "apple_data[i]['%s']" %(t)
        elif(data_type == 'n'):
                path[index] = "nasdaq_data[i]['%s']" %(t)
	elif(data_type == 's'):
		path[index] = "sp500_data[i]['%s']" %(t)

#Creates the equation that the tree represents
def createEquation(path):
        paths = map(lambda node: str(node), path)
        final_path = reduce(lambda x,y: x + " " + y, paths)
        return final_path

