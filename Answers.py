import pandas as pd

#For question 1


df = pd.read_excel("people.xlsx")

df1 = df['age'].min()

#For question 2

df2 = df['age'].mean()



#For question 3

df3 = df['name'].count()


#For question 4

df4 = df['age'].sum()


#For question 5

df5 = df.loc[(df['gender'] == 'M')]
grouped = df5.groupby('gender')


#For question 6

df6 = df.loc[(df['age'] > 20)]
grouped2 = df6.groupby('age')


#For question 7

df7 = df.loc[(df['age'] > 17) | (df['age'] < 35)]
grouped3 = df7.groupby('age')


#For question 8

df8 = df.loc[(df['age'] == 9) | (df['age'] == 16) & (df['age'] == 25) | (df['age'] == 36) | (df['age'] == 49)]
grouped4 = df8.groupby('age')


#For question 9

df9 = df.loc[(df['gender'] == 'F')]
grouped5 = df9.groupby('name')


#For question 10

df10 = df.loc[(df['gender'] == 'F')]
grouped6 = df10.groupby('gender')



#For question 11

df11 = df.loc[(df['gender'] == 'M') & (df['name'] != 'Tal')]
grouped7 = df11.groupby('gender')



#For question 12

df12 = df['name'].unique()


#For question 13

df13 = df.groupby('name')


#For question 14
df14 = df.loc[(df['gender'] == 'M')]
grouped8 = df14.groupby('gender')



#For question 15
df15 = df.groupby('name')


#For question 16
df16 = df.loc[(df['name'] != 'Tal')]
grouped9 = df16.groupby('gender')



#For question 17
df17 = df.loc[(df['name'] == 'Ido') | (df['name'] == 'Shani')]
grouped10 = df17.groupby('name')


#For question 18
df18 = df.loc[(df['age'] >= 20) & (df['age'] <= 30)]


#For question 19
df19 = df.loc[(df['age'] < 20) & (df['age'] > 30)]



#For question 20
df20 = df.loc[(df['gender'] == 'F') & (df['age'] == 20) | (df['age'] <= 30)]


#For question 21
df21 = df.groupby('gender')
#print(df21['age'].mean())



#For question 22
df22 = df.groupby('gender')
#print(df21['age'].max())


#For question 23
df23 = df.groupby('birth_date')
#print(df23.count())


#For question 24
df24 = df.birth_date.value_counts()
df24 = df24[df24 > 1]
#print(len(df24.index))



#For question 25
df25 = df.name.value_counts()
df25 = df25[df25 > 1]
#print(df25)
