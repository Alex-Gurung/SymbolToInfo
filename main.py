from yahoo_finance import Share

inp = open('input.txt', 'r')
out = open('output.txt', 'w')
for line in inp:
	temp = Share(line)
	temp.refresh()
	out.write(line.rstrip("\n") + "," + temp.get_price() + "," + temp.get_change() + "\n")
	#FORMAT:  Symbol, last closing price, last change
temp = Share('FUSVX')
print(temp.get_stock_exchange())