#Rahul Ramakrishnan
#Custom module for pulling terminal data
#from sources including: .csv file

import random


#Could use yield here
def get_Terminal():
	terminal = ['Open', 'High', 'Low', 'Volume', 'DOW', 'S&P']
	#Add 10 random coefficients into terminal list
	#to be used when applying operators on signals
	for i in range(0,10):
		random_integer = random.randint(-5, 5)
		terminal.append(random_integer * random.random())	

	return terminal

def get_Functional():
	#Need to add more operators
	#like cube root 
	functional = ['+' , '/', '*', '-', '^']
	return functional
