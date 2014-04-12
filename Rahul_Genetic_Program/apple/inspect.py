#Rahul Ramakrishnan
#module: inspect

'''
        Tree Inspection 
	      &
	Testing Operators
'''

import recombination
import fitness
import initialize

from operator import itemgetter

#Prints Trees Level by Level
def printTreePopulation(population):
	map(lambda tree: printTree(tree), population)

#Prints Trees by their Equation (in-order)
def printEquationPopulation(population):
	size = len(population)
	equation_dict = {}
	print "Size of population in print Equation Population: %d" %(len(population))
	
        for tree in population:
                path = []
                recombination.loadPaths(tree.root, path)
                equation = fitness.createEquation(path)
                error = fitness.fitnessValue(tree)
		equation_dict[equation] = error
	#Sort based on value of dictionary
	sorted_equation = sorted(equation_dict.iteritems(), key=itemgetter(1))
	for i, e_and_f in enumerate(sorted_equation):
		print "%d: %s ===Fitness: %s" %(i,e_and_f[0], e_and_f[1])
	
	#To compare against average fitness
	population_fitness = map(lambda x: x.fitness, population)
	avg_fitness = sum(population_fitness)/float(size)
	print "First Calculated Fitness: %f" %(avg_fitness)

					
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

#Prints the equation
def printEquation(tree):
	path = []
	recombination.loadPaths(tree.root, path)
	equation = fitness.createEquation(path)
	print equation

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
        apple_tree_1 = initialize.initGeneticTree(depth)
        print "Before Mutation"
        printTree(apple_tree_1.root)
        mutate(apple_tree_1.root)
        print "After Mutation"
        printTree(apple_tree_1.root)

#Testing Crossover
def testCrossover():
        depth = 5
        apple_tree_1 = initialize.initGeneticTree(depth)
        apple_tree_2 = initialize.initGeneticTree(depth)
        print "Tree 1"
        #printTree(apple_tree_1.root)
	printEquation(apple_tree_1)
        print "Tree 2"
        #printTree(apple_tree_2.root)
	printEquation(apple_tree_2)

        recombination.crossover(apple_tree_1.root, apple_tree_2.root)
        print "After Crossover"
	#printTree(qpple_tree_1)
        printEquation(apple_tree_1)
	#printTree(apple_tree_2)
        printEquation(apple_tree_2)
