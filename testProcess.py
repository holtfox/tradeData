import csv
import gzip
import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv("new_songs.csv")
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Create minute Panda
minuteData = pd.DataFrame()
minuteData['timestamp'] = pd.date_range('3/1/2019', periods=43200, freq='T')
print data.head()

for index, row in minuteData.iterrows():
	 print(index+4, row['timestamp'])

#print data.loc[data['timestamp'] == "2019-03-01 00:00:05"]

#minuteData.iloc[5,0]
#print data[data.timestamp==minuteData.loc[1,1]]
#merge the data set

# Print to csv
#minuteData.to_csv('minuteData.csv')
#results.to_csv('testData.csv')
