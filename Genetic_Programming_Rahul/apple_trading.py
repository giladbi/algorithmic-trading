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

#Initializes one tree with x  nodes
#and fills it with data
#will be random soon


apple_tree_1 = GP.initializeGeneticTree(5)
apple_tree_2 = GP.initializeGeneticTree(5)


print "Testing mutation---------------------\n\n\n"
GP.printTree(apple_tree_1.root)
GP.mutate(apple_tree_1.root)
GP.printTree(apple_tree_1.root)


print "Testing recombination---------------\n\n\n"

GP.printTree(apple_tree_1.root)
GP.printTree(apple_tree_2.root)
GP.recombination(apple_tree_1.root, apple_tree_2.root)
GP.printTree(apple_tree_1.root)
GP.printTree(apple_tree_2.root)











