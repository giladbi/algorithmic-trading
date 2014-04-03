import random
import math
import operator

from individual import Individual

random.seed(1234)

def percent_diff(approx , correct):
    #print "approx, correct"
    #print approx, correct
    return ((approx - correct) / float(correct))


class Population(object):
    def __init__(self, size, signal_ranges, data, pm = 0.1, pc = 0.7):
        individual_size = len(signal_ranges)
        self.population = []
        self.signal_ranges = signal_ranges
        self.pm = pm
        self.pc = pc
        self.size = size
        self.num_signals = len(signal_ranges)
        self.data = data
        #print "self.data"
        #print self.data
        self.data_size = len(data)
        for i in xrange(size):
            self.population.append(Individual(individual_size))


    def __getitem__(self, key):
        return self.population[key]

    def fitness_function(self, individual):
        transformed_individual = individual.transform_individual(self.signal_ranges)
        #print "Transformed individual"
        #print transformed_individual
        positive = 0
        count = 0
        for element in self.data:
            #one_iter = []
            #print "element"
            #print element
            for item in xrange(self.num_signals):
            #for item in xrange(3):
            
                #threshold = int(0.6 * self.num_signals)
                #print "GA, value"
                #print transformed_individual[item]
                #print "actual value"
                #print element[item]
                #print "Delta"
                #print transformed_individual[item] - element[item]
                #one_iter.append(percent_diff(transformed_individual[item], element[item]))
                #print transformed_individual[item]
                #print "element[item]"
                #print element[item]
                #print "abs percent diff"
                #print abs(percent_diff(transformed_individual[item], element[item]))
                if abs(percent_diff(transformed_individual[item], element[item])) < 5 :
                    count = count + 1
                    #if count > threshold:
                    #    positive = positive + 1
                    #    count = 0
                    #print positive
        #return float(positive) / self.data_size
        #return float(positive) 
        #print one_iter
        #print "count"
        #print count
        total_items = self.num_signals * self.data_size
        val = float(count) / total_items
        return val


    def sus_sampler(self, fitness_list):
        size = len(fitness_list)
        total_fitness = reduce(operator.add, fitness_list)

        if total_fitness == 0.0:
            print "total_fitness == 0"
            sel_prob_list = fitness_list
        else:
            sel_prob_list = [x/ total_fitness for x in fitness_list]
        summed_prob_list = []
        for i in xrange(1, len(sel_prob_list) + 1):
            summed_prob_list.append(reduce(operator.add, sel_prob_list[:i]))
        #print summed_prob_list
            

        i = 0
        r = random.uniform(0, 1.0/size)
        mating_pool = []
        while len(mating_pool) <= size -1:
            while r < summed_prob_list[i]:
                mating_pool.append(self.population[i])
                r = r + 1.0/size
            i += 1
        self.population = mating_pool

    def mutation(self):
        for individual in self.population:
            individual.mutate(self.pm)

    def crossover(self):
        for i in xrange(0, self.size, 2):
            self.population[i].crossover_2way(self.population[i+1], self.pc)


