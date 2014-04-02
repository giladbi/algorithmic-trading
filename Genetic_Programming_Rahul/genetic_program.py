#Rahul Ramakrishnan
#Stochastic Optimization

import random
import data_scrape
from genetic_node_tree import Node 
from genetic_node_tree import Tree

'''
	Initialization Functions
	and Wrappers
'''
#Initializes a genetic tree with 
#the specified number of nodes
def initializeGeneticTree(number_of_nodes):	
	GT = Tree()
	decision = ['left', 'right']
	for i in range(0,number_of_nodes):
		createRandomNodes(GT.root, decision)
	fillGeneticTree(GT.root)
	
	#return Tree object
	return GT

#Traverse the binary tree and adds a pair 
#of left and right nodes in a random place
def createRandomNodes(root, decision):
        choice = random.choice(decision)
        if(choice == 'left' and root.left == None):
                root.left = Node('l')
		root.right = Node('r')
        elif(choice == 'right' and root.right == None):
                root.right = Node('r')
		root.left = Node('l')
        else:
                if(choice == 'left'):
                        createRandomNodes(root.left, decision)
                else: #choice = 'right'
                        createRandomNodes(root.right, decision)


#Insert terminal and functional nodes into the
#genetic tree. 
def fillGeneticTree(root):
	#Load terminal list with terminal nodes
	terminal = data_scrape.getTerminal()
	#Load functional list with functional nodes
	functional = data_scrape.getFunctional()	
	
	#Keeps track of functional and terminal
	#list positions
	terminal_index = 0
	functional_index = 0

	stack = []
	stack.append(root)

	#shuffle terminal
	temp_terminal = random.sample(terminal, len(terminal)) 
	#shuffle functional
	temp_functional = random.sample(functional,len(functional))

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


'''
	Mutation & Recombination 
	Functions and Wrappers 
'''

def mutate(root):
	#Choose to swap terminal
	#or functional nodes
	node_type = random.choice(['t', 'f'])
	if(node_type == 't'): #(terminal node)
		t_node_values = findRandomNodes(root,1)
		v_1 = random.choice(t_node_values)
		#remove from pool
		t_node_values.remove(v_1)
		v_2 = random.choice(t_node_values)
		#Retrieve node references
		node_1 = DFS(root, v_1)
		node_2 = DFS(root, v_2)
		swap_values(node_1, node_2)
	else: #type == 'f' (functional node)
		f_node_values = findRandomNodes(root,2)
		v_1 = random.choice(f_node_values)
		#remove from pool
		f_node_values.remove(v_1)
		v_2 = random.choice(f_node_values)
		#Retrieve node references
		node_1 = DFS(root, v_1)
		node_2 = DFS(root, v_2)
		swap_values(node_1, node_2)				

def recombination(root_1, root_2):
        #Find random functional node value in tree 1
        f_1_node_values = findRandomNodes(root_1,2)
        v_1 = random.choice(f_1_node_values)
        #Find random functional node value in tree 2
        f_2_node_values = findRandomNodes(root_2,2)
        v_2 = random.choice(f_2_node_values)
        #Retrieve node references               
        n_1 = DFS(root_1, v_1)
        n_2 = DFS(root_2, v_2)
        #Swap subtrees
        swap_values(n_1, n_2)
        swap_nodes(n_1, n_2)


def findRandomNodes(root,a_t_f=0):	
	nodes = []
	loadPaths(root, nodes, a_t_f)	
	return nodes

def swap_values(node_1, node_2):
	temp_value = node_1.value
	node_1.value = node_2.value
	node_2.value = temp_value

def swap_nodes(node_1, node_2):
	temp_left = node_1.left
	temp_right = node_1.right
	node_1.left = node_2.left
	node_1.right = node_2.right
	node_2.left = temp_left
	node_2.right = temp_right

#Loads path with an in-order traversal	
#all, terminal, or functional nodes
def loadPaths(root, path=[], a_t_f=0):	
	if root == None:
		return
	loadPaths(root.left, path, a_t_f)
	if(a_t_f == 2): #Only append functional nodes
		if(root.left != None and root.right != None):
			path.append(root.value)
	elif(a_t_f == 1): #Only append terminal Nodes
		if(root.left == None and root.right == None):
			path.append(root.value)
	else: # a_t_f == 0, append all nodes
		path.append(root.value)
	loadPaths(root.right, path, a_t_f)

#Depth first search
def DFS(root, target_value):
        if(root == None):
                return    
        if root.value == target_value:
                return root
        return DFS(root.left, target_value) or DFS(root.right, target_value)

'''
	Fitness Functions & Wrappers
'''
#Returns the fitness value of a genetic tree
def fitnessValue(root):
        path = []    
        fitness = 0 
        loadPaths(root, path)
        print path 	
	#getAppleData
	#getNasdaqData
	#get length of dataset
	#While not at end of apple_data and nasdaq_data (should be same length)
		#Load into the tree
		#createEquation
			#Find predicted float value
		#Find error between actual price of next day
		#Sum the error
		#loop through both data sets	
	#return the average error
	#store this fitness on the tree object
		

def createEquation(path):
	pass

#iterate through the population getting their fitness
#and storing it into a list
#fitness_values is the list 
#in the same order as the population
#that contains the fitness of the corresponding
#tree
def roulletteWheel(fitness_values):
	pass
#Sum the values
#new list of percentages fitness/sum_fitness
#inverse the this percentage 
#Figure ^^^ out later




'''
	Tree Inspection & Testing Operators
'''
#Depth of a tree
def depth(root):
	if(root == None):
		return 0
	else:
		return 1 + max(depth(root.left), depth(root.right))


#Prints each level
def printTree(root):
	print "\n\n\n-----Tree Level by Level--- Depth of Tree: %d" %(depth(root))
	result = createLeveledTree(root)
	for level_index, level in enumerate(result):
		nodes = []
		for node in level:
			nodes.append(node.value)	
		print str(level_index) + ":  " +  str(nodes)

#Creates a list of levels of a tree
def createLeveledTree(root):
	result = []	
	current = []
	if(root != None):
		current.append(root)
	while (len(current) > 0):
		result.append(current)
		parents = current
		current = []
		for parent in parents:
			if (parent.left != None):
				current.append(parent.left)
			if (parent.right != None):
				current.append(parent.right)
	return result

#Traverses the tree in-order
#for viewing purposes
def inOrderTraversal(root):
	if root == None:
		return
	inOrderTraversal(root.left)
	print root.value
	inOrderTraversal(root.right)



