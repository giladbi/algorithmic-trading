
_in = open('./APPLE_STOCK.csv', 'r')
out = open('./apple_stock.txt','w')

lines = []

for line in _in:
	lines.append(line)

lines.reverse()

for line in lines:
	out.write(str(line))

	
