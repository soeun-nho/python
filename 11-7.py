import pandas as pd

file_path='csvfiles/titanic.csv'
df = pd.read_csv(file_path)
print(df)

t_c_backup=df.copy()
df.to_csv('t_c_backup.csv')

df.info()

print(df.describe())
print(df.loc[0])

df1=df.sort_values(by=['Fare'],axis=0)
print(df1)

df2=df.sort_index(axis=1)
print(df2)

print(df['Survived'].value_counts())

print(df.pivot_table(['Survived'], index=['Sex', 'Pclass']))