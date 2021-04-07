import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
# 输出原始的行数
print(tips.shape)
print(tips['size'].value_counts())

tips_filtered = tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
print(tips_filtered.shape)
print(tips_filtered['size'].value_counts())

tips_10 = sns.load_dataset('tips').sample(10, random_state = 42)
print(tips_10)

grouped = tips_10.groupby('sex')
print(grouped)

print(grouped.groups)

# 计算各列的平均值
avgs = grouped.mean()
print(avgs)
# 获取Female分组
female = grouped.get_group('Female')
print(female)

for sex_group in grouped:
  print(sex_group)

for sex_group in grouped:
  # 获取对象的类型（元祖）
  print('the type is: {}\n'.format(type(sex_group)))
  # 获取对象的长度（两个元素）
  print('the length is: {}\n'.format(len(sex_group)))
  # 获取第一个元素
  first_element = sex_group[0]
  print('the first element is: {}\n'.format(first_element))
  # 第一个元素的类型（字符串）
  print('it has a type of: {}\n'.format(type(sex_group[0])))
  # 获取第二个元素
  second_element = sex_group[1]
  print('the second element is: \n{}\n'.format(second_element))
  # 获取第二个元素的类型（DataFrame）
  print('it has a type of: {}\n'.format(type(second_element)))
  # 输出sex_group
  print('what we have:')
  print(sex_group)
  # 迭代第一次后停止
  break
# 按照sex和time计算平均值
bill_sex_time = tips_10.groupby(['sex', 'time'])
group_avg = bill_sex_time.mean()
print(group_avg)

# group_avg的类型
print(type(group_avg))
print(group_avg.columns)
print(group_avg.index)

group_method = tips_10.groupby(['sex', 'time']).mean().reset_index()
print(group_method)

group_param = tips_10.groupby(['sex', 'time'], as_index = False).mean()
print(group_param)

intv_df = pd.read_csv('epi_sim.txt')
# 总行数超过900万
print(intv_df.shape)

print(intv_df.head())

count_only = intv_df.\
  groupby(['rep', 'intervened', 'tr'])['ig_type'].\
  count()
print(count_only.head(n = 10))

print(type(count_only))
# 传入[0,1,2]代表分别指定第1级、第2级和第3级索引操作
count_mean = count_only.\
  groupby(level = [0, 1, 2]).\
  mean()
print(count_mean.head(n = 10))

count_mean = intv_df.\
  groupby(['rep', 'intervened', 'tr'])['ig_type'].\
  count().\
  groupby(level = [0, 1, 2]).\
  mean()

import matplotlib.pyplot as plt
fig = sns.lmplot(x = 'intervened', y = 'ig_type', hue = 'rep', col = 'tr',
                 fit_reg = False, data = count_mean.reset_index())
plt.show()

cumulative_count = intv_df.\
  groupby(['rep', 'intervened', 'tr'])['ig_type'].\
  count().\
  groupby(level = ['rep']).\
  cumsum().\
  reset_index()
fig = sns.lmplot(x = 'intervened', y = 'ig_type', hue = 'rep', col = 'tr',
                 fit_reg = False, data = cumulative_count)
plt.show()