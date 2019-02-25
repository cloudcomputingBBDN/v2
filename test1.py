import datetime
import csv
"""
date_text='07-02-2019:51-43-23'
try:
	datetime.datetime.strptime(date_text, '%d-%m-%Y:%S-%M-%H')
	print("valid")
except :
	print("Incorrect data format, should be YYYY-MM-DD")












































"""
from operator import itemgetter
with open('acts.csv', 'rb') as f:
		next(f)
		reader = csv.reader(f)
		l = list(reader)
ll=[]
for line in l:
	if(line[1]=="school"):
		l1=[]
		l1.append(line[0])
		l1.append(line[1])
		l1.append(line[2])
		l1.append(line[3])
		l1.append(line[4])
		l1.append(line[5])
		ll.append(l1)

ll.sort(key=lambda x: x[3][12])
ll.sort(key=lambda x: x[3][11])
ll.sort(key=lambda x: x[3][15])
ll.sort(key=lambda x: x[3][14])
ll.sort(key=lambda x: x[3][18])
ll.sort(key=lambda x: x[3][17])
ll.sort(key=lambda x: x[3][0])
ll.sort(key=lambda x: x[3][1])
ll.sort(key=lambda x: x[3][3])
ll.sort(key=lambda x: x[3][4])
ll.sort(key=lambda x: x[3][3])
ll.sort(key=lambda x: x[3][9])
ll.sort(key=lambda x: x[3][8])
ll.sort(key=lambda x: x[3][7])
ll.sort(key=lambda x: x[3][6])


	
for line in ll:
	print(line[3])
