from matplotlib import pyplot as plt

x = ['커피', '콜라', '사이다', '물']
y1 = [10, 20, 15, 30]
y2 = [20, 15, 20, 35]

plt.rcParams['font.family'] = 'Malgun Gothic'

plt.rcParams['axes.edgecolor']="red"
plt.rcParams['axes.facecolor']="yellow"

plt.plot(x, y1, 'o-b', mec='blue', mfc='blue')
plt.plot(x, y2, 'x:r', mec='red', mfc='red')

plt.title("음료수 종류별 전년대비 판매량")

plt.xlabel("음료수 종류")
plt.ylabel("판매량")

plt.legend(['2022', '2023'])
plt.show()