import client

USERNAME = "rcb"
PASSWORD = "pass1"

def myCash():
    print(client.run(USERNAME, PASSWORD, "MY_CASH"))

def mySecurities():
    print(client.run(USERNAME, PASSWORD, "MY_SECURITIES"))

def myOrders():
    print(client.run(USERNAME, PASSWORD, "MY_ORDERS"))

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
