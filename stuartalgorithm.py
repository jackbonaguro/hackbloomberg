import sys
import client
import parse
import time


class stuartalgorithm():


    def __init__(self):
        self.tickers = ["AMZN", "DIS", "FB", "GOOGL" , "IBM","IVW", "KING", "KO", "NFLX","TSLA"]
        self.main()

    def main(self):

        groups = {"AMZN" : [], "DIS" : [], "FB" : [], "GOOGL" : [], "IBM" : [],
            "IVW" : [], "KING" : [], "KO" : [], "NFLX" : [],"TSLA" : []}

        try:
            #algorithim run time (seconds)
            k = 0

            #used to identify successful bids
            prevSecurities = parse.mySecurities()
            currSecurities = ""


            while k < 5:
                currSecurities = parse.mySecurities()
                newtransactions = findNewTransactions(currSecurities, prevSecurities)
                k = k + 1
                time.sleep(1)
                prevSecurities = currSecurities
        except:
            print("lose")


    def findNewTransactions(self,currSecurities, prevSecurities):
        print("searching for new transactions...")
        #calculate difference in the 2
        #for ticker in self.tickers:



        return -1


if __name__ == '__main__':
  prof = stuartalgorithm()
