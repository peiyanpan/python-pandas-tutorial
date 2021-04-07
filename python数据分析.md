# python数据分析

## 第1章   Pandas DataFrame 基础知识

### 1.2 加载数据集

```python
import pandas as pd 
# read_csv:加载csv数据文件
# 把sep参数设置成\t,显示指明使用制表符分隔
df = pd.read_csv('gapminder.tsv',sep='\t') 
# 调用head方法,只显示前五行数据
print(df.head())
'''
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
'''
print(type(df)) # <class 'pandas.core.frame.DataFrame'>
# shape属性指明DataFrame的行数和列数,返回值是一个元祖
print(df.shape) # (1704, 6)
# columns属性获取列名
print(df.columns) # Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='object')
# 获取每列的dtype
print(df.dtypes)
'''
country       object
continent     object
year           int64
lifeExp      float64
pop            int64
gdpPercap    float64
dtype: object
'''
# 获取更多数据信息
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1704 entries, 0 to 1703
Data columns (total 6 columns):
country      1704 non-null object
continent    1704 non-null object
year         1704 non-null int64
lifeExp      1704 non-null float64
pop          1704 non-null int64
gdpPercap    1704 non-null float64
dtypes: float64(2), int64(2), object(2)
memory usage: 80.0+ KB
None
'''
```

| Pandas类型 | Python类型 | 说明                                                     |
| ---------- | ---------- | -------------------------------------------------------- |
| object     | string     | 最常用的数据类型                                         |
| int64      | int        | 整型                                                     |
| float64    | float      | 带小数的数字                                             |
| datetime64 | datetime   | Python标准库包含datetime，但默认不加载，需要导入才能使用 |

### 1.3 查看列、行和单元格

#### 1.3.1 获取列子集

```python
# 1.根据名称获取列子集
# 只获取country列,并将其保存到一个变量中
country_df = df['country']
# 显示前五行
print(country_df.head())
'''
0    Afghanistan
1    Afghanistan
2    Afghanistan
3    Afghanistan
4    Afghanistan
Name: country, dtype: object
'''
# 显示最后五行
print(country_df.tail())
'''
1699    Zimbabwe
1700    Zimbabwe
1701    Zimbabwe
1702    Zimbabwe
1703    Zimbabwe
Name: country, dtype: object
'''
# 查看country,continent,year列
subset = df[['country','continent','year']]
print(subset.head())
'''
       country continent  year
0  Afghanistan      Asia  1952
1  Afghanistan      Asia  1957
2  Afghanistan      Asia  1962
3  Afghanistan      Asia  1967
4  Afghanistan      Asia  1972
'''
print(subset.tail())
'''
       country continent  year
1699  Zimbabwe    Africa  1987
1700  Zimbabwe    Africa  1992
1701  Zimbabwe    Africa  1997
1702  Zimbabwe    Africa  2002
1703  Zimbabwe    Africa  2007
'''
```

#### 1.3.2 获取行子集

| 获取行子集的方法 | 说明                         |
| ---------------- | ---------------------------- |
| loc              | 通过索引标签获取行子集(行名) |
| iloc             | 基于行索引获取行子集(行号)   |

```python
'''
country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
'''
# 左侧是行号(索引标签)
# 获取第一行
# Python从0开始计数
print(df.loc[0])
'''
country      Afghanistan
continent           Asia
year                1952
lifeExp           28.801
pop              8425333
gdpPercap        779.445
Name: 0, dtype: object
'''
# 获取第100行
# Python从0开始计数
print(df.loc[99])
'''
country      Bangladesh
continent          Asia
year               1967
lifeExp          43.453
pop            62821884
gdpPercap       721.186
Name: 99, dtype: object
'''
# 准确获取最后一行
# 通过shape的第一个值获取行数
number_of_rows = df.shape[0]
last_row_Index = number_of_rows - 1
print(df.loc[last_row_Index])
'''
country      Zimbabwe
continent      Africa
year             2007
lifeExp        43.487
pop          12311143
gdpPercap     469.709
Name: 1703, dtype: object
'''
# 通过tail方法返回最后一行
print(df.tail(n=1))
'''
       country continent  year  lifeExp       pop   gdpPercap
1703  Zimbabwe    Africa  2007   43.487  12311143  469.709298
'''
# 选取多行
print(df.loc[0,99,999])
'''
         country continent  year  lifeExp       pop    gdpPercap
0    Afghanistan      Asia  1952   28.801   8425333   779.445314
99    Bangladesh      Asia  1967   43.453  62821884   721.186086
999     Mongolia      Asia  1967   51.253   1149500  1226.041130
'''
```

```python
# 通过行号获取行:iloc
# 获取第2行
print(df.iloc[1])
'''
country      Afghanistan
continent           Asia
year                1957
lifeExp           30.332
pop              9240934
gdpPercap        820.853
Name: 1, dtype: object
'''
# 获取第100行
print(df.iloc[99])
'''
country      Bangladesh
continent          Asia
year               1967
lifeExp          43.453
pop            62821884
gdpPercap       721.186
Name: 99, dtype: object
'''
# 传入-1获取最后一行数据
print(df.iloc[-1])
'''
country      Zimbabwe
continent      Africa
year             2007
lifeExp        43.487
pop          12311143
gdpPercap     469.709
Name: 1703, dtype: object
'''
# 传入多行
print(df.iloc[0,99,999])
'''
         country continent  year  lifeExp       pop    gdpPercap
0    Afghanistan      Asia  1952   28.801   8425333   779.445314
99    Bangladesh      Asia  1967   43.453  62821884   721.186086
999     Mongolia      Asia  1967   51.253   1149500  1226.041130
'''
```

#### 1.3.3 混合

> loc和iloc属性可用于获取列、行或者二者的子集。loc和iloc的一般语法是使用带逗号的方括号。逗号左边是待取子集的行值，逗号右边是待取子集的列值，即df.loc[[行],[列]]或者df.iloc[[行],[列]]

```python
# 1.获取列子集 df.loc[:,[列]]
# 使用loc获取列子集
subset = df.loc[:,['year','pop']]
print(subset.head())
'''
   year       pop
0  1952   8425333
1  1957   9240934
2  1962  10267083
3  1967  11537966
4  1972  13079460
'''
# 使用iloc获取列子集，支持整数
subset = df.iloc[:,[2,4,-1]]
print(subset.head())
'''
   year       pop   gdpPercap
0  1952   8425333  779.445314
1  1957   9240934  820.853030
2  1962  10267083  853.100710
3  1967  11537966  836.197138
4  1972  13079460  739.981106
'''
# 2.通过范围选择列子集
small_range = list(range(5)) # [0,1,2,3,4]
subset = df.iloc[:,small_range]
print(subset.head())
'''
       country continent  year  lifeExp       pop
0  Afghanistan      Asia  1952   28.801   8425333
1  Afghanistan      Asia  1957   30.332   9240934
2  Afghanistan      Asia  1962   31.997  10267083
3  Afghanistan      Asia  1967   34.020  11537966
4  Afghanistan      Asia  1972   36.088  13079460
'''
small_range = list(range(3,6)) # [3,4,5]
subset = df.iloc[:,small_range]
print(subset.head())
'''
   lifeExp       pop   gdpPercap
0   28.801   8425333  779.445314
1   30.332   9240934  820.853030
2   31.997  10267083  853.100710
3   34.020  11537966  836.197138
4   36.088  13079460  739.981106
'''
small_range = list(range(0,6,2)) # [0,2,4] 获取0-6之间的偶数，不包含6
subset = df.iloc[:,small_range]
print(subset.head())
'''
       country  year       pop
0  Afghanistan  1952   8425333
1  Afghanistan  1957   9240934
2  Afghanistan  1962  10267083
3  Afghanistan  1967  11537966
4  Afghanistan  1972  13079460
'''
# 3.使用切片语法获取列子集

subset = df.iloc[:,:3] # 获取前三列
print(subset.head())
'''
       country continent  year
0  Afghanistan      Asia  1952
1  Afghanistan      Asia  1957
2  Afghanistan      Asia  1962
3  Afghanistan      Asia  1967
4  Afghanistan      Asia  1972
'''
subset = df.iloc[:,3:6] # 获取3-5列
print(subset.head())
'''
   lifeExp       pop   gdpPercap
0   28.801   8425333  779.445314
1   30.332   9240934  820.853030
2   31.997  10267083  853.100710
3   34.020  11537966  836.197138
4   36.088  13079460  739.981106
'''
subset = df.iloc[:,0:6:2] # 获0,2,4列
print(subset.head())
'''
       country  year       pop
0  Afghanistan  1952   8425333
1  Afghanistan  1957   9240934
2  Afghanistan  1962  10267083
3  Afghanistan  1967  11537966
4  Afghanistan  1972  13079460
'''
# 4.获取行和列的子集
print(df.loc[42,'country']) # Angola
print(df.iloc[42,0]) # Angola
# 5.获取多行和多列
print(df.iloc([0,99,999],[0,3,5]))
'''
         country  lifeExp    gdpPercap
0    Afghanistan   28.801   779.445314
99    Bangladesh   43.453   721.186086
999     Mongolia   51.253  1226.041130
'''
print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])
'''
         country  lifeExp    gdpPercap
0    Afghanistan   28.801   779.445314
99    Bangladesh   43.453   721.186086
999     Mongolia   51.253  1226.041130
'''
```

### 1.4 分组和聚合计算

```python
# 计算每年的平均寿命
print(df.head(n=10))
'''
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
5  Afghanistan      Asia  1977   38.438  14880372  786.113360
6  Afghanistan      Asia  1982   39.854  12881816  978.011439
7  Afghanistan      Asia  1987   40.822  13867957  852.395945
8  Afghanistan      Asia  1992   41.674  16317921  649.341395
9  Afghanistan      Asia  1997   41.763  22227415  635.341351
'''
```

#### 1.4.1 分组方式(分割-应用-组合)

```python
print(df.groupby('year')['lifeExp'].mean())
'''
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
'''
# groupby用来分组
# 创建一个分组对象
grouped_year_df = df.groupby('year') # 按照年份来分组
print(type(grouped_year_df))
# <class 'pandas.core.groupby.groupby.DataFrameGroupBy'>
print(grouped_year_df) # 返回它所在的内存位置
# <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x000001CDF5372CC0>

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
# <class 'pandas.core.groupby.groupby.SeriesGroupBy'>
print(grouped_year_df_lifeExp)
# <pandas.core.groupby.groupby.SeriesGroupBy object at 0x000002C497C9AEF0>

# mean()求平均值
mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)
'''
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
'''
```

```python
# 对人口和GDP求平均
multi_group_var = df.\
       groupby(['year','continent'])\
       [['lifeExp','gdpPercap']].\
       mean()
print(multi_group_var)
'''
                  lifeExp     gdpPercap
year continent
1952 Africa     39.135500   1252.572466
     Americas   53.279840   4079.062552
     Asia       46.314394   5195.484004
     Europe     64.408500   5661.057435
     Oceania    69.255000  10298.085650
1957 Africa     41.266346   1385.236062
     Americas   55.960280   4616.043733
     Asia       49.318544   5787.732940
     Europe     66.703067   6963.012816
     Oceania    70.295000  11598.522455
1962 Africa     43.319442   1598.078825
     Americas   58.398760   4901.541870
     Asia       51.563223   5729.369625
     Europe     68.539233   8365.486814
     Oceania    71.085000  12696.452430
1967 Africa     45.334538   2050.363801
     Americas   60.410920   5668.253496
     Asia       54.663640   5971.173374
     Europe     69.737600  10143.823757
     Oceania    71.310000  14495.021790
1972 Africa     47.450942   2339.615674
     Americas   62.394920   6491.334139
     Asia       57.319269   8187.468699
     Europe     70.775033  12479.575246
     Oceania    71.910000  16417.333380
1977 Africa     49.580423   2585.938508
     Americas   64.391560   7352.007126
     Asia       59.610556   7791.314020
     Europe     71.937767  14283.979110
     Oceania    72.855000  17283.957605
1982 Africa     51.592865   2481.592960
     Americas   66.228840   7506.737088
     Asia       62.617939   7434.135157
     Europe     72.806400  15617.896551
     Oceania    74.290000  18554.709840
1987 Africa     53.344788   2282.668991
     Americas   68.090720   7793.400261
     Asia       64.851182   7608.226508
     Europe     73.642167  17214.310727
     Oceania    75.320000  20448.040160
1992 Africa     53.629577   2281.810333
     Americas   69.568360   8044.934406
     Asia       66.537212   8639.690248
     Europe     74.440100  17061.568084
     Oceania    76.945000  20894.045885
1997 Africa     53.598269   2378.759555
     Americas   71.150480   8889.300863
     Asia       68.020515   9834.093295
     Europe     75.505167  19076.781802
     Oceania    78.190000  24024.175170
2002 Africa     53.325231   2599.385159
     Americas   72.422040   9287.677107
     Asia       69.233879  10174.090397
     Europe     76.700600  21711.732422
     Oceania    79.740000  26938.778040
2007 Africa     54.806038   3089.032605
     Americas   73.608120  11003.031625
     Asia       70.728485  12473.026870
     Europe     77.648600  25054.481636
     Oceania    80.719500  29810.188275
'''
# 平铺DataFrame,使用reset_index
flat = multi_group_var.reset_index()
print(flat.head(15))
'''
		year continent    lifeExp     gdpPercap
0   1952    Africa  39.135500   1252.572466
1   1952  Americas  53.279840   4079.062552
2   1952      Asia  46.314394   5195.484004
3   1952    Europe  64.408500   5661.057435
4   1952   Oceania  69.255000  10298.085650
5   1957    Africa  41.266346   1385.236062
6   1957  Americas  55.960280   4616.043733
7   1957      Asia  49.318544   5787.732940
8   1957    Europe  66.703067   6963.012816
9   1957   Oceania  70.295000  11598.522455
10  1962    Africa  43.319442   1598.078825
11  1962  Americas  58.398760   4901.541870
12  1962      Asia  51.563223   5729.369625
13  1962    Europe  68.539233   8365.486814
14  1962   Oceania  71.085000  12696.452430
'''
```

#### 1.4.2 分组频率计数

> nunique方法计算Series中唯一值的数目

```python
print(df.groupby('continent')['country'].nunique())
'''
continent
Africa      52
Americas    25
Asia        33
Europe      30
Oceania      2
Name: country, dtype: int64
'''
```

### 1.5 基本绘图

```python
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)
'''
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
'''
global_yearly_life_expectancy.plot()
plt.show()
```

## 第2章 Pandas数据结构

### 2.2 创建数据

#### 2.2.1 创建Series

> Series简介: 在Pandas中，Series是一维容器，类似于Python的列表。这种数据类型表示DataFrame的每一列。

```python
import pandas as pd
s = pd.Series(['banana',42])
print(s)
'''
0    banana
1        42
dtype: object
'''
s = pd.Series(['Wes Mckinney','Creator of Pandas'],index=['Person','Who'])
print(s)
'''
Person         Wes Mckinney
Who       Creator of Pandas
dtype: object
'''
```

#### 2.2.2 创建DataFrame

> 可以把DataFrame看作由Series对象组成的字典

```python
scientist = pd.DataFrame({
  'Name':['Rosaline Franklin','William Gosset'],
  'Occupation':['Chemist','Statistician'],
  'Born':['1920-07-25','1876-06-13'],
  'Died':['1958-04-16','1937-10-16'],
  'Age':[37,61]
})
print(scientist)
'''
                Name    Occupation        Born        Died  Age
0  Rosaline Franklin       Chemist  1920-07-25  1958-04-16   37
1     William Gosset  Statistician  1876-06-13  1937-10-16   61
'''
# 用name当做索引
scientist = pd.DataFrame(
  data={
    'Occupation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]
  },
  index=['Rosaline Franklin','William Gosset'],
  columns=['Occupation','Born','Died','Age'] # columns参数指定列顺序
)
print(scientist)
'''
                     Occupation        Born        Died  Age
Rosaline Franklin       Chemist  1920-07-25  1958-04-16   37
William Gosset     Statistician  1876-06-13  1937-10-16   61
'''
# 有序写法OrderedDict
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
'''
                name   Occupation        Born        Died  Age
0  Rosaline Franklin      Chemist  1920-07-25  1958-04-16   37
1     William Gosset  Statistcian  1876-06-13  1937-10-16   61
'''
```

### 2.3 Series

```python
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
'''
                     Occupation        Born        Died  Age
Rosaline Franklin       Chemist  1920-07-25  1958-04-16   37
William Gosset     Statistician  1876-06-13  1937-10-16   61
'''
# 行索引选择
first_row = scientist.loc['William Gosset']
print(type(first_row)) # 行索引选出一位科学家
'''
<class 'pandas.core.series.Series'>
'''
print(first_row)
'''
Occupation    Statistician
Born            1876-06-13
Died            1937-10-16
Age                     61
Name: William Gosset, dtype: object
'''
print(first_row.index) # 输出索引
'''
Index(['Occupation', 'Born', 'Died', 'Age'], dtype='object')
'''
print(first_row.values) # 输出值
'''
['Statistician' '1876-06-13' '1937-10-16' 61]
'''
print(first_row.keys()) # index属性的别名
'''
Index(['Occupation', 'Born', 'Died', 'Age'], dtype='object')
'''
print(first_row.index[0]) # 获取第一个索引
# Occupation
print(first_row.keys()[0]) # 获取第一个索引
# Occupation
```

| 属性          | 说明                           |
| ------------- | ------------------------------ |
| loc           | 使用索引值取子集               |
| iloc          | 使用索引位置取子集             |
| dtype或dtypes | Series内容的类型               |
| T             | Series的转置矩阵               |
| shape         | 数据的维数                     |
| size          | Series中元素的数量             |
| values        | ndarray或类似于ndarray的Series |

#### 2.3.1 类似于ndarray的Series

> Series是pandas的一种数据结构，与numpy.ndarray非常相似。ndarray的很多方法和函数也适用于Series。Series也称为向量。

__Series方法__

```python
# 从scientist DataFrame获取Age列(这是一个Series)
# 获取Series列
ages = scientist['Age']
print(ages)
'''
Rosaline Franklin    37
William Gosset       61
Name: Age, dtype: int64
'''
# 科学计算
print(ages.mean()) # 49.0
print(ages.min()) # 37
print(ages.max()) # 61
print(ages.std()) # 16.97056274847714
```

| Series方法     | 说明                                                 |
| -------------- | ---------------------------------------------------- |
| append         | 连接两个或多个Series                                 |
| corr           | 计算与另一个Series的相关系数                         |
| cov            | 计算与另一个Series的协方差                           |
| describe       | 计算概括统计量                                       |
| drop_duplicate | 返回一个不含重复项的Series                           |
| equals         | 判断两个Series是否有相同元素                         |
| get_values     | 获取Series的值，功能和values属性相同                 |
| hist           | 绘制直方图                                           |
| isin           | 逐个检查Series中的每个元素是否存在于参数指定的序列中 |
| min            | 返回最小值                                           |
| max            | 返回最大值                                           |
| mean           | 返回算术平均值                                       |
| median         | 返回中位数                                           |
| mode           | 返回众数                                             |
| quantile       | 返回指定位置的四分位数                               |
| replace        | 用指定值代替Series中的值                             |
| sample         | 返回Series的随机采样值                               |
| sort_values    | 对值进行排序                                         |
| to_frame       | 把Series转换为DataFrame                              |
| transpose      | 返回转置矩阵                                         |
| unique         | 返回由唯一值组成的numpy.ndarray                      |

#### 2.3.2 布尔子集:Series

```python
import pandas as pd
scientist = pd.read_csv('scientists.csv')
ages = scientist['Age']
print(ages)
'''
0    37
1    61
2    90
3    66
4    56
5    45
6    41
7    77
Name: Age, dtype: int64
'''
# 获取基本统计量
print(ages.describe())
'''
count     8.000000
mean     59.125000
std      18.325918
min      37.000000
25%      44.000000
50%      58.500000
75%      68.750000
max      90.000000
Name: Age, dtype: float64
'''
# 所有年龄的平均值
print(ages.mean()) # 59.125
# 获取大于平均值的年龄
print(ages[ages>ages.mean()])
'''
1    61
2    90
3    66
7    77
Name: Age, dtype: int64
'''
print(type(ages>ages.mean())) 
'''
0    False
1     True
2     True
3     True
4    False
5    False
6    False
7     True
Name: Age, dtype: bool
'''
print(type(ages[ages>ages.mean()])) # <class 'pandas.core.series.Series'>
# 上面的dtype类型为bool，可以使用布尔向量获取子集
manual_bool_values = [True,True,False,False,True,True,False,True]
print(ages[manual_bool_values])
'''
0    37
1    61
4    56
5    45
7    77
Name: Age, dtype: int64
'''
```

#### 2.3.3 操作自动对齐和向量化（广播）

__1.同长度向量__

> 如果在两个长度相同的向量之间执行计算，所得向量的每个元素是两个向量对应元素的计算结果

```python
print(ages + ages)
'''
0     74
1    122
2    180
3    132
4    112
5     90
6     82
7    154
Name: Age, dtype: int64
'''
print(ages * ages)
'''
0    1369
1    3721
2    8100
3    4356
4    3136
5    2025
6    1681
7    5929
Name: Age, dtype: int64
'''
```

__2.向量和整数(标量)运算__

> 当对向量和标量运算时，标量会与向量中的每个元素逐一进行计算

```python
print(ages + 100)
'''
0    137
1    161
2    190
3    166
4    156
5    145
6    141
7    177
Name: Age, dtype: int64
'''
print(ages * 2)
'''
0     74
1    122
2    180
3    132
4    112
5     90
6     82
7    154
Name: Age, dtype: int64
'''
```

__3.不同长度向量间的运算__

> 处理不同长度的向量时，处理方式取决于向量的类型。对于Series，对向量的操作会根据索引进行。结果向量的其余元素会被填充成“缺失”值，用NaN表示，指“非数值”。这种处理方式称为“广播”，在不同的语言中各有区别。Pandas中的“广播”是指不同shape的数组之间的运算方式

```python
print(ages + pd.Series([1,100]))
'''
0     38.0
1    161.0
2      NaN
3      NaN
4      NaN
5      NaN
6      NaN
7      NaN
dtype: float64
'''
```

__4.带有常见索引标签的向量(自动对齐)__

> pandas会自动对齐数据。执行操作时，数据会尽可能依据索引标签进行对齐

```python
print(ages)
'''
0    37
1    61
2    90
3    66
4    56
5    45
6    41
7    77
'''
rev_ages = ages.sort_index()
'''
7    77
6    41
5    45
4    56
3    66
2    90
1    61
0    37
Name: Age, dtype: int64
'''
# 使用ages和rev_ages执行某一项操作时，仍是逐个元素进行，但在执行操作前会首先对齐向量
print(age * 2)
'''
0     74
1    122
2    180
3    132
4    112
5     90
6     82
7    154
Name: Age, dtype: int64
'''
print(ages + rev_ages)
'''
0     74
1    122
2    180
3    132
4    112
5     90
6     82
7    154
Name: Age, dtype: int64
'''
```

### 2.4 DataFrame

#### 2.4.1 布尔子集:DataFrame

```python
# 使用布尔向量获取部分数据行
print(scientist[scientist['Age'] > scientist['Age'].mean()])
'''
                   Name        Born        Died  Age     Occupation
1        William Gosset  1876-06-13  1937-10-16   61   Statistician
2  Florence Nightingale  1820-05-12  1910-08-13   90          Nurse
3           Marie Curie  1867-11-07  1934-07-04   66        Chemist
7          Johann Gauss  1777-04-30  1855-02-23   77  Mathematician
'''
# 传入包含4个值的布尔向量
# 返回3行
print(scientist.loc[[True,True,False,True]])
'''
                Name        Born        Died  Age    Occupation
0  Rosaline Franklin  1920-07-25  1958-04-16   37       Chemist
1     William Gosset  1876-06-13  1937-10-16   61  Statistician
3        Marie Curie  1867-11-07  1934-07-04   66       Chemist
'''
```

__获取子集的一些方法__

| 方法                        | 执行结果                       |
| --------------------------- | ------------------------------ |
| df[column_name]             | 单列                           |
| df[[column1,column2,...]]   | 多列                           |
| df.loc[row_label]           | 使用行索引标签(行名)获取数据行 |
| df.loc[[label1,label2,...]] | 使用索引标签获取多行           |
| df.iloc[row_label]          | 使用行号获取行                 |
| df.iloc[[row1,row2,...]]    | 使用行号获取多行               |
| df[bool]                    | 使用布尔值获取行               |
| df[[bool1,bool2,...]]       | 使用布尔值获取多行             |
| df[start:stop:step]         | 使用切片方法获取数据行         |

#### 2.4.2 操作自动对齐和向量化(广播)

> pandas支持广播，广播源自NumPy库。它实际描述的是在类数组对象(比如Series和DataFrame)之间执行操作的效果。这些行为取决于对象的类型、长度以及与对象关联的标签。

```python
# 从scientist DataFrame获取两个子集
first_half = scientist[:4]
second_half = scientist[4:]
print(first_half)
'''
                   Name        Born        Died  Age    Occupation
0     Rosaline Franklin  1920-07-25  1958-04-16   37       Chemist
1        William Gosset  1876-06-13  1937-10-16   61  Statistician
2  Florence Nightingale  1820-05-12  1910-08-13   90         Nurse
3           Marie Curie  1867-11-07  1934-07-04   66       Chemist
'''
print(second_half)
'''
            Name        Born        Died  Age          Occupation
4  Rachel Carson  1907-05-27  1964-04-14   56           Biologist
5      John Snow  1813-03-15  1858-06-16   45           Physician
6    Alan Turing  1912-06-23  1954-06-07   41  Computer Scientist
7   Johann Gauss  1777-04-30  1855-02-23   77       Mathematician
'''
# 当DataFrame和标量进行运算时，DataFrame中的每个元素会分别和标量进行运算
# 数值翻倍，字符串翻倍
'''
                                       Name                  Born                  Died  Age                            Occupation
0        Rosaline FranklinRosaline Franklin  1920-07-251920-07-25  1958-04-161958-04-16   74                        ChemistChemist
1              William GossetWilliam Gosset  1876-06-131876-06-13  1937-10-161937-10-16  122              StatisticianStatistician
2  Florence NightingaleFlorence Nightingale  1820-05-121820-05-12  1910-08-131910-08-13  180                            NurseNurse
3                    Marie CurieMarie Curie  1867-11-071867-11-07  1934-07-041934-07-04  132                        ChemistChemist
4                Rachel CarsonRachel Carson  1907-05-271907-05-27  1964-04-141964-04-14  112                    BiologistBiologist
5                        John SnowJohn Snow  1813-03-151813-03-15  1858-06-161858-06-16   90                    PhysicianPhysician
6                    Alan TuringAlan Turing  1912-06-231912-06-23  1954-06-071954-06-07   82  Computer ScientistComputer Scientist
7                  Johann GaussJohann Gauss  1777-04-301777-04-30  1855-02-231855-02-23  154            MathematicianMathematician'''
```

### 2.5 更改Series和DataFrame

#### 2.5.1 添加列

```python
print(scientist['Born'].dtype) # object
print(scientist['Died'].dtype) # object
# object表明它们都是字符串类型，可以把他们转化为datetime类型，这样就可以执行常见的日期和时间操作了(例如计算两个日期之差或人的年龄)。这里采用format = '%Y-%m-%d'

born_datatime = pd.to_datetime(scientist['Born'],format='%Y-%m-%d') # 把Born列格式化为datatime
print(born_datatime)
'''
0   1920-07-25
1   1876-06-13
2   1820-05-12
3   1867-11-07
4   1907-05-27
5   1813-03-15
6   1912-06-23
7   1777-04-30
Name: Born, dtype: datetime64[ns]
'''
died_datetime = pd.to_datetime(scientist['Died'],format='%Y-%m-%d')
# 创建一组新列，其中包含object(字符串)日期的datetime表示形式。下面的例子使用了Python的多重赋值语法
scientist['born_dt'],scientist['died_dt'] = (born_datatime,died_datetime)
print(scientist.head())
'''
                   Name        Born        Died  Age    Occupation    born_dt    died_dt
0     Rosaline Franklin  1920-07-25  1958-04-16   37       Chemist 1920-07-25 1958-04-16
1        William Gosset  1876-06-13  1937-10-16   61  Statistician 1876-06-13 1937-10-16
2  Florence Nightingale  1820-05-12  1910-08-13   90         Nurse 1820-05-12 1910-08-13
3           Marie Curie  1867-11-07  1934-07-04   66       Chemist 1867-11-07 1934-07-04
4         Rachel Carson  1907-05-27  1964-04-14   56     Biologist 1907-05-27 1964-04-14
'''
print(scientist.shape) # (8, 7)
```

#### 2.5.2 直接更改列

```python
print(scientist['Age'])
'''
0    37
1    61
2    90
3    66
4    56
5    45
6    41
7    77
Name: Age, dtype: int64
'''
# 把这些值打乱
import random
random.seed(42)
random.shuffle(scientist['Age'])

print(scientist['Age'])
'''
0    66
1    56
2    41
3    77
4    90
5    45
6    37
7    61
Name: Age, dtype: int64
'''
# 使用random_state减少随机化
scientist['Age'] = scientist['Age'].\
  sample(len(scientist['Age']), random_state = 24).\
         reset_index(drop = True)
# 把Age列打乱两次
print(scientist['Age'])
'''
0    61
1    45
2    37
3    90
4    56
5    66
6    77
7    41
Name: Age, dtype: int64
'''
```

#### 2.5.3 删除值

```python
# 当前数据中的所有列
print(scientist.columns) 
# Index(['Name', 'Born', 'Died', 'Age', 'Occupation', 'born_dt', 'died_dt'], dtype='object')
# 删除列Age,设置参数axis=1，删除列
scientist_dropped = scientist.drop(['Age'],axis=1)
# 删除指定列之后输出
print(scientist_dropped.columns)
# Index(['Name', 'Born', 'Died', 'Occupation', 'born_dt', 'died_dt'], dtype='object')
```

### 2.6 导入和导出数据

#### 2.6.1 保存数据

__1.Series__

> Series的许多导出方法也适用于DataFrame

```python
names = scientist['Name']
print(names)
'''
0       Rosaline Franklin
1          William Gosset
2    Florence Nightingale
3             Marie Curie
4           Rachel Carson
5               John Snow
6             Alan Turing
7            Johann Gauss
Name: Name, dtype: object
'''
# 调用to_pickle方法以二进制格式保存数据，打开是一群乱码
names.to_pickle('scientists_names_series.pickle')
```

