def algorithm(tickers, prices, averages):
	print(prices[tickers[0]][-1][1] + .1)
	return [[tickers[0], "BID", (prices[tickers[0]][-1][1] + .1), 1]]
