import parse
import client
import jbdata

secutities = jbdata.secutities
averages = {}
def initalializeSecuritiesDict():
    for sec in parse.getTickers():
        SECURITIES[sec] = []

def calculateMovingAverage(length):