__2.DataFrame__

> to_pickle方法也可以用于保存DataFrame对象

__3.读取.pickle文件__

```python
scientist_names_from_pickle = pd.read_pickle('scientists_names_series.pickle')
print(scientist_names_from_pickle)
'''
0       Rosaline Franklin
1          William Gosset
2    Florence Nightingale
3             Marie Curie
4           Rachel Carson
5               John Snow
6             Alan Turing
7            Johann Gauss
Name: Name, dtype: object
'''
```

#### 2.6.2 CSV

#### 2.6.3 Excel

#### 2.6.4 feather文件格式

#### 2.6.5 其他数据输出格式

| 导出方法     | 说明                                   |
| ------------ | -------------------------------------- |
| to_clipboard | 把数据保存到系统剪贴板，方便粘贴       |
| to_dense     | 把稀疏对象转换成标准密集形式           |
| to_dict      | 把数据转换为Python字典                 |
| to_gbq       | 把数据转换成Google BigQuery表          |
| to_hdf       | 把数据保存为HDF格式                    |
| to_msgpack   | 把数据保存为类似于Json的便携二进制格式 |
| to_html      | 把数据转换成html表                     |
| to_json      | 把数据转换成Json字符串                 |
| to_latex     | 把数据转换成LaTex表格环境              |
| to_records   | 把数据转换成记录数组                   |
| to_string    | 在标准输出以字符串显示DataFrame        |
| to_sparse    | 把数据转换为SparceDataFrame            |
| to_sql       | 把数据保存到SQL数据库                  |
| to_stata     | 把数据转换成Stata dta文件              |

## 第3章 绘图入门

```python
import seaborn as sns
anscombe = sns.load_dataset("anscombe")
print(anscombe)
'''
   dataset     x      y
0        I  10.0   8.04
1        I   8.0   6.95
2        I  13.0   7.58
3        I   9.0   8.81
4        I  11.0   8.33
5        I  14.0   9.96
6        I   6.0   7.24
7        I   4.0   4.26
8        I  12.0  10.84
9        I   7.0   4.82
10       I   5.0   5.68
11      II  10.0   9.14
12      II   8.0   8.14
13      II  13.0   8.74
14      II   9.0   8.77
15      II  11.0   9.26
16      II  14.0   8.10
17      II   6.0   6.13
18      II   4.0   3.10
19      II  12.0   9.13
20      II   7.0   7.26
21      II   5.0   4.74
22     III  10.0   7.46
23     III   8.0   6.77
24     III  13.0  12.74
25     III   9.0   7.11
26     III  11.0   7.81
27     III  14.0   8.84
28     III   6.0   6.08
29     III   4.0   5.39
30     III  12.0   8.15
31     III   7.0   6.42
32     III   5.0   5.73
33      IV   8.0   6.58
34      IV   8.0   5.76
35      IV   8.0   7.71
36      IV   8.0   8.84
37      IV   8.0   8.47
38      IV   8.0   7.04
39      IV   8.0   5.25
40      IV  19.0  12.50
41      IV   8.0   5.56
42      IV   8.0   7.91
43      IV   8.0   6.89
'''
```

### 3.2 matplotlib

```python
'''
sublot有三个参数
1.子图的行数
2.子图的列数
3.子图的位置
'''
import seaborn as sns
import matplotlib.pyplot as plt
anscombe = sns.load_dataset("anscombe")
print(anscombe)

dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

plt.plot(dataset_1['x'], dataset_1['y'])
plt.show()
plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.show()

fig = plt.figure()  # 创建画布用于放置子图

# 位置1,2,3,4
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)
# 在4个位置中画图
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')
# 各个小图中添加小标题
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")
# 添加大标题
fig.suptitle("Anscombe Data")
# 使用紧凑布局
fig.tight_layout()
plt.show()
```

### 3.3 使用matplotlib绘制统计图

> seaborn的tips数据集，其中包括某个餐厅服务员收集的顾客付小费的相关数据，涉及多个变量，包括总费用，聚餐人数，星期几等

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''
```

#### 3.3.1 单变量(univariate)

```python
# 画直方图
fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips['total_bill'], bins = 10)
axes1.set_title("Histigram of Total Bill")
axes1.set_xlabel("Frequency")
axes1.set_ylabel("Total Bill")
plt.show()
```

#### 3.3.2 双变量(bivariate)

__1.散点图__

> 表示一个变量随另一个变量的变化所呈现的趋势

```python
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
plt.show()
```

__2.箱线图__

> 用于展示一个离散变量随一个连续变量的变化而呈现出来的分布情况

```python
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)
axes1.boxplot(
  [tips[tips['sex'] == 'Female']['tip'],
   tips[tips['sex'] == 'Male']['tip']],
  labels = ['Famale', 'Male']
)
axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')
plt.show()
```

#### 3.3.3多变量数据



### 3.4 seaborn

#### 3.4.1 单变量

__1.直方图__

```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
# 使用subplot函数创建画布，并在其中添加各个子图
hist, ax = plt.subplots()

# 使用seaborn的distplot函数绘图
ax = sns.distplot(tips['total_bill'])
ax.set_title('Total Bill Histogram with Density Plot')
plt.show()
```

> distplot默认同时绘制直方图和密度图(使用核密度估计法)。如果想直绘制直方图，可以把kde参数设置为False

```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
# 使用subplot函数创建画布，并在其中添加各个子图
hist, ax = plt.subplots()

# 使用seaborn的distplot函数绘图
ax = sns.distplot(tips['total_bill'], kde = False)
ax.set_title('Total Bill Histogram with Density Plot')
plt.show()
```

__2.密度图(核密度估计)__

> 密度图是展现单变量分布的另一种方法，本质上是通过绘制以每个数据点为中心的正态分布，然后消除重叠的图，使曲线下的面积为1来创建的

```python
den, ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], hist = False)
ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')
plt.show()
```

__3.频数图(rug plot)__

> 频数图是变量分布的一维表示，常与其他图一起使用，以增强可视化效果

```python
hist_den_rug, ax = plt.subplots()
ax = sns.distplot(tips['total_bill'],rug = True)
ax.set_title('Total Bill Histogram with Density and Rug Plot')
ax.set_xlabel('Total Bill')
plt.show()
```

__4.计数图(条形图)__

> 对离散变量计数

```python
count, ax = plt.subplots()
ax = sns.countplot('day', data = tips)
ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')
plt.show()
```

#### 3.4.2 双变量数据

__1.散点图__

> 创建散点图可以使用regplot函数。该函数不仅可以绘制散点图，还会拟合回归线。如果把fit_reg设置为False，只显示散点图

```python
scatter, ax = plt.subplots()
ax = sns.regplot(x = 'total_bill', y = 'tip', data = tips)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()
```

> lmplot函数和regplot函数类似。两者的主要区别是regplot创建轴域，而lmplot创建图

```python
fig = sns.lmplot(x = 'total_bill', y = 'tip', data = tips)
plt.show()
```

> 还可以使用jointplot在每个轴上创建包含单个变量的散点图。jointplot与其他绘图函数的主要区别是，他不返回轴域，所以无需创建带有轴域的画布来放置图。jointplot函数会创建并返回JointGrid对象

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

joint = sns.jointplot(x = "total_bill", y = "tip", data = tips)
joint.set_axis_labels(xlabel = 'Total Bill', ylabel = 'Tip')
# 添加标题，设置字号
# 移动轴域上方的文字
joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize = 10, y = 1.03)
plt.show()

hexbin = sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')
hexbin.set_axis_labels(xlabel = 'Total Bill', ylabel = 'Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip', fontsize = 10, y = 1.03)
plt.show()
```

__2.蜂巢图__

> 散点图适用于比较两个变量，但有时图中的点太多反而会失去意义。解决该问题的一种方法是把图中的点装箱。就像直方图可将变量装箱来创建条形图一样，蜂巢图可以对两个变量装箱，显示它们的频次分布情况

```python

```

__3.2D密度图__

> 2D核密度图是跨两个变量的

```python
kde, ax = plt.subplots()
ax = sns.kdeplot(data = tips['total_bill'], data2 = tips['tip'], shade = True)
ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_ylabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()
```

__4.条形图__

> 用于展示多个变量，barplot默认计算平均值

```python
bar, ax = plt.subplots()
ax = sns.barplot(x = 'time', y = 'total_bill', data = tips)
ax.set_title('Bar plot of average total bill for time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Average total bill')
plt.show()
```

__5.箱线图__

> 显示多种统计信息:最小值、第一个四分位数、中位数、第三个四分位数、最大值

```python
box, ax = plt.subplots()
ax = sns.boxplot(x = 'time', y = 'total_bill', data = tips)
ax.set_title('Boxplot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')
plt.show()
```

__6.小提琴图__

> 显示与箱线相同的值，但是它把“箱线”绘成核密度估计

```python
violin, ax = plt.subplots()
ax = sns.violinplot(x = 'time', y = 'total_bill', data = tips)
ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')
plt.show()
```

__7.成对关系<不太懂>__

> 当数据大部分是数值时，可以使用pairplot函数把所有成对关系描述出来。函数会为每对变量绘制散点图，并且为单变量数据绘制直方图

```python
fig = sns.pairplot(tips)
plt.show()
```

> 缺点：存在冗余信息,即图的上半部分和下半部分相同。可以使用pairgrid手动指定图的上半信息和下半信息

```python
pair_grid = sns.PairGrid(tips)
# 可以使用plt.scatter代替sns.regplot
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug = True)
plt.show()
```

#### 3.4.3 多变量数据

__1.颜色__

> 使用violinplot函数时，可以通过hue参数按性别(sex)给图着色

```python
violin, ax = plt.subplots()
ax = sns.violinplot(x = 'time', y = 'total_bill', hue = 'sex', data = tips, split = True)
plt.show()
```

> lmplot设置hue参数的效果

```python
scatter = sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', fit_reg = False)
plt.show()
```

> 通过向hue参数传入一个类别变量，可以让图变得更有意义

```python
fig = sns.pairplot(tips, hue = 'sex')
plt.show()
```

__2.大小和形状__

> lmplot的参数scatter_kw都接收键值对，具体而言，是python字典。键值对先传给scatter_kw,然后传给matplotlib函数plt.scatter。可以通过这种方法访问s参数来改变点的大小

```python
scatter = sns.lmplot(x = 'total_bill', y = 'tip', data = tips, fit_reg = False, hue = 'sex',
                     scatter_kws = {'s': tips['size'] * 10})
plt.show()
```

```python
scatter = sns.lmplot(x = 'total_bill', y = 'tip', data = tips,
                     fit_reg = False, hue = 'sex', markers = ['o', 'x'],
                     scatter_kws = {'s': tips['size'] * 10})
plt.show()
```

__3.分面__

> 如果要显示更多变量，或者确定了要实现的可视化图，但基于一个分类变量画出多幅图，可以使用分面（facet）来满足这些需求。无需单独去数据子集并在图中设置坐标轴，seaborn中的分面可以代劳。
>
> 要使用分面，数据必须是整洁数据，数据中的每一行都表示一个观测值，每一列都是一个变量。

### 3.5 Pandas对象

> pandas对象本身都具有绘图功能。与seaborn一样，pandas中的绘图函数只是使用预设直包装了matplotlib
>
> 使用pandas绘图时，通常要按照如下格式使用绘图函数:DataFrame.plot.PLOT_TYPE或Series.plot.PLOT_TYPE

#### 3.5.1 直方图

> 可以使用Series.plot.hist函数或者DataFrame.plot.hist函数绘制直方图
>

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
ax = tips['total_bill'].plot.hist()
plt.show()
# 为DataFrame绘制直方图
# 设置alpha通道透明度，使重叠的部分透明可见
fig, ax = plt.subplots()
ax = tips[['total_bill', 'tip']].plot.hist(alpha = 0.5, bins = 20, ax = ax)
plt.show()
```

#### 3.5.2 密度图

> 可以使用DataFrame.plot.kde函数创建核密度估计图

```python
fig ,ax = plt.subplots()
ax = tips['tips'].plot.kde()
plt.show()
```

#### 3.5.3 散点图

> 可以使用DataFrame.plot.scatter函数创建散点图

```python
fig, ax = plt.subplots()
ax = tips.plot.scatter(x = 'total_bill', y = 'tip', ax = ax)
plt.show()
```

#### 3.5.4 蜂巢图

> 可以使用DataFrame.plot.hexbin函数创建散点图

```python
fig, ax = plt.subplots()
ax = tips.plot.hexbin(x = 'total_bill', y = 'tip', ax = ax)
plt.show()
# 可以通过gridsize参数调整网格大小
fig, ax = plt.subplots()
ax = tips.plot.hexbin(x = 'total_bill', y = 'tip', ax = ax, gridsize = 10)
plt.show()
```

#### 3.5.5 箱线图

> 可以使用DataFrame.plot.box函数创建散点图

```python
fig, ax = plt.subplots()
ax = tips.plot.box(ax = ax)
plt.show()
```

### 3.6 seaborn主题和样式

> seaborn都采用了默认样式，可以使用sns.set_style函数来更改样式
>
> seaborn有5种样式:darkgrid、whitegrid、dark、white、ticks

```python
# 未设置样式
fig, ax = plt.subplots()
ax = sns.violinplot(x = 'time', y = 'total_bill',
                    hue = 'sex', data = tips,
                    split = True)
plt.show()

# 设置样式之后
sns.set_style('whitegrid')
fig, ax = plt.subplots()
ax = sns.violinplot(x = 'time', y = 'total_bill',
                    hue = 'sex', data = tips,
                    split = True)
plt.show()
```

> 展示所有样式

```python
fig = plt.figure()
seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
for idx, style in enumerate(seaborn_styles):
  plot_position = idx + 1
  with sns.axes_style(style):
    ax = fig.add_subplot(2, 3, plot_position)
    violin = sns.violinplot(x = 'time', y = 'total_bill',data = tips,
                            ax = ax)
    violin.set_title(style)
fig.tight_layout()
plt.show()
```

## 第4章 数据组合

### 4.2 整理数据

> 整洁数据:每个观测值成一行；每个变量成一列；每种观测单元构成一个表格
>
> 组合数据集：

### 4.3 连接

#### 4.3.1 添加行

```python
import pandas as pd

df1 = pd.read_csv('concat_1.csv')
df2 = pd.read_csv('concat_2.csv')
df3 = pd.read_csv('concat_3.csv')
row_concat = pd.concat([df1, df2, df3]) # concat:连接函数(原始行索引的简单堆积),把三个对象放在一个列表里
print(row_concat)
'''
     A    B    C    D
0   a0   b0   c0   d0
1   a1   b1   c1   d1
2   a2   b2   c2   d2
3   a3   b3   c3   d3
0   a4   b4   c4   d4
1   a5   b5   c5   d5
2   a6   b6   c6   d6
3   a7   b7   c7   d7
0   a8   b8   c8   d8
1   a9   b9   c9   d9
2  a10  b10  c10  d10
3  a11  b11  c11  d11
'''
# 获取第四行
print(row_concat.iloc[3,])
'''
A    a3
B    b3
C    c3
D    d3
Name: 3, dtype: object
'''
# 新建一行数据
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(new_row_series)
'''
0    n1
1    n2
2    n3
3    n4
dtype: object
'''
# 尝试向DataFrame添加新行
print(pd.concat([df1, new_row_series]))
'''
     A    B    C    D    0
0   a0   b0   c0   d0  NaN
1   a1   b1   c1   d1  NaN
2   a2   b2   c2   d2  NaN
3   a3   b3   c3   d3  NaN
0  NaN  NaN  NaN  NaN   n1
1  NaN  NaN  NaN  NaN   n2
2  NaN  NaN  NaN  NaN   n3
3  NaN  NaN  NaN  NaN   n4
'''
# 将Series转换成DataFrame
# 尝试向DataFrame添加新行
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']],
                          columns = ['A', 'B', 'C', 'D'])
print(new_row_df)
'''
    A   B   C   D
0  n1  n2  n3  n4
'''
print(pd.concat([df1, new_row_df]))
'''
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
0  n1  n2  n3  n4
'''
```

> concat是通用函数，可以同时连接多个对象。如果只需向DataFrame追加一个对象，完全可以使用append函数来实现

```python
print(df1.append(df2))
'''
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
0  a4  b4  c4  d4
1  a5  b5  c5  d5
2  a6  b6  c6  d6
3  a7  b7  c7  d7
'''
# 添加只有一行数据的DataFrame
print(df1.append(new_row_data))
'''
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
0  n1  n2  n3  n4
'''
# 使用Python字典添加行
data_dict = {'A': 'n1',
             'B': 'n2',
             'C': 'n3',
             'D': 'n4'}
print(df1.append(data_dict, ignore_index = True))
'''
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
4  n1  n2  n3  n4
'''
```

> 忽略索引:当向DataFrame添加一个字典时，必须使用ignore_index.
>
> concat也可以使用ignore_index

```python
row_concat_i = pd.concat([df1, df2, df3],ignore_index = True)
print(row_concat_i)
'''
      A    B    C    D
0    a0   b0   c0   d0
1    a1   b1   c1   d1
2    a2   b2   c2   d2
3    a3   b3   c3   d3
4    a4   b4   c4   d4
5    a5   b5   c5   d5
6    a6   b6   c6   d6
7    a7   b7   c7   d7
8    a8   b8   c8   d8
9    a9   b9   c9   d9
10  a10  b10  c10  d10
11  a11  b11  c11  d11
'''
```

#### 4.3.2 添加列

> 连接列和连接行的做法非常相似，主要区别在于concat函数中的轴参数。axis的默认值是0，按行连接数据。如果把axis=1传递给concat函数，它将按列连接数据

```python
col_concat = pd.concat([df1, df2, df3], axis = 1)
print(col_concat)
'''
    A   B   C   D   A   B   C   D    A    B    C    D
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11
'''
print(col_concat['A'])
'''
    A   A    A
0  a0  a4   a8
1  a1  a5   a9
2  a2  a6  a10
3  a3  a7  a11
'''
# 添加一列
col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print(col_concat)
'''
    A   B   C   D   A   B   C   D    A    B    C    D new_col_list
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8           n1
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9           n2
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10           n3
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11           n4
'''
col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(col_concat)
'''
    A   B   C   D   A      ...          B    C    D new_col_list new_col_series
0  a0  b0  c0  d0  a4      ...         b8   c8   d8           n1             n1
1  a1  b1  c1  d1  a5      ...         b9   c9   d9           n2             n2
2  a2  b2  c2  d2  a6      ...        b10  c10  d10           n3             n3
3  a3  b3  c3  d3  a7      ...        b11  c11  d11           n4             n4
'''
# 重置列索引
print(pd.concat([df1, df2, df3], axis = 1, ignore_index = True))
'''
   0   1   2   3   4   5   6   7    8    9    10   11
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11
'''
```

#### 4.3.3 不同索引下的连接操作

__1.连接具有不同列的行__

```python
# 调整DataFrame
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']
print(df1)
'''
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
'''
print(df2)
'''
    E   F   G   H
0  a4  b4  c4  d4
1  a5  b5  c5  d5
2  a6  b6  c6  d6
3  a7  b7  c7  d7
'''
print(df3)
'''
     A    C    F    H
0   a8   b8   c8   d8
1   a9   b9   c9   d9
2  a10  b10  c10  d10
3  a11  b11  c11  d11
'''
# 连接
row_concat = pd.concat([df1, df2, df3])
print(row_concat)
'''
     A    B    C    D    E    F    G    H
0   a0   b0   c0   d0  NaN  NaN  NaN  NaN
1   a1   b1   c1   d1  NaN  NaN  NaN  NaN
2   a2   b2   c2   d2  NaN  NaN  NaN  NaN
3   a3   b3   c3   d3  NaN  NaN  NaN  NaN
0  NaN  NaN  NaN  NaN   a4   b4   c4   d4
1  NaN  NaN  NaN  NaN   a5   b5   c5   d5
2  NaN  NaN  NaN  NaN   a6   b6   c6   d6
3  NaN  NaN  NaN  NaN   a7   b7   c7   d7
0   a8  NaN   b8  NaN  NaN   c8  NaN   d8
1   a9  NaN   b9  NaN  NaN   c9  NaN   d9
2  a10  NaN  b10  NaN  NaN  c10  NaN  d10
3  a11  NaN  b11  NaN  NaN  c11  NaN  d11
'''
```

> 为了避免NaN值，可只保留要连接的对象共有的列。concat函数有一个参数join，可用它来实现。默认情况下，join的值为outer，这意味着它会保留所有列。但可将其设置为join='inner',只保留数据集都有的列
>
> 如果试图保留上面3个DataFrame的共有列，会得到一个空的DataFrame，因为它们不含相同的列

```python
print(pd.concat([df1, df2, df3], join = 'inner'))
'''
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
'''
print(pd.concat([df1, df3], ignore_index = False, join = 'inner'))
'''
     A    C
0   a0   c0
1   a1   c1
2   a2   c2
3   a3   c3
0   a8   b8
1   a9   b9
2  a10  b10
3  a11  b11
'''
```

__2.连接具有不同行的列__

```python
df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]
print(df1)
'''
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
'''
print(df2)
'''
    E   F   G   H
4  a4  b4  c4  d4
5  a5  b5  c5  d5
6  a6  b6  c6  d6
7  a7  b7  c7  d7
'''
print(df3)
'''
     A    C    F    H
0   a8   b8   c8   d8
2   a9   b9   c9   d9
5  a10  b10  c10  d10
7  a11  b11  c11  d11
'''
# 按列连接
col_concat = pd.concat([df1, df2, df3], axis = 1)
print(col_concat)
'''
     A    B    C    D    E    F    G    H    A    C    F    H
0   a0   b0   c0   d0  NaN  NaN  NaN  NaN   a8   b8   c8   d8
1   a1   b1   c1   d1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
2   a2   b2   c2   d2  NaN  NaN  NaN  NaN   a9   b9   c9   d9
3   a3   b3   c3   d3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4  NaN  NaN  NaN  NaN   a4   b4   c4   d4  NaN  NaN  NaN  NaN
5  NaN  NaN  NaN  NaN   a5   b5   c5   d5  a10  b10  c10  d10
6  NaN  NaN  NaN  NaN   a6   b6   c6   d6  NaN  NaN  NaN  NaN
7  NaN  NaN  NaN  NaN   a7   b7   c7   d7  a11  b11  c11  d11
'''
print(pd.concat([df1, df3], axis = 1, join = 'inner'))
'''
    A   B   C   D   A   C   F   H
0  a0  b0  c0  d0  a8  b8  c8  d8
2  a2  b2  c2  d2  a9  b9  c9  d9
'''
```

### 4.4 合并多个数据集

> 在数据库中，合并数据表时会用join='inner'和默认的join='outer'参数
>
> 除了行索引或列索引进行连接之外，也可以依据共有数据值把两个或多个DataFrame组合起来。在数据库中，这种操作称为join
>
> Pandas提供了pd.join命令，但在背后真正起作用的是pd.merge命令，join会根据索引合并DataFrame对象，相比之下，merge命令更灵活

```python
import pandas as pd

person = pd.read_csv('survey_person.csv')
site = pd.read_csv('survey_site.csv')
survey = pd.read_csv('survey_survey.csv')
visited = pd.read_csv('survey_visited.csv')
print(person)
'''
      ident   personal    family
0      dyer    William      Dyer
1        pb      Frank   Pabodie
2      lake   Anderson      Lake
3       roe  Valentina   Roerich
4  danforth      Frank  Danforth
'''
print(site)
'''
    name    lat    long
0   DR-1 -49.85 -128.57
1   DR-3 -47.15 -126.72
2  MSK-4 -48.87 -123.40
'''
print(visited)
'''
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
'''
print(survey)
'''
    taken person quant  reading
0     619   dyer   rad     9.82
1     619   dyer   sal     0.13
2     622   dyer   rad     7.80
3     622   dyer   sal     0.09
4     734     pb   rad     8.41
5     734   lake   sal     0.05
6     734     pb  temp   -21.50
7     735     pb   rad     7.22
8     735    NaN   sal     0.06
9     735    NaN  temp   -26.00
10    751     pb   rad     4.35
11    751     pb  temp   -18.50
12    751   lake   sal     0.10
13    752   lake   rad     2.19
14    752   lake   sal     0.09
15    752   lake  temp   -16.00
16    752    roe   sal    41.60
17    837   lake   rad     1.46
18    837   lake   sal     0.21
19    837    roe   sal    22.50
20    844    roe   rad    11.25
'''
```

> 当前，数据被分成了多个部分，每个部分是一个观测单元。如果想查看每个站点的日期以及该站点的经纬度信息必须把多个DataFrame组合起来，可以使用merge函数来实现，她是DataFrame的方法
>
> 在调用这个方法时，被调用的DataFrame称为’左DataFrame‘。在merge函数中，第一个参数是’右DataFrame‘，随后一个参数影响最终合并结果的外观。然后设置on参数，它指定要匹配的列。如果左边列和右边列的名称不同，可以使用left_on和right_on代替

| Pandas | SQL         | 描述                   |
| ------ | ----------- | ---------------------- |
| left   | left outer  | 从左侧保留所有键       |
| right  | right outer | 从右侧保留所有键       |
| outer  | full outer  | 从左右两侧保留所有键   |
| inner  | inner       | 只保留左右两侧都有的键 |

#### 4.4.1 一对一合并

```python
# 修改visited_subset,使其不含重复的site值
visited_subset = visited.loc[[0, 2, 6],]
# 一对一合并
# merge函数的参数how默认值为inner
o2o_merge = site.merge(visited_subset,
                       left_on = 'name', right_on = 'site')
print(o2o_merge)
'''
    name    lat    long  ident   site       dated
0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
1   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
2  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14
'''
```

> 基于两个独立DataFrame创建出新的DataFrame，其中行是基于一组特定列匹配的。在SQL语言中，用于匹配的列称为’键‘

#### 4.4.2 多对一合并

```python
m2o_merge = site.merge(visited, left_on = 'name', right_on = 'site')
print(m2o_merge)
'''
    name    lat    long  ident   site       dated
0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
1   DR-1 -49.85 -128.57    622   DR-1  1927-02-10
2   DR-1 -49.85 -128.57    844   DR-1  1932-03-22
3   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
4   DR-3 -47.15 -126.72    735   DR-3  1930-01-12
5   DR-3 -47.15 -126.72    751   DR-3  1930-02-26
6   DR-3 -47.15 -126.72    752   DR-3         NaN
7  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14
'''
# 其中，site中的信息(name,lat和long)被复制了，并且与visited数据匹配了
```

#### 4.4.3 多对多合并

```python
# 合并person和survey
ps = person.merge(survey, left_on = 'ident', right_on = 'person')
# 合并visited和survey
vs = visited.merge(survey,left_on = 'ident', right_on = 'taken')
print(ps)
'''
   ident   personal   family  taken person quant  reading
0   dyer    William     Dyer    619   dyer   rad     9.82
1   dyer    William     Dyer    619   dyer   sal     0.13
2   dyer    William     Dyer    622   dyer   rad     7.80
3   dyer    William     Dyer    622   dyer   sal     0.09
4     pb      Frank  Pabodie    734     pb   rad     8.41
5     pb      Frank  Pabodie    734     pb  temp   -21.50
6     pb      Frank  Pabodie    735     pb   rad     7.22
7     pb      Frank  Pabodie    751     pb   rad     4.35
8     pb      Frank  Pabodie    751     pb  temp   -18.50
9   lake   Anderson     Lake    734   lake   sal     0.05
10  lake   Anderson     Lake    751   lake   sal     0.10
11  lake   Anderson     Lake    752   lake   rad     2.19
12  lake   Anderson     Lake    752   lake   sal     0.09
13  lake   Anderson     Lake    752   lake  temp   -16.00
14  lake   Anderson     Lake    837   lake   rad     1.46
15  lake   Anderson     Lake    837   lake   sal     0.21
16   roe  Valentina  Roerich    752    roe   sal    41.60
17   roe  Valentina  Roerich    837    roe   sal    22.50
18   roe  Valentina  Roerich    844    roe   rad    11.25
'''
print(vs)
'''
    ident   site       dated  taken person quant  reading
0     619   DR-1  1927-02-08    619   dyer   rad     9.82
1     619   DR-1  1927-02-08    619   dyer   sal     0.13
2     622   DR-1  1927-02-10    622   dyer   rad     7.80
3     622   DR-1  1927-02-10    622   dyer   sal     0.09
4     734   DR-3  1939-01-07    734     pb   rad     8.41
5     734   DR-3  1939-01-07    734   lake   sal     0.05
6     734   DR-3  1939-01-07    734     pb  temp   -21.50
7     735   DR-3  1930-01-12    735     pb   rad     7.22
8     735   DR-3  1930-01-12    735    NaN   sal     0.06
9     735   DR-3  1930-01-12    735    NaN  temp   -26.00
10    751   DR-3  1930-02-26    751     pb   rad     4.35
11    751   DR-3  1930-02-26    751     pb  temp   -18.50
12    751   DR-3  1930-02-26    751   lake   sal     0.10
13    752   DR-3         NaN    752   lake   rad     2.19
14    752   DR-3         NaN    752   lake   sal     0.09
15    752   DR-3         NaN    752   lake  temp   -16.00
16    752   DR-3         NaN    752    roe   sal    41.60
17    837  MSK-4  1932-01-14    837   lake   rad     1.46
18    837  MSK-4  1932-01-14    837   lake   sal     0.21
19    837  MSK-4  1932-01-14    837    roe   sal    22.50
20    844   DR-1  1932-03-22    844    roe   rad    11.25
'''
```

```python
# 多对多合并，只需把匹配的多列以python列表形式传入merge函数中即可
ps_vs = ps.merge(vs,
                 left_on = ['ident', 'taken', 'quant', 'reading'],
                 right_on = ['person', 'ident', 'quant', 'reading'])
print(ps_vs.loc[0, ]) # 输出第一行
'''
ident_x           dyer
personal       William
family            Dyer
taken_x            619
person_x          dyer
quant              rad
reading           9.82
ident_y            619
site              DR-1
dated       1927-02-08
taken_y            619
person_y          dyer
Name: 0, dtype: object
'''
# 名称存在冲突pandas会自动向列名添加后缀，带_x后缀的列值来自"左DataFrame",带_y的后缀来自"右DataFrame"
```

## 第5章 缺失数据

### 5.2 何为NaN值

> 缺失值和其它类型的数据不同，实际上它们无甚意义。NaN也不等同于0或空字符串

```python
from numpy import NaN, NAN, nan
import pandas as pd

