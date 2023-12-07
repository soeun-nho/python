from matplotlib import pyplot as plt

x=[1,2,3,4]
y=[10,5,6,12]

plt.plot(x,y,'*:r', ms=20, mec='r',mfc='y')

plt.rcParams['font.family'] = 'Malgun Gothic'

plt.title("분기별 커피 판매량")
plt.xlabel("분기")
plt.ylabel("판매")
plt.legend(['커피'])
plt.show()


