#Rahul Ramakrishnan
#module: scrape
'''
	1. Scrapes stock data
	2. Structures data
	3. Returns data
'''

import datetime
import random

#Could use a generator, yield
def getTerminal():
	
	terminals = ['apple_open', 'apple_high', 'apple_low', 
		     'apple_close', 'apple_volume', 'nasdaq_open', 
		     'nasdaq_high', 'nasdaq_low', 'nasdaq_close', 
                     'nasdaq_volume', 'sp500_open', 'sp500_high', 
		     'sp500_low', 'sp500_close', 'sp500_volume']

	#Add 10 random coefficients into terminal list
	#to be used when applying operators on signals
	for i in range(0,15):
		random_integer = random.randint(-500, 500)
		number = random_integer * random.random()
		#Protect against divide by zero
		if(number == 0):
			number = .0001
		terminals.append(number)	

	random.shuffle(terminals)	
	return terminals

def getFunctional():
	functionals = ['+' , '/', '*', '-']	
	#Will add math.exp, math.log, math.ln, math.e	
	random.shuffle(functionals)
	return functionals

def getNasdaqData():
	#Open file reading stream
	nasdaq = open('/Users/rahulramakrishnan/OneDrive/Projects/algorithmic-trading/Rahul_Genetic_Program/data/nasdaq.txt', 'r')
	#Training dates
	begin_date = datetime.date(2011, 01, 01)	
	end_date = datetime.date(2013, 12, 31)
	#Set up data structor to store the data
	nasdaq_data = []
	#Parse file
	for line in nasdaq:
		info = line.split(',')		
		date = info[0]	
		year = int(date[:4]) 
		month = int(date[5:7]) 
		day = int(date[8:10])
	        current = datetime.date(year, month, day)	
		#Financial Placeholder for current data
		finance_dict = {}
		#Check data date
		if current >= begin_date and current <= end_date:
			#Store financial data
			finance_dict["nasdaq_open"] = float(info[1])
			finance_dict["nasdaq_low"] = float(info[2])
			finance_dict["nasdaq_high"] = float(info[3])
			finance_dict["nasdaq_close"] = float(info[4])
			finance_dict["nasdaq_volume"] = float(info[5])
			#Storing financial data in the list
			nasdaq_data.append(finance_dict)	
	return nasdaq_data	


def getAppleData():	
	apple = open('/Users/rahulramakrishnan/OneDrive/Projects/algorithmic-trading/Rahul_Genetic_Program/data/apple_stock.txt', 'r')
	begin_date = datetime.date(2011, 01, 01)
	end_date = datetime.date(2013, 12, 31)
	apple_data = []
	for line in apple:
		info = line.split(',')
		date = info[0]
		year = int(date[:4]) 
		month = int(date[5:7]) 
		day = int(date[8:10])
		current = datetime.date(year, month, day)	
		finance_dict = {}
		if current >= begin_date and current <= end_date:
			finance_dict["apple_open"] = float(info[1])
			finance_dict["apple_low"] = float(info[2])
			finance_dict["apple_high"] = float(info[3])
			finance_dict["apple_close"] = float(info[4])
			finance_dict["apple_volume"] = float(info[5])
			apple_data.append(finance_dict)
	return apple_data		


def getSP500Data():
        sp500= open('/Users/rahulramakrishnan/OneDrive/Projects/algorithmic-trading/Rahul_Genetic_Program/data/sp_500.txt', 'r')
        begin_date = datetime.date(2011, 01, 01) 
        end_date = datetime.date(2013, 12, 31) 
        sp500_data = []
        for line in sp500:
                info = line.split(',')
                date = info[0]
                year = int(date[:4]) 
                month = int(date[5:7]) 
                day = int(date[8:10])
                current = datetime.date(year, month, day)    
                finance_dict = {}
                if current >= begin_date and current <= end_date:
                        finance_dict["sp500_open"] = float(info[1])
                        finance_dict["sp500_low"] = float(info[2])
                        finance_dict["sp500_high"] = float(info[3])
                        finance_dict["sp500_close"] = float(info[4])
                        finance_dict["sp500_volume"] = float(info[5])
                        sp500_data.append(finance_dict)
        return sp500_data


