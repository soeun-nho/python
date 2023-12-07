import pandas as pd

data=[41,24,3,42,1]
scores = pd.Series(data)
print(scores)
print(scores.index)
print(scores.values)
print(scores[0])

data=[[1,2,3], [4,5,6], [7,8,9]]
idx = ['첫째행', '둘째행', '셋째행']
colum = ['컬럼1', '컬럼2', '컬럼3']

df1= pd.DataFrame(data, columns=colum)
print(df1)

print(df1.shape)

info = {"이름" : ["김봄", "오여름", "나가을", "이겨울"],
        "나이" : [19, 22, 20, 26],
        "성별": ["남자", "여자", "남자", "여자"],
        "평점": [3.45, 4.1, 3.9, 4.5] 
        }

df2 = pd.DataFrame(info)
print(df2)

print(df2.columns)
print(df2.values)
print(df2['이름'])

df2.columns=['Name', 'Age' ,'Sex', 'Grade']
print(df2) 

no=pd.Series(['101', '102', '103', '104'])
df3 = df2.set_index(keys=no)

print(df3)
print(df2['Grade'])
df2['Grade']=0

print(df2['Grade'])
df2['what']=[1,2,3,4]
print(df2)

print(df2[['Name','Grade']])

print(df2[0:3])

print("\n이름이 인덱스가 되도록 바꾸기")
df3=df2.set_index(keys='Name')
print(df3)

print(df3.loc['김봄']) 
print(df3.loc['김봄':'나가을'])

print(df3.loc['김봄', '나가을'], ['Age','Sex'])