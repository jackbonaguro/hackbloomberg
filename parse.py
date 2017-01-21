import client

USERNAME = "rcb"
PASSWORD = "pass1"
def getTickers():
    secList = []
    sec_str = client.run(USERNAME, PASSWORD, "SECURITIES").split(" ")
    i = 1
    while i in range(len(sec_str)):
        secList.append(sec_str[i])
        i += 4
    return secList


TICKERS = getTickers()

def myCash():
    myCashSt = client.run(USERNAME, PASSWORD, "MY_CASH")
    myCash = myCashSt.split(' ')
    myCash = float(myCash[1])
    # print(myCash)
    return myCash


def mySecurities():
    securities = {}
    mySecSt = client.run(USERNAME, PASSWORD, "MY_SECURITIES")
    mySec = mySecSt.split(' ')
    for tick in TICKERS:
        ind = mySec.index(tick)
        securities[tick] = (int(mySec[ind + 1]), float(mySec[ind + 2]))
    # print(securities)
    return securities



def myOrders():
    myOrdersSt = client.run(USERNAME, PASSWORD, "MY_ORDERS")
    myOrders = myOrdersSt.split(' ')[1:]
    orders = []
    # print(myOrders)
    i = 0
    while i in range(len(myOrders)):
        orders.append((myOrders[i], myOrders[i + 1], float(myOrders[i + 2]), int(myOrders[i + 3])))
        i += 4

    # print(orders)
    return orders

def securities():
    securities = {}
    secSt = client.run(USERNAME, PASSWORD, "SECURITIES")
    sec = secSt.split(' ')
    # print(sec)
    for tick in TICKERS:
        ind = sec.index(tick)
        securities[tick] = (float(sec[ind + 1]), float(sec[ind + 2]), float(sec[ind + 3]))
    # print(securities)
    return securities


def orders(security):
    myOrdersSt = client.run(USERNAME, PASSWORD, "ORDERS " + str.upper(security))
    myOrders = myOrdersSt.split(' ')[1:]
    orders =[]
    i = 0
    while i in range(len(myOrders)):
        orders.append((myOrders[i], float(myOrders[i + 2]), int(myOrders[i + 3])))
        i += 4
    # print(orders)
    return orders



def bid(ticker, price, shares):
    return client.run(USERNAME, PASSWORD, "BID " + str.upper(ticker) + " " + str(price) + " " + str(shares))

def ask(ticker, price, shares):
    return client.run(USERNAME, PASSWORD, "ASK " + str.upper(ticker) + " " + str(price) + " " + str(shares))

def clearBid(ticker):
    return client.run(USERNAME, PASSWORD, "CLEAR_BID " + str.upper(ticker))

def clearAsk(ticker):
    return client.run(USERNAME, PASSWORD, "CLEAR_ASK " + str.upper(ticker))

def subscribe():
    return client.run(USERNAME, PASSWORD, "SUBSCRIBE")

def subscribe():
    return client.run(USERNAME, PASSWORD, "UNSUBSCRIBE")

def close():
    return client.run(USERNAME, PASSWORD, "CLOSE_CONNECTION")
