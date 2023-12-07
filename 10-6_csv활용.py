import csv

f=open('csvfiles/weather.csv')
data = csv.reader(f)
min = 1000

for row in data:
    if float(row[3]) < min:
        min = row[3]

for row in data:
    if row[3] == min:
        print(f'data: {row}')

f.close()