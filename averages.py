import parse
import client

import data

securities = data.securities

def calculateMovingAverage(tick, length):
    if len(securities[tick]) >= length:
        return sum(securities[tick][-length:])/length
    else:
        return 0

def getAverages(tick, first=10, second=50, third=200):
    return (calculateMovingAverage(tick, first), calculateMovingAverage(tick, second), calculateMovingAverage(tick, third))
