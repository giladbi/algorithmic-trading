#Generates a Histogram
#Rahul Ramakrishnan


import json
import os


#first_dir = '/Users/rahulramakrishnan/Desktop/Trial_1_Dataset'
#second_dir = '/Users/rahulramakrishnan/Desktop/Trial_2_Dataset'
#third_dir = '/Users/rahulramakrishnan/Desktop/Trial_3_Dataset'
#first_dir = '/Users/rahulramakrishnan/OneDrive/Academia/Stochastic Optimization/Algorithmic_Trading_Data/Tournament Selection Data/T_S_Trial_1'
#second_dir = '/Users/rahulramakrishnan/OneDrive/Academia/Stochastic Optimization/Algorithmic_Trading_Data/Tournament Selection Data/T_S_Trial_2'
#third_dir = '/Users/rahulramakrishnan/OneDrive/Academia/Stochastic Optimization/Algorithmic_Trading_Data/Tournament Selection Data/T_S_Trial_3'

mean_histogram = { 0 : 0, 
	      	   100 : 0,
	           1000 : 0, 
              	   10000 : 0,
	      	   100000 : 0, 
              	   1000000 : 0,
	      	   10000000 : 0, 
	      	   100000000 : 0, 
	           1000000000 : 0 }

best_histogram = { 0 : 0,  
              	   100 : 0,
              	   1000 : 0,  
              	   10000 : 0,
              	   100000 : 0,  
              	   1000000 : 0,
              	   10000000 : 0,  
              	   100000000 : 0,  
              	   1000000000 : 0 } 

files = []
for root, dirs, filenames in os.walk(third_dir):
	for f in filenames:
		files.append(open(os.path.join(root, f), 'r'))

mean_histogram_file = open('./mean_histo_3.txt', 'w')
best_histogram_file = open('./best_histo_3.txt', 'w')

for i in range(1, len(files)):
	for line in files[i]:	
		words = line.split(' ')
		mean = words[0]
		best = words[1]	
	
		mean_num = float(mean)
		best_num = float(best)
	
	 	if mean_num >= 0 and mean_num < 100:		
			mean_histogram[0] += 1
		elif mean_num >= 100 and mean_num < 1000:	
			mean_histogram[100] += 1
		elif mean_num >= 1000 and mean_num < 10000:
			mean_histogram[1000] += 1
		elif mean_num >= 10000 and mean_num < 100000:
			mean_histogram[10000] += 1
		elif mean_num >= 100000 and mean_num < 1000000:
			mean_histogram[100000] += 1
		elif mean_num >= 1000000 and mean_num < 10000000:
			mean_histogram[1000000] += 1
		elif mean_num >= 10000000 and mean_num < 100000000:
			mean_histogram[10000000] += 1
		elif mean_num >= 100000000 and mean_num < 1000000000:
			mean_histogram[100000000] += 1	
		elif mean_num >= 1000000000:
			mean_histogram[1000000000] += 1

		if best_num >= 0 and best_num < 100:
                	best_histogram[0] += 1
                elif best_num >= 100 and best_num < 1000:
                	best_histogram[100] += 1
                elif best_num >= 1000 and best_num < 10000:
                	best_histogram[1000] += 1
                elif best_num >= 10000 and best_num < 100000:
                	best_histogram[10000] += 1
                elif best_num >= 100000 and best_num < 1000000:
                	best_histogram[100000] += 1
                elif best_num >= 1000000 and best_num < 10000000:
                	best_histogram[1000000] += 1
                elif best_num >= 10000000 and best_num < 100000000:
                	best_histogram[10000000] += 1
                elif best_num >= 100000000 and best_num < 1000000000:
                	best_histogram[100000000] += 1  
                elif best_num >= 1000000000:
                	best_histogram[1000000000] += 1

json.dump(mean_histogram, mean_histogram_file)
json.dump(best_histogram, best_histogram_file)

	
