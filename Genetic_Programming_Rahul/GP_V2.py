#Rahul Ramakrishnan
#Stochastic Optimization
#Homework 3 Program

import random
import math
from itertools import permutations

cities = ['a', 'b', 'c', 'd', 'e', 'f']
distance_matrix = { 'a' : {'b': 12, 'c': 24, 'd': 63, 'e': 3, 'f': 101}, 
					'b' : {'a': 12, 'c': 31, 'd': 9,  'e': 100, 'f': 44},
					'c' : {'a': 24, 'b': 31, 'd': 18, 'e': 28, 'f': 51},
					'd' : {'a': 63, 'b': 9,  'c': 18, 'e': 81, 'f': 15},
					'e' : {'a': 3,  'b': 100,'c': 28, 'd': 81, 'f': 74},
					'f' : {'a': 101,'b': 44, 'c': 51, 'd': 15, 'e': 74} }  

#BRUTE FORCE SEARCH

#This outputs the permutations of a list
#When calculating the path distance we append the first city to the end
#To have a complete path back home

print "--------------------BRUTE FORCE SEARCH INITIALIZE---------------------"

perms = [''.join(p) for p in permutations(cities)]


#Complete the perms by having the last city as the first city
#So the travelling salesman goes home
#Find the distance between cities, and keep track of the minimum
paths = []
min_path = ' '

for p in perms:
	distance = 0
	for i in range(0,6):	#Sum all of the path distances up to get entire distance
		if(i == 5):
			distance += distance_matrix[p[i]][p[0]]
		else:
			distance += distance_matrix[p[i]][p[i+1]]
	paths.append(distance)
	print "Path: %s ------> Distance: %d" % (p + p[0], distance)

#Get the minimum path back
min_path = perms[paths.index(min(paths))] + perms[paths.index(min(paths))][0]	
print "Best path is %s and its Distance is: %d after %d iterations" %(min_path, min(paths), 720)




#GENETIC PROGRAM SEARCH
print "--------------------GENETIC PROGRAM SEARCH INITIALIZE---------------------"

#Global variables
decision = ['left', 'right']
node_list = []
path = []


#TreeNode class
class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None
		self.fitness = None

#Traverse the binary tree and add a Node
#in a random place
def add_Node(root, decision):
	choice = random.choice(decision)
	if(choice == 'left' and root.left == None):
		root.left = Node('l')
	elif(choice == 'right' and root.right == None):
		root.right = Node('r')
	else:
		if(choice == 'left'):
			add_Node(root.left, decision)
		else:
			add_Node(root.right, decision)


#This calculates the fitness of a particular path
def fitness_Value(root, path):
	fitness = 0
	for i in range(0,6):	#Sum all of the path distances up to get entire distance
		if(i == 5):
			fitness += distance_matrix[path[i]][path[0]]
		else:
			fitness += distance_matrix[path[i]][path[i+1]]
	#Reset path list
	path[:] = []
	#Set root fitness for survivor selection
	root.fitness = fitness
	#Return fitness value
	return fitness


#This calculates the path taken so we can apply the 
#fitness value calculation on it
def fitness_Function(root, path):
	if(root == None):
		return
	fitness_Function(root.left, path)
	path.append(root.value)
	fitness_Function(root.right, path)

#Inorder traversal of a binary tree
def in_Order_Traversal(root):
	if(root == None):
		return
	in_Order_Traversal(root.left)
	print root.value 
	in_Order_Traversal(root.right)

#This is for testing purposes
def pre_Order_Traversal(root):
	if(root == None):
		return
	print root.value
	pre_Order_Traversal(root.left) 
	pre_Order_Traversal(root.right)

#Inserts nodes iteratively so we can keep track
#of an index on cities
def pre_Order_Insertion(root, cities):
	index = 0 
	temp_cities = random.sample(cities,6)		#Reshuffle cities
	stack = []
	stack.append(root)
	while(len(stack) > 0):
		current = stack.pop()
		#print current.value
		current.value = temp_cities[index]
		index += 1  			 		#Increment index
		if index == 6:
			index = 0			 		#Reset index if out of bounds
		temp_node = current.right
		if temp_node != None:
			stack.append(temp_node) 	#stack.push
		temp_node = current.left
		if temp_node != None:
			stack.append(temp_node)   	#stack.push

#Find two node values to swap
def mutation_Operation(root, cities):
	choice_1_node = find_Random_Node(root, cities)
	choice_2_node = find_Random_Node(root, cities)
	#print "Swapping " + str(choice_1_node.value) + "   " +  str(choice_2_node.value)
	swap_values(choice_1_node, choice_2_node)
	

def find_Random_Node(root, cities):
	target_value = random.choice(cities)	#Choose a random city to swap
	temp_node = DFS(root, target_value)		#Find that node
	return temp_node


def swap_values(node_1, node_2):
	temp_value = node_1.value
	node_1.value = node_2.value
	node_2.value = temp_value


def DFS(root, target_value):
	if (root == None):
		return
	if root.value == target_value:
		return root
	return DFS(root.left, target_value) or DFS(root.right, target_value)


#Verification that the 100 trees are filled
def verification(population):
	print "In Order Traversal"
	for i in range(0,10):
		in_Order_Traversal(population[i])
		print ' '

#Copy population list into a temporary list
def copy_Population(population , copy_of_population):
	for p in population:
		copy_of_population.append(p)



#Initialize the 10 root nodes and append them to the population list
population = []
for i in range(0,10):
	node = Node(0)	
	population.append(node)

#Add 5 more nodes to each of the 10 trees
for i in range(0,10):
	for j in range(0,5): 
		add_Node(population[i], decision)

#Insert cities into these trees
print "Pre Order Insertion No Recursion"
for i in range(0,10):
	pre_Order_Insertion(population[i], cities)


#List to keep track of fitness Values of current generation
generation_fitness = []
roullette_wheel= []
copy_of_population = []

#100 Generations
for i in range(0,100):
	
	print "Generation:  " + str(i)
	#100 Genetic Program Trees per Generation
	for j in range(0,10):

		#Perform mutations on the populations
		#20% chance of a mutation
		if ( random.random() < float(.2)):
			mutation_Operation(population[j], cities)
		#Perform fitness function
		fitness_Function(population[j], path)
		generation_fitness.append(fitness_Value(population[j], path)) 
		#Perform survivor selection with roullette wheel
		# mu, lambda 
		#Create probability list -> Roullete Wheel of indexes
		#Take the inverse of the fitness beceause we are trying to maximize
		temp_fitness = math.pow(population[j].fitness, -1) * math.pow(10,5)
		number_of_chances = int(temp_fitness)
		#print number_of_chances
		for k in range(0, number_of_chances):
			roullette_wheel.append(j)

	#Copy Population
	copy_Population(population, copy_of_population)
	#print len(roullette_wheel)
	#Shuffle roullete wheel
	random.shuffle(roullette_wheel)
	#Reset population
	population[:] = []
	#Create offspring, next generation
	for l in range(0,10):
		population.append(copy_of_population[random.choice(roullette_wheel)])
	#Reset copy of population
	copy_of_population[:] = []
	#Reset roullette wheel
	roullette_wheel[:] = []

	print "Average Fitness: %f" % (sum(generation_fitness)/float(len(generation_fitness)))
	print "Min fitness: %f" % ( min(generation_fitness) )
	if min(generation_fitness) == 118:
		print "--------------Found GLOBAL OPTIMA! after %d generations" % (i)
		in_Order_Traversal(population[generation_fitness.index(min(generation_fitness))])
		break

	generation_fitness[:] = [] #Reset generation_Fitness








