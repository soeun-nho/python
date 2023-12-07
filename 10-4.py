line_counter = 0
weathers = []

with open('csvfiles/weather.csv') as f:
    for data in f:
        data = data.rstrip()
        if not data:
            break
        if line_counter ==0:
            data_header=data.split(",")
        else: 
            weathers.append(data.split(","))
        line_counter+=1
print("Header", data_header)

for i in range(10):
    print(f'data{i} : {weathers[i]}')

# print(weathers)