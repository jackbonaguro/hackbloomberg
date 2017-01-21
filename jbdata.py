import sys
import client
import parse
import time

my_securities = []
securities = []

"""sec_str = parse.securities().split(" ")
for i in range(len(sec_str)):
	1 + i*
print(sec_str)"""

i = 0
while i < 60:
	mysecurities.append(parse.mySecurities())
	securities.append(parse.securities())
	time.sleep(1)

print(list(map(lambda x: x['AMZN'][0], mysecurities)