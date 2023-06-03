#pip install pandas
import pandas as pd

#Read data from csv file fire department of New York City (FDNY)
df_fdny_csv_data_raw = pd.read_csv('FDNY_Firehouse_Listing.csv')
#View content of the data
print('Content: \n', df_fdny_csv_data_raw.describe)

#View first five records
print('First 5 records: \n', df_fdny_csv_data_raw.head(5))

#Skip the first row from dataset
df_fdny_csv_data = pd.read_csv('FDNY_Firehouse_Listing.csv', skiprows=1)
#View first five records from fixed dataset
print('First 5 records (processed data): \n', df_fdny_csv_data.head(5))

#View data statistics using describe()
print('Statistics: \n', df_fdny_csv_data.describe())

#View columns of the dataset
print('Columns: \n', df_fdny_csv_data.columns)

#View index of dataset
print('Index: \n', df_fdny_csv_data.index)

#Count number of records
print('Number of records: \n', df_fdny_csv_data.count())

#View datatypes
print('Datatypes are: \n', df_fdny_csv_data.dtypes)

#Select FDNY information boroughwise
groupby_borough = df_fdny_csv_data_raw.groupby('Borough')
#View FDNY information for each Borough
print('Group rows info by "Borough": \n', groupby_borough.size())

#Select FDNY information for Manhattan
fdny_info_Manhattan = groupby_borough.get_group('Manhattan')
#View FDNY information for Manhattan
print('Info about "Manhattan": \n', fdny_info_Manhattan)


#source: https://catalog.data.gov/dataset/fdny-firehouse-listing
