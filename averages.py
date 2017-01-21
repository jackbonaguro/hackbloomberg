import parse
import client

import data

prices = data.prices

def calculateMovingAverage(tick, length):
    if len(prices[tick]) >= length:
        return sum(prices[tick][-length:])/length
    else:
        return 0

def getAverages(tick, first=10, second=50, third=200):
    return (calculateMovingAverage(tick, first), calculateMovingAverage(tick, second), calculateMovingAverage(tick, third))
