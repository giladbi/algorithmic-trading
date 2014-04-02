#Rahul Ramakrishnan
#Stochastic Optimization
#Custom module for pulling terminal data
#from sources including: .csv file

import random

#Could use yield here
def get_Terminal():
	terminals = ['apple_open', 'apple_high', 'apple_low', 
		     'apple_close', 'apple_volume', 'dow_open', 
		     'dow_high', 'dow_low', 'dow_close', 
                     'dow_volume']

	#Add 10 random coefficients into terminal list
	#to be used when applying operators on signals

	for i in range(0,10):
		random_integer = random.randint(-5, 5)
		terminals.append(random_integer * random.random())	

	random.shuffle(terminals)	
	return terminals

def get_Functional():
	#Need to add more operators
	#like cube root 
	functionals = ['+' , '/', '*', '-', '^', 'exp', 'log', 'ln']
	random.shuffle(functionals)
	return functionals

