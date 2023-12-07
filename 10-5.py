import csv

f = open('csvfiles/weather.csv')
data = csv.reader(f)
cnt = 0 

print(data)
header = next(data)

for row in data:
    if cnt <10:
        print(f'data : {row}')
    else: 
        break
    cnt+=1
f.close()
