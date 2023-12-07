import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

info=[['김봄', 19, '남자', 3.45], ['오여름', 22,'여자', 4.1], ['나가을', 20, '남자', 3.9], ['이겨울', 26, '여자', 4.5]]

df = pd.DataFrame(info)
df.columns = ['이름', '나이', '성별', '평점']

matplotlib.rcParams['font.family']='Malgun Gothic'
# df.plot(kind='line')
df.plot(kind='line', x='이름', y=['나이', '평점'])
plt.show()