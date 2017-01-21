import client

USERNAME = "rcb"
PASSWORD = "pass1"

def myCash():
    client.run(USERNAME, PASSWORD, "MY_CASH")

def mySecurities():
    client.run(USERNAME, PASSWORD, "MY_SECURITIES")

def myOrders():
    client.run(USERNAME, PASSWORD, "MY_ORDERS")

def securities():
    client.run(USERNAME, PASSWORD, "SECURITIES")

def orders(security):
    client.run(USERNAME, PASSWORD, "ORDERS " + str.upper(security))

def bid(ticker, price, shares):
    client.run(USERNAME, PASSWORD, "BID " + str.upper(ticker) + " " + str(price) + " " + str(shares))

def ask(ticker, price, shares):
    client.run(USERNAME, PASSWORD, "ASK " + str.upper(ticker) + " " + str(price) + " " + str(shares))

def clearBid(ticker):
    client.run(USERNAME, PASSWORD, "CLEAR_BID " + str.upper(ticker))

def clearAsk(ticker):
    client.run(USERNAME, PASSWORD, "CLEAR_ASK " + str.upper(ticker))

def subscribe():
    client.run(USERNAME, PASSWORD, "SUBSCRIBE")

def subscribe():
    client.run(USERNAME, PASSWORD, "UNSUBSCRIBE")

def close():
    client.run(USERNAME, PASSWORD, "CLOSE_CONNECTION")
