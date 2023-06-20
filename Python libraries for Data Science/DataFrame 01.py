#pip install pandas
#pip install numpy

import pandas as pd
import numpy as np

#Create DataFrame from dict of equal lenght lists
#Last 8 Olympics data: hosting city, year and number of nations who participated

#Declare a list and pass the indices
olympic_data_list = {'HostCity': ['Tokyo', 'Rio', 'London', 'Beijing', 'Athens', 'Sydney', 'Atlanta', 'Barcelona'],
                     'Year': [2021, 2016, 2012, 2008, 2004, 2000, 1998, 1996],
                     'No. of Nations': [206, 207, 204, 204, 201, 199, 197, 169]}

#Pass the list to the DataFrame method
df_olympic_data = pd.DataFrame(olympic_data_list, columns=['HostCity', 'Year', 'No. of Nations'])
print('\nCreate DataFrame from dict of equal lenght lists\n', df_olympic_data)

#Create DataFrame from a series of dicts
olympic_data_dict = {'London': {2012: 204}, 'Beijing': {2008: 204}}
#Pass the dict to the DataFrame method
df_olympic_data_dict = pd.DataFrame(olympic_data_dict)
print('\nCreate DataFrame from a series of dicts\n', df_olympic_data_dict)

#View a DataFrame by refering to the column name or with the describe function
#select by City name
print('\nSelect by City name\n', df_olympic_data.HostCity)

#Use describe function to display the content
print('\nUse describe function to display the content\n', df_olympic_data.describe)


#Create DataFrame from dict of series
olympic_series_participation = pd.Series([206, 207, 204, 204, 201, 199, 197, 169], index=[2021, 2016, 2012, 2008, 2004, 2000, 1998, 1996])
olympic_series_country = pd.Series(['Tokyo', 'Rio', 'London', 'Beijing', 'Athens', 'Sydney', 'Atlanta', 'Barcelona'],
                                   index=[2021, 2016, 2012, 2008, 2004, 2000, 1998, 1996])
#pass both the dicts and series in the DataFrame
df_olympic_series = pd.DataFrame({'No. of Nations': olympic_series_participation,
                                  'Host Cities': olympic_series_country})
print('\nCreate DataFrame from dict of series\n', df_olympic_series)


#Create DataFrame from dict of ndarray
#Create an ndarray of Olympic years and pass it the the DataFrame as an object
#Create an ndarrays with years
np_array = np.array([2021, 2016, 2012, 2008, 2004, 2000, 1998, 1996])
#Create a dict with the ndarray
dict_ndarray = {'Year': np_array}
#Pass this dict to a new DataFrame 'df_ndarray' as an object
df_ndarray = pd.DataFrame(dict_ndarray)
#New DataFrame listing all the years
print('\nCreate DataFrame from dict of ndarray\n', df_ndarray)


#Create a DataFrame from a DataFrame by passing it as an object
df_from_df = pd.DataFrame(df_olympic_series)
#Displays the range of data elements that were passed as an argument in the earlier DataFrame 'df_olympic_series'
print('\nCreate a DataFrame from a DataFrame\n', df_from_df)

#source: https://www.topendsports.com/events/summer/countries/number.htm
