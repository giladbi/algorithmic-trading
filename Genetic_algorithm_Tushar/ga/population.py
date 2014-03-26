import random
import math

from individual import Individual


class Population(object):
    def __init__(self, size, signal_ranges, data, pm = 0.5, pc = 0.7):
        individual_size = len(signal_ranges)
        self.population = []
        self.signal_ranges = signal_ranges
        self.pm = pm
        self.pc = pc
        self.size = size
        self.num_signals = len(signal_ranges)
        self.data = data
        self.data_size = len(data)
        for i in xrange(size):
            self.population.append(Individual(individual_size))


    def __getitem__(self, key):
        return self.population[key]

    def fitness_function(self, individual):
        transformed_individual = individual.transform_individual(self.signal_ranges)
        positive = 0
        for element in self.data:
            count = 0
            for item in xrange(self.num_signals):
                threshold = int(0.8 * self.num_signals)
                if abs(transformed_individual[item]) > abs(element[item]):
                    count = count + 1
                    if count > threshold:
                        positive = positive + 1
                        count = 0
        return float(positive) / self.data_size


    def sus_sampler(self, fitness_list):
        fitness_list = fitness(self.fitness_function)
        size = len(fitness_list)
        total_fitness = reduce(operator.add, fitness_list)

        sel_prob_list = [x/ total_fitness for x in fitness_list]
        summed_prob_list = []
        for i in xrange(1, len(sel_prob_list) + 1):
            summed_prob_list.append(reduce(operator.add, sel_prob_list[:i]))

        i = 0
        r = random.uniform(0, 1.0/size)
        mating_pool = []
        while len(mating_pool) <= size -1:
            while r <= summed_prob_list[i]:
                mating_pool.append(population[i])
                r = r + 1.0/size
            i += 1
        self.population = mating_pool

    def mutation(self):
        for individual in self.population:
            individual.mutate(self.pm)

    def crossover(self):
        for i in xrange(0, self.size, 2):
            self.population[i].crossover_2way(self.population[i+1], self.pc)


