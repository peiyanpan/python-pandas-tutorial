from datetime import datetime
now = datetime.now()
print(now)
# 手动创建datetime
t1 = datetime.now()
t2 = datetime(1970, 1, 1)
diff = t1 - t2
print(diff)
print(type(diff))

import pandas as pd
ebola = pd.read_csv('country_timeseries.csv')
# 获取左上角数据
print(ebola.iloc[:5, :5])
print(ebola.info())
# 可以创建新列--date_dt，调用to_datetime方法把Date列转换为datetime后赋给date_dt
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
# 还可以显示指定如何把数据转换为datetime对象。to_datetime函数有一个参数format，允许手动指定日期格式
ebola['date_dt'] = pd.to_datetime(ebola['Date'], format = '%m/%d/%Y')
print(ebola.info())
ebola = pd.read_csv('country_timeseries.csv', parse_dates = [0])
print(ebola.info())

d = pd.to_datetime('2016-02-29')
print(d)
print(type(d))
print(d.year)
print(d.month)
print(d.day)

ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola[['Date', 'date_dt']].head())
ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']].head())

ebola['month'], ebola['day'] = (ebola['date_dt'].dt.month,
                                ebola['date_dt'].dt.day)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']].head())
print(ebola.info())

print(ebola.iloc[-5:, :5])

print(ebola['date_dt'].min())
ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'Day', 'outbreak_d']].head())
print(ebola[['Date', 'Day', 'outbreak_d']].tail())
print(ebola.info())

banks = pd.read_csv('banklist.csv')
print(banks.head())
banks = pd.read_csv('banklist.csv', parse_dates = [5, 6])
print(banks.info())

banks['closing_quarter'], banks['closing_year'] = \
  (banks['Closing Date'].dt.quarter,
   banks['Closing Date'].dt.year)
print(banks.head())
# 可以计算每年破产的银行数量
closing_year = banks.groupby(['closing_year']).size()
print(closing_year)

closing_year_q = banks.groupby(['closing_year', 'closing_quarter']).size()
print(closing_year_q)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()

fig, ax = plt.subplots()
ax = closing_year_q.plot()
plt.show()

