from data.read_stock import DataHandler
from ga.individual import Individual
from ga.population import Population


dataHandler = DataHandler(['apple_data.csv', 'NASDAQ_data.csv'])
data = dataHandler.get_signal_list()
signal_ranges = dataHandler.signal_ranges()

data_element = len(data[0])


population = Population(100 , signal_ranges, data)
initial_fitess_values  = map(population.fitness_function, population)  


number_generations = 100

for i in xrange(number_generations):
    population.crossover()
    population.mutation()
    print max(map(population.fitness_function, population))



