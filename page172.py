import pandas as pd
df = pd.read_csv('gapminder.tsv', sep = '\t')
# 计算每年平均预期寿命
avg_life_exp_by_year = df.groupby('year').lifeExp.mean()
print(avg_life_exp_by_year)
avg_life_exp_by_year = df.groupby('year')['lifeExp'].mean()
# 获取数据中年份唯一值的列表
year = df.year.unique()
print(year)
# 遍历每一年取子集
# 针对1952年的数据取子集
y1952 = df.loc[df.year == 1952, :]
print(y1952.head())
y1952_mean = y1952.lifeExp.mean()
print(y1952_mean)
continent_describe = df.groupby('continent').lifeExp.describe()
print(continent_describe)

import numpy as np
# 计算各州的平均预期寿命
# 使用np.mean函数
cont_le_agg = df.groupby('continent').lifeExp.agg(np.mean)
print(cont_le_agg)
cont_le_agg2 = df.groupby('continent').lifeExp.aggregate(np.mean)
print(cont_le_agg2)
def my_mean(values):
  """计算平均值
  """
  # 获得每个数值，用做分母
  n = len(values)
  # 从0开始求和
  sum = 0
  for value in values:
    sum += value
  return sum / n
agg_my_mean = df.groupby('year').lifeExp.agg(my_mean)
print(agg_my_mean)

def my_mean_diff(values, diff_value):
  """计算平均值和diff_value之差
  """
  n = len(values)
  sum = 0
  for value in values:
    sum += value
  mean = sum / n
  return (mean - diff_value)
# 计算全球寿命的平均值
global_mean = df.lifeExp.mean()
print(global_mean)
# 带有多个参数的自定义聚合函数
agg_mean_diff = df.groupby('year').lifeExp.\
  agg(my_mean_diff, diff_value = global_mean)
print(agg_mean_diff)

gdf = df.groupby('year').lifeExp.\
  agg([np.count_nonzero, np.mean, np.std])
print(gdf)

# 对DataFrame使用字典聚合不同列
# 对于每一年，计算平均值lifeExp、中位数pop和中位数gdpPercap
gdf_dict = df.groupby('year').agg({
  'lifeExp': 'mean',
  'pop': 'median',
  'gdpPercap': 'median'
})
print(gdf_dict)

gdf = df.groupby('year')['lifeExp'].\
  agg([np.count_nonzero,
       np.mean,
       np.std]).\
  rename(columns = {'count_nonzero': 'count',
                    'mean': 'avg',
                    'std': 'std_dev'}).\
  reset_index()
print(gdf)

def my_zscore(x):
  """计算给定数据的z分数，是一个向量或序列值
  """
  return ((x - x.mean()) / x.std())
# 然后使用该函数按组转换数据
transform_z = df.groupby('year').lifeExp.transform(my_zscore)
# 输出数据的行数
print(df.shape)
# 转换之后的值的个数
print(transform_z.shape)
# 从scipy.stats导入zscore函数
from scipy.stats import zscore
# 计算分组的zscore
sp_z_grouped = df.groupby('year').lifeExp.transform(zscore)
# 计算非分组的zscore
sp_z_nogroup = zscore(df.lifeExp)
# 分组的z分数
print(transform_z.head())
# 使用SciPy计算得到的分组z分数
print(sp_z_grouped.head())
# 计算非分组的z分数
print(sp_z_nogroup[:5])
import seaborn as sns
import numpy as np
# 设置种子以确定结果
np.random.seed(42)
# 从tips中抽取10行
tips_10 = sns.load_dataset('tips').sample(10)
# 随机抽取4个total_bill值作为缺失值
tips_10.loc[np.random.permutation(tips_10.index)[:4],
            'total_bill'] = np.NaN
print(tips_10)

count_sex = tips_10.groupby('sex').count()
print(count_sex)

def fill_na_mean(x):
  """返回给定向量的平均值
  """
  avg = x.mean()
  return (x.fillna(avg))
# 按sex列计算total_bill的平均值
total_bill_group_mean = tips_10.\
  groupby('sex').\
  total_bill.\
  transform(fill_na_mean)
# 可以在原数据创建新列
# 也可以直接使用total_bill替换原始列
tips_10['fill_total_bill'] = total_bill_group_mean
print(tips_10)
print(tips_10[['sex', 'total_bill', 'fill_total_bill']])