#Rahul Ramakrishnan
#Stochastic Optimization



#Genetic Node Class
class Node(object):
        #Constructor for Node object
        def __init__(self, value=None):
                self.value = value
                self.left = None
                self.right = None    


#Genetic Tree Class
class Tree(object):	
	#Constructor
	def __init__(self):
		#Initializes root node
		#Will be overwritten
		self.root = Node('root') 
		self.size = 1
		self.decision = ['left', 'right']
		self.fitness = None
