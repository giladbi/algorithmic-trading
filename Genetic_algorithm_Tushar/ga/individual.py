
# import range related functions
# import representation related functions

import operator
import random

from random import randint as ri
from random import uniform as ru

random.seed(1234)

class Individual:
    def __init__(self, number_of_signals, bit_length = 16):
        self.rep = ""
        self.sig_size = bit_length
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

        individual_signals = [ self.rep[i:i+n] for i in xrange(0, len(self.rep), n) ] 
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

        for i in xrange(self.sig_size):
            r = ru(0,1)
            if r < mutate_probability:
                for j in xrange(i,self.sig_size, self.sig_size):
                    if l[j] == '1':
                        l[j] = '0'
                    elif l[j] == '0':
                        l[j] = '1'

        self.rep = "".join(l)


    def crossover_2way(self, other_parent, crossover_probability):
        l1 = len(self.rep)
        l2 = len(other_parent.rep)
        expected_length = 0
        #print "before crossover"
        #print self.rep
        #print other_parent.rep
        if l1 == l2:
            expected_length = l1
            tmp_p1 = ""
            tmp_p2 = ""
            for i in xrange(0, l1 , self.sig_size):
                p1 = self.rep[i: (i+self.sig_size) ]
                p2 = other_parent.rep[i: (i+self.sig_size) ]
                point = ri(0, self.sig_size  - 1) 
                #print point
                tmp1 = p1[point:]
                tmp2 = p2[point:]
                p1 = p1[:point] + tmp2
                p2 = p2[:point] + tmp1
                tmp_p1 = tmp_p1 + p1
                tmp_p2 = tmp_p2 + p2
            #print "After crossover"
            #print tmp_p1
            #print tmp_p2
            # used parent replaces children survivor selection
            if expected_length != 0:
                self.change_individual(tmp_p1.zfill(expected_length))
                other_parent.change_individual(tmp_p2.zfill(expected_length))
            #print "After crossover"
            #print self.rep 
            #print other_parent.rep 
        else:
            print "length of both parents must be equal"

