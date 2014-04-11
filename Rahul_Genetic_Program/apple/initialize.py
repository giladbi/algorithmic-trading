#Rahul Ramakrishnan
#module: initialize

from tree import Node
from tree import Tree
import scrape 

from random import choice
from random import sample

'''
	Initialization 
	Functions and Wrappers
'''
#Initialize genetic tree population
def initializePopulation(number_of_trees):
	population = []
	for i in xrange(0, number_of_trees):
		tree = initializeGeneticTree()
		population.append(tree)
	return population

#Initializes a genetic tree with 
#the specified number of nodes
def initializeGeneticTree(number_of_nodes):	
	tree = Tree()
	decision = ['left', 'right']
	for i in range(0,number_of_nodes):
		createRandomNodes(tree.root, decision)
	fillGeneticTree(tree.root)
	return tree 

#Traverse the binary tree and adds a pair 
#of left and right nodes in a random place
def createRandomNodes(root, decision):
        chosen = choice(decision)
        if(chosen == 'left' and root.left == None):
                root.left = Node('l')
		root.right = Node('r')
        elif(chosen == 'right' and root.right == None):
                root.right = Node('r')
		root.left = Node('l')
        else:
                if(chosen == 'left'):
                        createRandomNodes(root.left, decision)
                else: #chosen = 'right'
                        createRandomNodes(root.right, decision)


#Insert terminal and functional nodes into the
#genetic tree. 
def fillGeneticTree(root):
	#Load terminal list with terminal nodes
	terminal = scrape.getTerminal()
	#Load functional list with functional nodes
	functional = scrape.getFunctional()	
	
	#Keeps track of functional and terminal
	#list positions
	terminal_index = 0
	functional_index = 0

	stack = []
	stack.append(root)

	temp_terminal = sample(terminal, len(terminal))      #shuffle terminal
	temp_functional = sample(functional,len(functional)) #shuffle functional

	#While loop ensures that initial population
	#are filled with atleast one of each type of functional node
	#and one of each type of terminal node	
	while(len(stack) > 0):		
		current = stack.pop()	

		if(current.left == None and current.right == None):
			#Node is a leaf, insert terminal node
			current.value = temp_terminal[terminal_index]
			terminal_index += 1
		else:   #Node is not a leaf, insert a functional node
			current.value = temp_functional[functional_index]
			functional_index += 1

		#Resets indices if out of bounds
		if terminal_index == len(temp_terminal):
			terminal_index = 0  
		if functional_index == len(temp_functional):
			functional_index = 0
		
		temp_node = current.right		
		if temp_node != None:
			stack.append(temp_node) #stack.push

		temp_node = current.left
		if temp_node != None:
			stack.append(temp_node) #stack.push