print(NaN == True) # False
print(NaN == False) # False
print(NaN == 0 # False
print(NaN == '') # False
# 一个缺失值和另一个缺失值也不相等
print(NaN == NaN) # False
print(NaN == nan) # False
print(NaN == NAN) # False
print(nan == NAN) # False
# pandas提供了isnull方法，用于测试某个值是否为缺失值
print(pd.isnull(NaN)) # True
print(pd.isnull(nan)) # True
print(pd.isnull(NAN)) # True
# pandas提供了notnull方法，用于测试某个值是否为缺失值
print(pd.notnull(NaN)) # False
print(pd.notnull(42)) # True
print(pd.notnull('missing')) # True
```

### 5.3 缺失值从何而来

> 一是包含缺失值的数据集，二是数据整理过程

#### 5.3.1 加载数据

> 在read_csv函数中，有三个参数与缺失值的读取有关：na_values, keep_default, na_filter
>
> na_values允许指定额外的缺失值或NaN值。读取文件时，可以传入Python str或列表对象，自动将其编码为缺失值。当然，现有默认缺失值(比如NA, NaN, nan)可用，因此该参数并不常用。
>
> keep_default_na参数是布尔值，它允许指定是否要把其他任何值视为缺失值。默认情况下改参数为True，这意味着使用na_values参数额外指定的缺失值都会追加到缺失值列表中。不过，也可以把keep_default_na设置为False(keep_default_na=False)，这将只使用na_values中指定的缺失值
>
> na_filter参数也是布尔值，用于指定某些值是否会被解读成"缺失值"。默认情况下，na_filter=True表示缺失值会被编码为NaN。如果设置na_filter=False，那么不会将任何值重新编码为"缺失值"。可以把该参数看作关闭na_values和keep_default_na参数设置的一种方法，想通过加载不含缺失值的数据来提升性能时经常使用它。

```python
visited_file = 'survey_visited.csv'
print(pd.read_csv(visited_file))
'''
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
'''
# 加载数据，不包含默认缺失值
print(pd.read_csv(visited_file, keep_default_na = False))
'''
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3            
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
'''
# 手动指定缺失值
print(pd.read_csv(visited_file,
                  na_values = [''],
                  keep_default_na = False))
'''
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
'''
```

#### 5.3.2 合并数据

```python
visited = pd.read_csv('survey_visited.csv')
survey = pd.read_csv('survey_survey.csv')
print(visited)
'''
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
'''
print(survey)
'''
    taken person quant  reading
0     619   dyer   rad     9.82
1     619   dyer   sal     0.13
2     622   dyer   rad     7.80
3     622   dyer   sal     0.09
4     734     pb   rad     8.41
5     734   lake   sal     0.05
6     734     pb  temp   -21.50
7     735     pb   rad     7.22
8     735    NaN   sal     0.06
9     735    NaN  temp   -26.00
10    751     pb   rad     4.35
11    751     pb  temp   -18.50
12    751   lake   sal     0.10
13    752   lake   rad     2.19
14    752   lake   sal     0.09
15    752   lake  temp   -16.00
16    752    roe   sal    41.60
17    837   lake   rad     1.46
18    837   lake   sal     0.21
19    837    roe   sal    22.50
20    844    roe   rad    11.25
'''
vs = visited.merge(survey, left_on = 'ident', right_on = 'taken')
print(vs)
'''
    ident   site       dated  taken person quant  reading
0     619   DR-1  1927-02-08    619   dyer   rad     9.82
1     619   DR-1  1927-02-08    619   dyer   sal     0.13
2     622   DR-1  1927-02-10    622   dyer   rad     7.80
3     622   DR-1  1927-02-10    622   dyer   sal     0.09
4     734   DR-3  1939-01-07    734     pb   rad     8.41
5     734   DR-3  1939-01-07    734   lake   sal     0.05
6     734   DR-3  1939-01-07    734     pb  temp   -21.50
7     735   DR-3  1930-01-12    735     pb   rad     7.22
8     735   DR-3  1930-01-12    735    NaN   sal     0.06
9     735   DR-3  1930-01-12    735    NaN  temp   -26.00
10    751   DR-3  1930-02-26    751     pb   rad     4.35
11    751   DR-3  1930-02-26    751     pb  temp   -18.50
12    751   DR-3  1930-02-26    751   lake   sal     0.10
13    752   DR-3         NaN    752   lake   rad     2.19
14    752   DR-3         NaN    752   lake   sal     0.09
15    752   DR-3         NaN    752   lake  temp   -16.00
16    752   DR-3         NaN    752    roe   sal    41.60
17    837  MSK-4  1932-01-14    837   lake   rad     1.46
18    837  MSK-4  1932-01-14    837   lake   sal     0.21
19    837  MSK-4  1932-01-14    837    roe   sal    22.50
20    844   DR-1  1932-03-22    844    roe   rad    11.25
'''
```

#### 5.3.3 用户输入值

> 用户可以自己创建缺失值，比如依据计算或人工向量来创建值向量。对于Series和DataFrame来说，NaN是有效值

```python
# Series包含缺失值
num_legs = pd.Series({'goal': 4, 'amoeba': nan})
print(num_legs)
'''
goal      4.0
amoeba    NaN
dtype: float64
'''
# DataFrame包含缺失值
scientists = pd.DataFrame({'Name': ['Rosaline Franklin', 'William Gosset'],
                           'Occupation': ['Chemist', 'Statistician'],
                           'Born': ['1920-07-25', '1876-06-13'],
                           'Died': ['1958-04-16', '1937-10-16']})
# 指定唯一缺失值
scientists['missing'] = nan
print(scientists)
'''
                Name    Occupation        Born        Died  missing
0  Rosaline Franklin       Chemist  1920-07-25  1958-04-16      NaN
1     William Gosset  Statistician  1876-06-13  1937-10-16      NaN
'''
```

#### 5.3.4 重建索引

> 另一种把缺失值引入数据的方法是为DataFrame重建索引。如果想向DataFrame添加新索引，并且保留其原始值，该方法非常有用。一个常见的使用场景是：在一个DataFrame中，其索引表示某段时间，而你想向该DataFrame中添加更多日期

```python
gapminder = pd.read_csv('gapminder.tsv', sep = '\t')
life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
print(life_exp)
'''
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
'''
# 可以通过数据切片重建索引
# 可以在前面的代码基础上添加loc
print(life_exp.loc[range(2000, 2010), ])
'''
year
2000          NaN
2001          NaN
2002    65.694923
2003          NaN
2004          NaN
2005          NaN
2006          NaN
2007    67.007423
2008          NaN
2009          NaN
Name: lifeExp, dtype: float64
'''
# 也可以分别取数据子集，然后调用reindex方法
y2000 = life_exp[life_exp.index > 2000]
print(y2000)
'''
year
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
'''
# 调用reindex方法
print(y2000.reindex(range(2000, 2010)))
'''
year
2000          NaN
2001          NaN
2002    65.694923
2003          NaN
2004          NaN
2005          NaN
2006          NaN
2007    67.007423
2008          NaN
2009          NaN
Name: lifeExp, dtype: float64
'''
```

### 5.4 处理缺失数据

#### 5.4.1 查找和统计缺失数据

```python
ebola = pd.read_csv('country_timeseries.csv')
# 统计非缺失值的个数
print(ebola.count())
'''
Date                   122
Day                    122
Cases_Guinea            93
Cases_Liberia           83
Cases_SierraLeone       87
Cases_Nigeria           38
Cases_Senegal           25
Cases_UnitedStates      18
Cases_Spain             16
Cases_Mali              12
Deaths_Guinea           92
Deaths_Liberia          81
Deaths_SierraLeone      87
Deaths_Nigeria          38
Deaths_Senegal          22
Deaths_UnitedStates     18
Deaths_Spain            16
Deaths_Mali             12
dtype: int64
'''
# 总行数减去不包含缺失值的行数
num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)
'''
Date                     0
Day                      0
Cases_Guinea            29
Cases_Liberia           39
Cases_SierraLeone       35
Cases_Nigeria           84
Cases_Senegal           97
Cases_UnitedStates     104
Cases_Spain            106
Cases_Mali             110
Deaths_Guinea           30
Deaths_Liberia          41
Deaths_SierraLeone      35
Deaths_Nigeria          84
Deaths_Senegal         100
Deaths_UnitedStates    104
Deaths_Spain           106
Deaths_Mali            110
dtype: int64
'''
# 统计缺失值的总数，可以用count_nonzero和isnull
print(np.count_nonzero(ebola.isnull())) # 1214
print(np.count_nonzero(ebola['Cases_Guinea'].isnull())) # 29
# 也可以使用Series的values_counts方法获取缺失值个数。该方法会输出值的频率表。使用dropna参数也可以获取缺失值的个数
# 从Cases_Guinea列获取前五个值的统计数
print(ebola.Cases_Guinea.value_counts(dropna = False).head())
'''
NaN       29
 86.0      3
 495.0     2
 112.0     2
 390.0     2
Name: Cases_Guinea, dtype: int64
'''
```

#### 5.4.2 清理缺失数据

> 可以用其他值替换缺失数据/使用现有数据填充缺失数据、直接将其从数据集中删除

__1.重新编码/替换__

> 可以用fillna方法把缺失值重新编码为其他值。比如将缺失值编码为0。查看文档，就会发现fillna和其他许多pandas函数一样有inplace参数。开启该参数意味着直接在原始数据上进行改动，并不会新建副本。对于大型数据，若想保持代码高效，可以使用该参数。

```python
print(ebola.fillna(0).iloc[0:10, 0:5])
'''
         Date  Day        ...          Cases_Liberia  Cases_SierraLeone
0    1/5/2015  289        ...                    0.0            10030.0
1    1/4/2015  288        ...                    0.0             9780.0
2    1/3/2015  287        ...                 8166.0             9722.0
3    1/2/2015  286        ...                 8157.0                0.0
4  12/31/2014  284        ...                 8115.0             9633.0
5  12/28/2014  281        ...                 8018.0             9446.0
6  12/27/2014  280        ...                    0.0             9409.0
7  12/24/2014  277        ...                 7977.0             9203.0
8  12/21/2014  273        ...                    0.0             9004.0
9  12/20/2014  272        ...                 7862.0             8939.0
'''
```

__2.前值填充__

> 对于缺失值，可以使用内置方法做前值补充(fill forward)或后值填充(fill backward)。做前值补充时，将按照前一个值填充缺失值，这样缺失值会被最后的已知值或被记录的值所替代

```python
print(ebola.fillna(0).iloc[0:10, 0:5])
print(ebola.fillna(method = 'ffill').iloc[0:10, 0:5])
'''
         Date  Day        ...          Cases_Liberia  Cases_SierraLeone
0    1/5/2015  289        ...                    NaN            10030.0
1    1/4/2015  288        ...                    NaN             9780.0
2    1/3/2015  287        ...                 8166.0             9722.0
3    1/2/2015  286        ...                 8157.0             9722.0
4  12/31/2014  284        ...                 8115.0             9633.0
5  12/28/2014  281        ...                 8018.0             9446.0
6  12/27/2014  280        ...                 8018.0             9409.0
7  12/24/2014  277        ...                 7977.0             9203.0
8  12/21/2014  273        ...                 7977.0             9004.0
9  12/20/2014  272        ...                 7862.0             8939.0
'''
# 如果某一列以一个缺失值开始，那么该缺失值会继续存在
```

__3.后值填充__

```python
print(ebola.fillna(method = 'bfill').iloc[:, 0:5].tail())
'''
          Date  Day        ...          Cases_Liberia  Cases_SierraLeone
117  3/27/2014    5        ...                    8.0                6.0
118  3/26/2014    4        ...                    NaN                NaN
119  3/25/2014    3        ...                    NaN                NaN
120  3/24/2014    2        ...                    NaN                NaN
121  3/22/2014    0        ...                    NaN                NaN
'''
```

__4.插值__

> 使用现有值来填充缺失值。pandas默认以线性方式填充缺失值。具体而言，它会把缺失值视为等距分隔值

```python
print(ebola.interpolate().iloc[0:10, 0:5])
'''
         Date  Day        ...          Cases_Liberia  Cases_SierraLeone
0    1/5/2015  289        ...                    NaN            10030.0
1    1/4/2015  288        ...                    NaN             9780.0
2    1/3/2015  287        ...                 8166.0             9722.0
3    1/2/2015  286        ...                 8157.0             9677.5
4  12/31/2014  284        ...                 8115.0             9633.0
5  12/28/2014  281        ...                 8018.0             9446.0
6  12/27/2014  280        ...                 7997.5             9409.0
7  12/24/2014  277        ...                 7977.0             9203.0
8  12/21/2014  273        ...                 7919.5             9004.0
9  12/20/2014  272        ...                 7862.0             8939.0
'''
# interpolate有一个参数method，用于指定插值方式
```

__5.删除缺失值__

> dropna方法删除缺失数据，并且可以设置参数控制删除方式。例如how参数用于指定行或列的删除条件，它的取值有两种：any(只要包含NA值就删除)与all(全为NA值才能删除)。thresh参数允许在删除行或列之前指定非NaN值的数量

```python
print(ebola.shape) # (122,18)
ebola_dropna = ebola.dropna()
print(ebola_dropna.shape) # (1,18)
print(ebola_dropna)
# 只保留那些完整的病例，最终只得到一行数据
'''
          Date  Day     ...       Deaths_Spain  Deaths_Mali
19  11/18/2014  241     ...                0.0          6.0
'''
```

#### 5.4.3 缺失值计算

```python
ebola['Cases_multiple'] = ebola['Cases_Guinea'] + \
                          ebola['Cases_Liberia'] + \
                          ebola['Cases_SierraLeone']
ebola_subset = ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia',
                             'Cases_SierraLeone', 'Cases_multiple']]
print(ebola_subset.head(n = 10))
'''
   Cases_Guinea       ...        Cases_multiple
0        2776.0       ...                   NaN
1        2775.0       ...                   NaN
2        2769.0       ...               20657.0
3           NaN       ...                   NaN
4        2730.0       ...               20478.0
5        2706.0       ...               20170.0
6        2695.0       ...                   NaN
7        2630.0       ...               19810.0
8        2597.0       ...                   NaN
9        2571.0       ...               19372.0
'''
```

> 

## 第6章 整理数据

> 整理数据是指对数据集进行结构化处理，使其易于分析和可视化

### 6.2 包含值而非变量的列

> 数据可以有包含值而非变量的列。这种格式更便于数据收集和展示

#### 6.2.1 固定一列

> 查看该数据集，可以看到每一列都是变量。与收入有关的值分布在多列中。对于在表格

```python
import pandas as pd

pew = pd.read_csv('pew.csv')
print(pew.iloc[:, 0:6])
'''
                   religion  <$10k  $10-20k  $20-30k  $30-40k  $40-50k
0                  Agnostic     27       34       60       81       76
1                   Atheist     12       27       37       52       35
2                  Buddhist     27       21       30       34       33
3                  Catholic    418      617      732      670      638
4        Don’t know/refused     15       14       15       11       10
5          Evangelical Prot    575      869     1064      982      881
6                     Hindu      1        9        7        9       11
7   Historically Black Prot    228      244      236      238      197
8         Jehovah's Witness     20       27       24       24       21
9                    Jewish     19       19       25       25       30
10            Mainline Prot    289      495      619      655      651
11                   Mormon     29       40       48       51       56
12                   Muslim      6        7        9       10        9
13                 Orthodox     13       17       23       32       32
14          Other Christian      9        7       11       13       13
15             Other Faiths     20       33       40       46       49
16    Other World Religions      5        2        3        4        2
17             Unaffiliated    217      299      374      365      341
'''
```

> 这种数据视图也称“宽”数据。要想将其转换成整洁的“长”数据格式，必须对DataFrame做“逆透视”/融合/聚合(unpivot/melt/gather)处理。pandas的melt函数可以把DataFrame重塑成整洁的数据格式。melt函数有如下几个参数
>
> id_vars:该参数是一个容器（列表、元祖或ndarray），所表示的变量会保持原样。
>
> value_vars:指定想“融合”（或转换为行）的列。它默认会“融合”未在id_vars参数中指定的所有列。
>
> var_name:该字符串用于指定values_vars融合后的新列名。默认为variable
>
> value_name:该字符串为新列名，代表var_name的值。默认为value

```python
# 不必指定value_vars，因为想对除"religion"列以外的所有列进行透视
pew_long = pd.melt(pew, id_vars = 'religion')
print(pew_long.head())
'''
             religion variable  value
0            Agnostic    <$10k     27
1             Atheist    <$10k     12
2            Buddhist    <$10k     27
3            Catholic    <$10k    418
4  Don’t know/refused    <$10k     15
'''
print(pew_long.tail())
'''
                  religion            variable  value
175               Orthodox  Don't know/refused     73
176        Other Christian  Don't know/refused     18
177           Other Faiths  Don't know/refused     71
178  Other World Religions  Don't know/refused      8
179           Unaffiliated  Don't know/refused    597
'''
# 更改默认值，以便命名进行融合/逆透视的列
pew_long = pd.melt(pew,
                   id_vars = 'religion',
                   var_name = 'income', # 变量命名
                   value_name = 'count') # 变量值命名
print(pew_long.head())
'''
             religion income  count
0            Agnostic  <$10k     27
1             Atheist  <$10k     12
2            Buddhist  <$10k     27
3            Catholic  <$10k    418
4  Don’t know/refused  <$10k     15
'''
print(pew_long.tail())
'''
                  religion              income  count
175               Orthodox  Don't know/refused     73
176        Other Christian  Don't know/refused     18
177           Other Faiths  Don't know/refused     71
178  Other World Religions  Don't know/refused      8
179           Unaffiliated  Don't know/refused    597
'''
```

#### 6.2.2 固定多列

> 当对其余列做“逆透视”时，并非每个数据集都有一列可以固定不动

```python
billboard = pd.read_csv('billboard.csv')
# 查看前几行和前几列
print(billboard.iloc[0:5, 0:16])
'''
   year        artist                    track  ...    wk9  wk10  wk11
0  2000         2 Pac  Baby Don't Cry (Keep...  ...    NaN   NaN   NaN
1  2000       2Ge+her  The Hardest Part Of ...  ...    NaN   NaN   NaN
2  2000  3 Doors Down               Kryptonite  ...   51.0  51.0  51.0
3  2000  3 Doors Down                    Loser  ...   62.0  61.0  61.0
4  2000      504 Boyz            Wobble Wobble  ...   53.0  57.0  64.0
'''
# 如果只使用其中的wk列
billboard_long = pd.melt(
  billboard,
  id_vars = ['year', 'artist', 'track', 'time', 'date.entered'],
  var_name = 'week',
  value_name = 'rating'
)
print(billboard_long.head())
'''
   year        artist                    track  ...   date.entered week rating
0  2000         2 Pac  Baby Don't Cry (Keep...  ...     2000-02-26  wk1   87.0
1  2000       2Ge+her  The Hardest Part Of ...  ...     2000-09-02  wk1   91.0
2  2000  3 Doors Down               Kryptonite  ...     2000-04-08  wk1   81.0
3  2000  3 Doors Down                    Loser  ...     2000-10-21  wk1   76.0
4  2000      504 Boyz            Wobble Wobble  ...     2000-04-15  wk1   57.0
'''
print(billboard_long.tail())
'''
       year            artist  ...    week rating
24087  2000       Yankee Grey  ...    wk76    NaN
24088  2000  Yearwood, Trisha  ...    wk76    NaN
24089  2000   Ying Yang Twins  ...    wk76    NaN
24090  2000     Zombie Nation  ...    wk76    NaN
24091  2000   matchbox twenty  ...    wk76    NaN
'''
```

### 6.3 包含多个变量的列

> 有时，数据集的列可能表示多个变量

```python
ebola = pd.read_csv('country_timeseries.csv')
print(ebola.columns)
'''
Index(['Date', 'Day', 'Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone',
       'Cases_Nigeria', 'Cases_Senegal', 'Cases_UnitedStates', 'Cases_Spain',
       'Cases_Mali', 'Deaths_Guinea', 'Deaths_Liberia', 'Deaths_SierraLeone',
       'Deaths_Nigeria', 'Deaths_Senegal', 'Deaths_UnitedStates',
       'Deaths_Spain', 'Deaths_Mali'],
      dtype='object')
'''
# 输出所选行
print(ebola.iloc[:5, [0, 1, 2, 3, 10, 11]])
'''
         Date  Day       ...        Deaths_Guinea  Deaths_Liberia
0    1/5/2015  289       ...               1786.0             NaN
1    1/4/2015  288       ...               1781.0             NaN
2    1/3/2015  287       ...               1767.0          3496.0
3    1/2/2015  286       ...                  NaN          3496.0
4  12/31/2014  284       ...               1739.0          3471.0
'''
# 列名Cases_Guinea和Death_Guinea包含两个变量:个人概况(分别是病例和死亡)，和国家名称。数据以“宽”格式排列，需要做“逆透视”
ebola_long = pd.melt(ebola, id_vars = ['Date', 'Day'])
print(ebola_long.head())
'''
         Date  Day      variable   value
0    1/5/2015  289  Cases_Guinea  2776.0
1    1/4/2015  288  Cases_Guinea  2775.0
2    1/3/2015  287  Cases_Guinea  2769.0
3    1/2/2015  286  Cases_Guinea     NaN
4  12/31/2014  284  Cases_Guinea  2730.0
'''
print(ebola_long.tail())
'''
           Date  Day     variable  value
1947  3/27/2014    5  Deaths_Mali    NaN
1948  3/26/2014    4  Deaths_Mali    NaN
1949  3/25/2014    3  Deaths_Mali    NaN
1950  3/24/2014    2  Deaths_Mali    NaN
1951  3/22/2014    0  Deaths_Mali    NaN
'''
```

#### 6.3.1 单独拆分和添加列(简单方法)

> 从概念上讲，可以依据列名中的下划线(_)拆分感兴趣的列。第一部分是新的状态列，第二部分是新的国家列。对此需要做字符串解析和拆分。在Python中，字符串是对象，类似于Series和DataFrame对象。第二章讲过Series(比如mean)和DataFrame有许多方法，本例使用split根据给定的分割符拆分字符串

```python
# 获取variable列
# 访问字符串方法
# 依据分割符拆分列
variable_split = ebola_long.variable.str.split('_')
print(variable_split[:5])
'''
0    [Cases, Guinea]
1    [Cases, Guinea]
2    [Cases, Guinea]
3    [Cases, Guinea]
4    [Cases, Guinea]
Name: variable, dtype: object
'''
print(variable_split[-5:])
'''
1947    [Deaths, Mali]
1948    [Deaths, Mali]
1949    [Deaths, Mali]
1950    [Deaths, Mali]
1951    [Deaths, Mali]
Name: variable, dtype: object
'''
# 整个容器
print(type(variable_split)) # <class 'pandas.core.series.Series'>
# 容器中的第一个元素
print(type(variable_split[0])) # <class 'list'>
# 拆分好列以后，下面把拆分得到的部分指派给一个新列。不过首先要提取status列的所有0号元素和country列的1号元素。再次访问字符串方法，然后使用get方法对各行索引取想要的索引
status_values = variable_split.str.get(0)
country_values = variable_split.str.get(1)
print(status_values[:5])
'''
0    Cases
1    Cases
2    Cases
3    Cases
4    Cases
'''
print(status_values[-5:])
'''
1947    Deaths
1948    Deaths
1949    Deaths
1950    Deaths
1951    Deaths
Name: variable, dtype: object
'''
print(country_values[:5])
'''
0    Guinea
1    Guinea
2    Guinea
3    Guinea
4    Guinea
Name: variable, dtype: object
'''
print(country_values[-5:])
'''
1947    Mali
1948    Mali
1949    Mali
1950    Mali
1951    Mali
Name: variable, dtype: object
'''
ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long.head())
'''
         Date  Day      variable   value status country
0    1/5/2015  289  Cases_Guinea  2776.0  Cases  Guinea
1    1/4/2015  288  Cases_Guinea  2775.0  Cases  Guinea
2    1/3/2015  287  Cases_Guinea  2769.0  Cases  Guinea
3    1/2/2015  286  Cases_Guinea     NaN  Cases  Guinea
4  12/31/2014  284  Cases_Guinea  2730.0  Cases  Guinea
'''
```

#### 6.3.2 在单个步骤中进行拆分和组合(简单方法)

> 返回的向量的顺序和数据的顺序相同。可以连接新向量或原始数据

```python
variable_split = ebola_long.variable.str.split('_', expand = True) # 拆分
variable_split.columns = ['status', 'country'] # 组合
ebola_parsed = pd.concat([ebola_long, variable_split], axis = 1) # 连接
print(ebola_parsed.head())
'''
         Date  Day      variable   value status country status country
0    1/5/2015  289  Cases_Guinea  2776.0  Cases  Guinea  Cases  Guinea
1    1/4/2015  288  Cases_Guinea  2775.0  Cases  Guinea  Cases  Guinea
2    1/3/2015  287  Cases_Guinea  2769.0  Cases  Guinea  Cases  Guinea
3    1/2/2015  286  Cases_Guinea     NaN  Cases  Guinea  Cases  Guinea
4  12/31/2014  284  Cases_Guinea  2730.0  Cases  Guinea  Cases  Guinea
'''
print(ebola_parsed.tail())
'''
           Date  Day     variable  value  status country  status country
1947  3/27/2014    5  Deaths_Mali    NaN  Deaths    Mali  Deaths    Mali
1948  3/26/2014    4  Deaths_Mali    NaN  Deaths    Mali  Deaths    Mali
1949  3/25/2014    3  Deaths_Mali    NaN  Deaths    Mali  Deaths    Mali
1950  3/24/2014    2  Deaths_Mali    NaN  Deaths    Mali  Deaths    Mali
1951  3/22/2014    0  Deaths_Mali    NaN  Deaths    Mali  Deaths    Mali
'''
```

#### 6.3.3 在单个步骤中进行拆分和组合(复杂方法)

> 可以使用内置的zip函数把拆分项列表组合在一起。zip函数接收一组迭代器（比如列表或元祖），创建一个由输入迭代器组成的新容器，每个新容器都拥有和输入容器相同的索引

```python
# zip函数返回迭代器
# 为了显示zip对象的内容，必须使用列表把zip函数包裹起来
constants = ['pi', 'e']
values = ['3.14', '2.718']
print(list(zip(constants, values))) # [('pi', '3.14'), ('e', '2.718')]
```

> 其中每个元素都由一个常量和对应值组成。从概念上讲，每个容器就像拉链上的一对齿扣。当把容器打包时，就会匹配并返回索引
>
> 可以把zip函数的功能理解为：zip函数把每个传入的容器堆叠起来，创建各种DataFrame，然后以元祖形式逐列返回值

```python
# 使用ebola_long.variable.str.split('_')拆分列值，由于结果是容器Series对象，现将其拆包（*操作符拆包），得到容器内容（每个状态-国家列表）
ebola_long['status'], ebola_long['country'] = zip(*ebola_long.variable.str.split('_'))
print(ebola_long.head())
```

### 6.4 行与列中的变量

> 有时数据会被格式化，变量同时出现在行和列中，即组合出现。

```python
# 一列数据包含两个变量，将变量转换为单独的列
weather = pd.read_csv('weather.csv')
print(weather.iloc[:5, :11])
'''
        id  year  month element  d1    d2    d3  d4    d5  d6  d7
0  MX17004  2010      1    tmax NaN   NaN   NaN NaN   NaN NaN NaN
1  MX17004  2010      1    tmin NaN   NaN   NaN NaN   NaN NaN NaN
2  MX17004  2010      2    tmax NaN  27.3  24.1 NaN   NaN NaN NaN
3  MX17004  2010      2    tmin NaN  14.4  14.4 NaN   NaN NaN NaN
4  MX17004  2010      3    tmax NaN   NaN   NaN NaN  32.1 NaN NaN
'''
# 天气数据包括每月中的每天（d1，d2，...，d31）记录的最低气温及最高气温（在element列分别用tmax和tmin表示）
# 对day进行融合
weather_melt = pd.melt(weather,
                       id_vars = ['id', 'year', 'month', 'element'],
                       var_name = 'day',
                       value_name = 'temp')
print(weather_melt.head())
'''
        id  year  month element day  temp
0  MX17004  2010      1    tmax  d1   NaN
1  MX17004  2010      1    tmin  d1   NaN
2  MX17004  2010      2    tmax  d1   NaN
3  MX17004  2010      2    tmin  d1   NaN
4  MX17004  2010      3    tmax  d1   NaN
'''
print(weather_melt.tail())
'''
          id  year  month element  day  temp
677  MX17004  2010     10    tmin  d31   NaN
678  MX17004  2010     11    tmax  d31   NaN
679  MX17004  2010     11    tmin  d31   NaN
680  MX17004  2010     12    tmax  d31   NaN
681  MX17004  2010     12    tmin  d31   NaN
'''
# 然后调整element列存储的变量。使用DataFrame的方法pivot_table
weather_tidy = weather_melt.pivot_table(
  index = ['id', 'year', 'month', 'day'],
  columns = 'element',
  values = 'temp'
)
print(weather_tidy.head())
'''
element                 tmax  tmin
id      year month day            
MX17004 2010 1     d30  27.8  14.5
             2     d11  29.7  13.4
                   d2   27.3  14.4
                   d23  29.9  10.7
                   d3   24.1  14.4
'''
# 每个element都是一个单独的列
# 将其平铺
weather_tidy_flat = weather_tidy.reset_index()
print(weather_tidy_flat.head())
'''
element       id  year  month  day  tmax  tmin
0        MX17004  2010      1  d30  27.8  14.5
1        MX17004  2010      2  d11  29.7  13.4
2        MX17004  2010      2   d2  27.3  14.4
3        MX17004  2010      2  d23  29.9  10.7
4        MX17004  2010      2   d3  24.1  14.4
'''
weather_tid = weather_melt.\
  pivot_table(
    index = ['id', 'year', 'month', 'day'],
    columns = 'element',
    values = 'temp').\
  reset_index()
