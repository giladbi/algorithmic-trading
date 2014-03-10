#Rahul Ramakrishnan
#Custom module that operates
#on genetic trees
import random
import data_scrape
from genetic_node import Genetic_Node as Node
import Genetic_Tree as GT #Don't use in this file

decision = ['left', 'right'] #Used for generating random trees

#Traverse the binary tree and adds a pair 
#of left and right nodes in a random place
def create_Random_Nodes(root):
        choice = random.choice(decision)
        if(choice == 'left' and root.left == None):
                root.left = Node('l')
		root.right = Node('r')
        elif(choice == 'right' and root.right == None):
                root.right = Node('r')
		root.left = Node('l')
        else:
                if(choice == 'left'):
                        create_Random_Nodes(root.left)
                else: #choice = 'right'
                        create_Random_Nodes(root.right)

#Traverses the tree in-order
#for viewing purposes
def in_Order_Traversal(root):
	if root == None:
		return
	in_Order_Traversal(root.left)
	print root.value
	in_Order_Traversal(root.right)


#Returns the fitness value of a genetic tree
def fitness_Value(root):
	path = []
	fitness = 0
	fitness_Function(root, path)
	for p in path:
		print p	

#Loads path with the in-order traversal	
def fitness_Function(root, path):
	if root == None:
		return
	fitness_Function(root.left, path)
	path.append(root.value)
	fitness_Function(root.right, path)


#Insert terminal and functional nodes into the
#genetic tree. 
def fill_Genetic_Tree(root):
	#Load terminal list with terminal nodes
	terminal = data_scrape.get_Terminal()
	#Load functional list with functional nodes
	functional = data_scrape.get_Functional()	
	
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


#Depth first search
def DFS(root, target_value):
	if(root == None):
		return 			
	if root.value == target_value:
		return root
	return DFS(root.left, target_value) or DFS(root.right, target_value)
	
