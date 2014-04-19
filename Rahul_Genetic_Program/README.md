Predicting Apple Stock
======================
Evolutionary Computing - Genetic Program
========================================

###Class: Stochastic Optimization
###Professor: Jason Lohn
###Author: Rahul Ramakrishnan

**Description:**
Predicts apple stock price using a genetic program. 
It is trained using 2010-2013 apple and nasdaq data for
now, however, more data will be added soon.


**Quick Start**

*Step 1:*
Install python 2.7 interpretter

```
sudo apt-get install python2.7
```

Install pip (pip installs python):

http://pip.readthedocs.org/en/latest/installing.html


On Linux:
```
sudo apt-get install python-pip
```


Install colors

```
sudo pip install termcolor
```

*Step 2:*
Ensure that Rahul_Genetic_Program/ contains
- a. predict.py
- b. apple/ (package containing modules)
	- config.py
	- tree.py
	- initialize.py
	- scrape.py
	- inspect.py
	- recombination.py
	- selection.py
	- fitness.py
- c. data/ (contains data)
- d. output/ (statistical data outputted)
- e. You can change default parameters in the config.py file


*Step 3:*
```
$ python predict.py
```

*Step 4:*
Populations will be outputted to the screen


**TO DO:**
- Add more signals (S&P, apple tweets, etc.) 
- Fix early convergence from crossover ---------------------------DONE
- Refactor all for loops into map/reduce/filter/scan -------------DONE
- Add colors to output -------------------------------------------DONE
- Add graphs of mean generational error and best fitness----------PROGRESS
- Add best tree output along with average generational error -----DONE

