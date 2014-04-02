#Rahul Ramakrishnan
#Stochastic Optimization
#Algorithmic Trading Script

'''
	TO DO:
	1. Fix initialization of tree -----------Done
	2. Fix mutation -------------------------Done
	3. Fix recombination --------------------Done
	   a. Add P_mutation (i.e. .3)
	   b. Add P_recombination (i.e. .4)
	4. Complete data scraping ---------------Will Finish Tonight (trivial)
	5. Complete fitness function ------------Will Finish Tonight
	   a. Find a way to turn a string--------Eval, finally found an example 
	      online, will finish tonight
	      into symbols so you can use the function
	6. Test on test data--------------------Tomorrow
	7. Find a visualization tool to show----Done, however, how can 
	   I include lines from parents to corresponding children the tree
'''


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
apple_tree_2 = GP.initializeGeneticTree(3)


