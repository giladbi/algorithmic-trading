#Rahul Ramakrishnan
#Stochastic Optimization
#Genetic Program Module

import random
import config
import data_scrape
from genetic_node_tree import Node 
from genetic_node_tree import Tree

'''
	Initialization Functions
	and Wrappers
'''
#Initialize genetic tree population
def initializePopulation(number_of_trees):
	population = []
	for i in xrange(0, number_of_trees):
		tree = initializeGeneticTree(5)
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
def performMutation(population):
	m_probability = .8		
	for tree in xrange(0, len(population)):
		dice_roll = random.random()
		if (dice_roll < .8):
			mutate(population[tree].root)

def mutate(root):
	#Choose to swap terminal or functional nodes
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
		swapValues(node_1, node_2)
	else: #type == 'f' (functional node)
		f_node_values = findRandomNodes(root,2)
		#Safeguards against a one element f_node
		if (len(f_node_values) > 1):
			v_1 = random.choice(f_node_values)
			#remove from pool
			f_node_values.remove(v_1)
			v_2 = random.choice(f_node_values)

			#Retrieve node references
			node_1 = DFS(root, v_1)
			node_2 = DFS(root, v_2)
			swapValues(node_1, node_2)				

def performCrossover(population):
	c_probability = .8
	for tree in xrange(0, len(population)):	
		if (random.random() < c_probability):
			one = random.choice(population)
			two = random.choice(population)
		 	if(one != two):
				crossover(one.root, two.root)
		
def crossover(root_1, root_2):
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
        swapValues(n_1, n_2)
        swapNodes(n_1, n_2)


def findRandomNodes(root, a_t_f=0):	
	nodes = []
	loadPaths(root, nodes, a_t_f)	
	return nodes

def swapValues(node_1, node_2):
	temp_value = node_1.value
	node_1.value = node_2.value
	node_2.value = temp_value

def swapNodes(node_1, node_2):
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
#Replaces path with data
def nodeReplace(path):
	terminal = data_scrape.getTerminal()	
	for t in terminal:
		if (type(t) == type('str')):
			if t in path:	
				#t_i = path.index(t)			
				#indices = filter(for i,x in enumerate(path) if x == t, path)
				indices = [i for i,x in enumerate(path) if x == t]	
				if t[0] == 'a':
					for index in indices:
						path[index] = "apple_data[i]['%s']" %(t)
				else: #nasdaq
					for index in indices:
						path[index] = "nasdaq_data[i]['%s']" %(t)	
				

#Calculate the fitness value of a single GP tree
#and stores it in the tree object
def fitnessValue(tree):
        path = []    
        fitness = 0 
	_sum_of_errors = 0
        loadPaths(tree.root, path)

	#Load market data	
	apple_data = data_scrape.getAppleData()	
	nasdaq_data = data_scrape.getNasdaqData()
		
	for i in xrange(0, len(apple_data)-1):	
		nodeReplace(path)
		equation = createEquation(path)	
		predicted_price = eval(equation)
		actual_price = apple_data[i+1]['apple_close']
		error = abs(actual_price - predicted_price)
		_sum_of_errors += error	

	total = float(len(apple_data)-1)	
	fitness = _sum_of_errors/total
	tree.fitness = fitness		
		
def createEquation(path):
	path_str = ""
	for node in path:
		path_str += str(node) + " "
	return path_str

def roulletteWheel(population):
	#Sort in descending order by fitness(error) highest error --> lowest error
	sorted_pop = sorted(population, key=lambda tree: tree.fitness, reverse=True)
	#Sum Ranks
	total = len(population)
	_rank_sum = reduce(lambda x,y: x+y, xrange(0, total))
	#Assign probability
	probabilities = map(lambda i: (i+1)/float(_rank_sum), xrange(0, total))
	#Generate intervals
	roulletteWheel = []
	for i,p in enumerate(probabilities):
		if i = 0:
			roulletteWheel[0] = probabilities[0]
		else:
			roulletteWheel[i] = roulletteWheel[i-1] + probabilities[i] 
	
		
	return roulletteWheel	

def parentSelection(roulletteWheel):	
	for i in xrange(0, config.population_size):
		pass	
		#FILL IN THIS SHIT RIGHT HERE
	new_pop = []
	for i in xrange(0, config.population_size):
		chosen = random.choice(roulletteWheel)
		new_pop.append(chosen)	
	return new_pop
							
def averageFitness(population):
	_sum = 0
	for tree in population:	
		_sum += tree.fitness
	avg_fitness = _sum / float(len(population))
	print "Average Fitness: %f" %(avg_fitness)	
	return avg_fitness

def generateFitnesses(population):
	for tree in xrange(0, len(population)):
                fitnessValue(population[tree])


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
	print "\n\n-----Tree Level by Level--- Depth of Tree: %d" %(depth(root))
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


#Testing Mutation
def testMutation():
	depth = 4
        apple_tree_1 = GP.initializeGeneticTree(depth)
        print "Before Mutation"
        printTree(apple_tree_1.root)
        mutate(apple_tree_1.root)
        print "After Mutation"
        GP.printTree(apple_tree_1.root)

#Testing Crossover
def testCrossover():
	depth = 4
        apple_tree_1 = GP.initializeGeneticTree(depth)
        apple_tree_2 = GP.initializeGeneticTree(depth)
        print "Tree 1"
        GP.printTree(apple_tree_1.root) 
        print "Tree 2"
        GP.printTree(apple_tree_2.root)
        GP.crossover(apple_tree_1.root, apple_tree_2.root)      
        print "After Crossover"
        GP.printTree(apple_tree_1.root)
        GP.printTree(apple_tree_2.root)
