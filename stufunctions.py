import sys
import parse



#average price of all asks and bids for ticker
def bidAskMarket(ticker):
    print("calculating market value per share for ticker: {}".format(ticker))
    orders = parse.orders(ticker)

    bid = 0
    ask = 0
    market = 0


    numBidOrders = 0
    numAskOrders = 0
    totalorders = 0

    for order in orders:
        orderType = order[0]
        orderPrice = order[1]
        orderNumShares = order[2]

        if orderType == "BID":
            bid+= (orderPrice * orderNumShares)
            market+= (orderPrice * orderNumShares)
            numBidOrders+=1
            totalorders+=1
        elif orderType == "ASK":
            ask+= (orderPrice * orderNumShares)
            numAskOrders+=1 (orderPrice * orderNumShares)
            totalorders+=1

    if numBidOrders > 0:
        bidAvgPerShare = bid / numBidOrders
    else:
        bidAvgPerShare = -1

    if numAskOrders > 0:
        askAvgPerShare = ask / numAskOrders
    else:
        askAvgPerShare = -1

    if totalorders > 0:
        markAvgPerShare = market / totalorders
    else:
        markAvgPerShare = -1

    return (bidAvgPerShare, askAvgPerShare, markAvgPerShare)


def checkForOldOrders():
    print("checking for old orders")






#TODO market price




bidAskMarket("INTL")
