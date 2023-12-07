# import pandas as pd

# data = [41, 92, 91, 20, 29]
# scores = pd.Series(data)

# print(scores)
# print(type(scores))
# print(scores.index)
# print(scores.values)
# print(scores[0])#첫번째?

# data=[[1,2,3], [4,5,6], [7,8,9]]
# print(type(data))

# info={"이름": ["김봄", "오여름", "나가을", "이겨울"],}

import pandas as pd
from matplotlib import pyplot as plt

info=[['김봄', 19, '남자', 3.45], ['오여름', 22, '여자', 4.1], ['송송', 24, '여자', 3.6]]

df = pd.DataFrame(info)

df.columns=['이름', '나이', '성별', '평점']
df1 = df.set_index(keys=['이름'])
print(df)
print(df1)

