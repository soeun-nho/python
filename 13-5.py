import matplotlib.pyplot as plt
import random

#20개의 랜덤한 숫자 생성
n=20
x=[random.randint(1,10)*10 for i in range(n)] #1~100사이 숫자
y=[random.randint(1,10) for i in range(n)] #1~10사이 숫자

print(x)
print(y)

plt.rcParams['font.family']='Malgun Gothic'
plt.xlabel('점수') 
plt.scatter(x,y)

plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.show()