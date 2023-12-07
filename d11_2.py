import pandas as pd

data = {
    '이름': ['신짱구', '최자두', '코난', '맹구'],
    '국어':[10,100,20,30],
    '영어': [13,20,40,70],
}

print(type(data))

df1 = pd.DataFrame(data)
print(df1)