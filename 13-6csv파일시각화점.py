from matplotlib import pyplot as plt
import csv

infile=open("./csvfiles/weather.csv","r", encoding='utf-8')
data = csv.reader(infile)

data_list = list(data)
x=[row[0] for row in data_list[1:]]
y=[float(row[1]) for row in data_list[1:]]
infile.close()

#이후에 시각화
plt.plot(x, y, 'o-b', mec='blue', mfc='blue')

plt.rcParams['font.family']='Malgun Gothic'
plt.title('2022년 서울 월평균 강수량')
plt.xlabel('월')
plt.ylabel('강수량(mm)')

