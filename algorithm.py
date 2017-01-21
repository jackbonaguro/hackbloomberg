def algorithm(tickers, prices, averages):
	orders = []
	for t in tickers:
		if (averages[t][-1][0] > averages[t][-1][1]) and (averages[t][-2][0] < averages[t][-2][1]):
			flag = False
			for i in range(5):
				if (averages[t][(-i-2)][0] > averages[t][(-i-2)][2]):
					flag = True
			if not flag:
				#bid
				orders.append([t, "BID", (prices[t][-1][1] + .01), 2])
		elif (averages[t][-1][0] < averages[t][-1][1]) and (averages[t][-2][0] > averages[t][-2][0]):
			flag = False
			for i in range(5):
				if (averages[t][(-i-1)][0] < averages[t][(-i-1)][2]):
					flag = True
			if not flag:
				#sell
				orders.append([t, "ASK", (prices[t][-1][0] - .01), 2])
	return orders
