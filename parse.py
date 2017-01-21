import client

TICKERS = ["AMZN", "DIS", "FB", "GOOGL", "IBM", "IVW", "KING", "KO", "NFLX", "TSLA"]
USERNAME = "rcb"
PASSWORD = "pass1"

def myCash():
    myCashSt = client.run(USERNAME, PASSWORD, "MY_CASH")
    myCash = myCashSt.split(' ')
    myCash = float(myCash[1])
    print(myCash)
    return myCash


def mySecurities():
    securities = {"AMZN" : [], "DIS" : [], "FB" : [], "GOOGL" : [], "IBM" : [], "IVW" : [], "KING" : [], "KO" : [], "NFLX" : [],"TSLA" : []}
    mySecSt = client.run(USERNAME, PASSWORD, "MY_SECURITIES")
    mySec = mySecSt.split(' ')
    for tick in securities.keys():
        ind = mySec.index(tick)
        securities[tick] = (int(mySec[ind + 1]), float(mySec[ind + 2]))
    print(securities)
    return securities



def myOrders():
    myOders = []
    myOrdersSt = client.run(USERNAME, PASSWORD, "MY_ORDERS")
    myOrders = myOrdersSt.split(' ')[1:]
    orders = {}
    for tick in TICKERS:
        if tick in myOrders:
            ind = myOrders.index(tick)
            orders[tick] = (myOrders[ind - 1], myOrders[ind + 1], myOrders[ind + 2])

    # print(orders)
    return orders

def securities():
    print(client.run(USERNAME, PASSWORD, "SECURITIES"))

def orders(security):
    print(client.run(USERNAME, PASSWORD, "ORDERS " + str.upper(security)))

def bid(ticker, price, shares):
    print(client.run(USERNAME, PASSWORD, "BID " + str.upper(ticker) + " " + str(price) + " " + str(shares)))

def ask(ticker, price, shares):
    print(client.run(USERNAME, PASSWORD, "ASK " + str.upper(ticker) + " " + str(price) + " " + str(shares)))

def clearBid(ticker):
    print(client.run(USERNAME, PASSWORD, "CLEAR_BID " + str.upper(ticker)))

def clearAsk(ticker):
    print(client.run(USERNAME, PASSWORD, "CLEAR_ASK " + str.upper(ticker)))

def subscribe():
    print(client.run(USERNAME, PASSWORD, "SUBSCRIBE"))

def subscribe():
    print(client.run(USERNAME, PASSWORD, "UNSUBSCRIBE"))

def close():
    print(client.run(USERNAME, PASSWORD, "CLOSE_CONNECTION"))
