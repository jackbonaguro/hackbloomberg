import sys
import parse



#average price of all asks and bids for ticker
def bidAskMarket(ticker):
    print("calculating market value per share for ticker: {}".format(ticker))
    orders = parse.orders(ticker)

    askshares = 0
    askpricesum = 0
    bidshares = 0
    bidpricesum = 0

    for order in orders:
        orderType = order[0]
        orderPrice = order[1]
        orderNumShares = order[2]

        if orderType == "BID":
            
        elif orderType == "ASK":
            askshares = askshares + numshares



def checkForOldOrders():
    print("checking for old orders")






#TODO market price




getMarketValue("INTL")
