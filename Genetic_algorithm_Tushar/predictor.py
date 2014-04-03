from data.read_stock import DataHandler
from ga.individual import Individual
from ga.population import Population
import numpy as np


dataHandler = DataHandler(['apple_test_data.csv', 'NASDAQ_test_data.csv'])
#dataHandler = DataHandler(['apple_data.csv', 'NASDAQ_data.csv'])
data = dataHandler.get_signal_list()
signal_ranges = dataHandler.signal_ranges()
#print signal_ranges

data_element = len(data[0])
#print "data[0]"
#print data[0]


population = Population(100 , signal_ranges, data)
#for i in population:
#    print i.transform_individual(signal_ranges)
initial_fitess_values  = map(population.fitness_function, population)  
#print initial_fitess_values


number_generations = 100

population.sus_sampler(initial_fitess_values)
max_list = []
mean_list = []

for i in xrange(number_generations):
    #print "initial population"
    #for i in population:
    #    print i.rep
    #print "before crossover"
    population.crossover()
    #print "after crossover"
    #for i in population:
    #    print i.rep
    #print "before mutation"
    population.mutation()
    #for i in population:
    #    print i.rep
    #print "after mutation"
    fitness_vals = map(population.fitness_function, population)
    population.sus_sampler(fitness_vals)
    mean_val = np.mean(fitness_vals)
    max_val = max(fitness_vals)
    print mean_val, max_val
    mean_list.append(mean_val)
    max_list.append(max_val)


