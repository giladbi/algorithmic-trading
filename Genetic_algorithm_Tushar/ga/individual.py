
# import range related functions
# import representation related functions

import operator
from random import randint as ri
from random import uniform as ru
class Individual:
    def __init__(self, number_of_signals, bit_length = 16):
        self.rep = ""
        #self.signal_range = signal_ranges(datasets)
        for i in xrange(number_of_signals):
            random_val =  bin(ri(0, 2 ** bit_length))[2:]
            random_val = random_val.zfill(bit_length)
            self.rep = self.rep + random_val 

    def change_individual(self, bit_string):
        if bit_string != None and type(bit_string) is str:
            self.rep = bit_string
        else:
            print "incorrect input"


    def transform_individual(self, signal_ranges):
        """ Takes a list of 2 tuples defining the signal ranges and scales the binary string to the appropriate value
        """
        num_signals = len(signal_ranges)
        repr_size = len(self.rep)
        n = repr_size / num_signals

        individual_signals = [self.rep[i:i+n] for i in xrange(0, len(self.rep), n)] 
        individual_vals = []

        for i in range(num_signals):
            min_val = signal_ranges[i][0]
            max_val = signal_ranges[i][1]
            range_val = abs(max_val - min_val) 
            signal_value = min_val + (range_val * (float(int(individual_signals[i], 2)) / 2 ** n))
            individual_vals.append(signal_value)

        return individual_vals


    
    def mutate(self, mutate_probability):
        l = list(self.rep)
        for i in xrange(len(self.rep)):
            r = ru(0,1)
            if r < mutate_probability:
                if l[i] == '1':
                    l[i] = '0'
                elif l[i] == '0':
                    l[i] = '1'
                

        self.rep = "".join(l)


    def crossover_2way(self, other_parent, crossover_probability):
        l1 = len(self.rep)
        l2 = len(other_parent.rep)
        if l1 == l2:
            p1 = self.rep
            p2 = other_parent.rep
            point = ri(0,l1 - 1) 
            tmp1 = p1[point:]
            tmp2 = p2[point:]
            p1 = p1[:point] + tmp2
            p2 = p2[:point] + tmp1
            # used parent replaces children survivor selection
            self.change_individual(p1)
            other_parent.change_individual(p2)
        else:
            print "length of both parents must be equal"

