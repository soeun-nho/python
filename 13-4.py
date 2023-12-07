import matplotlib.pyplot as plt 

ratio = [10,40,20,30]
labels = ['attendance', 'midterm', 'report', 'final']
explode=[0.3,0,0,0]

plt.rcParams['font.family']='Malgun Gothic'
plt.title("평가 비율")
plt.pie(ratio, labels=labels,  autopct='%.1f%%',explode=explode, shadow=True)
plt.show()