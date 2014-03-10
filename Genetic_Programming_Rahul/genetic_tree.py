#Rahul Ramakrishnan
#Custom module for Genetic Tree
#Requires node class

from genetic_node import Genetic_Node as Node

class Genetic_Tree(object):
	
	#Constructor
	def __init__(self):
		self.root = Node('root') #Initializes root node
		self.size = 1
		self.decision = ['left', 'right']
