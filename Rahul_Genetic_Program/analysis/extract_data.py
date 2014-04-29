#Extracts Data from Trials
#Rahul Ramakrishnan

import os
first_dir = '/Users/rahulramakrishnan/Desktop/T_S_Trial_1'
#second_dir = '/Users/rahulramakrishnan/Desktop/T_S_Trial_2'
#third_dir = '/Users/rahulramakrishnan/Desktop/T_S_Trial_3'

mean_files = []
best_files = []

for root, dirs, filenames in os.walk(first_dir):
    for f in filenames:
	mean_files.append(open(os.path.join(root, f), 'r'))		
	best_files.append(open(os.path.join(root, f), 'r'))

mean_file = open('./mean.txt', 'w')
best_file = open('./best.txt', 'w')

def multiReadMean(f):
	mean_in_f = []
	for line in f:
		words = line.split(' ')
		mean = words[0]
		mean_in_f.append(mean)
	return mean_in_f

def multiReadBest(f):
	best_in_f = []
	for line in f:
		words = line.split(' ')
		best = words[1]
		best_in_f.append(best)
	return best_in_f


means = map(lambda f: multiReadMean(f), mean_files)
bests = map(lambda f: multiReadBest(f), best_files)

#means = [ [], [], [], [], [] ]

means.pop(0)
bests.pop(0)

final_means = []
for i in range(0, len(means[0])):
	generation_means = map(lambda x: float(x[i]), means)
	final_means.append(min(generation_means))

final_bests = []
for i in range(0, len(bests[0])):
	generation_bests = map(lambda x: float(x[i]), bests)
	final_bests.append(min(generation_bests))

for m in final_means:
	mean_file.write(str(m) +'\n')

for b in final_bests:
	best_file.write(str(b) +'\n')

