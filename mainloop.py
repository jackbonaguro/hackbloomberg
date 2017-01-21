import parse
import client
import time
<<<<<<< HEAD
import data
=======
import averages

avgs = {}
parse.TICKERS
for tick in parse.TICKERS:
	averages[tick] = []
>>>>>>> 9bbb7272e1f1be7884bad02c17f368ae5c2bcdc6

def mainloop():
	try:
		data.tickers = parse.getTickers()
		for t in data.tickers:
			data.my_securities[t] = []
			data.securities[t] = []
			#data.orders[t] = []
			averages = {}
			prices = {}
			my_orders = {}
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
			"""for t in data.tickers:
				o = parse.orders(t)
				data.orders[t] = o"""

<<<<<<< HEAD
			#Run algorithm

			#Execute Trades
=======
		#Run algorithm
		for tick in parse.TICKERS:
			avgs.append(averages.getAverages(tick))
		#Execute Trades
>>>>>>> 9bbb7272e1f1be7884bad02c17f368ae5c2bcdc6

			#Wait for 1 sec
			while((time.time() - starttime) < 1):
				pass
			print("Loop")
	except:
		pass

mainloop()
