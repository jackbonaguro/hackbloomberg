import parse
import client
import time
import averages

avgs = {}
parse.TICKERS
for tick in parse.TICKERS:
	averages[tick] = []

def mainloop():
	running = True
	while(running):
		starttime = time.time()
		#Update data from server

		#Run algorithm
		for tick in parse.TICKERS:
			avgs.append(averages.getAverages(tick))
		#Execute Trades

		#Wait for 1 sec
		while((time.time() - starttime) < 1):
			pass
		print("Loop")

mainloop()
