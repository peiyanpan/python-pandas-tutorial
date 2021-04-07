import pandas as pd

def my_sq(x):
  """
  求平方
  """
  return x ** 2
def avg_2(x, y):
  """求两个数的平均值
  """
  return (x + y) / 2
print(my_sq(4))
print(avg_2(10, 20))

df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})
print(df)
print(df['a'] ** 2)
# 获取第一列
print(type(df['a']))
# 获取第一行
print(type(df.iloc[0]))

sq = df['a'].apply(my_sq)
print(sq)

def my_exp(x, e):
  return x ** e
cb = my_exp(2, 3)
print(cb)

ex = df['a'].apply(my_exp, e = 2)
print(ex)
ex = df['a'].apply(my_exp, e = 3)
print(ex)

def print_me(x):
  print(x)
df.apply(print_me, axis = 0)
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.info())

import numpy as np
# （1）缺失值数目
def count_missing(vec):
  """计算一个向量中缺失值的个数
  """
  # 根据值是否缺失获取一个由True/False值组成的向量
  null_vec = pd.isnull(vec)
  # 得到null_vec中null值的个数
  # null值对应True，True为1
  null_count = np.sum(null_vec)
  # 返回向量中缺失值的个数
  return null_count
# （2）缺失值占比
def prop_missing(vec):
  """向量中缺失值的占比
  """
  # 计算缺失值的个数
  # 计算刚刚编写的count_missing函数
  num = count_missing(vec)
  # 获得向量中元素的个数
  # 也需要统计缺失值的个数

  dem = vec.size
  # 返回缺失值的占比
  return num / dem
# （3）完整值所占比例
def prop_complete(vec):
  """"""
  # 先计算缺失值所占的比例
  # 然后用1减去缺失值的占比
  return 1 - prop_missing(vec)
cmis_col = titanic.apply(count_missing)
pmis_col = titanic.apply(prop_missing)
pcom_col = titanic.apply(prop_complete)
print(cmis_col)
print(pmis_col)
print(pcom_col)

print(titanic.loc[pd.isnull(titanic.embark_town), :])

cmis_row = titanic.apply(count_missing, axis = 1)
pmis_row = titanic.apply(prop_missing, axis = 1)
pcom_row = titanic.apply(prop_complete, axis = 1)
print(cmis_row.head())
print(pmis_row.head())
print(pcom_row.head())
print(cmis_row.value_counts())

titanic['num_missing'] = titanic.apply(count_missing, axis = 1)
print(titanic.head())

df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})
print(df)
def avg_2(x, y):
  return (x + y) / 2
print(avg_2(df['a'], df['b']))
def avg_2_mod(x, y):
  if x == 20:
    return np.NaN
  else:
    return (x + y) / 2
avg_2_mod_vec = np.vectorize(avg_2_mod)
print(avg_2_mod_vec(df['a'], df['b']))
# 为了使用vectorize装饰器， 要在函数定义之前使用@符号
@np.vectorize
def v_avg_2_mod(x, y):
  """当x不等于20时，计算平均值
  和前面一样，但这里只使用的是vectorize装饰器
  """
  if x == 20:
    return np.NaN
  else:
    return (x + y) / 2
# 然后，可以直接使用向量化的函数
# 不必创建新函数
print(v_avg_2_mod(df['a'], df['b']))

import numba
@numba.vectorize
def v_avg_2_numba(x, y):
  """当x不等于20时，计算平均值
  使用numba装饰器"""
  # 现在必须向函数添加类型信息
  if int(x) == 20:
    return np.NaN
  else:
    return (x + y) / 2
# print(v_avg_2_numba(df['a'], df['b']))
print(v_avg_2_numba(df['a'].values, df['b'].values))

docs = pd.read_csv('doctors.csv', header = None)
import regex
p = regex.compile('\w+\s+\w+')
def get_name(s):
  return p.match(s).group()
docs['name_func'] = docs[0].apply(get_name)
print(docs)

docs['name_lamb'] = docs[0].apply(lambda x: p.match(x).group())
print(docs)