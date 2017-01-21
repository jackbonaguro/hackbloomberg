import parse
import client
import time
import data

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

			#Run algorithm

			#Execute Trades

			#Wait for 1 sec
			while((time.time() - starttime) < 1):
				pass
			print("Loop")
	except:
		pass

mainloop()