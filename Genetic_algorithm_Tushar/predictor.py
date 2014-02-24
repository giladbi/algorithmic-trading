import csv
import math
import random
import numpy

def initialize_population():
    # initialize population based on the data available
    pass


class Chromosome:
    
    def mutate(self):
        # mutation 
        # This definition might change based on the type of mutation we wish to
        # perform
        pass

    def crossover(self, chromosome):
        # performs crossover between two chromosomes
        pass



class Population:
    def __init__(self):
        # read the CSV file and initialize the initial population
        self.generation = 0
        self.population = initialize_population()
        pass

    def filter_data(self):
        # transform the data into values that will be useful for computing the
        # trading information
        pass

    def selection(self):
        # Selection of the individuals going to the next generation
        pass

    def evolve(self):
        # create the next generation 
        # Perform crossover
        # Perform mutation
        # Perform selection
        self.generation = self.generation + 1
        pass

    def select_parents(self):
        # Choose parents to be mated from population
        pass


