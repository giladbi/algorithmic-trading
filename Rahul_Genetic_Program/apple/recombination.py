#Rahul Ramakrishnan
#module: recombination 

'''
	Mutation & Crossover
	Functions and Wrappers 
'''
import config
from random import choice
from random import random
from copy import deepcopy

'''
	Mutation
'''
def performMutation(population):	
	for tree in xrange(0, len(population)):
		dice_roll = random()
		if (dice_roll < config.m_probability):
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
	size = len(population)
	#print "Inside performCrossover, size: %d " %(size)
	for i in xrange(0, size, 2):
		if(random() <= config.c_probability):
			crossover(population[i].root, population[i+1].root)		

def crossover(root_1, root_2):

        #Find random functional node value in tree 1
        f_1_nodes = findRandomNodes(root_1,3)
	#f_1_node_values = map(lambda x: x.value, f_1_nodes)
        node_1 = choice(f_1_nodes)
        f_2_nodes = findRandomNodes(root_2,3)
	#f_2_node_values = map(lambda x: x.value, f_2_nodes)
        node_2 = choice(f_2_nodes)
        #Retrieve node references               
        #n_1 = DFS(root_1, v_1)
        #n_2 = DFS(root_2, v_2)

        #Swap subtrees
        swapValues(node_1, node_2)
	#print "Crossover: Swapping %s with %s" %(n_1.value, n_2.value)
        swapNodes(node_1, node_2)


'''
	Wrappers
'''
def findRandomNodes(root, t_or_f=0):	
	nodes = []
	loadPaths(root, nodes, t_or_f)
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
def loadPaths(root, path=[], t_or_f=0):	
	if root == None:
		return
	loadPaths(root.left, path, t_or_f)
	if(t_or_f == 2): #Only append functional nodes
		if(root.left != None and root.right != None):
			path.append(root.value)	
	elif(t_or_f == 1): #Only append terminal Nodes
		if(root.left == None and root.right == None):
			path.append(root.value)
	elif(t_or_f == 3): #Only append functional node REFERENCES
		if(root.left != None and root.right != None):
			path.append(root)
	else: # t_or_f == 0, append all nodes
		path.append(root.value)
	loadPaths(root.right, path, t_or_f)

#Depth first search
def DFS(root, target_value):
        if(root == None):
                return    
        if root.value == target_value:
                return root
        return DFS(root.left, target_value) or DFS(root.right, target_value)

