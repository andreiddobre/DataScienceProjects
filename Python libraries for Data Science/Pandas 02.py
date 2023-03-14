import pandas as pd

#Read the faa (Federal Aviation Authority) dataset
#source: https://www.kaggle.com/code/anjusunilkumar/federal-aviation-authority
df_faa_dataset = pd.read_csv('faa_ai_prelim.csv')

#View the dataset shape
print('\nDataset shape is: \n', df_faa_dataset.shape)

#View the first five observations
print('\nThe first five observations are: \n', df_faa_dataset.head())
#View all the columns present in the dataset
print('\nColumns present in the dataset: \n', df_faa_dataset.columns)

#Create a new data frame with only required columns
df_analyze_dataset = df_faa_dataset[['ACFT_MAKE_NAME', 'LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT', 'FLT_PHASE', 'EVENT_TYPE_DESC', 'FATAL_FLAG']]
#View the object type
print('\nThe object type is: \n', type(df_analyze_dataset))
#Output:  <class 'pandas.core.frame.DataFrame'>

#View first five observations
print('\nThe first five observations are: \n', df_analyze_dataset.head())
#Replace all NaN for Fatal flag with 'No', but using the fillna function would not change the actual dataset when you execute them
df_analyze_dataset['FATAL_FLAG'].fillna('No', inplace = True)
#View first five observations
print('\nAfter cleaning, the first five observations are: \n', df_analyze_dataset.head())

#the dataset is now cleaned up where all the NaN fatal flags are replaced with "NO"
#View the shape of the dataset
print('\nNew shape is: \n', df_analyze_dataset.shape)
#Output: (83, 7)

#Drop values where ACFT_MAKE_NAME (aircraft make name) is not available
df_final_dataset = df_analyze_dataset.dropna(subset=['ACFT_MAKE_NAME'])
#View the new shape of the dataset
print('\nNew shape is: \n', df_final_dataset.shape)
#Output: (78, 7)

#Group by aircraft name
aircraftType = df_final_dataset.groupby('ACFT_MAKE_NAME')
#View them by aircraft using size method
print('\nAircraft by size\n', aircraftType.size())

#Now group the dataset by fatal flag
fatalAccidents = df_final_dataset.groupby('FATAL_FLAG')
#View the fatal accidents size
print('\nFatal accidents by size\n', fatalAccidents.size())

#Select the accidents with fatality with fatal flag yes
accidents_with_fatality = fatalAccidents.get_group('Yes')
#View the accidents with fatality
print('\nAccidents with fatality\n', accidents_with_fatality)
