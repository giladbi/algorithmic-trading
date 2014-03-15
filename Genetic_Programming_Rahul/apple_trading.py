#Rahul Ramakrishnan
#Algorithmic Trading Script

import genetic_program as GP
from genetic_tree import Genetic_Tree as GT

apple_tree = GT()

for i in range(0,10):
	GP.create_Random_Nodes(apple_tree.root)
GP.fill_Genetic_Tree(apple_tree.root)
GP.in_Order_Traversal(apple_tree.root)
