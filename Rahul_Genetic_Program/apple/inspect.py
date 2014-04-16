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

from termcolor import colored


#Prints Trees Level by Level
def printTreePopulation(population):
	map(lambda tree: printTree(tree), population)

#Prints Trees by their Equation (in-order)
def printEquationPopulation(population, generation):
	size = len(population)
	equation_dict = {}
	#print (colored("Size of population: %d", 'blue') %(len(population)))
	
        for tree in population:
		path = []
                recombination.loadPaths(tree.root, path)
                equation = fitness.createEquation(path)
                error = fitness.fitnessValue(tree)
		if equation not in set(equation_dict.keys()):
			equation_dict[equation] = {}
			equation_dict[equation][error] = 1
		else:
			equation_dict[equation][error] += 1
		
	#Output Generation Number
	first_part = colored("\nGENERATION: %d ", 'magenta') %(generation)
	boundary = "=" * 100
	second_part = colored(boundary, 'magenta')
	print first_part + second_part
	
	#Sort based on value of dictionary
	sorted_equation = sorted(equation_dict.iteritems(), key=lambda x: x[1])
	for i, equation_and_error in enumerate(sorted_equation):
		for j in range(0, equation_and_error[1].values()[0]):
			equation = (colored("%s", 'green') %(equation_and_error[0]))
			error = (colored("Fitness: %s", 'blue') %(equation_and_error[1].keys()[0]))
			print equation + " === " + error
	
	#To compare against average fitness
	population_fitness = map(lambda x: x.fitness, population)
	best_fitness = min(population_fitness)
	avg_fitness = sum(population_fitness)/float(size)
	output_avg_fitness = colored("Mean Fitness: %f", 'yellow') %(avg_fitness)	
	output_best_fitness = colored("Best Fitness: %f", 'red') %(best_fitness)
	print output_avg_fitness + "\n" + output_best_fitness

					
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
        printTree(apple_tree_1.root)
        print "Tree 2"
        printTree(apple_tree_2.root)
        recombination.crossover(apple_tree_1.root, apple_tree_2.root)
        print "\nAfter Crossover"
	print "Tree 1"
	printTree(qpple_tree_1)   
	print "Tree 2"
	printTree(apple_tree_2)
       
