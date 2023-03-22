import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import the auto data set Mileage per gallon performances of various cars
df_auto_dataset = pd.read_csv('auto-mpg.csv')

#view the top 5 record
print('Top 5 records are: \n', df_auto_dataset.head())

#write a user defined function for origin
#1-USA, 2-Europe, 3-Asia
def origin(num):
    if num==1:
        return 'USA'
    elif num==2:
        return 'Europe'
    else:
        return 'Asia'

#use apply function
df_auto_dataset['origin'] = df_auto_dataset['origin'].apply(origin)

#view first 30 data points after applying the user defined function to data set
print('First 30 records are: \n', df_auto_dataset.head(30))

#draw the pair plot using sns for mpg, weight, origin and with hue origin, set the size to 4
#note: hue is variable in data set to map plot aspects to different colors
sns.pairplot(df_auto_dataset[['mpg', 'weight', 'origin']], hue='origin', height=4)
plt.show()

#source: The dataset is downloaded from UCI Machine Learning Repository
