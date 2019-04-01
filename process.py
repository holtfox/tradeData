import csv

with open('dataFiles/20190323.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    time = 0
    input_time = 0
    temp_hour = 0
    temp_minute = 0 

    for row in csv_reader:
        if line_count == 0:
#            print('Column names are {", ".join(row)}')
            line_count += 1
        if row["symbol"] == 'ETHUSD':
		input_time = row["timestamp"].split("D")[1].split(".")[0]
		temp_hour = input_time.split(":")[0]
		temp_minute = input_time.split(":")[1]
		input_time = temp_hour + ":" + temp_minute		
		if input_time != time:
			print input_time, ',' , row["price"]
			time = input_time
		        line_count += 1

