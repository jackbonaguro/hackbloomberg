

def algorithm(tickers, prices, averages, cash):
	orders = []
	for t in tickers:
		if(len(averages[t]) <= 5):
			return []
		elif (averages[t][-1][0] > averages[t][-1][1]) and (averages[t][-2][0] < averages[t][-2][1]):
			#Intersections
			flag = False
			for i in range(2):
				if (averages[t][(-i-2)][0] > averages[t][(-i-2)][2]):
					flag = True
			if not flag:
				#bid
				orders.append([t, "BID", (prices[t][-1][1] + .01), (cash/(4*(prices[t][-1][1] * 1.01)))])

		elif (averages[t][-1][0] < averages[t][-1][1]) and (averages[t][-2][0] > averages[t][-2][1]):
			flag = False
			for i in range(2):
				if (averages[t][(-i-1)][0] < averages[t][(-i-1)][2]):
					flag = True
			if not flag:
				#sell
				orders.append([t, "ASK", (prices[t][-1][0] * .99), (cash/(4*(prices[t][-1][0] * .99)))])
	return orders


def buyUp(tickers, prices, averages, cash):
	sum = 0
	orders = []
	for t in tickers:
		sum += (prices[t][-1][1] + .01)
	numToBuy = int((cash*.75)/sum)
	for t in tickers:
		orders.append([t, "BID", (prices[t][-1][1] * 1.01), numToBuy])
	return orders