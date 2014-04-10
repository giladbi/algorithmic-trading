#Rahul Ramakrishnan
#module: recombination 

'''
	Mutation & Crossover
	Functions and Wrappers 
'''
from random import choice
from random import random

'''
	Mutation
'''
def performMutation(population):
	m_probability = 1.0
	for tree in xrange(0, len(population)):
		dice_roll = random()
		if (dice_roll < m_probability):
			mutate(population[tree].root)	

def mutate(root):
	#Choose to swap terminal or functional nodes
	node_type = choice(['t', 'f'])
	if(node_type == 't'): #(terminal node)
		t_node_values = findRandomNodes(root,1)
		v_1 = choice(t_node_values)
		#remove from pool
		t_node_values.remove(v_1)
		v_2 = choice(t_node_values)
		#Retrieve node references
		node_1 = DFS(root, v_1)
		node_2 = DFS(root, v_2)
		#print "Mutation: swapping %s with %s" %(node_1.value, node_2.value)
		swapValues(node_1, node_2)
	else: #type == 'f' (functional node)
		f_node_values = findRandomNodes(root,2)
		#Safeguards against a one element f_node
		if (len(f_node_values) > 1):
			v_1 = choice(f_node_values)
			#remove from pool
			f_node_values.remove(v_1)
			v_2 = choice(f_node_values)
			#Retrieve node references
			node_1 = DFS(root, v_1)
			node_2 = DFS(root, v_2)
			swapValues(node_1, node_2)				


'''
	Crossover
'''
def performCrossover(population):
	c_probability = .5 
	size = len(population)
	print "Inside performCrossover, size: %d " %(size)
	for i in xrange(0, size, 2):
		if(random() < c_probability):
			crossover(population[i].root, population[i+1].root)
		#	if(population[i].root != population[i+1].root):
		#		crossover(population[i].root, population[i+1].root)		

def crossover(root_1, root_2):
        #Find random functional node value in tree 1
        f_1_node_values = findRandomNodes(root_1,2)
        v_1 = choice(f_1_node_values)
        f_2_node_values = findRandomNodes(root_2,2)
        v_2 = choice(f_2_node_values)
        #Retrieve node references               
        n_1 = DFS(root_1, v_1)
        n_2 = DFS(root_2, v_2)
        #Swap subtrees
        swapValues(n_1, n_2)
	print "Crossover: Swapping %s with %s" %(n_1.value, n_2.value)
        swapNodes(n_1, n_2)


'''
	Wrappers
'''
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

