import csv
with open('t.csv', 'rb') as f:
    reader = csv.reader(f)
    l = list(reader)
for line in l:
	if(line[0]=="church"):
		print(line[0],line[1])

