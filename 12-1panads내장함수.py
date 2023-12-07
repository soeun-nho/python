import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./csvfiles/titanic.csv')

print("1. 처음 3개 행 출력:")
print(df.head(3))

print("\n2.최소 운임요금:", df['Fare'].min())

print("\n3.결측치 수:")
print(df.isnull().sum())

print("\n4.생존자 수:")
print(df['Survived'].value_counts()) #숫자 데이터 총 합? 

print("\n5.성별에 따른 생존자 수")
print(df.groupby('Sex')['Survived'].value_counts())

print("\n7.객실 등급별 생존자 수:")
print(df.groupby('Pclass')['Survived'].sum()) #얘는 왜 sum()

# print("\n12.탑승 항구별 승객 수:")
# print(df['Embarked'].value_counts())

print("\n13.가장 적은 티켓을 가진 사람의 정보:") 
least_tickets = df[df['Ticket']==df['Ticket'].value_counts().idxmin()]
print(least_tickets[['Name', 'Ticket']])

print("\n15. 승선 항구별 생존자 비율:")
embarked_survival_rate = df.groupby('Embarked')['Survived'].mean()
print(embarked_survival_rate)
