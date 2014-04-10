#Rahul Ramakrishnan
#Stochastic Optimization
#Test Program Module

'''
        Tree Inspection & Testing Operators
'''

from apple import recombination
from apple import fitness
from apple import initialize
from operator import itemgetter

#Prints Trees Level by Level
def printTreePopulation(population):
        for tree in population:
                printTree(tree)

#Prints Trees by their Equation (in-order)
def printEquationPopulation(population):
	equation_dict = {}
	print "Size of population in print Equation Population: %d" %(len(population))
        for i,tree in enumerate(population):
                path = []
                recombination.loadPaths(tree.root, path)
                equation = fitness.createEquation(path)
                fitness = fitness.fitnessValue(tree)
		equation_dict[equation] = fitness 
	#Sort based on value of dictionary
	sorted_equation = sorted(equation_dict.iteritems(), key=itemgetter(1))
	for i, e_and_f in enumerate(sorted_equation):
		print "%d: %s ===Fitness: %s" %(i,e_and_f[0], e_and_f[1])
	
			
#Depth of a tree
def depth(root):
        if(root == None):
                return 0
        else:
                return 1 + max(depth(root.left), depth(root.right))

#Prints each level
def printTree(tree):
        root = tree.root
        print "-----Tree Level by Level--- Depth of Tree: %d" %(depth(root))
        result = createLeveledTree(root)
        for level_index, level in enumerate(result):
                nodes = []
                for node in level:
                        nodes.append(node.value)
                print str(level_index) + ":  " +  str(nodes)
        print "Tree's Fitness: %f " %(tree.fitness)

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
        apple_tree_1 = initialize.initializeGeneticTree(depth)
        print "Before Mutation"
        printTree(apple_tree_1.root)
        mutate(apple_tree_1.root)
        print "After Mutation"
        printTree(apple_tree_1.root)

#Testing Crossover
def testCrossover():
        depth = 4
        apple_tree_1 = initialize.initializeGeneticTree(depth)
        apple_tree_2 = initialize.initializeGeneticTree(depth)
        print "Tree 1"
        printTree(apple_tree_1.root)
        print "Tree 2"
        printTree(apple_tree_2.root)
        crossover(apple_tree_1.root, apple_tree_2.root)
        print "After Crossover"
        printTree(apple_tree_1.root)
        printTree(apple_tree_2.root)
	print equation_dict.values()
