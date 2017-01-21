import sys
import parse



#returns (average bid price, average ask price, average market share price)
def bidAskMarket(ticker):
    #print("calculating market value per share for ticker: {}".format(ticker))
    orders = parse.orders(ticker)
    bid = 0
    ask = 0
    market = 0

    numBidShares = 0
    numAskShares = 0
    totalShares = 0

    for order in orders:
        orderType = order[0]
        orderPrice = order[1]
        orderNumShares = order[2]

        if orderType == "BID":
            bid+= (orderPrice * orderNumShares)
            market+= (orderPrice * orderNumShares)
            numBidShares+= orderNumShares
            totalShares+= orderNumShares
        elif orderType == "ASK":
            ask+= (orderPrice * orderNumShares)
            market+= (orderPrice * orderNumShares)
            numAskShares+= orderNumShares
            totalShares+= orderNumShares

    if numBidShares > 0:
        bidAvgPerShare = bid / numBidShares
    else:
        bidAvgPerShare = -1

    if numAskShares > 0:
        askAvgPerShare = ask / numAskShares
    else:
        askAvgPerShare = -1

    if totalShares > 0:
        markAvgPerShare = market / totalShares
    else:
        markAvgPerShare = -1

    return (bidAvgPerShare, askAvgPerShare, markAvgPerShare)

#trades - [(ticker, type,  price, shares)]
def executeTrades(trades):
    print("executing trades")
    for trade in trades:
        ticker = trade[0]
        price = trade[2]
        shares = trade[3]
        if trade[1] == "BID":
            parse.bid(ticker, price, shares)
        elif trade[1] == "ASK":
            parse.ask(ticker, price, shares)
            
def calcNetWorth(securities, cash):
    total = 0
    for s in securities:
        total += s[0]*s[1]
    total += cash
    return total