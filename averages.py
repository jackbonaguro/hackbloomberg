import parse
import client

import data

prices = data.prices

def calculateMovingAverage(tick, length):
    if len(prices[tick]) >= length:
        return sum(map(lambda x: x[2], (prices[tick][-length:])))/length
    else:
        return 0

def getAverages(tick, first=1, second=2, third=4):
    return (calculateMovingAverage(tick, first), calculateMovingAverage(tick, second), calculateMovingAverage(tick, third))
