import pandas as pd

person = pd.read_csv('survey_person.csv')
site = pd.read_csv('survey_site.csv')
survey = pd.read_csv('survey_survey.csv')
visited = pd.read_csv('survey_visited.csv')
print(person)
print(site)
print(visited)
print(survey)

visited_subset = visited.loc[[0, 2, 6],]
# merge函数的参数how默认值为inner
o2o_merge = site.merge(visited_subset,
                       left_on = 'name', right_on = 'site')
print(o2o_merge)
m2o_merge = site.merge(visited, left_on = 'name', right_on = 'site')
print(m2o_merge)

ps = person.merge(survey, left_on = 'ident', right_on = 'person')
vs = visited.merge(survey,left_on = 'ident', right_on = 'taken')
print(ps)
print(vs)

ps_vs = ps.merge(vs,
                 left_on = ['ident', 'taken', 'quant', 'reading'],
                 right_on = ['person', 'ident', 'quant', 'reading'])
print(ps_vs.loc[0, ])