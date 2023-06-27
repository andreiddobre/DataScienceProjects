#pip install pandas

import pandas as pd

#Loading .csv File in Python
df = pd.read_csv("BostonHousing.csv")
print('CSV | The number of maximum returned rows is:\n', pd.options.display.max_rows)
#col = ((df == 5 ) & (df == )).any()
print('CSV | Specific column using condition >= 500\n', df.loc[df['Unnamed: 0.2'] >= 500])
print('CSV | When using "to_string" Pandas will only return the first 5 rows, and the last 5 rows\n', df.to_string()) 

#Load Data to .csv File
df.to_csv("BostonHousing_woHeader.csv", header=False, sep='|')


#Loading .xlsx File in Python
df = pd.read_excel("BostonHousing.xlsx")
print('XLSX | The number of maximum returned rows is:\n', pd.options.display.max_rows)
print('XLSX | Reading specific columns\n', df.loc[:, ['AGE', 'TAX']])
print('XLSX | When using "to_string" Pandas will only return the first 5 rows, and the last 5 rows\n', df.to_string())

#Load Data to .xlsx File
df.to_excel("BostonHousing_filteredCol.xlsx", columns = ['CRIM', 'INDUS', 'TAX'])


#source: https://faculty.tuck.dartmouth.edu/images/uploads/faculty/business-analytics/Boston_Housing.xlsx
#source: https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset/input
