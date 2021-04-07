# 导入并使用pandas_datareader从网络中获取数据
import pandas as pd
import pandas_datareader as pdr

# 获取Tesla的股票信息
# tesla = pdr.get_data_yahoo('TSLA')

# 保存获取的股票信息
# 无须再依赖网络
# 加载保留的股票信息文件
tesla = pd.read_csv('tesla_stock_yahoo.csv', parse_dates = [0])

print(tesla.head())
print(tesla.tail())

print(tesla.loc[(tesla.Date.dt.year == 2010)&\
                (tesla.Date.dt.month == 6)])
# 把Date列作为索引
tesla.index = tesla['Date']
print(tesla.index)
print(tesla['2015'].iloc[:5, :5])
print(tesla['2010-06'].iloc[:, :5])

tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()
# 然后把timedelta指派给index
tesla.index = tesla['ref_date']
print(tesla.iloc[:5, :5])
print(tesla['0 day': '5 day'].iloc[:5, :5])

ebola = pd.read_csv('country_timeseries.csv',
                    parse_dates = [0])
print(ebola.iloc[:5, :5])
print(ebola.iloc[-5:, :5])

hand_range = pd.date_range(start = '2014-12-31', end = '2015-01-05')
print(hand_range)

ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']
ebola_5.reindex(hand_range)
print(ebola_5.iloc[:, :5])

# 2017年1月1日这周所有的工作日
print(pd.date_range('2017-01-01', '2017-01-07', freq = 'B'))

# 从2017年1月1日这周隔一天取一个工作日
print(pd.date_range('2017-01-01', '2017-01-07', freq = '2B'))
print(pd.date_range('2017-01-01', '2017-12-31', freq = 'WOM-1THU'))
print(pd.date_range('2017-01-01', '2017-12-31', freq = 'WOM-3FRI'))

import matplotlib.pyplot as plt
ebola.index = ebola['Date']
fig, ax = plt.subplots()
ax = ebola.plot(ax = ax)
ax.legend(fontsize = 7,
          loc = 2,
          borderaxespad = 0.)
plt.show()

ebola_sub = ebola[['Day', 'Cases_Guinea', 'Cases_Liberia']]
print(ebola_sub.tail(10))

ebola = pd.read_csv('country_timeseries.csv',
                    index_col = 'Date',
                    parse_dates = ['Date'])
print(ebola.head().iloc[:, :4])

print(ebola.tail().iloc[:, :4])
new_idx = pd.date_range(ebola.index.min(), ebola.index.max())
print(new_idx)
new_idx = reversed(new_idx)
# 重建索引
ebola = ebola.reindex(new_idx)

print(ebola.head().iloc[:, :4])
print(ebola.tail().iloc[:, :4])
last_valid = ebola.apply(pd.Series.last_valid_index)
print(last_valid)
# 获取数据集中最早的日期
earliest_date = ebola.index.min()
print(earliest_date)
shift_values = last_valid - earliest_date
print(shift_values)
ebola_dict = {}
for idx, col in enumerate(ebola):
  d = shift_values[idx].days
  shifted = ebola[col].shift(d)
  ebola_dict[col] = shifted
# 有了这个字典，就可以使用Pandas DataFrame函数把它转换成DataFrame
ebola_shift = pd.DataFrame(ebola_dict)
# dict对象是无序的，但可以传入原来的ebola列来重排这些值
ebola_shift = ebola_shift[ebola.columns]
print(ebola_shift.tail())

ebola_shift.index = ebola_shift['Day']
ebola_shift = ebola_shift.drop(['Day'], axis = 1)
print(ebola_shift.tail())

down = ebola.resample('M').mean()
print(down.iloc[:5, :5])

up = down.resample('D').mean()
print(up.iloc[:5, :5])

import pytz
print(len(pytz.all_timezones))
# 输出美国的时区
import re
regex = re.compile(r'^US')
selected_files = filter(regex.search, pytz.common_timezones)
print(list(selected_files))
# 东部时间上午7点
depart = pd.Timestamp('2017-08-29 7:00', tz = 'US/Eastern')
print(depart)
arrive = pd.Timestamp('2017-08-29 09:57')
print(arrive)
arrive = arrive.tz_localize('US/Pacific')
print(arrive)
# 再把时区转换为东部时区
print(arrive.tz_convert('US/Eastern'))

# 计算航班飞行时间
duration = arrive.tz_convert('US/Eastern') - depart
print(duration)