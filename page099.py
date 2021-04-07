from numpy import NaN, NAN, nan
import pandas as pd
import numpy as np

print(NaN == True)
print(NaN == False)
print(NaN == 0)
print(NaN == '')

print(NaN == NaN)
print(NaN == nan)
print(NaN == NAN)
print(nan == NAN)


print(pd.isnull(NaN))
print(pd.isnull(nan))
print(pd.isnull(NAN))

print(pd.notnull(NaN))
print(pd.notnull(42))
print(pd.notnull('missing'))

visited_file = 'survey_visited.csv'
print(pd.read_csv(visited_file))
print(pd.read_csv(visited_file, keep_default_na = False))

print(pd.read_csv(visited_file,
                  na_values = [''],
                  keep_default_na = False))
visited = pd.read_csv('survey_visited.csv')
survey = pd.read_csv('survey_survey.csv')
print(visited)
print(survey)
vs = visited.merge(survey, left_on = 'ident', right_on = 'taken')
print(vs)

num_legs = pd.Series({'goal': 4, 'amoeba': nan})
print(num_legs)

scientists = pd.DataFrame({'Name': ['Rosaline Franklin', 'William Gosset'],
                           'Occupation': ['Chemist', 'Statistician'],
                           'Born': ['1920-07-25', '1876-06-13'],
                           'Died': ['1958-04-16', '1937-10-16']})
# 指定唯一缺失值
scientists['missing'] = nan
print(scientists)

gapminder = pd.read_csv('gapminder.tsv', sep = '\t')
life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
print(life_exp)
print(life_exp.loc[range(2000, 2010), ])

y2000 = life_exp[life_exp.index > 2000]
print(y2000)
print(y2000.reindex(range(2000, 2010)))

ebola = pd.read_csv('country_timeseries.csv')

print(ebola.count())
num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)

print(np.count_nonzero(ebola.isnull()))

print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))
print(ebola.Cases_Guinea.value_counts(dropna = False).head())

print(ebola.fillna(0).iloc[0:10, 0:5])
print(ebola.fillna(method = 'ffill').iloc[0:10, 0:5])

print(ebola.fillna(method = 'bfill').iloc[:, 0:5].tail())

print(ebola.interpolate().iloc[0:10, 0:5])

print(ebola.shape)
ebola_dropna = ebola.dropna()
print(ebola_dropna.shape)
print(ebola_dropna)

ebola['Cases_multiple'] = ebola['Cases_Guinea'] + \
                          ebola['Cases_Liberia'] + \
                          ebola['Cases_SierraLeone']
ebola_subset = ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia',
                             'Cases_SierraLeone', 'Cases_multiple']]
print(ebola_subset.head(n = 10))

