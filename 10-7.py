import csv

with open('csvfiles/weather.csv', 'r', newline='') as f:
    data = csv.reader(f)

    next(data)
    min_temp = 1000
    coldes_day = ""

    for row in data:
        temparature = float(row[3])
        if temparature <min_temp:
            min_temp = temparature
            coldest_day = row[0]

    print(f"가장 추운 온도 : {min_temp}")
    print(f"가장 추운 날{coldest_day}")