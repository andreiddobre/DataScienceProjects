import numpy as np
import pandas as pd

#basic pandas 'Series' function
first_series = pd.Series(list('abcdef'))
print("First series\n", first_series)

#numpy 'array' creation routine and pandas 'Series' function
np_country = np.array(['Iceland', 'Indonesia', 'Romania', 'Nigeria', 'Vietnam', 'Canada', 'Argentina', 'Singapore', 'Italy', 'Kenya', 'South Korea', 'Israel'])
s_country = pd.Series(np_country)
print('Countries series\n', s_country)

#Constructing Series from a list
d = [0.024, 1.015, 0.212, 0.376, 0.224, 1.647, 0.637, 0.324, 1.944, 0.079, 1.531, 0.353]
dict_country_gdp = pd.Series(data=d, index=['Iceland', 'Indonesia', 'Romania', 'Nigeria', 'Vietnam', 'Canada', 'Argentina', 'Singapore', 'Italy', 'Kenya', 'South Korea', 'Israel'])
print('Latest official GDP by Country published by the World Bank in 2017 [$ trillion])\n', dict_country_gdp)

#Scalar series
scalar_series = pd.Series(0.5,index=['a', 'b', 'c', 'd', 'e'])
print('Scalar series\n', scalar_series)

#Acces elements in the series
print('GDP first position in the series\n', dict_country_gdp[0])

#Acces first 5 countries from the series
#print(type(dict_country_gdp))
print('GDP first 5 positions in the series\n', dict_country_gdp[0:5])

#Look up a country by name or index
print('GDP location\n', dict_country_gdp.loc['Italy'])

#Look up by position in the series
print('Identify location by position\n', dict_country_gdp.iloc[0])

first_vector_series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
second_vector_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print('1.First vector+second vector series\n', first_vector_series+second_vector_series)

second_vector_series = pd.Series([10, 20, 30, 40], index = ['a', 'd', 'b', 'c'])
print('2.First vector+second vector series\n', first_vector_series+second_vector_series)

#Now replace few indexes with new ones in second vector series
#Adding e and f that have no value, these indices will not be added to the result and would holt Not a Number value, or NaN
second_vector_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'e', 'f'])
print('3.First vector+second vector series\n', first_vector_series+second_vector_series)

#GDPs by Country data source: https://www.worldometers.info/gdp/gdp-by-country/
