import csv
import gzip
import pandas as pd
from datetime import datetime

trade_url = "https://public.bitmex.com/?prefix=data/trade/"

url = "https://www.bitmex.com/api/v1/trade?symbol=.ETHUSDPI&count=200&columns=price&reverse=true"
df = pd.read_json(url)
print df.head()

with gzip.open('dataFiles/20190301.csv.gz') as f:
    tradeData = pd.read_csv(f)
    ETHData = tradeData[tradeData['symbol'] == 'ETHUSD']
    
for x in xrange(2,27):
	if x < 10:
		date = "dataFiles/2019030" + str(x) + ".csv.gz"
		with gzip.open(date) as f:
			temp = pd.read_csv(f)
			temp = temp[temp['symbol'] == 'ETHUSD']
			ETHData = ETHData.append(temp)
			print "Eth tail"
			print ETHData.tail(4)
			print "temp tail"
			print temp.tail(4)
	else:
		date = "dataFiles/201903" + str(x) + ".csv.gz"
		with gzip.open(date) as f:
			temp = pd.read_csv(f)
			temp = temp[temp['symbol'] == 'ETHUSD']
			ETHData = ETHData.append(temp)
			print "th tail"
			print ETHData.tail(4)
			print "temp tail"
			print temp.tail(4)


ETHData = ETHData.drop(columns=["tickDirection","trdMatchID","grossValue","homeNotional","foreignNotional"])
ETHData['timestamp'] =  pd.to_datetime(tradeData['timestamp'], format='%Y-%m-%dD%H:%M:%S.%f000')
print ETHData.dtypes

ETHData.to_csv('compiledData.csv')


