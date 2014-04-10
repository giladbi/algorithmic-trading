#Rahul Ramakrishnan
#Stochastic Optimization

#Test Data Convert
def getAppleData():
	#Same thing for nasdaq data as apple
	apple = open('../nasdaq.txt', 'r')
	test_apple = open('./test_apple_data.txt', 'w')	
	for line in apple:
		info = line.split(',')
		apple_open = float(info[1])
		apple_low = float(info[2])
		apple_high = float(info[3])
		apple_volume = float(info[5])
		apple_close_price = apple_volume / 1000 - apple_open / 10 + apple_low - apple_high + 1000  
		print apple_close_price
		new_line = "%s,%s,%s,%s,%s,%s,%s" %(info[0], info[1], info[2], info[3], str(apple_close_price), info[5], info[6])
		test_apple.write(new_line)
		
getAppleData()
