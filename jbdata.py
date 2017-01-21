import sys
import client
import parse
import time

my_securities = []
securities = []

def getSecNames():
	secList = []
	sec_str = parse.securities().split(" ")
	for i in range(len(sec_str)):
		secList.append(sec_str[1 + i*4])
	return secList

i = 0
while i < 60:
	my_securities.append(parse.mySecurities())
	securities.append(parse.securities())
	time.sleep(1)

print(list(map(lambda x: x['ANR'][0], my_securities)))

def dataloop():
	i = 0
	while i < 30:
		parse.myCash()
		print(parse.mySecurities())
		i += 1
		pass
