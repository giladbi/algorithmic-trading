#Rahul Ramakrishnan
#Custom module for pulling terminal data
#from sources including: .csv file

import random

def get_Terminal():
	terminal = [Open, High, Low, Volume, DOW, S&P]
	#Add 10 random coefficients into terminal list
	#to be used when applying operators on signals
	for i in range(0,10):
		random_integer = random.randInt(-10, 10)
		termain.append(random_integer * random.random())	

	return terminal

def get_Functional():
	#Need to add more operators
	#like cube root 
	functional = ['+' , '/', '*', '-', '^']
	return functional
