import parse
import client
import time
import averages
from averages import data
import data
import algorithm
import stufunctions

for tick in parse.TICKERS:
	data.averages[tick] = []

def mainloop():
	maintime = time.time()
	try:
		data.tickers = parse.getTickers()
		try:
			for t in data.tickers:
				data.cash = parse.myCash()
				try:
					data.my_securities[t] = []
				except:
					print(1)
				try:
					data.securities[t] = []
				except:
					print(2)
				try:
					data.averages[t] = []
				except:
					print(3)
				try:
					data.prices[t] = []
					data.averages[t] = []
				except:
					print(4)
		except:
			print("Init failed")
		running = True
		while(running):
			if(time.time() - maintime > 10):
				running = False
			starttime = time.time()

			try:
				#Update data from server
				try:
					ms = parse.mySecurities()
					for t in data.tickers:
						data.my_securities[t].append(ms[t])
				except:
					print(1)
				try:
					s = parse.securities()
					for t in data.tickers:
						data.securities[t].append(s[t])
				except:
					print(2)
				try:
					for t in data.tickers:
						try:
							data.prices[t].append(stufunctions.bidAskMarket(t))
						except:
							print("Price calc failed")
						try:
							data.averages[t].append(averages.getAverages(t, int(data.a1), int(data.a2), int(data.a3)))
						except:
							print("Average calc failed")
				except:
					print(3)
			except:
				print("Data download failed")
			#Run algorithm

			try:
				data.a1 = data.a1 * 1.01
				data.a1 = data.a1 * 1.01
				data.a1 = data.a1 * 1.01
				orders = algorithm.algorithm(data.tickers, data.prices, data.averages, data.cash)
			except:
				print("Algo failed")

			#Execute Trades
			try:
				stufunctions.executeTrades(orders)
			except:
				print("Ordering failed")
			#Wait for 1 sec
			while((time.time() - starttime) < 1):
				pass
			print("Loop")
	except:
		print("Main loop failed")

mainloop()
