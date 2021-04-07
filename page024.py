import pandas as pd
from collections import OrderedDict
scientist = pd.DataFrame(OrderedDict([
  ('name',['Rosaline Franklin','William Gosset']),
  ('Occupation',['Chemist','Statistcian']),
  ('Born',['1920-07-25','1876-06-13']),
  ('Died',['1958-04-16','1937-10-16']),
  ('Age',[37,61])
]))
print(scientist)

scientist = pd.DataFrame(
  data={
    'Occupation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]
  },
  index=['Rosaline Franklin','William Gosset'],
  columns=['Occupation','Born','Died','Age'] 
)
print(scientist)
# 行索引选择
first_row = scientist.loc['William Gosset']
print(type(first_row))
print(first_row)
print(first_row.index)
print(first_row.values)
print(first_row.keys())
print(first_row.index[0])

ages = scientist['Age']
print(ages)
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())