import matplotlib.pyplot as plt

X=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Y=[-8,-5,-3,-4,-1,-10,-7] #y값

plt.title("temparature per week")
plt.bar(X, Y, color='orange', width=0.3)

plt.xlabel("week")
plt.ylabel("temparature")

plt.rc('axes', edgecolor='#0000ff') #axes: 그래프축
plt.rc('axes', facecolor='#ffff00')

# plt.rcParams['axes.edgecolor']="red"
# plt.rcParams['axes.facecolor']="yellow"

plt.show()

plt.rcParams['font.family']='Malgun Gothic'
plt.title('그래프2')
plt.barh(X, Y, color='red')
plt.xlabel('X축 레이블')
plt.ylabel('Y축 레이블')

plt.show()
