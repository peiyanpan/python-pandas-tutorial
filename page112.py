import pandas as pd

pew = pd.read_csv('pew.csv')
print(pew.iloc[:, 0:6])

# 不必指定value_vars，因为想对除"religion"列以外的所有列进行透视
pew_long = pd.melt(pew, id_vars = 'religion')
print(pew_long.head())

print(pew_long.tail())

pew_long = pd.melt(pew,
                   id_vars = 'religion',
                   var_name = 'income',
                   value_name = 'count')
print(pew_long.head())

print(pew_long.tail())

billboard = pd.read_csv('billboard.csv')
# 查看前几行和前几列
print(billboard.iloc[0:5, 0:16])

billboard_long = pd.melt(
  billboard,
  id_vars = ['year', 'artist', 'track', 'time', 'date.entered'],
  var_name = 'week',
  value_name = 'rating'
)
print(billboard_long.head())

print(billboard_long.tail())

ebola = pd.read_csv('country_timeseries.csv')
print(ebola.columns)
print(ebola.iloc[:5, [0, 1, 2, 3, 10, 11]])

ebola_long = pd.melt(ebola, id_vars = ['Date', 'Day'])
print(ebola_long.head())

print(ebola_long.tail())

variable_split = ebola_long.variable.str.split('_')
print(variable_split[:5])

print(variable_split[-5:])

print(type(variable_split[0]))

status_values = variable_split.str.get(0)
country_values = variable_split.str.get(1)
print(status_values[:5])
print(status_values[-5:])
print(country_values[:5])
print(country_values[-5:])
ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long.head())

variable_split = ebola_long.variable.str.split('_', expand = True)
variable_split.columns = ['status', 'country']
ebola_parsed = pd.concat([ebola_long, variable_split], axis = 1)
print(ebola_parsed.head())
print(ebola_parsed.tail())

constants = ['pi', 'e']
values = ['3.14', '2.718']
print(list(zip(constants, values)))

ebola_long['status'], ebola_long['country'] = zip(*ebola_long.variable.str.split('_'))
print(ebola_long.head())

weather = pd.read_csv('weather.csv')
print(weather.iloc[:5, :11])

weather_melt = pd.melt(weather,
                       id_vars = ['id', 'year', 'month', 'element'],
                       var_name = 'day',
                       value_name = 'temp')
print(weather_melt.head())
print(weather_melt.tail())

weather_tidy = weather_melt.pivot_table(
  index = ['id', 'year', 'month', 'day'],
  columns = 'element',
  values = 'temp'
)
print(weather_tidy.head())
weather_tidy_flat = weather_tidy.reset_index()
print(weather_tidy_flat.head())

weather_tid = weather_melt.\
  pivot_table(
    index = ['id', 'year', 'month', 'day'],
    columns = 'element',
    values = 'temp').\
  reset_index()
print(weather_tid.head())

print(billboard_long.head())

print(billboard_long[billboard_long.track == 'Loser'].head())

billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
print(billboard_songs.shape)
billboard_songs =billboard_songs.drop_duplicates()
print(billboard_songs.shape)

billboard_songs['id'] = range(len(billboard_songs))
print(billboard_songs.head(n = 10))

billboard_ratings = billboard_long.merge(
  billboard_songs, on = ['year', 'artist', 'track', 'time']
)
print(billboard_ratings.head())
billboard_ratings = billboard_ratings[['id', 'date.entered', 'week', 'rating']]
print(billboard_ratings.head())