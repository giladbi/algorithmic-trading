#Rahul Ramakrishnan
#Stochastic Optimization
#Algorithmic Trading Script

import genetic_program as GP

'''
	Tests
'''
#Testing Mutation
def testMutation(depth):
	apple_tree_1 = GP.initializeGeneticTree(depth)
	print "Before Mutation"
	GP.printTree(apple_tree_1.root)
	GP.mutate(apple_tree_1.root)
	print "After Mutation"
	GP.printTree(apple_tree_1.root)

#Testing Crossover
def testCrossover(depth):
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


#testMutation(3)
#testCrossover(4)

apple_tree_1 = GP.initializeGeneticTree(3)
#apple_tree_2 = GP.initializeGeneticTree(3)
GP.fitnessValue(apple_tree_1.root)
#GP.fitnessValue(apple_tree_2.root)


