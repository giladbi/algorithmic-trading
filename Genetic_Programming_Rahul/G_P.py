#Primary Author: Rahul Ramakrishnan
#Algorithmic Trading
#Genetic Programming

import random
import math

#Node Class
class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None


#Genetic Program Tree Class
class GP_Tree(object):
	#During initialization process
	#Randomly select
	functional_nodes = ['+', '-', '/', '%', '*', '^']
	#if conditions 
	

	#Initializes the G_P Binary Tree
	#and creates the root node
	def __init__(self, name, limit=100):
		self.name = name
		self.root = Node(value)
		self.size = 1
		self.limit = limit
		self.fitness = 0.0

	def add_Left(self, value):
		node = Node(value)
		pass

	def add_Right(self, value):
		node = Node(value)
		pass

	def random_Tree(self):
		pass
		#Create a balanced Tree
		#Ramped half and half
		#500 -> fixed depth, 
		#Width is determined by functions



#Genetic Program Functions

#Fitness function
def fitness_Function(GP_Tree):
	pass




#Mutation functions
def peform_Mutation(GP_Tree):
	#randomly chooses between
	#insertion, deletion
	pass

def delete_Mutate(GP_Tree):
	pass

def insert_Mutate(GP_Tree):
	pass



#Crossover functions
def perform_Crossover(GP_Tree_1, GP_Tree_2):
	pass




#Reproduction functions
def perform_Mutations(GP_Tree_1, GP_Tree_2):
	pass



#Initialize Random Population
def initialize_Random_Population(size):
	for i in range(0,size):
		gp_tree = GP_Tree()
		gp_tree.random_Tree()
		population.append(gp_tree)

#Population
population = []
dice_roll = ['mutate', 'crossover', 'reproduction']

#if (random.choice(dice_roll)


