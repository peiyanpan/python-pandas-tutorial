import pandas as pd
scientist = pd.read_csv('scientists.csv')
ages = scientist['Age']
print(ages)
print(ages.describe())
print(ages.mean())
print(ages[ages>ages.mean()])
print(ages>ages.mean())
print(type(ages[ages>ages.mean()]))
manual_bool_values = [True,True,False,False,True,True,False,True]
print(ages[manual_bool_values])
print(ages + ages)
print(ages * ages)
print(ages + 100)
print(ages * 2)
print(ages + pd.Series([1,100]))
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)
print(ages * 2)
print(ages + rev_ages)
print(scientist[scientist['Age'] > scientist['Age'].mean()])
# print(scientist.loc[[True, True, False, True]])

first_half = scientist[:4]
second_half = scientist[4:]
print(first_half)
print(second_half)

print(scientist * 2)

print(scientist['Born'].dtype)
print(scientist['Died'].dtype)

born_datatime = pd.to_datetime(scientist['Born'],format='%Y-%m-%d')
print(born_datatime)
died_datetime = pd.to_datetime(scientist['Died'],format='%Y-%m-%d')
scientist['born_dt'],scientist['died_dt'] = (born_datatime,died_datetime)
print(scientist.head())
print(scientist.shape)

print(scientist['Age'])
import random
random.seed(42)
random.shuffle(scientist['Age'])

print(scientist['Age'])
# 使用random_state减少随机化
scientist['Age'] = scientist['Age'].\
  sample(len(scientist['Age']), random_state = 24).\
         reset_index(drop = True)
# 把Age列打乱两次
print(scientist['Age'])

print(scientist.columns)
scientist_dropped = scientist.drop(['Age'],axis=1)
print(scientist_dropped.columns)

names = scientist['Name']
print(names)
names.to_pickle('scientists_names_series.pickle')
scientist_names_from_pickle = pd.read_pickle('scientists_names_series.pickle')
print(scientist_names_from_pickle)