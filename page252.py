import pandas as pd
acs = pd.read_csv('acs_ny.csv')
print(acs.columns)

from patsy import dmatrices
response, predictors = dmatrices(
  'Family'
)