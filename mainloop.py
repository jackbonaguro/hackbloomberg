import parse
import client
import time
import data
import averages

for tick in parse.TICKERS:
	averages[tick] = []

def mainloop():
	try:
		data.tickers = parse.getTickers()
		for t in data.tickers:
			data.my_securities[t] = []
			data.securities[t] = []

			data.averages[t] = []
			data.prices[t] = []
			data.my_orders[t] = []
		running = True
		while(running):
			starttime = time.time()
			
			#Update data from server
			ms = parse.mySecurities()
			for t in data.tickers:
				data.my_securities[t].append(ms[t])
			s = parse.securities()
			for t in data.tickers:
				data.securities[t].append(s[t])
			for t in data.tickers:
				data.prices[t] = stufunctions.bidAskMarket(t)
				data.averages[t] = averages.getAverages(t)

			#Run algorithm

			#Execute Trades

			#Wait for 1 sec
			while((time.time() - starttime) < 1):
				pass
			print("Loop")
	except:
		pass

mainloop()