print(weather_tid.head())
'''
element       id  year  month  day  tmax  tmin
0        MX17004  2010      1  d30  27.8  14.5
1        MX17004  2010      2  d11  29.7  13.4
2        MX17004  2010      2   d2  27.3  14.4
3        MX17004  2010      2  d23  29.9  10.7
4        MX17004  2010      2   d3  24.1  14.4
'''
```

### 6.5 一张表中的多个观测单元(归一化)

> 了解一张表中是否有多个观测单元，最简单的方法是查看每一行，并记录行间重复的所有单元或值。

```python
print(billboard_long.head())
'''
   year        artist                    track  ...   date.entered week rating
0  2000         2 Pac  Baby Don't Cry (Keep...  ...     2000-02-26  wk1   87.0
1  2000       2Ge+her  The Hardest Part Of ...  ...     2000-09-02  wk1   91.0
2  2000  3 Doors Down               Kryptonite  ...     2000-04-08  wk1   81.0
3  2000  3 Doors Down                    Loser  ...     2000-10-21  wk1   76.0
4  2000      504 Boyz            Wobble Wobble  ...     2000-04-15  wk1   57.0
'''
# 取特定track（Loser）取数据子集
print(billboard_long[billboard_long.track == 'Loser'].head())
'''
      year        artist  track  time date.entered week  rating
3     2000  3 Doors Down  Loser  4:24   2000-10-21  wk1    76.0
320   2000  3 Doors Down  Loser  4:24   2000-10-21  wk2    76.0
637   2000  3 Doors Down  Loser  4:24   2000-10-21  wk3    72.0
954   2000  3 Doors Down  Loser  4:24   2000-10-21  wk4    69.0
1271  2000  3 Doors Down  Loser  4:24   2000-10-21  wk5    67.0
'''
billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
print(billboard_songs.shape) # (24092, 4)
# 删除重复的行
billboard_songs =billboard_songs.drop_duplicates()
print(billboard_songs.shape) # (317, 4)
# 为每一行数据分配唯一的id
billboard_songs['id'] = range(len(billboard_songs))
print(billboard_songs.head(n = 10))
'''
   year          artist                    track  time  id
0  2000           2 Pac  Baby Don't Cry (Keep...  4:22   0
1  2000         2Ge+her  The Hardest Part Of ...  3:15   1
2  2000    3 Doors Down               Kryptonite  3:53   2
3  2000    3 Doors Down                    Loser  4:24   3
4  2000        504 Boyz            Wobble Wobble  3:35   4
5  2000            98^0  Give Me Just One Nig...  3:24   5
6  2000         A*Teens            Dancing Queen  3:44   6
7  2000         Aaliyah            I Don't Wanna  4:15   7
8  2000         Aaliyah                Try Again  4:03   8
9  2000  Adams, Yolanda            Open My Heart  5:30   9
'''
billboard_ratings = billboard_long.merge(
  billboard_songs, on = ['year', 'artist', 'track', 'time']
)
print(billboard_ratings.head())
'''
   year artist                    track  time date.entered week  rating  id
0  2000  2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26  wk1    87.0   0
1  2000  2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26  wk2    82.0   0
2  2000  2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26  wk3    72.0   0
3  2000  2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26  wk4    77.0   0
4  2000  2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26  wk5    87.0   0
'''
billboard_ratings = billboard_ratings[['id', 'date.entered', 'week', 'rating']]
print(billboard_ratings.head())
'''
   id date.entered week  rating
0   0   2000-02-26  wk1    87.0
1   0   2000-02-26  wk2    82.0
2   0   2000-02-26  wk3    72.0
3   0   2000-02-26  wk4    77.0
4   0   2000-02-26  wk5    87.0
'''
```

### 6.6 跨多张表的观测单元

#### 6.6.1 使用循环加载多个文件

#### 6.6.2 实用列表推导加载多个文件

## 第7章 数据类型

### 7.2 数据类型

```python
import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")
# 获取DataFrame每列的数据类型
print(tips.dtypes)
'''
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
dtype: object
'''
# category数据类型表示分类变量，它和普通的object不同
```

### 7.3 类型转换

#### 7.3.1 转换为字符串对象

```python
# 把列值转换为字符串使用astype方法
tips['sex_str'] = tips['sex'].astype(str) # 将其转换为str类型
print(tips.dtypes)
'''
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
'''
```

#### 7.3.2 转换为数值类型

```python
# Series也可以使用astype进行转换
# 转换为字符串
tips['total_bill'] = tips['total_bill'].astype(str)
print(tips.dtypes)
'''
total_bill      object
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
'''
# 转换为float
tips['total_bill'] = tips['total_bill'].astype(float)
print(tips.dtypes)
'''
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
'''
```

__1.to_numeric函数__

> 把变量转换为数值类型

```python
# 获取tips子集
tips_sub_miss = tips.head(10)
# 添加一些缺失值,将total_bill中的NaN装换为missing显示出来
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
print(tips_sub_miss)
'''
  total_bill   tip     sex smoker  day    time  size sex_str
0      16.99  1.01  Female     No  Sun  Dinner     2  Female
1    missing  1.66    Male     No  Sun  Dinner     3    Male
2      21.01  3.50    Male     No  Sun  Dinner     3    Male
3    missing  3.31    Male     No  Sun  Dinner     2    Male
4      24.59  3.61  Female     No  Sun  Dinner     4  Female
5    missing  4.71    Male     No  Sun  Dinner     4    Male
6       8.77  2.00    Male     No  Sun  Dinner     2    Male
7    missing  3.12    Male     No  Sun  Dinner     4    Male
8      15.04  1.96    Male     No  Sun  Dinner     2    Male
9      14.78  3.23    Male     No  Sun  Dinner     2    Male
'''
# total_bill列变成object类型
print(tips_sub_miss.dtypes)
'''
total_bill      object
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
'''
```

> to_numeric有一个参数errors，它决定了当该函数遇到无法转换为数值的值时该如何处理。默认情况下，该参数值为raise，即如果to_numeric遇到无法转换为数值的值，它就会“引发”一个错误
>
> errors的三中取值
>
> raise：默认值，遇到无法转换为数值的值，它就会“引发”一个错误
>
> coerce：遇到无法转换为数值的值，转换为NaN
>
> ignore：遇到无法转换为数值的值时放弃转换，直接返回整列

```python
tips_sub_miss['total_bill'] = pd.to_numeric(
  tips_sub_miss['total_bill'], errors = 'ignore'
)
print(tips_sub_miss) # 无变化
'''
  total_bill   tip     sex smoker  day    time  size sex_str
0      16.99  1.01  Female     No  Sun  Dinner     2  Female
1    missing  1.66    Male     No  Sun  Dinner     3    Male
2      21.01  3.50    Male     No  Sun  Dinner     3    Male
3    missing  3.31    Male     No  Sun  Dinner     2    Male
4      24.59  3.61  Female     No  Sun  Dinner     4  Female
5    missing  4.71    Male     No  Sun  Dinner     4    Male
6       8.77  2.00    Male     No  Sun  Dinner     2    Male
7    missing  3.12    Male     No  Sun  Dinner     4    Male
8      15.04  1.96    Male     No  Sun  Dinner     2    Male
9      14.78  3.23    Male     No  Sun  Dinner     2    Male
'''
print(tips_sub_miss.dtypes)
'''
total_bill      object
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
'''
tips_sub_miss['total_bill'] = pd.to_numeric(
  tips_sub_miss['total_bill'], errors = 'coerce'
)
print(tips_sub_miss)
'''
   total_bill   tip     sex smoker  day    time  size sex_str
0       16.99  1.01  Female     No  Sun  Dinner     2  Female
1         NaN  1.66    Male     No  Sun  Dinner     3    Male
2       21.01  3.50    Male     No  Sun  Dinner     3    Male
3         NaN  3.31    Male     No  Sun  Dinner     2    Male
4       24.59  3.61  Female     No  Sun  Dinner     4  Female
5         NaN  4.71    Male     No  Sun  Dinner     4    Male
6        8.77  2.00    Male     No  Sun  Dinner     2    Male
7         NaN  3.12    Male     No  Sun  Dinner     4    Male
8       15.04  1.96    Male     No  Sun  Dinner     2    Male
9       14.78  3.23    Male     No  Sun  Dinner     2    Male
'''
print(tips_sub_miss.dtypes)
'''
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
'''
```

__2.to_numeric向下转型__

> to_numeric函数还有一个downcast参数，它允许把列（或向量）转换为数值向量后，把数值类型更改（即向下转型）为最小的数值类型。默认情况下，downcast的值为None，其它可能有的值有“interge”“unsigned”“signed”“float”

```python
tips_sub_miss['total_bill'] = pd.to_numeric(
  tips_sub_miss['total_bill'],
  errors = 'coerce',
  downcast = 'float'
)
print(tips_sub_miss)
'''
   total_bill   tip     sex smoker  day    time  size sex_str
0       16.99  1.01  Female     No  Sun  Dinner     2  Female
1         NaN  1.66    Male     No  Sun  Dinner     3    Male
2       21.01  3.50    Male     No  Sun  Dinner     3    Male
3         NaN  3.31    Male     No  Sun  Dinner     2    Male
4       24.59  3.61  Female     No  Sun  Dinner     4  Female
5         NaN  4.71    Male     No  Sun  Dinner     4    Male
6        8.77  2.00    Male     No  Sun  Dinner     2    Male
7         NaN  3.12    Male     No  Sun  Dinner     4    Male
8       15.04  1.96    Male     No  Sun  Dinner     2    Male
9       14.78  3.23    Male     No  Sun  Dinner     2    Male
'''
print(tips_sub_miss.dtypes)
'''
total_bill     float32 # 转换为float32，使用的内存变小了
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
'''
```

### 7.4 分类数据

> pandas有一种categor dtype，用于对分类值进行编码。优点如下
>
> 采用这种方法能显著节约内存，提高速度
>
> 当一列值存在一定的顺序时，应转换成分类数据
>
> 有些Python库可以处理分类数据

#### 7.4.1 转换为category类型

> 调用astype方法时，只要把category传递给它，他就能把一列的数据类型转换为category类型
>

```python
# 首先把sex列转换为字符串对象
tips['sex'] = tips['sex'].astype('str')
print(type(tips)) # <class 'pandas.core.frame.DataFrame'>
print(tips.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype   
---  ------      --------------  -----   
 0   total_bill  244 non-null    float64 
 1   tip         244 non-null    float64 
 2   sex         244 non-null    object  
 3   smoker      244 non-null    category
 4   day         244 non-null    category
 5   time        244 non-null    category
 6   size        244 non-null    int64   
 7   sex_str     244 non-null    object  
dtypes: category(3), float64(2), int64(1), object(2)
memory usage: 10.7+ KB
None
'''
# 把sex列的数据类型转换为category类型
tips['sex'] = tips['sex'].astype('category')
print(tips.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype   
---  ------      --------------  -----   
 0   total_bill  244 non-null    float64 
 1   tip         244 non-null    float64 
 2   sex         244 non-null    category
 3   smoker      244 non-null    category
 4   day         244 non-null    category
 5   time        244 non-null    category
 6   size        244 non-null    int64   
 7   sex_str     244 non-null    object  
dtypes: category(4), float64(2), int64(1), object(1)
memory usage: 9.2+ KB
None
'''
```

#### 7.4.2 操作分类数据

| 属性或方法                            | 说明               |
| ------------------------------------- | ------------------ |
| Series.cat.categories                 | 类别               |
| Series.cat.ordered                    | 类别是否有顺序     |
| Series.cat.codes                      | 返回类别的整数代码 |
| Series.cat.rename_categories()        | 重命名类别         |
| Series.cat.reorder_categories()       | 对类别重新排序     |
| Series.cat.add_categories()           | 添加新类别         |
| Series.cat.remove_categories()        | 删除类别           |
| Series.cat.remove_unused_categories() | 删除未使用的类别   |
| Series.cat.set_categories()           | 设置新类别         |
| Series.cat.as_categories()            | 对类别排序         |
| Series.cat.as_unordered()             | 使类别无序         |

## 第8章 字符串和文本数据

### 8.2 字符串

```python
word = 'grail'
sent = 'a scratch'
```

#### 8.2.1 取子串和字符串切片

| 索引     | 0    | 1    | 2    | 3    | 4    |
| -------- | ---- | ---- | ---- | ---- | ---- |
| 字符串   | g    | r    | a    | i    | l    |
| 负数索引 | -5   | -4   | -3   | -2   | -1   |

| 索引     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
| -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 字符串   | a    |      | s    | c    | r    | a    | t    | c    | h    |
| 负数索引 | -9   | -8   | -7   | -6   | -5   | -4   | -3   | -2   | -1   |

__1.单个字符__

```python
print(word[0]) # g
print(sent[0]) # a
```

__2.字符串切片__

```python
# 获取前三个字符
# 索引3代表第4个字符
print(word[0:3]) # gra
# 左包含右排除，即包含冒号左侧索引值而不包含右侧索引值
```

__3.负数索引__

```python
print(sent[-1]) # h
print(sent[-9:-8]) # a
# 负数索引和非负结合
print(sent[0:-8]) # a
print(sent[2:-1]) # scratc
print(sent[-7:-1]) # scratc
```

#### 8.2.2 获取字符串的最后一个字符

> 负数索引-1

```python
s_len = len(sent)
print(s_len) # 9
print(sent[2:s_len]) # scratch
```

__1.从头开始或取到末尾的切片__

```python
print(word[0:3]) # gra
print(word[ :3]) # gra
print(sent:[2:len(sent)]) # Scratch
print(sent[2: ]) # Scratch
# 取整个字符串
print(sent[:]) # a scratch
```

__2.增量切片__

```python
# 每隔一个字符取一个字符
print(sent[::2]) # asrth
# 每隔两个字符取一个字符
print(sent[::3]) # act
```

### 8.3 字符串方法

| 方法       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| capitalize | 把首字母大写                                                 |
| count      | 统计指定字符串出现的次数                                     |
| startswith | 检查字符串是否以指定值开始，若是，返回True                   |
| endswith   | 检查字符串是否以指定值结束，若是，返回True                   |
| find       | 在字符串查找指定字符串，若找到，则返回首次出现的索引，否则返回-1 |
| index      | 功能和find相同，但当匹配失败时，返回ValueError               |
| isalpha    | 若字符串中的所有字符都是字母，则返回True                     |
| isdecimal  | 若字符串中的所有字符都是十进制，则返回True。类似的还有isdigit、isnumeric等 |
| isalnum    | 若字符串中的所有字母都是字母要么是数字，则返回True           |
| lower      | 把字符串的所有字母改为小写                                   |
| upper      | 把字符串的所有字母改为大写                                   |
| replace    | 把字符串中的old替换成new                                     |
| strip      | 删除字符串头尾指定的字符                                     |
| split      | 按照指定分割符分割字符串，并返回有这些分割片段组成的列表     |
| partition  | 类似于split(maxsplit=1)，但它会同时返回分割符                |
| center     | 把字符串居中对齐到指定宽度                                   |
| zfill      | 按指定宽度复制字符串，原字符串向右靠齐，前面填充0            |

```python
print("black Knight".capitalize()) # Black knight
print("It's just a flesh wound".count('u')) # 2
print("Halt! Who goes there?".startswith('Halt')) # True
print("coconut".endswith('nut')) # True
print("It's just a flesh wound!".find('u')) # 6
print("It's just a flesh wound!".index('scratch')) # ValueError
print("old woman".isalpha()) # False(因为有空格)
print("37".isdecimal()) # True
print("I'm 37.".isalnum()) # False(因为有'和空格)
print("Black Knight".lower()) # black knight
print("Black Knight".upper()) # BLACK KNIGHT
print("flesh wound!".replace('flesh wound', 'scratch')) # scratch!
print(" I'm not dead. ".strip()) # I'm not dead.
print("NI! NI! NI! NI!".split(sep = ' ')) # ['NI!', 'NI!', 'NI!', 'NI!']
print("3,4".partition(',')) # ('3', ',', '4')
print("nine".center(10)) # '   nine   '
print("9".zfill(5)) # 00009
```

### 8.4 更多字符串方法

#### 8.4.1 join方法

> join方法带有一个参数，该参数是可迭代的容器（比如列表），返回通过指定字符连接元素后生成的新字符串。例如使用度（经纬度）、分和秒来返回坐标

```python
d2 = '73°'
m2 = "58'"
s2 = '26.302"'
u2 = 'W'
# 使用空格把这些值连接起来
coords = ' '.join([d1, m1, s1, u1, d2, m2, s2, u2])
print(coords) # 40° 46' 52.837" N 73° 58' 26.302" W
```

#### 8.4.2 splitlines方法

> splitlines方法和split相似。它通常用于跨多行的字符串，并返回一个列表，其中每个元素是该跨行字符串的一行

```python
multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.
"""
print(multi_str)
'''
Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.
'''
multi_str_split = multi_str.splitlines()
print(multi_str_split)
'''
['Guard: What? Ridden on a horse?', 'King Arthur: Yes!', "Guard: You're using coconuts!", 'King Arthur: What?', "Guard: You've got ... coconut[s] and you're bangin' 'em together."]
'''
guard = multi_str_split[::2]
print(guard)
'''
['Guard: What? Ridden on a horse?', "Guard: You're using coconuts!", "Guard: You've got ... coconut[s] and you're bangin' 'em together."]
'''
guard = multi_str.replace("Guard:", "").splitlines()[::2]
print(guard)
'''
[' What? Ridden on a horse?', " You're using coconuts!", " You've got ... coconut[s] and you're bangin' 'em together."]
'''
```

### 8.5 字符串格式化

#### 8.5.1 自定义字符串格式

#### 8.5.2 格式化字符串

> 格式化字符串需要编写一个带有特殊占位符的字符串，并在字符串上调用format方法向占位符插入值

```python
var = 'flesh wound'
s = "It's just a {}!"
print(s.format(var)) # It's just a flesh wound!
print(s.format('scratch')) # It's just a scratch!
# 占位符还可以通过索引多次引用变量
s = """Black Knight: 'Tis but a {0}.
King Arthur: A{0}? Your arm's off!
"""
print(s.format('scratch'))
'''
Black Knight: 'Tis but a scratch.
King Arthur: Ascratch? Your arm's off!
'''
# 也可以给占位符一个变量
s = 'Hayden Planetarium Coordinates: {lat}, {lon}'
print(s.format(lat='40.7815°N', lon='73.9733°W')) # Hayden Planetarium Coordinates: 40.7815°N, 73.9733°W
```

#### 8.5.3 格式化数字

```python
print('Some digits of pi: {}'.format(3.14159265359))
# Some digits of pi: 3.14159265359
# ,表示千分位分割符
print("In 2005, Lu Chao of China recited {:,} digits of pi".format(67890))
# In 2005, Lu Chao of China recited 67,890 digits of pi
# {0:.4}和{0:.4%}中的0表示索引值，4表示保留多少位小数
# 如果添加上%，则会把小数格式化为百分数
print("I remember {0:.4} or {0:.4%} of what Lu Chao recited".format(7/67890))
# I remember 0.0001031 or 0.0103% of what Lu Chao recited
# 在{0:05d}中，第一个0表示索引值
# 第二个0是要填充的字符
# 5表示总共有多少个字符
# d表示要使用数字
# 整体表示总共有5个字符，前面使用0进行填充
print("My ID number is {0:05d}".format(42)) 
# My ID number is 00042
```

#### 8.5.4 C printf格式化风格

```python
s = 'I only know %d digits of pi' % 7
print(s) # I only know 7 digits of pi
# s代表字符串
# 字符串模式使用圆括号代替了花括号
# 传入的是一个Python字典，使用花括号
print('Some digits of %(cont)s: %(value).2f' % {'cont': 'e', 'value': 2.718})
# Some digits of e: 2.72
```

#### 8.5.5 Python 3.6+中的格式化字符串

> 格式化字符串是Python的新特性，其中字符串必须以字母f开头。然后可以直接在占位符{}中使用变量，无需调用format方法

```python
var = 'flesh wound'
s = f"It's just a {var}!"
print(s)
# It's just a flesh wound!
lat = '40.7815° N'
lon = '73.9733° W'
s = f'Hayden Planetarium Coordinates: {lat}, {lon}'
print(s)
# Hayden Planetarium Coordinates: 40.7815° N, 73.9733° W
```

### 8.6 正则表达式

| 语法  | 说明                                          |
| ----- | --------------------------------------------- |
| .     | 匹配所有字符串                                |
| ^     | 从字符串开头匹配                              |
| $     | 从字符串末尾匹配                              |
| *     | 匹配前一个字符任意次                          |
| +     | 匹配前一个字符一次或多次                      |
| ?     | 匹配前一个字符零次或一次                      |
| {m}   | 匹配前一个字符m次                             |
| {m,n} | 对于前一个字符，最少匹配m次且最多匹配n次      |
| \     | 转义字符                                      |
| []    | 一组字符（比如[a-z]）将匹配a到z之间的所有字母 |
| \|    | 或。A\|B匹配A或B                              |
| ()    | 精确匹配括号中指定的模式                      |

| 序列 | 说明                         |
| ---- | ---------------------------- |
| \d   | 匹配一个数字字符             |
| \D   | 匹配一个非数字字符(与\d相反) |
| \s   | 匹配任何不可见字符           |
| \S   | 匹配任何可见字符(与\s相反)   |
| \w   | 匹配单词符号                 |
| \W   | 匹配任何非单词字符(与\w相反) |

> 为了使用正则表达式，先编写一个正则表达式模式的字符串，并为这个待匹配的模块提供一个字符串。re模块中的许多函数可以用于处理各种特定需求。

| 函数      | 说明                                                     |
| --------- | -------------------------------------------------------- |
| search    | 在字符串中进行搜素，成功则返回匹配目标，失败返回None     |
| match     | 从字符串开头进行匹配，成功则返回匹配目标，失败则返回None |
| fullmatch | 匹配整个字符串                                           |
| split     | 根据模式分割字符串                                       |
| findall   | 查找字符串中的所有非重叠匹配                             |
| finditer  | 类似于findall，但返回Python迭代器                        |
| sub       | 用提供的字符串替代匹配模式                               |

#### 8.6.1 匹配模式

```python
import re
tele_num = '1234567890'
# match查看是否和字符串匹配，返回match对象
m = re.match(pattern = '\d\d\d\d\d\d\d\d\d\d', string = tele_num)
print(type(m)) # <class 're.Match'>
# 如果存在匹配，span会给出匹配字符串的索引，match会给出精确匹配的字符串
print(m) # <re.Match object; span=(0, 10), match='1234567890'>
# 判断是否存在匹配
print(bool(m)) # True
if m:
  print('match')
else:
  print('no match')
# match
# 如果想获取匹配对象的某些值，比如索引位置或实际匹配的字符串，可以使用match对象的一些方法
# 获取第一个匹配字符串的索引
print(m.start()) # 0
# 获取最后一个索引
print(m.end()) # 10
# 获取第一个和最后一个索引
print(m.span()) # (1,10)
# 获取与指定模式相匹配的字符串
print(m.group()) # 1234567890
# 电话号码复杂时
tele_num_spaces = '123 456 7890'
m = re.match(pattern = 'd\{10}', string = tele_num_spaces)
print(m) # None
# 匹配失败

# 可以把RegEx模式看作单独的变量
# 因为它可能变得很长，让对实际匹配函数的调用难以阅读
p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern = p, string = tele_num_spaces)
print(m) # <re.Match object; span=(0, 12), match='123 456 7890'>
# 电话号码更复杂时
tele_num_space_paren_dash = '(123) 456-7890'
p = '\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern = p, string = tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 14), match='(123) 456-7890'>
# 更复杂
cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern = p, string = cnty_tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 17), match='+1 (123) 456-7890'>
```

#### 8.6.2 查找模式

```python
p = '\d+'
# Python连接两个彼此靠近的字符串
s = "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "\
  "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
m = re.findall(pattern = p, string = s)
print(m) # ['13', '12', '11', '10', '9']
```

#### 8.6.3 模式替代

```python
p = '\w+\s?\w+:\s?'
s = re.sub(pattern = p, string = multi_str, repl = '')
print(s)
'''
What? Ridden on a horse?
Yes!
You're using coconuts!
What?
You've got ... coconut[s] and you're bangin' 'em together.
'''
guard = s.splitlines()[ ::2]
kinga = s.splitlines()[1::2] # 跳过第一个元素
print(guard)
'''
['What? Ridden on a horse?', "You're using coconuts!", "You've got ... coconut[s] and you're bangin' 'em together."]
'''
print(kinga) # ['Yes!', 'What?']
```

#### 8.6.4 编译模式

> 处理数据的时候，很多操作通常是按行或列进行的，Python的re模块支持对模式进行编译，以便复用它。这可能会提升性能，特别是当数据量很大时，性能提升会显著。
>
> 首先编写正则表达式模式，但这次不把它直接保存到变量中，而是把模式字符串传递到compile函数中并保存结果。然后就可以在这个编译好的模式上调用其他re函数了。而且，由于模式已经编译好了，无须再在方法中指定模式参数了

```python
p = re.compile('\d{10}')
s = '1234567890'
# 注意：这里直接在编译好的模式上调用match函数
# 并未使用re.match这种方式
m = p.match(s)
print(m) # <re.Match object; span=(0, 10), match='1234567890'>
p = re.compile('\d+')
s = "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "\
  "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
m = p.findall(s)
print(m) # ['13', '12', '11', '10', '9']
# 调用sub实施替换
p = re.compile('\w+\s?\w+:\s?')
s = "Guard: You're using coconuts!"
m = p.sub(string = s, repl = '')
print(m) # You're using coconuts!
```

### 8.7 regex库

```python
import regex
p = regex.compile('\d+')
s = "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "\
  "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
m = p.findall(s)
print(m) # ['13', '12', '11', '10', '9']
# www.rexegg,com
```

## 第9章 应用

### 9.2 函数

```python
# 两个实用的函数
def my_sq(x):
  """
  求平方
  """
  return x ** 2
def avg_2(x, y):
  """求两个数的平均值
  """
  return (x + y) / 2
print(my_sq(4)) # 16
print(avg_2(10, 20)) # 15.0
```

### 9.3 使用函数

```python
df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})
print(df)
'''
    a   b
0  10  20
1  20  30
2  30  40
'''
# 这时可以把自定义的函数应用于一个Series（即单独一行或一列）
print(df['a'] ** 2)
'''
0    100
1    400
2    900
Name: a, dtype: int64
'''
```

#### 9.3.1 Series的apply方法

> 在pandas中，当从DataFrame中取出一行或一列时，返回的对象类型是Series。Series有一个apply方法。该方法有一个func参数。当传递给它一个函数之后，apply方法就会把传入的函数应用于Series的每个元素

```python
# 获取第一列
print(type(df['a'])) # <class 'pandas.core.series.Series'>
# 获取第一行
print(type(df.iloc[0])) # <class 'pandas.core.series.Series'>
# 把平方函数应用于列a
sq = df['a'].apply(my_sq)
print(sq)
'''
0    100
1    400
2    900
Name: a, dtype: int64
'''
def my_exp(x, e):
  return x ** e
cb = my_exp(2, 3)
print(cb) # 8
# 当把my_exp函数应用于一个Series中，除了要把my_exp传递给apply之外，还要多传递一个参数，用于设置指数的大小
ex = df['a'].apply(my_exp, e = 2)
print(ex)
'''
0    100
1    400
2    900
Name: a, dtype: int64
'''
ex = df['a'].apply(my_exp, e = 3)
print(ex)
'''
0     1000
1     8000
2    27000
Name: a, dtype: int64
'''
```

#### 9.3.2DataFrame的apply方法

> DataFrame应用一个函数时，首先要指定应用函数的轴，例如逐行或逐列。按列使用把axis的参数设置为0。按行使用设置为1.

__1.按列应用__

```python
def print_me(x):
  print(x)
df.apply(print_me, axis = 0)
'''
0    10
1    20
2    30
Name: a, dtype: int64
0    20
1    30
2    40
Name: b, dtype: int64
'''
```

__2.按行应用__

### 9.4 apply高级用法

```python
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.6+ KB
None
'''
```

> 该数据集有891行和15列，age值都存在的有714个，deck值都存在的有203个。可以用apply计算数据中有多少个null或NaN值，以及每一列或每一行中数据完整案例所占的百分比

```python
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
```

#### 9.4.1 按列应用

```python
cmis_col = titanic.apply(count_missing)
pmis_col = titanic.apply(prop_missing)
pcom_col = titanic.apply(prop_complete)
print(cmis_col)
'''
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
'''
print(pmis_col)
'''
survived       0.000000
pclass         0.000000
sex            0.000000
age            0.198653
sibsp          0.000000
parch          0.000000
fare           0.000000
embarked       0.002245
class          0.000000
who            0.000000
adult_male     0.000000
deck           0.772166
embark_town    0.002245
alive          0.000000
alone          0.000000
dtype: float64
'''
print(pcom_col)
'''
survived       1.000000
pclass         1.000000
sex            1.000000
age            0.801347
sibsp          1.000000
parch          1.000000
fare           1.000000
embarked       0.997755
class          1.000000
who            1.000000
adult_male     1.000000
deck           0.227834
embark_town    0.997755
alive          1.000000
alone          1.000000
dtype: float64
'''
print(titanic.loc[pd.isnull(titanic.embark_town), :])
'''
     survived  pclass     sex   age  ...  deck  embark_town  alive alone
61          1       1  female  38.0  ...     B          NaN    yes  True
829         1       1  female  62.0  ...     B          NaN    yes  True
'''
```

#### 9.4.2 按行应用

```python
cmis_row = titanic.apply(count_missing, axis = 1)
pmis_row = titanic.apply(prop_missing, axis = 1)
pcom_row = titanic.apply(prop_complete, axis = 1)
print(cmis_row.head())
'''
0    1
1    0
2    1
3    0
4    1
dtype: int64
'''
print(pmis_row.head())
'''
0    0.066667
1    0.000000
2    0.066667
3    0.000000
4    0.066667
dtype: float64
'''
print(pcom_row.head())
'''
0    0.933333
1    1.000000
2    0.933333
3    1.000000
4    0.933333
dtype: float64
'''
# 有多少行包含多个缺失值
print(cmis_row.value_counts())
'''
1    549
0    182
2    160
dtype: int64
'''
titanic['num_missing'] = titanic.apply(count_missing, axis = 1)
print(titanic.head())
'''
   survived  pclass     sex   age  ...  embark_town  alive  alone num_missing
0         0       3    male  22.0  ...  Southampton     no  False           1
1         1       1  female  38.0  ...    Cherbourg    yes  False           0
2         1       3  female  26.0  ...  Southampton    yes   True           1
3         1       1  female  35.0  ...  Southampton    yes  False           0
4         0       3    male  35.0  ...  Southampton     no   True           1
'''
```

### 9.5 向量化函数

```python
df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})
print(df)
'''
    a   b
0  10  20
1  20  30
2  30  40
'''
def avg_2(x, y):
  return (x + y) / 2
print(avg_2(df['a'], df['b']))
'''
0    15.0
1    25.0
2    35.0
dtype: float64
'''
```

#### 9.5.1 使用NumPy

```python
# np.vectorize会创建一个新函数
def avg_2_mod(x, y):
  if x == 20:
    return np.NaN
  else:
    return (x + y) / 2
avg_2_mod_vec = np.vectorize(avg_2_mod) # 将该函数向量化
print(avg_2_mod_vec(df['a'], df['b'])) # [15. nan 35.]
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
print(v_avg_2_mod(df['a'], df['b'])) # [15. nan 35.]
```

#### 9.5.2 使用numba

> numba库是为了优化Python代码而设计的，尤其针对进行数学计算的数组计算

```python
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
print(v_avg_2_numba(df['a'], df['b'])) # numba不支持pandas对象
'''ValueError: cannot determine Numba type of <class 'pandas.core.series.Series'>'''#
# 必须将其转化为Numpy数组并传入
print(v_avg_2_numba(df['a'].values, df['b'].values)) # [15. nan 35.]
```

### 9.6 lambda函数

> 编写一个模式，从数据行提取所有字母，并把它们赋给新的name列。可以先编写一个函数，然后调用apply应用它

```python
docs = pd.read_csv('doctors.csv', header = None)
import regex
p = regex.compile('\w+\s+\w+')
def get_name(s):
  return p.match(s).group()
docs['name_func'] = docs[0].apply(get_name)
print(docs)
'''
                               0              name_func
0     William Hartnell (1963-66)       William Hartnell
1    Patrick Troughton (1966-69)      Patrick Troughton
2          Jon Pertwee (1970 74)            Jon Pertwee
3            Tom Baker (1974-81)              Tom Baker
4        Peter Davison (1982-84)          Peter Davison
5          Colin Baker (1984-86)            Colin Baker
6      Sylvester McCoy (1987-89)        Sylvester McCoy
7             Paul McGann (1996)            Paul McGann
8   Christopher Eccleston (2005)  Christopher Eccleston
9        David Tennant (2005-10)          David Tennant
10          Matt Smith (2010-13)             Matt Smith
11     Peter Capaldi (2014-2017)          Peter Capaldi
12        Jodie Whittaker (2017)        Jodie Whittaker
'''
```

> get_name函数非常简单，仅有一行代码。通常直接把代码写到apply方法中，即运用lambda函数。使用lambda函数重写上面的代码。

```python
docs['name_lamb'] = docs[0].apply(lambda x: p.match(x).group())
print(docs)
'''
                               0              name_func              name_lamb
0     William Hartnell (1963-66)       William Hartnell       William Hartnell
1    Patrick Troughton (1966-69)      Patrick Troughton      Patrick Troughton
2          Jon Pertwee (1970 74)            Jon Pertwee            Jon Pertwee
3            Tom Baker (1974-81)              Tom Baker              Tom Baker
4        Peter Davison (1982-84)          Peter Davison          Peter Davison
5          Colin Baker (1984-86)            Colin Baker            Colin Baker
6      Sylvester McCoy (1987-89)        Sylvester McCoy        Sylvester McCoy
7             Paul McGann (1996)            Paul McGann            Paul McGann
8   Christopher Eccleston (2005)  Christopher Eccleston  Christopher Eccleston
9        David Tennant (2005-10)          David Tennant          David Tennant
10          Matt Smith (2010-13)             Matt Smith             Matt Smith
11     Peter Capaldi (2014-2017)          Peter Capaldi          Peter Capaldi
12        Jodie Whittaker (2017)        Jodie Whittaker        Jodie Whittaker
'''
```

> 编写lambda函数要使用lambda关键字。由于apply函数会把整行或整列数据作为第一个参数传递过来，所以lambda只有一个参数x。可以直接编写函数
>
> 单行计算时才用lambda

## 第10章 分组操作：分割-应用-组合

### 10.1 简介

> 借助分割-应用-组合(split-apply-combine)模式，分组操作可以有效地聚合、转换和过滤数据
>
> 分割：基于键，把要处理的数据分割为小片段
>
> 应用：分别处理每个数据片段
>
> 组合：把处理结果组合成新数据集
>
> 该模式的强大之处在于，可以把原始数据分割成独立的片段分别进行处理

### 10.2 聚合

> 聚合是指获取多个值并返回单个值的过程。例如计算算术平均值，其中平均值就是单个值

#### 10.2.1 基本的单变量分组聚合

> 聚合也称汇总(summarization)。这两个术语都指某种形式的数据规约。例如计算汇总统计量（比如平均值时），会取多个值，而后用单个值替换它们。这样总数据量就减少了

```python
import pandas as pd
df = pd.read_csv('gapminder.tsv', sep = '\t')
# 计算每年平均预期寿命
avg_life_exp_by_year = df.groupby('year').lifeExp.mean()
print(avg_life_exp_by_year)
'''
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
'''
avg_life_exp_by_year = df.groupby('year')['lifeExp'].mean() # 方括号取子集
# 获取数据中年份唯一值的列表
years = df.year.unique()
print(years)
# [1952 1957 1962 1967 1972 1977 1982 1987 1992 1997 2002 2007]
# 遍历每一年取子集
# 针对1952年的数据取子集
y1952 = df.loc[df.year == 1952, :]
print(y1952.head())
'''
        country continent  year  lifeExp       pop    gdpPercap
0   Afghanistan      Asia  1952   28.801   8425333   779.445314
12      Albania    Europe  1952   55.230   1282697  1601.056136
24      Algeria    Africa  1952   43.077   9279525  2449.008185
36       Angola    Africa  1952   30.015   4232095  3520.610273
48    Argentina  Americas  1952   62.485  17876956  5911.315053
'''
# 向数据子集应用一个函数，求平均值
y1952_mean = y1952.lifeExp.mean()
print(y1952_mean) # 49.05761971830987
```

#### 10.2.2 Pandas内置的聚合方法

| Pandas方法       | NumPy/SciPy函数       | 说明                                                |
| ---------------- | --------------------- | --------------------------------------------------- |
| count            | np.count_nonzero      | 频率统计（不包含NaN值）                             |
| size             |                       | 频率统计（包含NaN值）                               |
| mean             | np.mean               | 求平均值                                            |
| std              | np.std                | 样本标准差                                          |
| min              | np.min                | 最小值                                              |
| quantile(q=0.25) | np.percentile(q=0.25) | 较小四分位数                                        |
| quantile(q=0.50) | np.percentile(q=0.50) | 中位数                                              |
| quantile(q=0.75) | np.percentile(q=0.75) | 较大四分位数                                        |
| max              | np.max                | 求最大值                                            |
| sum              | np.sum                | 求和                                                |
| var              | np.var                | 求偏方差                                            |
| sem              | scipy.stats.sem       | 平均值的无偏标准差                                  |
| describe         | scipy.stats.describe  | 计数、平均值、标准差、最小值、25%、50%、75%和最大值 |
| first            |                       | 返回第一行                                          |
| last             |                       | 返回最后一行                                        |
| nth              |                       | 返回第n行                                           |

```python
# 可以用describe函数同时计算多个汇总统计量
# 根据所在的洲分组，针对每个组做汇总统计
continent_describe = df.groupby('continent').lifeExp.describe()
print(continent_describe)
'''
           count       mean        std  ...      50%       75%     max
continent                               ...                           
Africa     624.0  48.865330   9.150210  ...  47.7920  54.41150  76.442
Americas   300.0  64.658737   9.345088  ...  67.0480  71.69950  80.653
Asia       396.0  60.064903  11.864532  ...  61.7915  69.50525  82.603
Europe     360.0  71.903686   5.433178  ...  72.2410  75.45050  81.757
Oceania     24.0  74.326208   3.795611  ...  73.6650  77.55250  81.235
'''
```

#### 10.2.3 聚合函数

__1.其他库的函数__

```python
import numpy as np
# 计算各州的平均预期寿命
# 使用np.mean函数
cont_le_agg = df.groupby('continent').lifeExp.agg(np.mean)
print(cont_le_agg)
'''
continent
Africa      48.865330
Americas    64.658737
Asia        60.064903
Europe      71.903686
Oceania     74.326208
Name: lifeExp, dtype: float64
'''
# 使用agg和aggregate实现相同功能
cont_le_agg2 = df.groupby('continent').lifeExp.aggregate(np.mean)
print(cont_le_agg2)
'''
continent
Africa      48.865330
Americas    64.658737
Asia        60.064903
Europe      71.903686
Oceania     74.326208
Name: lifeExp, dtype: float64
'''
```

__2.用户自定义函数__

> 可以把自己定义的函数my_mean直接传入agg方法或者aggregate方法

```python
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
'''
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
'''
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
print(global_mean) # 59.47443936619713
# 带有多个参数的自定义聚合函数
agg_mean_diff = df.groupby('year').lifeExp.\
  agg(my_mean_diff, diff_value = global_mean)
print(agg_mean_diff)
'''
year
1952   -10.416820
1957    -7.967038
1962    -5.865190
1967    -3.796150
1972    -1.827053
1977     0.095718
1982     2.058758
1987     3.738173
1992     4.685899
1997     5.540237
2002     6.220483
2007     7.532983
Name: lifeExp, dtype: float64
'''
```

#### 10.2.4 同时传入多个函数

> 多个聚合函数先把它们全部放在一个列表中，再将整个链表传入

```python
gdf = df.groupby('year').lifeExp.\
  agg([np.count_nonzero, np.mean, np.std])
print(gdf)
'''
      count_nonzero       mean        std
year                                     
1952          142.0  49.057620  12.225956
1957          142.0  51.507401  12.231286
1962          142.0  53.609249  12.097245
1967          142.0  55.678290  11.718858
1972          142.0  57.647386  11.381953
1977          142.0  59.570157  11.227229
1982          142.0  61.533197  10.770618
1987          142.0  63.212613  10.556285
1992          142.0  64.160338  11.227380
1997          142.0  65.014676  11.559439
2002          142.0  65.694923  12.279823
2007          142.0  67.007423  12.073021
'''
```

#### 10.2.5 在agg/aggregate中使用字典

> 也可以向agg方法中传入Python字典

__1.针对DataFrame__

> 对分组的DataFrame指定dict时，键是DataFrame的列，值是聚合计算使用的函数。这种方法允许对一个或多个变量进行分组，对不同列同时使用不同的聚合函数

```python
# 对DataFrame使用字典聚合不同列
# 对于每一年，计算平均值lifeExp、中位数pop和中位数gdpPercap
gdf_dict = df.groupby('year').agg({
  'lifeExp': 'mean',
  'pop': 'median',
  'gdpPercap': 'median'
})
'''
        lifeExp         pop    gdpPercap
year                                    
1952  49.057620   3943953.0  1968.528344
1957  51.507401   4282942.0  2173.220291
1962  53.609249   4686039.5  2335.439533
1967  55.678290   5170175.5  2678.334741
1972  57.647386   5877996.5  3339.129407
1977  59.570157   6404036.5  3798.609244
1982  61.533197   7007320.0  4216.228428
1987  63.212613   7774861.5  4280.300366
1992  64.160338   8688686.5  4386.085502
1997  65.014676   9735063.5  4781.825478
2002  65.694923  10372918.5  5319.804524
2007  67.007423  10517531.0  6124.371109
'''
```

__2.针对Series__

> 可以在groupby之后把一个dict传入Series中，直接做汇总统计并返回。dict的键是新的列名。这与把dict传入分组的DataFrame时的行为不同。

```python
gdf = df.groupby('year')['lifeExp'].\
  agg([np.count_nonzero,
       np.mean,
       np.std]).\
  rename(columns = {'count_nonzero': 'count',
                    'mean': 'avg',
                    'std': 'std_dev'}).\
  reset_index()
print(gdf)
'''
    year  count        avg    std_dev
0   1952  142.0  49.057620  12.225956
1   1957  142.0  51.507401  12.231286
2   1962  142.0  53.609249  12.097245
3   1967  142.0  55.678290  11.718858
4   1972  142.0  57.647386  11.381953
5   1977  142.0  59.570157  11.227229
6   1982  142.0  61.533197  10.770618
7   1987  142.0  63.212613  10.556285
8   1992  142.0  64.160338  11.227380
9   1997  142.0  65.014676  11.559439
10  2002  142.0  65.694923  12.279823
11  2007  142.0  67.007423  12.073021
'''
```

### 10.3 转换

> 转换数据时，需要把DataFrame中的值传递给一个函数，而后由该函数“转换”数据。前面讲过aggregate接收多个值并返回单个聚合值。与aggregate不同，transform接收多个值，但返回的是与这些值一一对应的转换值，即transform方法不会减少数据量

```python
# 计算z函数
def my_zscore(x):
  """计算给定数据的z分数，是一个向量或序列值
  """
  return ((x - x.mean()) / x.std())
# 然后使用该函数按组转换数据
transform_z = df.groupby('year').lifeExp.transform(my_zscore)
# 输出数据的行数
print(df.shape) # (1704, 6)
# 转换之后的值的个数
print(transform_z.shape) # (1704,)

# 从scipy.stats导入zscore函数
from scipy.stats import zscore
# 计算分组的zscore
sp_z_grouped = df.groupby('year').lifeExp.transform(zscore)
# 计算非分组的zscore
sp_z_nogroup = zscore(df.lifeExp)
# 分组的z分数
print(transform_z.head())
'''
0   -1.656854
1   -1.731249
2   -1.786543
3   -1.848157
4   -1.894173
Name: lifeExp, dtype: float64
'''
# 使用SciPy计算得到的分组z分数
print(sp_z_grouped.head())
'''
0   -1.662719
1   -1.737377
2   -1.792867
3   -1.854699
4   -1.900878
Name: lifeExp, dtype: float64
'''
# 计算非分组的z分数
print(sp_z_nogroup[:5])
'''
[-2.37533395 -2.25677417 -2.1278375  -1.97117751 -1.81103275]
'''
```

__缺失值示例__

```python
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
'''
     total_bill   tip     sex smoker   day    time  size
24        19.82  3.18    Male     No   Sat  Dinner     2
6          8.77  2.00    Male     No   Sun  Dinner     2
153         NaN  2.00    Male     No   Sun  Dinner     4
211         NaN  5.16    Male    Yes   Sat  Dinner     4
198         NaN  2.00  Female    Yes  Thur   Lunch     2
176         NaN  2.00    Male    Yes   Sun  Dinner     2
192       28.44  2.56    Male    Yes  Thur   Lunch     2
124       12.48  2.52  Female     No  Thur   Lunch     2
9         14.78  3.23    Male     No   Sun  Dinner     2
101       15.38  3.00  Female    Yes   Fri  Dinner     2
'''
# 可以使用groupby语句来计算统计值以填充缺失值
# 首先按sex统计非缺失值的数量
count_sex = tips_10.groupby('sex').count()
print(count_sex)
'''
        total_bill  tip  smoker  day  time  size
sex                                             
Male             4    7       7    7     7     7
Female           2    3       3    3     3     3
'''
# 计算分组平均值，用来填充缺失值
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
'''
     total_bill   tip     sex smoker   day    time  size  fill_total_bill
24        19.82  3.18    Male     No   Sat  Dinner     2          19.8200
6          8.77  2.00    Male     No   Sun  Dinner     2           8.7700
153         NaN  2.00    Male     No   Sun  Dinner     4          17.9525
211         NaN  5.16    Male    Yes   Sat  Dinner     4          17.9525
198         NaN  2.00  Female    Yes  Thur   Lunch     2          13.9300
176         NaN  2.00    Male    Yes   Sun  Dinner     2          17.9525
192       28.44  2.56    Male    Yes  Thur   Lunch     2          28.4400
124       12.48  2.52  Female     No  Thur   Lunch     2          12.4800
9         14.78  3.23    Male     No   Sun  Dinner     2          14.7800
101       15.38  3.00  Female    Yes   Fri  Dinner     2          15.3800
'''
# 只查看两列,发现sex不同值不同
print(tips_10[['sex', 'total_bill', 'fill_total_bill']])
'''
        sex  total_bill  fill_total_bill
24     Male       19.82          19.8200
6      Male        8.77           8.7700
153    Male         NaN          17.9525
211    Male         NaN          17.9525
198  Female         NaN          13.9300
176    Male         NaN          17.9525
192    Male       28.44          28.4400
124  Female       12.48          12.4800
9      Male       14.78          14.7800
101  Female       15.38          15.3800
'''
```

### 10.4 过滤器

```python
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
# 输出原始的行数
print(tips.shape) # (244, 7)
# 查看不同规模聚餐的行数
print(tips['size'].value_counts()) 
'''
2    156
3     38
4     37
5      5
6      4
1      4
Name: size, dtype: int64
'''
# 输出结果显示，人数1、5和6的情况并不常见。在本例中，需要过滤掉这些数据点，使每组包含30个或更多观测值
# 可以在分组基础上使用filter方法来实现
# 过滤数据，使每组包含30个或更多观测值
tips_filtered = tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
# 数据过滤结果
print(tips_filtered.shape) # (231, 7)
print(tips_filtered['size'].value_counts())
'''
2    156
3     38
4     37
Name: size, dtype: int64
'''
```

### 10.5 pandas.core.grupby.DataFrameGroupBy对象

#### 10.5.1 分组

> 本章会在groupby之后直接链接调用aggregate、transform或filter方法。但其实可以在执行这些方法之前先保存groupby的结果。首先取tips数据集的子集

```python
tips_10 = sns.load_dataset('tips').sample(10, random_state = 42)
print(tips_10)
'''
     total_bill   tip     sex smoker   day    time  size
24        19.82  3.18    Male     No   Sat  Dinner     2
6          8.77  2.00    Male     No   Sun  Dinner     2
153       24.55  2.00    Male     No   Sun  Dinner     4
211       25.89  5.16    Male    Yes   Sat  Dinner     4
198       13.00  2.00  Female    Yes  Thur   Lunch     2
176       17.89  2.00    Male    Yes   Sun  Dinner     2
192       28.44  2.56    Male    Yes  Thur   Lunch     2
124       12.48  2.52  Female     No  Thur   Lunch     2
9         14.78  3.23    Male     No   Sun  Dinner     2
101       15.38  3.00  Female    Yes   Fri  Dinner     2
'''
# 只保存分组对象
grouped = tips_10.groupby('sex')
# 请注意，只获得了一个DataFrameGroupBy对象及其内存位置
grouped = tips_10.groupby('sex')
print(grouped) # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001BCFA981A58>
# 查看groupby的实际分组
# 只返回索引
print(grouped.groups) # {'Male': [24, 6, 153, 211, 176, 192, 9], 'Female': [198, 124, 101]}
```

#### 10.5.2 涉及多个变量的分组计算

```python
# 计算各列的平均值
avgs = grouped.mean()
print(avgs)
'''
        total_bill       tip      size
sex                                   
Male         20.02  2.875714  2.571429
Female       13.62  2.506667  2.000000
'''
# 并非所有列都能计算平均值
```

#### 10.5.3 选择分组

> 如果想提取特定的列，可以使用get_group方法，并传入想要的组

```python
# 获取Female分组
female = grouped.get_group('Female')
print(female)
'''
     total_bill   tip     sex smoker   day    time  size
198       13.00  2.00  Female    Yes  Thur   Lunch     2
124       12.48  2.52  Female     No  Thur   Lunch     2
101       15.38  3.00  Female    Yes   Fri  Dinner     2
'''
```

#### 10.5.4 遍历分组

> 保存groupby对象便于逐个遍历分组。相比于aggregate、transform和filter，有时使用for循环解决问题更简单

```python
for sex_group in grouped:
  print(sex_group)
'''
('Male',      total_bill   tip   sex smoker   day    time  size
24        19.82  3.18  Male     No   Sat  Dinner     2
6          8.77  2.00  Male     No   Sun  Dinner     2
153       24.55  2.00  Male     No   Sun  Dinner     4
211       25.89  5.16  Male    Yes   Sat  Dinner     4
176       17.89  2.00  Male    Yes   Sun  Dinner     2
192       28.44  2.56  Male    Yes  Thur   Lunch     2
9         14.78  3.23  Male     No   Sun  Dinner     2)
('Female',      total_bill   tip     sex smoker   day    time  size
198       13.00  2.00  Female    Yes  Thur   Lunch     2
124       12.48  2.52  Female     No  Thur   Lunch     2
101       15.38  3.00  Female    Yes   Fri  Dinner     2)
'''
```

> 如果尝试从grouped对象获取第一个元素，会得到一条错误信息，因为该对象仍然是pandas.core.grouped.DataFrameGroupBy对象，而不是真正的Pandas容器
>
> 可以使用for循环

```python
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
'''
the type is: <class 'tuple'>

the length is: 2

the first element is: Male

it has a type of: <class 'str'>

the second element is: 
     total_bill   tip   sex smoker   day    time  size
24        19.82  3.18  Male     No   Sat  Dinner     2
6          8.77  2.00  Male     No   Sun  Dinner     2
153       24.55  2.00  Male     No   Sun  Dinner     4
211       25.89  5.16  Male    Yes   Sat  Dinner     4
176       17.89  2.00  Male    Yes   Sun  Dinner     2
192       28.44  2.56  Male    Yes  Thur   Lunch     2
9         14.78  3.23  Male     No   Sun  Dinner     2

it has a type of: <class 'pandas.core.frame.DataFrame'>

what we have:
('Male',      total_bill   tip   sex smoker   day    time  size
24        19.82  3.18  Male     No   Sat  Dinner     2
6          8.77  2.00  Male     No   Sun  Dinner     2
153       24.55  2.00  Male     No   Sun  Dinner     4
211       25.89  5.16  Male    Yes   Sat  Dinner     4
176       17.89  2.00  Male    Yes   Sun  Dinner     2
192       28.44  2.56  Male    Yes  Thur   Lunch     2
9         14.78  3.23  Male     No   Sun  Dinner     2)
'''
```

#### 10.5.5 多个分组

```python
# 按照sex和time计算平均值
bill_sex_time = tips_10.groupby(['sex', 'time'])
group_avg = bill_sex_time.mean()
print(group_avg)
'''
               total_bill       tip      size
sex    time                                  
Male   Lunch    28.440000  2.560000  2.000000
       Dinner   18.616667  2.928333  2.666667
Female Lunch    12.740000  2.260000  2.000000
       Dinner   15.380000  3.000000  2.000000
'''
```

#### 10.5.6 平铺结果

```python
# group_avg的类型
print(type(group_avg)) # <class 'pandas.core.frame.DataFrame'>
print(group_avg.columns) # Index(['total_bill', 'tip', 'size'], dtype='object')
print(group_avg.index)
'''
MultiIndex([(  'Male',  'Lunch'),
            (  'Male', 'Dinner'),
            ('Female',  'Lunch'),
            ('Female', 'Dinner')],
           names=['sex', 'time'])
'''
# 如果想得到一个普通的DataFrame，使用reset_index方法
group_method = tips_10.groupby(['sex', 'time']).mean().reset_index()
print(group_method)
'''
      sex    time  total_bill       tip      size
0    Male   Lunch   28.440000  2.560000  2.000000
1    Male  Dinner   18.616667  2.928333  2.666667
2  Female   Lunch   12.740000  2.260000  2.000000
3  Female  Dinner   15.380000  3.000000  2.000000
'''
# 或者在groupby方法中使用as_index = false参数
group_param = tips_10.groupby(['sex', 'time'], as_index = False).mean()
print(group_param)
'''
      sex    time  total_bill       tip      size
0    Male   Lunch   28.440000  2.560000  2.000000
1    Male  Dinner   18.616667  2.928333  2.666667
2  Female   Lunch   12.740000  2.260000  2.000000
3  Female  Dinner   15.380000  3.000000  2.000000
'''
```

### 10.6 使用多级索引

> 有时需要在groupby语句之后调用计算相关的函数。无论何时，总是可以平铺结果，然后执行另一条groupby语句，但这可能不是执行计算的最高效方式

```python
intv_df = pd.read_csv('epi_sim.txt')
# 总行数超过900万
print(intv_df.shape) # (9434653, 6)
```

> 该数据集包含6列
>
> ig_type：边类型（网络中两节点间的关系类型，比如“school”和“work”）
>
> intervened：模拟中对特定的人进行干预的时间
>
> pid：模拟人的ID编号
>
> rep：重复运行（每套模拟参数运行多次）
>
> sid：模拟ID
>
> tr：流感病毒的传播值

```python
print(intv_df.head())
'''
   ig_type  intervened        pid  rep  sid        tr
0        3          40  294524448    1  201  0.000135
1        3          40  294571037    1  201  0.000135
2        3          40  290699504    1  201  0.000135
3        3          40  288354895    1  201  0.000135
4        3          40  292271290    1  201  0.000135
'''
```

> 下面统计每次重复的干预次数、干预时间和治疗效果。这里随意计算ig_type，因为只需要一个值来得到分组的观测数

```python
count_only = intv_df.\
  groupby(['rep', 'intervened', 'tr'])['ig_type'].\
  count()
print(count_only.head(n = 10))
'''
rep  intervened  tr      
0    8           0.000166    1
     9           0.000152    3
                 0.000166    1
     10          0.000152    1
                 0.000166    1
     12          0.000152    3
                 0.000166    5
     13          0.000152    1
                 0.000166    3
     14          0.000152    3
Name: ig_type, dtype: int64
'''
print(type(count_only)) # <class 'pandas.core.series.Series'>
# 如果执行另一个groupby操作，必须传入levels参数
# 传入[0,1,2]代表分别指定第1级、第2级和第3级索引操作
count_mean = count_only.\
  groupby(level = [0, 1, 2]).\
  mean()
print(count_mean.head())
'''
rep  intervened  tr      
0    8           0.000166    1
     9           0.000152    3
                 0.000166    1
     10          0.000152    1
                 0.000166    1
Name: ig_type, dtype: int64
'''
import matplotlib.pyplot as plt
fig = sns.lmplot(x = 'intervened', y = 'ig_type', hue = 'rep', col = 'tr',
                 fit_reg = False, data = count_mean.reset_index())
plt.show()
# 接下来调用cumsum计算累计和
cumulative_count = intv_df.\
  groupby(['rep', 'intervened', 'tr'])['ig_type'].\
  count().\
  groupby(level = ['rep']).\
  cumsum().\
  reset_index()
fig = sns.lmplot(x = 'intervened', y = 'ig_type', hue = 'rep', col = 'tr',
                 fit_reg = False, data = cumulative_count)
plt.show()
```

## 第11章 datetime数据类型

### 11.2 Python的datetime对象

```python
from datetime import datetime
now = datetime.now() # 获取当前日期和时间
print(now) # 2021-03-08 22:12:45.414862
# 手动创建datetime
t1 = datetime.now()
t2 = datetime(1970, 1, 1)
# 做数学运算
diff = t1 - t2
print(diff) # 18694 days, 22:14:44.824146
# 运算结果为timedelta类型
print(type(diff)) # <class 'datetime.timedelta'>
```

### 11.3 转换为datetime

> 可以使用to_datetime函数把一个对象转换成datetime类型

```python
import pandas as pd
ebola = pd.read_csv('country_timeseries.csv')
# 获取左上角数据
print(ebola.iloc[:5, :5])
'''
         Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
0    1/5/2015  289        2776.0            NaN            10030.0
1    1/4/2015  288        2775.0            NaN             9780.0
2    1/3/2015  287        2769.0         8166.0             9722.0
3    1/2/2015  286           NaN         8157.0                NaN
4  12/31/2014  284        2730.0         8115.0             9633.0
'''
print(ebola.info())
# date列只是普通的字符串对象
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 18 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   Date                 122 non-null    object 
 1   Day                  122 non-null    int64  
 2   Cases_Guinea         93 non-null     float64
 3   Cases_Liberia        83 non-null     float64
 4   Cases_SierraLeone    87 non-null     float64
 5   Cases_Nigeria        38 non-null     float64
 6   Cases_Senegal        25 non-null     float64
 7   Cases_UnitedStates   18 non-null     float64
 8   Cases_Spain          16 non-null     float64
 9   Cases_Mali           12 non-null     float64
 10  Deaths_Guinea        92 non-null     float64
 11  Deaths_Liberia       81 non-null     float64
 12  Deaths_SierraLeone   87 non-null     float64
 13  Deaths_Nigeria       38 non-null     float64
 14  Deaths_Senegal       22 non-null     float64
 15  Deaths_UnitedStates  18 non-null     float64
 16  Deaths_Spain         16 non-null     float64
 17  Deaths_Mali          12 non-null     float64
dtypes: float64(16), int64(1), object(1)
memory usage: 17.3+ KB
None
'''
# Date列只是普通的字符串类型
# 可以创建新列--date_dt，调用to_datetime方法把Date列转换为datetime后赋给date_dt
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
# 还可以显示指定如何把数据转换为datetime对象。to_datetime函数有一个参数format，允许手动指定日期格式
ebola['date_dt'] = pd.to_datetime(ebola['Date'], format = '%m/%d/%Y')
print(ebola.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 19 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   Date                 122 non-null    object        
 1   Day                  122 non-null    int64         
 2   Cases_Guinea         93 non-null     float64       
 3   Cases_Liberia        83 non-null     float64       
 4   Cases_SierraLeone    87 non-null     float64       
 5   Cases_Nigeria        38 non-null     float64       
 6   Cases_Senegal        25 non-null     float64       
 7   Cases_UnitedStates   18 non-null     float64       
 8   Cases_Spain          16 non-null     float64       
 9   Cases_Mali           12 non-null     float64       
 10  Deaths_Guinea        92 non-null     float64       
 11  Deaths_Liberia       81 non-null     float64       
 12  Deaths_SierraLeone   87 non-null     float64       
 13  Deaths_Nigeria       38 non-null     float64       
 14  Deaths_Senegal       22 non-null     float64       
 15  Deaths_UnitedStates  18 non-null     float64       
 16  Deaths_Spain         16 non-null     float64       
 17  Deaths_Mali          12 non-null     float64       
 18  date_dt              122 non-null    datetime64[ns]
dtypes: datetime64[ns](1), float64(16), int64(1), object(1)
memory usage: 18.2+ KB
None
'''
# date_dt为datetime64[ns]类型
# to_datetime函数有许多参数。如果日期格式以“日”开始，或者以“年”开始，可以把dayfirst和yearfirst两个参数分别设置为True
```

| 符号 | 含义                         | 示例                          |
| ---- | ---------------------------- | ----------------------------- |
| %a   | 星期的缩略名                 | Sun,Mon,...Sat                |
| %A   | 星期的完整名字               | Sunday,Monday,...Saturday     |
| %w   | 以数字表示日期，0为周日      | 0,1,2,3,4,5,6                 |
| %d   | 一个月中的每一天（两个数字） | 01,02,...,31                  |
| %b   | 月份名的缩写形式             | Jan,Feb,...,Dec               |
| %B   | 月份名的完整形式             | January,February,...,December |
| %m   | 月份（两位数字）             | 01,02,...12                   |
| %y   | 年份（两位数字）             | 00,01,02...99                 |
| %Y   | 年份（四位数字）             | 0001,0002,...9999             |
| %H   | 小时（两位数，24小时制）     | 00,01,02,...23                |
| %I   | 小时（两位数，12小时制）     | 01,02,...12                   |
| %p   | AM或PM                       | AM,PM                         |
| %M   | 分钟（两位数）               | 00,01,...,59                  |
| %S   | 秒（两位数）                 | 00,01,...,59                  |
| %f   | 微秒                         | 000000,000001,...999999       |
| %z   | UTC偏移（+HHMM或-HHMM）      | （空）,+0000,-0400,...,+1030  |
| %Z   | 时区名                       | （空）,UTC,EST,CST            |
| %j   | 一年的每一天（三位数字）     | 001,002,...366                |
| %U   | 一年的周数（周日为第一天）   | 00,01,...,53                  |
| %W   | 一年的周数（周一为第一天）   | 00,01,...,53                  |
| %c   | 日期和时间表示               | Tue Aug 16 21:30:00 1988      |
| %x   | 日期表示                     | 08/16/88(None);08/16/1988     |
| %X   | 时间表示                     | 21:30:00                      |
| %%   | %字符                        | %                             |
| %G   | ISO 8601年                   | 0001,0002,...,2013,...,9999   |
| %u   | ISO 8601星期                 | 1,2,...,7                     |
| %V   | ISO 8601星期                 | 01,02,...,53                  |

### 11.4 加载包含日期的数据

> 本书使用的许多数据集都是csv格式的，或者来自seaborn库。Gapminder数据集例外，它是一个以制表符分隔的文件(TSV)。read_csv函数有很多参数，例如parse_dates、inher_datetime_format、keep_date_col、date_parser和dayfirst。在使用read_csv加载数据集时，可以直接在parse_dates参数中指定想要解析的列

```python
ebola = pd.read_csv('country_timeseries.csv', parse_dates = [0])
print(ebola.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 18 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   Date                 122 non-null    datetime64[ns]
 1   Day                  122 non-null    int64         
 2   Cases_Guinea         93 non-null     float64       
 3   Cases_Liberia        83 non-null     float64       
 4   Cases_SierraLeone    87 non-null     float64       
 5   Cases_Nigeria        38 non-null     float64       
 6   Cases_Senegal        25 non-null     float64       
 7   Cases_UnitedStates   18 non-null     float64       
 8   Cases_Spain          16 non-null     float64       
 9   Cases_Mali           12 non-null     float64       
 10  Deaths_Guinea        92 non-null     float64       
 11  Deaths_Liberia       81 non-null     float64       
 12  Deaths_SierraLeone   87 non-null     float64       
 13  Deaths_Nigeria       38 non-null     float64       
 14  Deaths_Senegal       22 non-null     float64       
 15  Deaths_UnitedStates  18 non-null     float64       
 16  Deaths_Spain         16 non-null     float64       
 17  Deaths_Mali          12 non-null     float64       
dtypes: datetime64[ns](1), float64(16), int64(1)
memory usage: 17.3 KB
None
'''
```

### 11.5 提取日期的各个部分

```python
d = pd.to_datetime('2016-02-29')
print(d) # 2016-02-29 00:00:00
print(type(d)) # <class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(d.year) # 2016
print(d.month) # 2
print(d.day) # 29
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola[['Date', 'date_dt']].head())
'''
        Date    date_dt
0 2015-01-05 2015-01-05
1 2015-01-04 2015-01-04
2 2015-01-03 2015-01-03
3 2015-01-02 2015-01-02
4 2014-12-31 2014-12-31
'''
ebola['year'] = ebola['date_dt'].dt.year # 提取year
print(ebola[['Date', 'date_dt', 'year']].head())
'''
        Date    date_dt  year
0 2015-01-05 2015-01-05  2015
1 2015-01-04 2015-01-04  2015
2 2015-01-03 2015-01-03  2015
3 2015-01-02 2015-01-02  2015
4 2014-12-31 2014-12-31  2014
'''
ebola['month'], ebola['day'] = (ebola['date_dt'].dt.month,
                                ebola['date_dt'].dt.day)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']].head())
'''
        Date    date_dt  year  month  day
0 2015-01-05 2015-01-05  2015      1    5
1 2015-01-04 2015-01-04  2015      1    4
2 2015-01-03 2015-01-03  2015      1    3
3 2015-01-02 2015-01-02  2015      1    2
4 2014-12-31 2014-12-31  2014     12   31
'''
# 重新解析数据
print(ebola.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 22 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   Date                 122 non-null    datetime64[ns]
 1   Day                  122 non-null    int64         
 2   Cases_Guinea         93 non-null     float64       
 3   Cases_Liberia        83 non-null     float64       
 4   Cases_SierraLeone    87 non-null     float64       
 5   Cases_Nigeria        38 non-null     float64       
 6   Cases_Senegal        25 non-null     float64       
 7   Cases_UnitedStates   18 non-null     float64       
 8   Cases_Spain          16 non-null     float64       
 9   Cases_Mali           12 non-null     float64       
 10  Deaths_Guinea        92 non-null     float64       
 11  Deaths_Liberia       81 non-null     float64       
 12  Deaths_SierraLeone   87 non-null     float64       
 13  Deaths_Nigeria       38 non-null     float64       
 14  Deaths_Senegal       22 non-null     float64       
 15  Deaths_UnitedStates  18 non-null     float64       
 16  Deaths_Spain         16 non-null     float64       
 17  Deaths_Mali          12 non-null     float64       
 18  date_dt              122 non-null    datetime64[ns]
 19  year                 122 non-null    int64         
 20  month                122 non-null    int64         
 21  day                  122 non-null    int64         
dtypes: datetime64[ns](2), float64(16), int64(4)
memory usage: 21.1 KB
None
'''
```

### 11.6 日期运算和Timedelta

> 获取date对象有助于进行日期计算。Ebola数据集中的Day列表示一个国家爆发埃博拉疫情的天数。可以通过日期运算重建该列。下面输出的是左下角的数据

```python
print(ebola.iloc[-5:, :5])
'''
          Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
117 2014-03-27    5         103.0            8.0                6.0
118 2014-03-26    4          86.0            NaN                NaN
119 2014-03-25    3          86.0            NaN                NaN
120 2014-03-24    2          86.0            NaN                NaN
121 2014-03-22    0          49.0            NaN                NaN
'''
# 可见，疫情爆发的第一天是2014-03-22。计算疫情爆发的天数时，只需用每个日期减去该日期即可
# 为了获取疫情爆发最早的日期，可以调用列中的min方法
print(ebola['date_dt'].min()) # 2014-03-22 00:00:00
ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'Day', 'outbreak_d']].head())
'''
        Date  Day outbreak_d
0 2015-01-05  289   289 days
1 2015-01-04  288   288 days
2 2015-01-03  287   287 days
3 2015-01-02  286   286 days
4 2014-12-31  284   284 days
'''
print(ebola[['Date', 'Day', 'outbreak_d']].tail())
'''
          Date  Day outbreak_d
117 2014-03-27    5     5 days
118 2014-03-26    4     4 days
119 2014-03-25    3     3 days
120 2014-03-24    2     2 days
121 2014-03-22    0     0 days
'''
# 执行这种运算，最终会得到一个timedelta对象
print(ebola.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 23 columns):
 #   Column               Non-Null Count  Dtype          
---  ------               --------------  -----          
 0   Date                 122 non-null    datetime64[ns] 
 1   Day                  122 non-null    int64          
 2   Cases_Guinea         93 non-null     float64        
 3   Cases_Liberia        83 non-null     float64        
 4   Cases_SierraLeone    87 non-null     float64        
 5   Cases_Nigeria        38 non-null     float64        
 6   Cases_Senegal        25 non-null     float64        
 7   Cases_UnitedStates   18 non-null     float64        
 8   Cases_Spain          16 non-null     float64        
 9   Cases_Mali           12 non-null     float64        
 10  Deaths_Guinea        92 non-null     float64        
 11  Deaths_Liberia       81 non-null     float64        
 12  Deaths_SierraLeone   87 non-null     float64        
 13  Deaths_Nigeria       38 non-null     float64        
 14  Deaths_Senegal       22 non-null     float64        
 15  Deaths_UnitedStates  18 non-null     float64        
 16  Deaths_Spain         16 non-null     float64        
 17  Deaths_Mali          12 non-null     float64        
 18  date_dt              122 non-null    datetime64[ns] 
 19  year                 122 non-null    int64          
 20  month                122 non-null    int64          
 21  day                  122 non-null    int64          
 22  outbreak_d           122 non-null    timedelta64[ns]
dtypes: datetime64[ns](2), float64(16), int64(4), timedelta64[ns](1)
memory usage: 22.0 KB
None
'''
```

### 11.7 datetime方法

> 以另一个数据集为例，里面包含了银行倒闭的数据

```python
banks = pd.read_csv('banklist.csv')
print(banks.head())
'''
                                           Bank Name  ... Updated Date
0                                Fayette County Bank  ...    26-Jul-17
1  Guaranty Bank, (d/b/a BestBank in Georgia & Mi...  ...    26-Jul-17
2                                     First NBC Bank  ...    26-Jul-17
3                                      Proficio Bank  ...    18-May-17
4                      Seaway Bank and Trust Company  ...    18-May-17
'''
# 也可在导入数据时直接解析日期
banks = pd.read_csv('banklist.csv', parse_dates = [5, 6])
print(banks.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 553 entries, 0 to 552
Data columns (total 7 columns):
 #   Column                 Non-Null Count  Dtype         
---  ------                 --------------  -----         
 0   Bank Name              553 non-null    object        
 1   City                   553 non-null    object        
 2   ST                     553 non-null    object        
 3   CERT                   553 non-null    int64         
 4   Acquiring Institution  553 non-null    object        
 5   Closing Date           553 non-null    datetime64[ns]
 6   Updated Date           553 non-null    datetime64[ns]
dtypes: datetime64[ns](2), int64(1), object(4)
memory usage: 30.4+ KB
None
'''
# 添加两列，分别代表银行破产的季度和年份
banks['closing_quarter'], banks['closing_year'] = \
  (banks['Closing Date'].dt.quarter,
   banks['Closing Date'].dt.year)
print(banks.head())
'''
                                           Bank Name  ... closing_year
0                                Fayette County Bank  ...         2017
1  Guaranty Bank, (d/b/a BestBank in Georgia & Mi...  ...         2017
2                                     First NBC Bank  ...         2017
3                                      Proficio Bank  ...         2017
4                      Seaway Bank and Trust Company  ...         2017
'''
# 可以计算每年破产的银行数量
closing_year = banks.groupby(['closing_year']).size()
print(closing_year)
'''
closing_year
2000      2
2001      4
2002     11
2003      3
2004      4
2007      3
2008     25
2009    140
2010    157
2011     92
2012     51
2013     24
2014     18
2015      8
2016      5
2017      6
dtype: int64
'''
# 计算每个季度的银行倒闭数量
closing_year_q = banks.groupby(['closing_year', 'closing_quarter']).size()
print(closing_year_q)
'''
2000          4                   2
2001          1                   1
              2                   1
              3                   2
2002          1                   6
              2                   2
              3                   1
              4                   2
2003          1                   1
              2                   1
              4                   1
2004          1                   3
              2                   1
2007          1                   1
              3                   1
              4                   1
2008          1                   2
              2                   2
              3                   9
              4                  12
2009          1                  21
              2                  24
              3                  50
              4                  45
2010          1                  41
              2                  45
              3                  41
              4                  30
2011          1                  26
              2                  22
              3                  26
              4                  18
2012          1                  16
              2                  15
              3                  12
              4                   8
2013          1                   4
              2                  12
              3                   6
              4                   2
2014          1                   5
              2                   7
              3                   2
              4                   4
2015          1                   4
              2                   1
              3                   1
              4                   2
2016          1                   1
              2                   2
              3                   2
2017          1                   3
              2                   3
dtype: int64
'''
# 画图展示
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()

fig, ax = plt.subplots()
ax = closing_year_q.plot()
plt.show()
```

### 11.8 获取股票数据

> 股票价格是包含数据日期的常见数据类型

```python
# 导入并使用pandas_datareader从网络中获取数据
import pandas as pd
import pandas_datareader as pdr

# 获取Tesla的股票信息
tesla = pdr.get_data_yahoo('TSLA')

# 保存获取的股票信息
# 无须再依赖网络
# 加载保留的股票信息文件
tesla = pd.read_csv('tesla_stock_yahoo.csv', parse_dates = [0])

print(tesla.head())
'''
        Date       Open   High        Low      Close  Adj Close    Volume
0 2010-06-29  19.000000  25.00  17.540001  23.889999  23.889999  18766300
1 2010-06-30  25.790001  30.42  23.299999  23.830000  23.830000  17187100
2 2010-07-01  25.000000  25.92  20.270000  21.959999  21.959999   8218800
3 2010-07-02  23.000000  23.10  18.709999  19.200001  19.200001   5139800
4 2010-07-06  20.000000  20.00  15.830000  16.110001  16.110001   6866900
'''
print(tesla.tail())
'''
           Date        Open        High  ...       Close   Adj Close    Volume
1786 2017-08-02  318.940002  327.119995  ...  325.890015  325.890015  13091500
1787 2017-08-03  345.329987  350.000000  ...  347.089996  347.089996  13535000
1788 2017-08-04  347.000000  357.269989  ...  356.910004  356.910004   9198400
1789 2017-08-07  357.350006  359.480011  ...  355.170013  355.170013   6276900
1790 2017-08-08  357.529999  368.579987  ...  365.220001  365.220001   7449837
'''
```

### 11.9 基于日期去数据子集

> 前面介绍了从列中提取日期各部分的方法。可以综合运用这些方法来获取数据子集，而不必手动解析各部分

```python
# 获取2010年6月的数据
print(tesla.loc[(tesla.Date.dt.year == 2010)&\
                (tesla.Date.dt.month == 6)])
'''
        Date       Open   High        Low      Close  Adj Close    Volume
0 2010-06-29  19.000000  25.00  17.540001  23.889999  23.889999  18766300
1 2010-06-30  25.790001  30.42  23.299999  23.830000  23.830000  17187100
'''
```

#### 11.9.1 DatetimeIndex对象

> 在处理包含datetime的数据时，经常需要把datetime对象设置成DataFrame的索引。前面多把DataFrame的行索引作为行号使用，但行索引有时不能作为行号使用。

```python
# 把Date列作为索引
tesla.index = tesla['Date']
print(tesla.index)
'''
DatetimeIndex(['2010-06-29', '2010-06-30', '2010-07-01', '2010-07-02',
               '2010-07-06', '2010-07-07', '2010-07-08', '2010-07-09',
               '2010-07-12', '2010-07-13',
               ...
               '2017-07-26', '2017-07-27', '2017-07-28', '2017-07-31',
               '2017-08-01', '2017-08-02', '2017-08-03', '2017-08-04',
               '2017-08-07', '2017-08-08'],
              dtype='datetime64[ns]', name='Date', length=1791, freq=None)
'''
# 把索引设置为日期对象后，就可以直接使用日期来获取某些数据行了
# 例如根据年份获取数据
print(tesla['2015'].iloc[:5, :5])
'''
                 Date        Open        High         Low       Close
Date                                                                 
2015-01-02 2015-01-02  222.869995  223.250000  213.259995  219.309998
2015-01-05 2015-01-05  214.550003  216.500000  207.160004  210.089996
2015-01-06 2015-01-06  210.059998  214.199997  204.210007  211.279999
2015-01-07 2015-01-07  213.350006  214.779999  209.779999  210.949997
2015-01-08 2015-01-08  212.809998  213.800003  210.009995  210.619995
'''
# 根据年份和月份获取数据
print(tesla['2010-06'].iloc[:, :5])
'''
                 Date       Open   High        Low      Close
Date                                                         
2010-06-29 2010-06-29  19.000000  25.00  17.540001  23.889999
2010-06-30 2010-06-30  25.790001  30.42  23.299999  23.830000
'''
```

#### 11.9.2 TimedeltaIndex对象

> 前面把一个DataFrame索引设置为了datetime，创建出了DatetimeIndex对象。同样，可以使用timedelta来创建timedeltaIndex

```python
# 首先创建一个timedelta
tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()
# 然后把timedelta指派给index
tesla.index = tesla['ref_date']
print(tesla.iloc[:5, :5])
'''
               Date       Open   High        Low      Close
ref_date                                                   
0 days   2010-06-29  19.000000  25.00  17.540001  23.889999
1 days   2010-06-30  25.790001  30.42  23.299999  23.830000
2 days   2010-07-01  25.000000  25.92  20.270000  21.959999
3 days   2010-07-02  23.000000  23.10  18.709999  19.200001
7 days   2010-07-06  20.000000  20.00  15.830000  16.110001
'''
# 基于ref_date来选择数据
print(tesla['0 day': '5 day'].iloc[:5, :5])
'''
               Date       Open   High        Low      Close
ref_date                                                   
0 days   2010-06-29  19.000000  25.00  17.540001  23.889999
1 days   2010-06-30  25.790001  30.42  23.299999  23.830000
2 days   2010-07-01  25.000000  25.92  20.270000  21.959999
3 days   2010-07-02  23.000000  23.10  18.709999  19.200001
'''
```

### 11.10 日期范围

> 并非每个数据集的值都有固定的频率。比如在Ebola数据集中就没有观察某个日期范围内的每一天

```python
ebola = pd.read_csv('country_timeseries.csv',
                    parse_dates = [0])
print(ebola.iloc[:5, :5])
'''
        Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
0 2015-01-05  289        2776.0            NaN            10030.0
1 2015-01-04  288        2775.0            NaN             9780.0
2 2015-01-03  287        2769.0         8166.0             9722.0
3 2015-01-02  286           NaN         8157.0                NaN
4 2014-12-31  284        2730.0         8115.0             9633.0
'''
# 可以看出，2015-01-01的数据缺失
print(ebola.iloc[-5:, :5])
'''
          Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
117 2014-03-27    5         103.0            8.0                6.0
118 2014-03-26    4          86.0            NaN                NaN
119 2014-03-25    3          86.0            NaN                NaN
120 2014-03-24    2          86.0            NaN                NaN
121 2014-03-22    0          49.0            NaN                NaN
'''
# 可以看出，2014-03-23的数据缺失
# 通常的解决方法是创建一个日期范围来为数据集重建索引，可以使用date_range来实现
# 例如可以为前几行数据创建一个日期范围
hand_range = pd.date_range(start = '2014-12-31', end = '2015-01-05')
print(hand_range)
'''
DatetimeIndex(['2014-12-31', '2015-01-01', '2015-01-02', '2015-01-03',
               '2015-01-04', '2015-01-05'],
              dtype='datetime64[ns]', freq='D')
'''
# 只创建5个数据
ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']
# 为数据重建索引
ebola_5.reindex(hand_range)
print(ebola_5.iloc[:, :5])
'''
                 Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
Date                                                                      
2015-01-05 2015-01-05  289        2776.0            NaN            10030.0
2015-01-04 2015-01-04  288        2775.0            NaN             9780.0
2015-01-03 2015-01-03  287        2769.0         8166.0             9722.0
2015-01-02 2015-01-02  286           NaN         8157.0                NaN
2014-12-31 2014-12-31  284        2730.0         8115.0             9633.0
'''
```

#### 11.10.1 频率

> 前面使用date_range函数创建了head_range，data_range函数有一个参数freq，其默认值为D（代表day），表示日期范围内的值是逐日递增的。
>
> 这些值可以在调用date_range时传入freq参数。例如2017年1月1日是周日，可以创建一个包含该周五个工作日的日期范围

```python
# 2017年1月1日这周所有的工作日
print(pd.date_range('2017-01-01', '2017-01-07', freq = 'B'))
'''
DatetimeIndex(['2017-01-02', '2017-01-03', '2017-01-04', '2017-01-05',
               '2017-01-06'],
              dtype='datetime64[ns]', freq='B')
'''
```

| 别名 | 说明                           | 别名 | 说明         |
| ---- | ------------------------------ | ---- | ------------ |
| B    | 工作日                         | QS   | 季度初       |
| C    | 自定义工作日                   | BQS  | 季度初工作日 |
| D    | 日历日                         | A    | 年末         |
| W    | 每周                           | BA   | 年末工作日   |
| M    | 月末                           | AS   | 年初         |
| SM   | 月中和月末（每月第15天和月末） | BAS  | 年初工作日   |
| BM   | 月末工作日                     | BH   | 工作时间     |
| CBM  | 自定义月末工作日               | H    | 小时         |
| MS   | 月初                           | T    | 分钟         |
| SMS  | 月初和月中                     | S    | 秒           |
| BMS  | 自定义月末工作日               | L    | 毫秒         |
| CBMS | 自定义月初工作日               | U    | 微秒         |
| Q    | 季度末                         | N    | 纳秒         |
| BQ   | 季度末工作日                   |      |              |

#### 11.10.2 偏移量

> 偏移量是在基本频率基础上做的一点调整。例如可以向刚刚创建的工作日范围添加一个偏移量，这样就可以隔一个工作日取一个工作日。

```python
# 从2017年1月1日这周隔一天取一个工作日
print(pd.date_range('2017-01-01', '2017-01-07', freq = '2B'))
'''
DatetimeIndex(['2017-01-02', '2017-01-04', '2017-01-06'], dtype='datetime64[ns]', freq='2B')
'''
```

> 如上所示，通过在基本频率前加一个倍数值创建出了偏移量。还可以将偏移量和其他基本频率结合使用。例如可以指定2017年每个月的第一个星期四

```python
print(pd.date_range('2017-01-01', '2017-12-31', freq = 'WOM-1THU'))
'''
DatetimeIndex(['2017-01-05', '2017-02-02', '2017-03-02', '2017-04-06',
               '2017-05-04', '2017-06-01', '2017-07-06', '2017-08-03',
               '2017-09-07', '2017-10-05', '2017-11-02', '2017-12-07'],
              dtype='datetime64[ns]', freq='WOM-1THU')
'''
# 每个月第三个星期五
print(pd.date_range('2017-01-01', '2017-12-31', freq = 'WOM-3FRI'))
'''
DatetimeIndex(['2017-01-20', '2017-02-17', '2017-03-17', '2017-04-21',
               '2017-05-19', '2017-06-16', '2017-07-21', '2017-08-18',
               '2017-09-15', '2017-10-20', '2017-11-17', '2017-12-15'],
              dtype='datetime64[ns]', freq='WOM-3FRI')
'''
```

### 11.11 移动

> 有些原因需要更改数据的日期。例如修正数据中的某个测量误差。或者对数据的开始日期进行标准化，以便比较趋势
>
> 尽管Ebola数据当前是不整洁的，但其当前格式便于将疫情爆发状况绘制成图

```python
import matplotlib.pyplot as plt
ebola.index = ebola['Date']
fig, ax = plt.subplots()
ax = ebola.plot(ax = ax)
ax.legend(fontsize = 7,
          loc = 2,
          borderaxespad = 0.)
plt.show()
# 观察数据可以看出，疫情在某国的传播速度相较于其他多国更快。下面从数据角度分析
ebola_sub = ebola[['Day', 'Cases_Guinea', 'Cases_Liberia']]
print(ebola_sub.tail(10))
'''
            Day  Cases_Guinea  Cases_Liberia
Date                                        
2014-04-04   13         143.0           18.0
2014-04-01   10         127.0            8.0
2014-03-31    9         122.0            8.0
2014-03-29    7         112.0            7.0
2014-03-28    6         112.0            3.0
2014-03-27    5         103.0            8.0
2014-03-26    4          86.0            NaN
2014-03-25    3          86.0            NaN
2014-03-24    2          86.0            NaN
2014-03-22    0          49.0            NaN
'''
```

> 可见各国疫情爆发日期不同，因此当日后出现新疫情时，就很难比较各国疫情的爆发情况
>
> 1.由于有些日期没有列出来，所以需要为数据集的所有日期创建一个日期范围
>
> 2.需要计算数据集中最早日期和每列最早有效日期（非NaN）之间的差值
>
> 3.然后根据计算移动每列
>
> 开始之前，首先读取Ebola数据集的一个副本。同时把Date列解析为date对象，并把该日期指派给index

```python
ebola = pd.read_csv('country_timeseries.csv',
                    index_col = 'Date',
                    parse_dates = ['Date'])
print(ebola.head().iloc[:, :4])
'''
            Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
Date                                                           
2015-01-05  289        2776.0            NaN            10030.0
2015-01-04  288        2775.0            NaN             9780.0
2015-01-03  287        2769.0         8166.0             9722.0
2015-01-02  286           NaN         8157.0                NaN
2014-12-31  284        2730.0         8115.0             9633.0
'''
print(ebola.tail().iloc[:, :4])
'''
            Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
Date                                                           
2014-03-27    5         103.0            8.0                6.0
2014-03-26    4          86.0            NaN                NaN
2014-03-25    3          86.0            NaN                NaN
2014-03-24    2          86.0            NaN                NaN
2014-03-22    0          49.0            NaN                NaN
'''
```

> 首先需要创建日期范围以填充数据中所有缺失的日期，这样当向下移动日期时，数据移动的天数将与所移动的行数相同

```python
new_idx = pd.date_range(ebola.index.min(), ebola.index.max())
print(new_idx)
'''
DatetimeIndex(['2014-03-22', '2014-03-23', '2014-03-24', '2014-03-25',
               '2014-03-26', '2014-03-27', '2014-03-28', '2014-03-29',
               '2014-03-30', '2014-03-31',
               ...
               '2014-12-27', '2014-12-28', '2014-12-29', '2014-12-30',
               '2014-12-31', '2015-01-01', '2015-01-02', '2015-01-03',
               '2015-01-04', '2015-01-05'],
              dtype='datetime64[ns]', length=290, freq='D')
'''
new_idx = reversed(new_idx)
# 重建索引,没有列举的日期都已填入，同时增加了NaN缺失值
ebola = ebola.reindex(new_idx)
print(ebola.head().iloc[:, :4])
'''
              Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
Date                                                             
2015-01-05  289.0        2776.0            NaN            10030.0
2015-01-04  288.0        2775.0            NaN             9780.0
2015-01-03  287.0        2769.0         8166.0             9722.0
2015-01-02  286.0           NaN         8157.0                NaN
2015-01-01    NaN           NaN            NaN                NaN
'''
print(ebola.tail().iloc[:, :4])
'''
            Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
Date                                                           
2014-03-26  4.0          86.0            NaN                NaN
2014-03-25  3.0          86.0            NaN                NaN
2014-03-24  2.0          86.0            NaN                NaN
2014-03-23  NaN           NaN            NaN                NaN
2014-03-22  0.0          49.0            NaN                NaN
'''
```

> 至此，就创建好了日期范围并将其指派给了index，下一步是计算数据集的最早日期和每列最早有效日期（非缺失值）之间的差值。可以只用Series的last_valid_index方法执行这种计算，它返回最后一个缺失值或非空值的索引值。类似的方法还有first_valid_index，它返回第一个非缺失值或非空值的索引值。由于要对所有列执行这种计算，需要使用apply方法

```python
last_valid = ebola.apply(pd.Series.last_valid_index)
print(last_valid)
'''
Day                   2014-03-22
Cases_Guinea          2014-03-22
Cases_Liberia         2014-03-27
Cases_SierraLeone     2014-03-27
Cases_Nigeria         2014-07-23
Cases_Senegal         2014-08-31
Cases_UnitedStates    2014-10-01
Cases_Spain           2014-10-08
Cases_Mali            2014-10-22
Deaths_Guinea         2014-03-22
Deaths_Liberia        2014-03-27
Deaths_SierraLeone    2014-03-27
Deaths_Nigeria        2014-07-23
Deaths_Senegal        2014-09-07
Deaths_UnitedStates   2014-10-01
Deaths_Spain          2014-10-08
Deaths_Mali           2014-10-22
dtype: datetime64[ns]
'''
# 获取数据集中最早的日期
earliest_date = ebola.index.min()
print(earliest_date) # 2014-03-22 00:00:00
# 然后用last_valid减去该值
shift_values = last_valid - earliest_date
print(shift_values)
'''
Day                     0 days
Cases_Guinea            0 days
Cases_Liberia           5 days
Cases_SierraLeone       5 days
Cases_Nigeria         123 days
Cases_Senegal         162 days
Cases_UnitedStates    193 days
Cases_Spain           200 days
Cases_Mali            214 days
Deaths_Guinea           0 days
Deaths_Liberia          5 days
Deaths_SierraLeone      5 days
Deaths_Nigeria        123 days
Deaths_Senegal        169 days
Deaths_UnitedStates   193 days
Deaths_Spain          200 days
Deaths_Mali           214 days
dtype: timedelta64[ns]
'''
# 最后遍历各列，根据shift_values中相应的值使用shift方法把列下移。请注意，shift_values中的值都是正数
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
'''
            Day  Cases_Guinea  ...  Deaths_Spain  Deaths_Mali
Date                           ...                           
2014-03-26  4.0          86.0  ...           1.0          NaN
2014-03-25  3.0          86.0  ...           NaN          NaN
2014-03-24  2.0          86.0  ...           NaN          NaN
2014-03-23  NaN           NaN  ...           NaN          NaN
2014-03-22  0.0          49.0  ...           1.0          1.0
'''
# Day不再代表一疫情爆发的第一天，而是指定国家疫情爆发的第一天
ebola_shift.index = ebola_shift['Day']
ebola_shift = ebola_shift.drop(['Day'], axis = 1)
print(ebola_shift.tail())
'''
     Cases_Guinea  Cases_Liberia  ...  Deaths_Spain  Deaths_Mali
Day                               ...                           
4.0          86.0            8.0  ...           1.0          NaN
3.0          86.0            NaN  ...           NaN          NaN
2.0          86.0            7.0  ...           NaN          NaN
NaN           NaN            3.0  ...           NaN          NaN
0.0          49.0            8.0  ...           1.0          1.0
'''
```

### 11.12 重采样

> 重采样会把datetime从一个频率转换到另一个频率。重采样有以下三类
>
> 1.下采样：从高频率到低频率（比如从每天到每月）
>
> 2.上采样：从低频率到高频率（比如从每月到每天）
>
> 3.原样采样：采样频率不变（比如从每月的第一个星期四到最后一个星期五）
>
> resample函数有一个rule参数，用于接收偏移量字符串

```python
# 下采样：从每天到每月
# 这里有多个值，需要把结果聚合起来
# 这里使用mean函数
down = ebola.resample('M').mean()
print(down.iloc[:5, :5])
'''
                   Day  Cases_Guinea  ...  Cases_SierraLeone  Cases_Nigeria
Date                                  ...                                  
2014-03-31    4.500000     94.500000  ...           3.333333            NaN
2014-04-30   24.333333    177.818182  ...           2.200000            NaN
2014-05-31   51.888889    248.777778  ...           7.333333            NaN
2014-06-30   84.636364    373.428571  ...         125.571429            NaN
2014-07-31  115.700000    423.000000  ...         420.500000       1.333333
'''
# 这里对下采样得到的值进行上采样
# 请注意填充了多少缺失日期
# 使用缺失值进行填充
up = down.resample('D').mean()
print(up.iloc[:5, :5])
'''
            Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone  Cases_Nigeria
Date                                                                          
2014-03-31  4.5          94.5            6.5           3.333333            NaN
2014-04-01  NaN           NaN            NaN                NaN            NaN
2014-04-02  NaN           NaN            NaN                NaN            NaN
2014-04-03  NaN           NaN            NaN                NaN            NaN
2014-04-04  NaN           NaN            NaN                NaN            NaN
'''
```

### 11.13 时区

> 自己编写的时区转换器不可取。Python的pytz库专用处理时区。Pandas对该库进行了包装

```python
import pytz
print(len(pytz.all_timezones)) # 593
# 输出美国的时区
import re
regex = re.compile(r'^US')
selected_files = filter(regex.search, pytz.common_timezones)
print(list(selected_files))
'''
['US/Alaska', 'US/Arizona', 'US/Central', 'US/Eastern', 'US/Hawaii', 'US/Mountain', 'US/Pacific']
'''
```

> 在pandas中处理时区，最简单的办法是使用pytz.all_timezones给出的字符串名
>
> 为了讲解时区，这里使用了Pandas的Timestamp函数创建两个时间戳

```python
# 东部时间上午7点
depart = pd.Timestamp('2017-08-29 7:00', tz = 'US/Eastern')
print(depart) # 2017-08-29 07:00:00-04:00
# 对时区编码的另一种方法是调用‘空’时间戳的tz_localize方法
arrive = pd.Timestamp('2017-08-29 09:57')
print(arrive) # 2017-08-29 09:57:00
arrive = arrive.tz_localize('US/Pacific')
print(arrive) # 2017-08-29 09:57:00-07:00
# 再把时区转换为东部时区
print(arrive.tz_convert('US/Eastern')) # 2017-08-29 12:57:00-04:00
# 还可以对时区进行计算，但必须在相同时区
# 计算航班飞行时间
duration = arrive.tz_convert('US/Eastern') - depart
print(duration) # 0 days 05:57:00
```

## 第12章 线性模型

### 12.2 简单线性回归

> 线性回归的目标是描述响应变量（也称”结果“或”因变量“）和预测变量（也称”特征“”协变量“或”自变量“）之间的直线关系
>
> 以tips数据集为例。想了解total_bill和小费之间的关系

```python
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head())
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''
```

#### 12.2.1 使用统计模型库

> 可以使用statsmodels库来实践简单的线性回归。下面使用statsmodels库的formula API

```python
import statsmodels.formula.api as smf
```

> 为了执行这个简单的线性回归，使用ols函数计算普通最小二乘值，它是线性回归中估计参数的一种方法。直线的公式是y = mx + b，其中y是响应变量，x是自变量，b是截距，m是斜率
>
> 公式有两部分组成，以波浪线（~）隔开，波浪线左边是响应变量，右边是自变量

```python
model = smf.ols(formula = 'tip ~ total_bill', data = tips)
# 拟合模型
results = model.fit()
# 查看结果
print(results.summary())
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    tip   R-squared:                       0.457
Model:                            OLS   Adj. R-squared:                  0.454
Method:                 Least Squares   F-statistic:                     203.4
Date:                Wed, 10 Mar 2021   Prob (F-statistic):           6.69e-34
Time:                        20:36:45   Log-Likelihood:                -350.54
No. Observations:                 244   AIC:                             705.1
Df Residuals:                     242   BIC:                             712.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.9203      0.160      5.761      0.000       0.606       1.235
total_bill     0.1050      0.007     14.260      0.000       0.091       0.120
==============================================================================
Omnibus:                       20.185   Durbin-Watson:                   2.151
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               37.750
Skew:                           0.443   Prob(JB):                     6.35e-09
Kurtosis:                       4.711   Cond. No.                         53.0
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
```

> 结果包含模型的Intercept（截距）和total_bill。有了这些参数，就能得到直线 y = 0.105x + 0.920。可以将这些数字解释为：total_bill每增加一个单位（即每次消费额增加1美元），小费就增加0.105个单位（即10.5美分）
>
> 如果只想要系数，可以借助results的params属性来获得

```python
print(results.params)
'''
Intercept     0.920270
total_bill    0.105025
dtype: float64
'''
# 对于某些领域，可能还需要一个置信区间，用于确定估计值。置信区间的值在[0.025,0.975]之间，可以用conf_int方法提取这些值
print(results.conf_int())
'''
                   0         1
Intercept   0.605622  1.234918
total_bill  0.090517  0.119532
'''
```

#### 12.2.2 使用sklearn库

> 可以使用sklearn库来拟合各种机器学习模型,需要引入linear_model模块

```python
from sklearn import linear_model
# 创建线性回归对象，LinearRegression
lr = linear_model.LinearRegression()
# 指定自变量X和响应变量y。为此，需要把想要的列传入模型
# 请注意，X是大写，y是小写
# 因为X只有一个变量，所以会失败
predicted = lr.fit(X = tips['total_bill'],
                   y = tips['tip'])
'''
ValueError: Expected 2D array, got 1D array instead:
array=[16.99 10.34 21.01 23.68 24.59 25.29  8.77 26.88 15.04 14.78 10.27 35.26
 15.42 18.43 14.83 21.58 10.33 16.29 16.97 20.65 17.92 20.29 15.77 39.42
 19.82 17.81 13.37 12.69 21.7  19.65  9.55 18.35 15.06 20.69 17.78 24.06
 16.31 16.93 18.69 31.27 16.04 17.46 13.94  9.68 30.4  18.29 22.23 32.4
 28.55 18.04 12.54 10.29 34.81  9.94 25.56 19.49 38.01 26.41 11.24 48.27
 20.29 13.81 11.02 18.29 17.59 20.08 16.45  3.07 20.23 15.01 12.02 17.07
 26.86 25.28 14.73 10.51 17.92 27.2  22.76 17.29 19.44 16.66 10.07 32.68
 15.98 34.83 13.03 18.28 24.71 21.16 28.97 22.49  5.75 16.32 22.75 40.17
 27.28 12.03 21.01 12.46 11.35 15.38 44.3  22.42 20.92 15.36 20.49 25.21
 18.24 14.31 14.    7.25 38.07 23.95 25.71 17.31 29.93 10.65 12.43 24.08
 11.69 13.42 14.26 15.95 12.48 29.8   8.52 14.52 11.38 22.82 19.08 20.27
 11.17 12.26 18.26  8.51 10.33 14.15 16.   13.16 17.47 34.3  41.19 27.05
 16.43  8.35 18.64 11.87  9.78  7.51 14.07 13.13 17.26 24.55 19.77 29.85
 48.17 25.   13.39 16.49 21.5  12.66 16.21 13.81 17.51 24.52 20.76 31.71
 10.59 10.63 50.81 15.81  7.25 31.85 16.82 32.9  17.89 14.48  9.6  34.63
 34.65 23.33 45.35 23.17 40.55 20.69 20.9  30.46 18.15 23.1  15.69 19.81
 28.44 15.48 16.58  7.56 10.34 43.11 13.   13.51 18.71 12.74 13.   16.4
 20.53 16.47 26.59 38.73 24.27 12.76 30.06 25.89 48.33 13.27 28.17 12.9
 28.15 11.59  7.74 30.14 12.16 13.42  8.58 15.98 13.42 16.27 10.09 20.45
 13.28 22.12 24.01 15.69 11.61 10.77 15.53 10.07 12.6  32.83 35.83 29.03
 27.18 22.67 17.82 18.78].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
'''
```

> 由于sklearn接收的是NumPy数组，所以有时需要处理数据，以便把DataFrame传入sklearn。上面输出的错误信息实际是告知传入矩阵的形状不对，需要重塑输入。根据是否只有一个变量（例如本例）或者一个样本（即多重观测），要分别指定reshape(-1, 1)或reshape(1, -1)
>
> 在列上直接调用reshape会引发DeprecationWarning（Pandas 0.17）或ValueError（Pandas 0.19），具体取决于所用的Pandas版本。为了重塑数据，必须使用values属性。当使用Pandas DataFrame或Series的values属性时，需要使用Numpy ndarray来表示数据

```python
# 请注意，X是大写，y是小写
# 重塑数据，使其符合sklearn的要求
predicted = lr.fit(X = ['total_bill'].values.reshape(-1, 1),
                   y = tips['tip'])
```

> 由于sklearn可以处理Numpy ndarray，所以在代码中把Numpy向量显示传入X或y参数：y = tips['tip'].values
>
> 然而sklearn并没有像statsmodels那样绘制出美观的汇总表。这主要反映了两个库背后不同的指导思想，即统计学和计算机科学/机器学习。在sklearn中，可以通过拟合模型的coef_属性来获得系数

```python
print(predicted.coef_) # [0.10502452]
# 获取截距
print(predicted.intercept_) # 0.9202696135546731
```

### 12.3 多元回归

> 在简单线性回归中，自变量在连续响应变量上线性回归。也可以使用多元回归把多个自变量放入模型中

#### 12.3.1 使用statsmodels库

> 用多元回归模型拟合数据集与拟合简单的线性回归模型非常相似。在formula参数中，可以轻松地把其他协变量”添加“到波浪线右边

```python
model = smf.ols(formula = 'tip ~ total_bill + size', data = tips).fit()
print(model.summary())
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    tip   R-squared:                       0.468
Model:                            OLS   Adj. R-squared:                  0.463
Method:                 Least Squares   F-statistic:                     105.9
Date:                Wed, 10 Mar 2021   Prob (F-statistic):           9.67e-34
Time:                        21:02:45   Log-Likelihood:                -347.99
No. Observations:                 244   AIC:                             702.0
Df Residuals:                     241   BIC:                             712.5
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.6689      0.194      3.455      0.001       0.288       1.050
total_bill     0.0927      0.009     10.172      0.000       0.075       0.111
size           0.1926      0.085      2.258      0.025       0.025       0.361
==============================================================================
Omnibus:                       24.753   Durbin-Watson:                   2.100
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               46.169
Skew:                           0.545   Prob(JB):                     9.43e-11
Kurtosis:                       4.831   Cond. No.                         67.6
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
```

> 对上面内容的解释和前面的完全相同。当然，对每个参数都是在所有其他变量保持不变的情况下。total_bill每增加1美元，小费就会增加0.09美元，前提是分组规模不变

#### 12.3.2 使用statsmodels和分类变量

> 前面都只在模型中使用连续自变量。如果查看info属性，就会发现数据中还包含分类变量

```python
print(tips.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype   
---  ------      --------------  -----   
 0   total_bill  244 non-null    float64 
 1   tip         244 non-null    float64 
 2   sex         244 non-null    category
 3   smoker      244 non-null    category
 4   day         244 non-null    category
 5   time        244 non-null    category
 6   size        244 non-null    int64   
dtypes: category(4), float64(2), int64(1)
memory usage: 7.3 KB
None
'''
```

> 在对分类变量进行建模时，必须创建虚拟变量，即分类中的每个唯一值都变成了新的二元特征。例如数据中的sex可以是Female或Male

```python
print(tips.sex.unique())
'''
['Female', 'Male']
Categories (2, object): ['Female', 'Male']
'''
```

> statsmodels会自动创建虚拟变量。为了避免多重共线性，通常会删除其中一个虚拟变量。例如有一列用于指明某人是否为女性，那么就知道此人不是女性就是男性（在该数据中）。在这种情况下，可以删除代表男性的虚拟变量，信息保持不变

```python
model = smf.ols(
  formula = 'tip ~ total_bill + size + sex + smoker + day + time',
  data = tips
).\
  fit()
print(model.summary())
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    tip   R-squared:                       0.470
Model:                            OLS   Adj. R-squared:                  0.452
Method:                 Least Squares   F-statistic:                     26.06
Date:                Wed, 10 Mar 2021   Prob (F-statistic):           1.20e-28
Time:                        21:45:52   Log-Likelihood:                -347.48
No. Observations:                 244   AIC:                             713.0
Df Residuals:                     235   BIC:                             744.4
Df Model:                           8                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
Intercept          0.5908      0.256      2.310      0.022       0.087       1.095
sex[T.Female]      0.0324      0.142      0.229      0.819      -0.247       0.311
smoker[T.No]       0.0864      0.147      0.589      0.556      -0.202       0.375
day[T.Fri]         0.1623      0.393      0.412      0.680      -0.613       0.937
day[T.Sat]         0.0408      0.471      0.087      0.931      -0.886       0.968
day[T.Sun]         0.1368      0.472      0.290      0.772      -0.793       1.066
time[T.Dinner]    -0.0681      0.445     -0.153      0.878      -0.944       0.808
total_bill         0.0945      0.010      9.841      0.000       0.076       0.113
size               0.1760      0.090      1.966      0.051      -0.000       0.352
==============================================================================
Omnibus:                       27.860   Durbin-Watson:                   2.096
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               52.555
Skew:                           0.607   Prob(JB):                     3.87e-12
Kurtosis:                       4.923   Cond. No.                         281.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
```

> 对这些参数的解释和之前一样。不过，对分类变量的解释必须和参考变量（即从分析中删除的虚拟变量）联系起来。例如sex[T.Female]的系数是0.0324，解释该值是要与参考值（Male）联系起来。也就是说，当sex从Male变为Female时，tip增加了0.324.对于day变量

```python
print(tips.day.unique())
'''
['Sun', 'Sat', 'Thur', 'Fri']
Categories (4, object): ['Sun', 'Sat', 'Thur', 'Fri']
'''
```

#### 12.3.3 使用sklearn库

> 在sklearn中，多元回归语法与库中的简单线性回归语法非常相似。为了向模型添加更多特征，可以把要使用的列传入模型

```python
lr = linear_model.LinearRegression()
# 由于执行的是多元回归，所以无需重塑X值
predicted = lr.fit(X = tips[['total_bill', 'size']],
                   y = tips['tip'])
print(predicted.coef_) # [0.09271334 0.19259779]
# 可以用intercept_获取截距
print(predicted.intercept_) # 0.6689447408125031
```

#### 12.3.4 使用sklearn和分类变量

> 必须手动为sklearn创建虚拟变量，可以使用Pandas的get_dummies函数来实现。该函数会自动把所有的分类变量转换为虚拟变量，所以不必再逐个传入各列了。sklearn的OneHotEncoder函数与之类似

```python
tips_dummy = pd.get_dummies(
  tips[['total_bill', 'size',
        'sex', 'smoker', 'day', 'time']]
)
print(tips_dummy.head())
'''
   total_bill  size  sex_Male  ...  day_Sun  time_Lunch  time_Dinner
0       16.99     2         0  ...        1           0            1
1       10.34     3         1  ...        1           0            1
2       21.01     3         1  ...        1           0            1
3       23.68     2         1  ...        1           0            1
4       24.59     4         0  ...        1           0            1
'''
# 可以向get_dummies函数传入drop_first = True来删除参考变量
x_tips_dummy_ref = pd.get_dummies(
  tips[['total_bill', 'size',
        'sex', 'smoker', 'day', 'time']], drop_first = True
)
print(x_tips_dummy_ref.head())
'''
   total_bill  size  sex_Female  ...  day_Sat  day_Sun  time_Dinner
0       16.99     2           1  ...        0        1            1
1       10.34     3           0  ...        0        1            1
2       21.01     3           0  ...        0        1            1
3       23.68     2           0  ...        0        1            1
4       24.59     4           1  ...        0        1            1
'''
# 拟合模型
lr = linear_model.LinearRegression()
predicted = lr.fit(X = x_tips_dummy_ref,
                   y = tips['tip'])
print(predicted.coef_)
'''
[ 0.09448701  0.175992    0.03244094  0.08640832  0.1622592   0.04080082
  0.13677854 -0.0681286 ]
'''
# 获取系数
print(predicted.intercept_) # 0.5908374259513769
```

### 12.4 保留sklearn的索引标签

> 在尝试解释sklearn模型时，一个棘手的问题是模型的系数不带标签，原因是NumPy ndarray无法存储这类元数据。如果想让输出的结果和statsmodels类似，需要手动存储标签，并添加系数

```python
import numpy as np
# 创建模型并拟合
lr = linear_model.LinearRegression()
predicted = lr.fit(X = x_tips_dummy_ref, y = tips['tip'])
# 获取截距以及其他系数
values = np.append(predicted.intercept_, predicted.coef_)
# 获取值的名称
names = np.append('intercept', x_tips_dummy_ref.columns)
# 把所有项放入一个带标签的DataFrame中
results = pd.DataFrame(values, index = names,
                       columns = ['coef'] # 这里用方括号
                       )
print(results)
'''
                 coef
intercept    0.590837
total_bill   0.094487
size         0.175992
sex_Female   0.032441
smoker_No    0.086408
day_Fri      0.162259
day_Sat      0.040801
day_Sun      0.136779
time_Dinner -0.068129
'''
```

### 12.5 小结

> 本章介绍了使用statsmodels库和sklearn库来拟合模型的基础知识。拟合模型时，经常需要向模型中添加多个特征和创建虚拟变量。本章主要介绍了如何拟合线性模型，其中涉及的响应变量是连续变量。之后拟合模型是涉及的响应变量将不再是连续变量

## 第13章 广义线性模型

> 其实并非每个响应变量都是连续的，线性回归模型也并不适用于所有情况。有些结果可能包含二元数据（例如生病与不生病），或者计数数据（例如硬币正面）。一种名为“广义线性模型”（GLM）的模型可用于解释这类数据，而它使用的仍是自变量的线性组合

### 13.2 逻辑回归

> 当响应变量为二值响应变量时，经常使用逻辑回归对数据建模。下面的数据来自美国社区调查（ACS）对纽约的一些调查数据

```python
import pandas as pd
acs = pd.read_csv('acs_ny.csv')
print(acs.columns)
'''
Index(['Acres', 'FamilyIncome', 'FamilyType', 'NumBedrooms', 'NumChildren',
       'NumPeople', 'NumRooms', 'NumUnits', 'NumVehicles', 'NumWorkers',
       'OwnRent', 'YearBuilt', 'HouseCosts', 'ElectricBill', 'FoodStamp',
       'HeatingFuel', 'Insurance', 'Language'],
      dtype='object')
'''
print(acs.head())
'''
  Acres  FamilyIncome   FamilyType  ...  HeatingFuel  Insurance        Language
0  1-10           150      Married  ...          Gas       2500         English
1  1-10           180  Female Head  ...          Oil          0         English
2  1-10           280  Female Head  ...          Oil       6600  Other European
3  1-10           330  Female Head  ...          Oil          0         English
4  1-10           330    Male Head  ...          Gas        660         Spanish
'''
```

> 要对这些数据建模，首先要创建一个二值响应变量。这里把FamilyIncome（家庭收入）变量分割成二值变量

```python
acs['ge150k'] = pd.cut(acs['FamilyIncome'],
                       [0, 150000, acs['FamilyIncome'].max()],
                       labels = [0, 1])
acs['ge150k_i'] = acs['ge150k'].astype(int)
print(acs['ge150k_i'].value_counts())
'''
0    18294
1     4451
Name: ge150k_i, dtype: int64
'''
# 这样就创建出一个二值变量（0/1）
print(acs.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22745 entries, 0 to 22744
Data columns (total 20 columns):
 #   Column        Non-Null Count  Dtype   
---  ------        --------------  -----   
 0   Acres         22745 non-null  object  
 1   FamilyIncome  22745 non-null  int64   
 2   FamilyType    22745 non-null  object  
 3   NumBedrooms   22745 non-null  int64   
 4   NumChildren   22745 non-null  int64   
 5   NumPeople     22745 non-null  int64   
 6   NumRooms      22745 non-null  int64   
 7   NumUnits      22745 non-null  object  
 8   NumVehicles   22745 non-null  int64   
 9   NumWorkers    22745 non-null  int64   
 10  OwnRent       22745 non-null  object  
 11  YearBuilt     22745 non-null  object  
 12  HouseCosts    22745 non-null  int64   
 13  ElectricBill  22745 non-null  int64   
 14  FoodStamp     22745 non-null  object  
 15  HeatingFuel   22745 non-null  object  
 16  Insurance     22745 non-null  int64   
 17  Language      22745 non-null  object  
 18  ge150k        22745 non-null  category
 19  ge150k_i      22745 non-null  int32   
dtypes: category(1), int32(1), int64(10), object(8)
memory usage: 3.2+ MB
None
'''
```

#### 13.2.1 使用statsmodels

> 使用logit函数执行逻辑回归。该函数的语法与第12章线性回归的函数的语法相同

```python
import statsmodels.formula.api as smf
model = smf.logit('ge150k_i ~ HouseCosts + NumWorkers + '\
                  'OwnRent + NumBedrooms + FamilyType',
                  data = acs)
results = model.fit()
'''
Optimization terminated successfully.
         Current function value: 0.391651
         Iterations 7
'''
print(results.summary())
'''
                           Logit Regression Results                           
==============================================================================
Dep. Variable:               ge150k_i   No. Observations:                22745
Model:                          Logit   Df Residuals:                    22737
Method:                           MLE   Df Model:                            7
Date:                Wed, 10 Mar 2021   Pseudo R-squ.:                  0.2078
Time:                        22:34:49   Log-Likelihood:                -8908.1
converged:                       True   LL-Null:                       -11244.
Covariance Type:            nonrobust   LLR p-value:                     0.000
===========================================================================================
                              coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------------
Intercept                  -5.8081      0.120    -48.456      0.000      -6.043      -5.573
OwnRent[T.Outright]         1.8276      0.208      8.782      0.000       1.420       2.236
OwnRent[T.Rented]          -0.8763      0.101     -8.647      0.000      -1.075      -0.678
FamilyType[T.Male Head]     0.2874      0.150      1.913      0.056      -0.007       0.582
FamilyType[T.Married]       1.3877      0.088     15.781      0.000       1.215       1.560
HouseCosts                  0.0007   1.72e-05     42.453      0.000       0.001       0.001
NumWorkers                  0.5873      0.026     22.393      0.000       0.536       0.639
NumBedrooms                 0.2365      0.017     13.985      0.000       0.203       0.270
===========================================================================================
'''
```

> 解释逻辑回归的结果并不像解释线性回归那样简单。在逻辑回归中，与所有的广义线性模型一样，都需要使用连接函数执行一定的转换，而解释结果时需要回到转换之前的状态
>
> 为了解释模型，首先要把结果指数化

```python
import numpy as np
odds_ratios = np.exp(results.params)
print(odds_ratios)
'''
Intercept                  0.003003
OwnRent[T.Outright]        6.219147
OwnRent[T.Rented]          0.416310
FamilyType[T.Male Head]    1.332901
FamilyType[T.Married]      4.005636
HouseCosts                 1.000731
NumWorkers                 1.799117
NumBedrooms                1.266852
dtype: float64
'''
```

> 然后，把这些值解释成“比值比”。可以把“比值比”看作结果“成真”的概率的倍数。这种说法不准确
>
> 对这些数字的一个解释是，NumBedrooms每增加一个单元，FamilyIncome（家庭收入）超过150000的概率就会增加1.27倍。也可以如此解释分类变量。前面提过，分类变量总是根据参考变量来进行解释。

```python
# OwnRent有如下三中取值
print(acs.OwnRent.unique()) # ['Mortgage' 'Rented' 'Outright']
```

> 可以把这些虚拟变量解释为：相比于以房屋抵押贷款的家庭，那些拥有房屋完全产权的家庭的FamilyIncome高于15万的概率增加了1.82倍

#### 13.2.2 使用sklearn

> 使用sklearn时，需要手动创建虚拟变量

```python
predictors = pd.get_dummies(
  acs[['HouseCosts', 'NumWorkers', 'OwnRent', 'NumBedrooms',
       'FamilyType']],
  drop_first = True
)
# 使用linear_model模块的LogisticRegression对象
from sklearn import linear_model
lr = linear_model.LogisticRegression(max_iter=1000)
# 调用fit方法拟合模型，这和拟合线性模型的方法相同
results = lr.fit(X = predictors, y = acs['ge150k_i'])
# 输出系数
print(results.coef_)
'''
[[ 6.96452832e-04  5.14195108e-01  1.93458756e-01  1.21424848e-01
  -2.02724801e+00 -1.08008243e+00  8.99632229e-01]]
'''
print(results.intercept_) # [-4.91594091]
# 以更友好的格式输出结果
values = np.append(results.intercept_, results.coef_)
# 得到值的名称
names = np.append('intercept', predictors.columns)
# 全部放入一个带标签的DataFrame中
results = pd.DataFrame(values, index = names,
                       columns = ['coef'])
print(results)
'''
                          coef
intercept            -4.915941
HouseCosts            0.000696
NumWorkers            0.514195
NumBedrooms           0.193459
OwnRent_Outright      0.121425
OwnRent_Rented       -2.027248
FamilyType_Male Head -1.080082
FamilyType_Married    0.899632
'''
# 为了解释系数，把值指数化

```

### 13.3 泊松回归

> 当响应变量涉及计数数据时，就需要用到泊松回归。例如在acs数据中，NumChildren变量就是计数数据

#### 13.3.1 使用statsmodels

> 可以使用statsmodels库提供的poisson函数执行泊松分布

```python
results = smf.poisson(
  'NumChildren ~ FamilyIncome + FamilyType + OwnRent',
  data = acs
).fit()
print(results.summary())
'''
                          Poisson Regression Results                          
==============================================================================
Dep. Variable:            NumChildren   No. Observations:                22745
Model:                        Poisson   Df Residuals:                    22739
Method:                           MLE   Df Model:                            5
Date:                Sat, 13 Mar 2021   Pseudo R-squ.:                     nan
Time:                        09:55:35   Log-Likelihood:                    nan
converged:                       True   LL-Null:                       -30977.
Covariance Type:            nonrobust   LLR p-value:                       nan
===========================================================================================
                              coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------------
Intercept                      nan        nan        nan        nan         nan         nan
FamilyType[T.Male Head]        nan        nan        nan        nan         nan         nan
FamilyType[T.Married]          nan        nan        nan        nan         nan         nan
OwnRent[T.Outright]            nan        nan        nan        nan         nan         nan
OwnRent[T.Rented]              nan        nan        nan        nan         nan         nan
FamilyIncome                   nan        nan        nan        nan         nan         nan
===========================================================================================
'''
```

> 使用广义模型的好处是，只需更改（需拟合的）模型的family和连接函数（转换数据）。也可以使用更通用的glm函数来执行相同的运算
>

```python
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
model = smf.glm(
  'NumChildren ~ FamilyIncome + FamilyType + OwnRent',
  data = acs,
  family = sm.families.Poisson(sm.genmod.families.links.log)
)
# 使用glm函数时，需要指定family参数，它接收一个link
results = model.fit()
print(results.summary())
'''
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            NumChildren   No. Observations:                22745
Model:                            GLM   Df Residuals:                    22739
Model Family:                 Poisson   Df Model:                            5
Link Function:                    log   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -30679.
Date:                Sat, 13 Mar 2021   Deviance:                       34643.
Time:                        09:55:38   Pearson chi2:                 3.34e+04
No. Iterations:                     6                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------------
Intercept                  -0.3257      0.021    -15.490      0.000      -0.367      -0.284
FamilyType[T.Male Head]    -0.0630      0.038     -1.637      0.102      -0.138       0.012
FamilyType[T.Married]       0.1440      0.021      6.707      0.000       0.102       0.186
OwnRent[T.Outright]        -1.9737      0.230     -8.599      0.000      -2.424      -1.524
OwnRent[T.Rented]           0.4086      0.021     19.772      0.000       0.368       0.449
FamilyIncome              5.42e-07   6.57e-08      8.247      0.000    4.13e-07    6.71e-07
===========================================================================================
'''
```

#### 13.3.2 负二项回归

> 如果泊松回归的假设不理想（例如数据过度离散），可用负二项回归来代替

```python
model = smf.glm(
  'NumChildren ~ FamilyIncome + FamilyType + OwnRent',
  data = acs,
  family = sm.families.NegativeBinomial(sm.genmod.families.links.log)
)
results = model.fit()
print(results.summary())
'''
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            NumChildren   No. Observations:                22745
Model:                            GLM   Df Residuals:                    22739
Model Family:        NegativeBinomial   Df Model:                            5
Link Function:                    log   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -29749.
Date:                Sat, 13 Mar 2021   Deviance:                       20731.
Time:                        10:03:55   Pearson chi2:                 1.77e+04
No. Iterations:                     6                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------------
Intercept                  -0.3345      0.029    -11.672      0.000      -0.391      -0.278
FamilyType[T.Male Head]    -0.0468      0.052     -0.905      0.365      -0.148       0.055
FamilyType[T.Married]       0.1529      0.029      5.200      0.000       0.095       0.211
OwnRent[T.Outright]        -1.9737      0.243     -8.113      0.000      -2.450      -1.497
OwnRent[T.Rented]           0.4164      0.030     13.754      0.000       0.357       0.476
FamilyIncome             5.398e-07   9.55e-08      5.652      0.000    3.53e-07    7.27e-07
===========================================================================================
'''
```

### 13.4 更多GLM

> statsmodels的GLM文档列出了可以传入GLM参数的许多分布族。可在sm.families.<FAMILY>下找到它们

* Binomial（二项式分布）
* Gamma（伽马分布）
* InverseGaussian（逆高斯分布）
* NegativeBinomial（负二项式子分布）
* Possion（泊松分布）
* Tweedie分布

> 可在sm.families.<FAMILY>.links下找到连接函数。连接函数如下所示，但请注意，这些连接函数并不适用于所有分布族

* CDFLink
* CLogLog
* Log
* Logit
* NegativeBinomial
* Power
* cauchy
* identity
* inverse_power
* inverse_squared

### 13.5 生存分析

> 从技术上看，生存分析不算是回归方法，但当对某事件发生的时间建模时常用到它。例如可用于医学研究，用于判断某种疗法在预防严重不良事件（比如死亡）方面是否优于标准疗法或其它疗法。当数据发生删失，即某事件的确切结果未知时，也会用到生存分析。例如采用某个治疗方案的患者有时在跟进过程中失联。
>
> 通常使用lifelines库进行生存分析。这里使用R survival包中的bladder数据，它记录了膀胱癌在经某种治疗后的复发情况

```python
bladder = pd.read_csv('bladder.csv')
print(bladder.head())
'''
   id  rx  number  size  stop  event  enum
0   1   1       1     3     1      0     1
1   1   1       1     3     1      0     2
2   1   1       1     3     1      0     3
3   1   1       1     3     1      0     4
4   2   1       2     1     4      0     1
'''
# 输出不同疗法（rx）的统计次数
print(bladder['rx'].value_counts())
'''
1    188
2    152
Name: rx, dtype: int64
'''
```

> 进行生存分析之前，先从lifelines库中导入KaplanMeierFitter

```python
from lifelines import KaplanMeierFitter
```

> 创建模型并拟合数据的过程与使用sklearn拟合模型的过程类似。stop变量表示事件发生的时间，event变量表示所关注的事件（膀胱癌复发）是否发生。event的值可为0，因为有些人可能再跟进过程中失联。这些数据称为“删失”数据

```python
from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(bladder['stop'], event_observed = bladder['event'])
# 通过图形展示
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax = kmf.survival_function_.plot(ax = ax)
ax.set_title('Survival function')
plt.show()
# 此外，还可以显示生存曲线的置信区间
fig, ax = plt.subplots()
ax = kmf.plot(ax = ax)
ax.set_title('Survival with confidence intervals')
plt.show()
```

> 前面只画出了生存曲线，还可以拟合出一个模型来预测存活率，称作“Cox比例风险模型”。可以使用lifelines中的CoxPHFitter类来拟合该模型

```python
from lifelines import CoxPHFitter
cph = CoxPHFitter()
# 传入用作自变量的列
cph_bladder_df = bladder[['rx', 'number', 'size',
                          'enum', 'stop', 'event']]
cph.fit(cph_bladder_df, duration_col = 'stop', event_col = 'event')
# <lifelines.CoxPHFitter: fitted with 340 total observations, 228 right-censored observations>
# 输出系数
print(cph.print_summary())
'''
             duration col = 'stop'
                event col = 'event'
      baseline estimation = breslow
   number of observations = 340
number of events observed = 112
   partial log-likelihood = -565.66
         time fit was run = 2021-03-13 02:39:12 UTC

---
            coef  exp(coef)   se(coef)   coef lower 95%   coef upper 95%  exp(coef) lower 95%  exp(coef) upper 95%
covariate                                                                                                         
rx         -0.60       0.55       0.20            -0.99            -0.20                 0.37                 0.82
number      0.22       1.24       0.05             0.13             0.31                 1.13                 1.36
size       -0.06       0.94       0.07            -0.20             0.08                 0.82                 1.09
enum       -0.60       0.55       0.09            -0.79            -0.42                 0.45                 0.66

              z      p   -log2(p)
covariate                        
rx        -2.97 <0.005       8.41
number     4.68 <0.005      18.38
size      -0.80   0.42       1.24
enum      -6.42 <0.005      32.80
---
Concordance = 0.75
Partial AIC = 1139.32
log-likelihood ratio test = 67.21 on 4 df
-log2(p) of ll-ratio test = 43.37

None
'''
```

> 检验Cox模型假设
>
> 检验Cox模型假设的一种方法是根据分层单独绘制生存曲线。前面的示例中，分层是rx列的值，这意味着要为每种疗法单独绘制一条曲线。如果log(-log(生存曲线))与log(时间)曲线相交，则表示模型需要按变量进行分层

```python
rx1 = bladder.loc[bladder['rx'] == 1]
rx2 = bladder.loc[bladder['rx'] == 2]
kmf1 = KaplanMeierFitter()
kmf1.fit(rx1['stop'], event_observed = rx1['event'])

kmf2 = KaplanMeierFitter()
kmf2.fit(rx2['stop'], event_observed = rx2['event'])

fig, axes = plt.subplots()
# 两张图放在一个坐标系中
kmf1.plot_loglogs(ax = axes)
kmf2.plot_loglogs(ax = axes)

axes.legend(['rx1', 'rx2'])
plt.show()
```

> 由于两条线交叉，因此对分析进行分层是有意义的

```python
cph_start = CoxPHFitter()
cph_start.fit(cph_bladder_df, duration_col = 'stop', event_col = 'event',
              strata = ['rx'])
print(cph_start.print_summary())
'''
             duration col = 'stop'
                event col = 'event'
                   strata = ['rx']
      baseline estimation = breslow
   number of observations = 340
number of events observed = 112
   partial log-likelihood = -493.52
         time fit was run = 2021-03-13 02:52:08 UTC

---
            coef  exp(coef)   se(coef)   coef lower 95%   coef upper 95%  exp(coef) lower 95%  exp(coef) upper 95%
covariate                                                                                                         
number      0.21       1.24       0.05             0.12             0.30                 1.13                 1.36
size       -0.05       0.95       0.07            -0.19             0.08                 0.82                 1.09
enum       -0.61       0.55       0.09            -0.79            -0.42                 0.45                 0.66

              z      p   -log2(p)
covariate                        
number     4.60 <0.005      17.84
size      -0.77   0.44       1.19
enum      -6.45 <0.005      33.07
---
Concordance = 0.74
Partial AIC = 993.04
log-likelihood ratio test = 61.84 on 3 df
-log2(p) of ll-ratio test = 41.93

None
'''
```

## 第14章 模型诊断

> 创建模型是持续性活动。当向模型中增添或删除变量时，需要设法比较模型，并需要统一的方法来衡量模型的性能。比较模型的方法有多种

### 14.2 残差

> 模型的残差指实际观测值与模型估计值之差。下面使用住房数据集来拟合几个模型

```python
import pandas as pd
housing = pd.read_csv('housing_renamed.csv')
print(housing.head())
'''
  neighborhood            type  units  ...     value  value_per_sq_ft       boro
0    FINANCIAL  R9-CONDOMINIUM     42  ...   7300000           200.00  Manhattan
1    FINANCIAL  R4-CONDOMINIUM     78  ...  30690000           242.76  Manhattan
2    FINANCIAL  RR-CONDOMINIUM    500  ...  90970000           164.15  Manhattan
3    FINANCIAL  R4-CONDOMINIUM    282  ...  67556006           271.23  Manhattan
4      TRIBECA  R4-CONDOMINIUM    239  ...  54320996           247.48  Manhattan
'''
```

> 首先拟合多元线性回归模型

```python
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf

house1 = smf.glm('value_per_sq_ft ~ units + sq_ft + boro',
                 data = housing).fit()
print(house1.summary())
'''
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:        value_per_sq_ft   No. Observations:                 2626
Model:                            GLM   Df Residuals:                     2619
Model Family:                Gaussian   Df Model:                            6
Link Function:               identity   Scale:                          1879.5
Method:                          IRLS   Log-Likelihood:                -13621.
Date:                Sat, 13 Mar 2021   Deviance:                   4.9224e+06
Time:                        11:01:21   Pearson chi2:                 4.92e+06
No. Iterations:                     3                                         
Covariance Type:            nonrobust                                         
=========================================================================================
                            coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------------
Intercept                43.2909      5.330      8.122      0.000      32.845      53.737
boro[T.Brooklyn]         34.5621      5.535      6.244      0.000      23.714      45.411
boro[T.Manhattan]       130.9924      5.385     24.327      0.000     120.439     141.546
boro[T.Queens]           32.9937      5.663      5.827      0.000      21.895      44.092
boro[T.Staten Island]    -3.6303      9.993     -0.363      0.716     -23.216      15.956
units                    -0.1881      0.022     -8.511      0.000      -0.231      -0.145
sq_ft                     0.0002   2.09e-05     10.079      0.000       0.000       0.000
=========================================================================================
'''
```

> 可以把模型的残差绘制出来。结果是一幅散点图。如果图中明显显现出某种模型，就需要研究数据和模型，分析这种模式出现的原因

```python
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax = sns.regplot(x = house1.fittedvalues,
                 y = house1.resid_deviance, fit_reg = False)
plt.show()
```

> 该残差图效果不佳，因为其中包含了明显的群集和组。下面通过boro变量为图着色，以不同颜色代表纽约每个区

```python
res_df = pd.DataFrame({
  'fittedvalues': house1.fittedvalues,
  'resid_deviance': house1.resid_deviance,
  'boro': housing['boro']
})
fig = sns.lmplot(x = 'fittedvalues', y = 'resid_deviance',
                 data = res_df, hue = 'boro', fit_reg = False)
plt.show()
```

> 当通过boro着色时，可以看到点簇受到了变量值的极大影响

> Q-Q图
>
> Q-Q图用于判断数据是否符合某个参考分布。许多模型假设都是正态分布的，因此Q-Q图常用于检验数据是否来自正态分布

```python
from scipy import stats
resid = house1.resid_deviance.copy()
resid_std = stats.zscore(resid)

fig = statsmodels.graphics.gofplots.qqplot(resid, line = 'r')
plt.show()
```

> 还可以绘制直方图，观察数据是否符合正态分布

```python
fig, ax = plt.subplots()
ax = sns.displot(resid_std)
plt.show()
```

> 如果Q-Q图上的点在红线上，就表示数据符合参考分布，否则要转换数据。下表列举了可以对数据做哪种转换。相比于红色参考线，如果Q-Q图是凸的，可以沿表向上转换数据；如果Q-Q图是凹的，可以沿表向下转换数据



### 14.3 比较多个模型

#### 14.3.1 比较线性模型

> 首先拟合5个模型。请注意，有些模型使用“+”运算符向模型中添加协变量。当在模型中指定交互时应使用“*”操作符。这意味着交互变量的行为不是相互独立的，它们的值相互影响，而不是简单地相加

```python
# 原始数据包含class列
# 使用class这个词会引发错误，因为class是Python的关键字
# 把列重命名为type
f1 = 'value_per_sq_ft ~ units + sq_ft + boro'
f2 = 'value_per_sq_ft ~ units * sq_ft + boro'
f3 = 'value_per_sq_ft ~ units + sq_ft * boro + type'
f4 = 'value_per_sq_ft ~ units + sq_ft * boro + sq_ft * type'
f5 = 'value_per_sq_ft ~ boro + type'
house1 = smf.ols(f1, data = housing).fit()
house2 = smf.ols(f2, data = housing).fit()
house3 = smf.ols(f3, data = housing).fit()
house4 = smf.ols(f4, data = housing).fit()
house5 = smf.ols(f5, data = housing).fit()
# 针对所有模型，获取系数和相关模型
mod_results = pd.concat([house1.params, house2.params, house3.params,
                         house4.params, house5.params], axis = 1).\
  rename(columns = lambda x: 'house' + str(x + 1)).\
  reset_index().\
  rename(columns = {'index': 'param'}).\
  melt(id_vars = 'param', var_name = 'model', value_name = 'estimate')
print(mod_results.head())
'''
                   param   model    estimate
0              Intercept  house1   43.290863
1       boro[T.Brooklyn]  house1   34.562150
2      boro[T.Manhattan]  house1  130.992363
3         boro[T.Queens]  house1   32.993674
4  boro[T.Staten Island]  house1   -3.630251
'''
print(mod_results.tail())
'''
                           param   model  estimate
85          sq_ft:boro[T.Queens]  house5       NaN
86   sq_ft:boro[T.Staten Island]  house5       NaN
87  sq_ft:type[T.R4-CONDOMINIUM]  house5       NaN
88  sq_ft:type[T.R9-CONDOMINIUM]  house5       NaN
89  sq_ft:type[T.RR-CONDOMINIUM]  house5       NaN
'''
# 把模型的系数绘制成一幅图
fig, ax = plt.subplots()
ax = sns.pointplot(x = "estimate", y = "param", hue = "model",
                   data = mod_results,
                   dodge = True, # jitter the points
                   join = False) # don't connect the points
plt.tight_layout()
plt.show()
```

> 这样就得到了线性模型。下面可以用方差分析（ANOVA）方法来比较它们。方差分析会给出残差平方和（RSS），可以通过它来评估模型的性能（残差平方和越小，模型的拟合效果越好）

```python
model_names = ['house1', 'house2', 'house3', 'house4', 'house5']
house_anova = statsmodels.stats.anova.anova_lm(
  house1, house2, house3, house4, house5
)
house_anova.index = model_names
print(house_anova)
'''
        df_resid           ssr  df_diff        ss_diff          F        Pr(>F)
house1    2619.0  4.922389e+06      0.0            NaN        NaN           NaN
house2    2618.0  4.884872e+06      1.0   37517.437605  20.039049  7.912333e-06
house3    2612.0  4.619926e+06      6.0  264945.539994  23.585728  2.754431e-27
house4    2609.0  4.576671e+06      3.0   43255.441192   7.701289  4.025581e-05
house5    2618.0  4.901463e+06     -9.0 -324791.847907  19.275539           NaN
'''
```

> 评估模型性能的另一种方法是使用赤池信息量准则（AIC）和贝叶斯信息准则（BIC）。这些方法均引入了与模型参数个数相关的惩罚项。因此，应尽量在模型的性能和间接性之间做好平衡（简单优于复杂）



#### 14.3.2 比较GLM

> 可以采用同样的方法评估和诊断GLM。不过，方差分析只评估模型的偏差

```python
def anova_deviance_table(*models):
  return pd.DataFrame({
    'df_residuals': [i.df_resid for i in models],
    'resid_stddev': [i.deviance for i in models],
    'df': [i.df_model for i in models],
    'deviance': [i.deviance for i in models]
  })
f1 = 'value_per_sq_ft ~ units + sq_ft + boro'
f2 = 'value_per_sq_ft ~ units * sq_ft + boro'
f3 = 'value_per_sq_ft ~ units + sq_ft * boro + type'
f4 = 'value_per_sq_ft ~ units + sq_ft * boro + sq_ft * type'
f5 = 'value_per_sq_ft ~ boro + type'

glm1 = smf.glm(f1, data = housing).fit()
glm2 = smf.glm(f2, data = housing).fit()
glm3 = smf.glm(f3, data = housing).fit()
glm4 = smf.glm(f4, data = housing).fit()
glm5 = smf.glm(f5, data = housing).fit()

glm_anova = anova_deviance_table(glm1, glm2, glm3, glm4, glm5)
print(glm_anova)
'''
   df_residuals  resid_stddev  df      deviance
0          2619  4.922389e+06   6  4.922389e+06
1          2618  4.884872e+06   7  4.884872e+06
2          2612  4.619926e+06  13  4.619926e+06
3          2609  4.576671e+06  16  4.576671e+06
4          2618  4.901463e+06   7  4.901463e+06
'''
# 在逻辑回归中也可以这样做
# 创建二值变量
housing['high_value'] = (housing['value_per_sq_ft'] >= 150).astype(int)
print(housing['high_value'].value_counts())
'''
0    1619
1    1007
Name: high_value, dtype: int64
'''
# 使用GLM创建与拟合逻辑回归

```

### 14.4 k折交叉验证

> 交叉验证是另外一种模型比较方法。它可以解释模型在新数据上的表现。这种方法会把数据分成k个部分，把其中一个部分用作测试集，把其余部分用作训练集以拟合模型。模型拟合好之后，使用测试集进行测试，并计算误差。不断重复这个过程，直到k个部分都测试过。模型的最终误差是所有模型的平均值。
>
> 进行交叉验证有多种方法。刚才介绍的方法叫“k折交叉验证”。而“留一交叉验证”方法每次只留下一个样本用作测试集，其它样本都用作训练集。
>
> 下面把数据分成k-1个测试集和训练集

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
print(housing.columns)
'''
Index(['neighborhood', 'type', 'units', 'year_built', 'sq_ft', 'income',
       'income_per_sq_ft', 'expense', 'expense_per_sq_ft', 'net_income',
       'value', 'value_per_sq_ft', 'boro', 'high_value'],
      dtype='object')
'''
# 获取训练数据和测试数据
X_train, X_test, y_train, y_test = train_test_split(
  pd.get_dummies(housing[['units', 'sq_ft', 'boro']],
                 drop_first = True),
  housing['value_per_sq_ft'],
  test_size = 0.20,
  random_state = 42
)
# 可以算出一个分数，衡量模型在测试数据上的表现
lr = LinearRegression().fit(X_train, y_train)
print(lr.score(X_test, y_test)) # 0.613712528503087
```

> 由于sklearn高度依赖NumPy ndarray，所以patsy库允许指定一个公式，比如statsmodels中的公式API，并且会返回合适的NumPy数组，以便在sklearn中使用。
>
> 下面的代码和前面基本相同，只是使用了patsy库中的dmatrices函数

```python
from patsy import dmatrices
y, X = dmatrices('value_per_sq_ft ~ units + sq_ft + boro', housing,
                 return_type = "dataframe")
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size = 0.20, random_state = 42
)
lr = LinearRegression().fit(X_train, y_train)
print(lr.score(X_test, y_test)) # 0.6137125285026597
# 为了执行k折交叉验证，需要先从sklearn库导入该函数
from sklearn.model_selection import KFold, cross_val_score
# 重新获取住房数据集
housing = pd.read_csv('housing_renamed.csv')
```

> 接下来，必须指定需要多少折，这取决于数据的行数。如果数据中包含的观测值不太多，可以选择一个较小的k（例如2）。k值通常介于5到10之间。但请注意，k值越大，所需要的计算的时间就越长，请根据实际情况选择合适的k值

```python
kf = KFold(n_splits = 5)
y, X = dmatrices('value_per_sq_ft ~ units + sq_ft + boro', housing)
# 在每一折上训练并测试数据
coefs = []
scores = []
for train, test in kf.split(X):
  X_train, X_test = X[train], X[test]
  y_train, y_test = y[train], y[test]
  lr = LinearRegression().fit(X_train, y_train)
  coefs.append(pd.DataFrame(lr.coef_))
  scores.append(lr.score(X_test, y_test))
coefs_df = pd.concat(coefs)
coefs_df.columns = X.design_info.column_names
print(coefs_df)
'''
   Intercept  boro[T.Brooklyn]  ...     units     sq_ft
0        0.0         33.369037  ... -0.205890  0.000220
0        0.0         32.889925  ... -0.146180  0.000155
0        0.0         30.975560  ... -0.179671  0.000194
0        0.0         41.449196  ... -0.207904  0.000232
0        0.0        -38.511915  ... -0.145829  0.000202
'''
```

> 可以使用apply和np.mean函数查看所有折的平均系数

```python
import numpy as np
print(coefs_df.apply(np.mean))
'''
Intercept                  0.000000
boro[T.Brooklyn]          20.034361
boro[T.Manhattan]        115.113918
boro[T.Queens]            22.187107
boro[T.Staten Island]     -3.422088
units                     -0.177095
sq_ft                      0.000201
dtype: float64
'''
```

> 还可以查看每个模型的分数。每个模型都有默认的计分方法。例如LinearRegression使用R的平方（决定系数）回归评分函数

```python
print(scores)
'''
[0.027314162909386153, -0.5538362212297483, -0.1563637168803247, -0.3234202061859879, -1.692965558624492]
'''
# 还可以使用cross_val_scores（交叉验证分数）计算cv分数
model = LinearRegression()
scores = cross_val_score(model, X, y, cv = 5)
print(scores) # [ 0.02731416 -0.55383622 -0.15636372 -0.32342021 -1.69296556]
# 比较多个模型可以使用比较平均分数
print(scores.mean()) # -0.5398543080022333
# 然后使用k折交叉验证重新拟合模型
# 创建预测变量矩阵和响应矩阵
y1, X1 = dmatrices('value_per_sq_ft ~ units + sq_ft + boro',
                   housing)
y2, X2 = dmatrices('value_per_sq_ft ~ units * sq_ft + boro',
                   housing)
y3, X3 = dmatrices('value_per_sq_ft ~ units + sq_ft * boro + type',
                   housing)
y4, X4 = dmatrices('value_per_sq_ft ~ units + sq_ft * boro + sq_ft * type',
                   housing)
y5, X5 = dmatrices('value_per_sq_ft ~ boro + type', housing)
# 拟合模型
model = LinearRegression()

scores1 = cross_val_score(model, X1, y1, cv = 5)
scores2 = cross_val_score(model, X2, y2, cv = 5)
scores3 = cross_val_score(model, X3, y3, cv = 5)
scores4 = cross_val_score(model, X4, y4, cv = 5)
scores5 = cross_val_score(model, X5, y5, cv = 5)
# 查看交叉验证分数
score_df = pd.DataFrame([scores1, scores2, scores3,
                         scores4, scores5])
print(score_df.apply(np.mean, axis = 1))
'''
0   -5.398543e-01
1   -1.088184e+00
2   -2.295436e+26
3   -4.283627e+25  
4   -3.119081e+24
dtype: float64
'''
```

## 第15章 正则化

### 15.2 何为正则化

```python
import pandas as pd
acs = pd.read_csv('acs_ny.csv')
print(acs.columns)
'''
Index(['Acres', 'FamilyIncome', 'FamilyType', 'NumBedrooms', 'NumChildren',
       'NumPeople', 'NumRooms', 'NumUnits', 'NumVehicles', 'NumWorkers',
       'OwnRent', 'YearBuilt', 'HouseCosts', 'ElectricBill', 'FoodStamp',
       'HeatingFuel', 'Insurance', 'Language'],
      dtype='object')
'''
# 使用patsy创建设计矩阵

```



### 15.3 LASSO回归



### 15.4 岭回归



### 15.5 弹性网



### 15.6 交叉验证



## 第16章 聚类

> 机器学习方法通常可以分为两大类：监督学习和无监督学习。前面创建的都是监督学习模型，因为是用目标变量y或响应变量来训练模型。换句话说，在模型的训练数据中，预设了“正确”答案。在无监督模型这种建模方法中，没有所谓的“正确”答案。有关聚类的方法有很多，其中k均值聚类和层次聚类较为重要

### 16.2 k均值聚类

> 使用k均值算法，首先要选定数据中的群集数（k）。它会随机选取数据中的k个点，计算每个数据点到最初选取的k个点之间的距离。最接近某个群集的点会被划分到同一个集群组。然后把每个群集的中心指定为新的群集中心。重复该过程，计算每个点到每个群集中心的距离，并将其分配给一个群集，然后选择一个新的中心。该算法会重复执行直至收敛。
>
> 有关k均值聚类的工作原理，网上有形象又详细的解释
>
> 下面以酒类数据为例来解释k均值聚类算法

```python
import pandas as pd
wine = pd.read_csv('wine.csv')
# 请注意，数据值全是数值
print(wine.head())
'''
   Cultivar  Alcohol  ...  OD280/OD315 of diluted wines  Proline            
0         1    14.23  ...                          3.92                 1065
1         1    13.20  ...                          3.40                 1050
2         1    13.16  ...                          3.17                 1185
3         1    14.37  ...                          3.45                 1480
4         1    13.24  ...                          2.93                  735
'''
```

> 删除Cultivar列，因为它与数据中的实际群集关联太过紧密

```python
wine = wine.drop('Cultivar', axis = 1)
print(wine.head())
'''
   Alcohol  Malic acid  ...  OD280/OD315 of diluted wines  Proline            
0    14.23        1.71  ...                          3.92                 1065
1    13.20        1.78  ...                          3.40                 1050
2    13.16        2.36  ...                          3.17                 1185
3    14.37        1.95  ...                          3.45                 1480
4    13.24        2.59  ...                          2.93                  735
'''
```

> sklearn库有一个k均值算法的实现--K-means。这里把k值设置成3，并使用数据集中的全部数据

```python
from sklearn.cluster import KMeans
# 创建三个群集
# 随机种子为42
# 可以忽略random_state参数
# 或者使用一个不同的值；使用42可以保证所得结果和本书结果一致
kmeans = KMeans(n_clusters = 3, random_state = 42).fit(wine.values)
# 输出kmeans对象
print(kmeans)
'''
KMeans(n_clusters=3, random_state=42)
'''
# 由于指定了群集数为3，所以只有3个特殊标签
import numpy as np
print(np.unique(kmeans.labels_, return_counts = True))
'''
(array([0, 1, 2]), array([62, 47, 69], dtype=int64))
'''
# 把这些标签转换成DataFrame，以便添加到数据集中
kmeans_3 = pd.DataFrame(kmeans.labels_, columns = ['cluster'])
print(kmeans_3.head())
'''
   cluster
0        1
1        1
2        1
3        1
4        0
'''
```

> 最后，可以把群集可视化。由于人眼只能看到三维空间中的事物，所以需要减少数据的维数。wine数据集有13列，需要减至3列，这样才便于理解。而且由于是在纸张（一种非交互媒介）上绘制这些点，所以应尽量把维数减至2

__使用PCA方法降维__

> 主成分分析是一种投影技术，用于减少数据集的维数。其工作原理是在数据中找到较低的维数，将方差最大化。想象一个三维球中有许多点，PCA的本质是在这些点发出光线并在二维平面上投射出阴影。理想情况下，这些阴影会尽可能分散开。虽然在PCA中相距很远的点可能不会引起关注，但是原来三维球中那些相距很远的点可以让光线通过它们，使投射的阴影彼此相邻。在解释彼此接近的点时千万要小心，因为这些点在原来的空间中可能相距很远
>
> 首先从sklearn中导入PCA

```python
from sklearn.decomposition import PCA
```

> 告知PCA数据要投射的维数。这里把数据投射到两个成分上

```python
# 把数据投射到两个成分上
pca = PCA(n_components = 2).fit(wine)
```

> 然后把数据转换到新空间，并向数据集中添加转换

```python
from sklearn.decomposition import PCA
# 把数据投射到两个成分上
pca = PCA(n_components = 2).fit(wine)
# 转换数据到新空间
pca_trans = pca.transform(wine)
# 为投影命名
pca_trans_df = pd.DataFrame(pca_trans, columns = ['pca1', 'pca2'])
# 连接数据
kmeans_3 = pd.concat([kmeans_3, pca_trans_df], axis = 1)
print(kmeans_3.head())
'''
   cluster        pca1       pca2
0        1  318.562979  21.492131
1        1  303.097420  -5.364718
2        1  438.061133  -6.537309
3        1  733.240139   0.192729
4        0  -11.571428  18.489995
'''
# 绘图展示结果
import seaborn as sns
import matplotlib.pyplot as plt
fig = sns.lmplot(x = 'pca1', y = 'pca2', data = kmeans_3,
                 hue = 'cluster', fit_reg = False)
plt.show()
```

> 前面介绍了K-means对葡萄酒数据的操作。下次再家在原始数据集，并保留之前删除的Cultivar列

```python
wine_all = pd.read_csv('wine.csv')
print(wine_all.head())
'''
   Cultivar  Alcohol  ...  OD280/OD315 of diluted wines  Proline            
0         1    14.23  ...                          3.92                 1065
1         1    13.20  ...                          3.40                 1050
2         1    13.16  ...                          3.17                 1185
3         1    14.37  ...                          3.45                 1480
4         1    13.24  ...                          2.93                  735
'''
```

> 如前所示，在数据上运行PCA，比较PCA的群集和Cultivar变量

```python
pca_all = PCA(n_components = 2).fit(wine_all)
pca_all_trans = pca_all.transform(wine_all)
pca_all_trans_df = pd.DataFrame(pca_all_trans,
                                columns = ['pca_all_1', 'pca_all_2'])
kmeans_3 = pd.concat([kmeans_3,
                      pca_all_trans_df,
                      wine_all['Cultivar']], axis = 1)
# 借助图来比较这些分组
with sns.plotting_context(font_scale = 5):
  fig = sns.lmplot(x = 'pca_all_1',
                   y = 'pca_all_2',
                   data = kmeans_3,
                   row = 'cluster', col = 'Cultivar',
                   fit_reg = False)
plt.show()
# 也可以查看交叉表频率计数
print(pd.crosstab(kmeans_3['cluster'],
                  kmeans_3['Cultivar'],
                  margins = True))
'''
Cultivar   1   2   3  All
cluster                  
0         13  20  29   62
1         46   1   0   47
2          0  50  19   69
All       59  71  48  178
'''
```

### 16.3 层次聚类

> 层次聚类旨在构建群集层次结构。具体实现方法有两种：一种是自下而上的凝聚法，另一种是从上而下的分析法
>
> 下面使用SciPy库来演示层次聚类

```python
from scipy.cluster import hierarchy
# 再次加载葡萄酒数据集，并删除Cultivar列
wine = pd.read_csv('wine.csv')
wine = wine.drop('Cultivar', axis = 1)
# 层次聚类有许多算法。可以使用matplotlib绘制结果
import matplotlib.pyplot as plt
```

#### 16.3.1 最长距离法

```python
wine_complete = hierarchy.complete(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_complete)
plt.show()
```

#### 16.3.2 最短距离法

```python
wine_single = hierarchy.single(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_single)
plt.show()
```

#### 16.3.3 平均距离法

```python
wine_averge = hierarchy.average(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_averge)
plt.show()
```

#### 16.3.4 重心法

```python
wine_centroid = hierarchy.centroid(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(wine_centroid)
plt.show()
```

#### 16.3.5 手动设置阈值

> 可以为color_threshold传入值来根据特定阈值给组着色。SciPy默认使用预设的MATLAB值

```python
wine_complete = hierarchy.complete(wine)
fig = plt.figure()
dn = hierarchy.dendrogram(
  wine_complete,
  # 默认MATLAB阈值
  color_threshold = 0.7 * max(wine_complete[:, 2]),
  above_threshold_color = 'y'
)
plt.show()
```

## 第17章 Pandas之外

## 第18章 感想









