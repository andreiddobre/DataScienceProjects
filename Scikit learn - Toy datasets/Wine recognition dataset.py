#pip install sklearn

from sklearn.datasets import load_wine

#load the dataset
wine = load_wine()

#show the dataset's keys
print('Print dataset keys: \n', list(wine))

#description of the dataset
print('Print description of the dataset: \n', wine['DESCR'])

#names of the 13 groups of data
print('Print names of the 13 groups of data: \n', wine['feature_names'])

#the 178 data points in each of the 13 groups of data, formatted as a 150x13 array
print('Print data points: \n', wine['data'][:2])

#names of the target data (the 3 wine cultivators)
print('Print the names of the 3 wine cultivators: \n', wine['target_names'])

#which group each data point is in (0, 1 or 2)
print('Print in which group each data point belongs: \n', wine['target'])

#the groups of data can be plotted against each other or against the target group as follows:
import matplotlib.pyplot as plt

#scatter plot
plt.scatter(wine['data'][:, 0], wine['data'][:, 9], c=wine['target'])
plt.title('Wine recognition dataset')
plt.xlabel(wine['feature_names'][0])
plt.ylabel(wine['feature_names'][9])
plt.show()

#the data is much easier to work with if it is converted into a data frame:
import pandas as pd

#extract the data
data = pd.DataFrame(wine['data'], columns=wine['feature_names'])
#extract the target
target = pd.DataFrame(wine['target'], columns=['cultivator'])
#combine into one dataset
df = pd.concat([target, data], axis='columns')

#plot dataframe converted
plt.scatter(df['hue'], df['malic_acid'], c=df['cultivator'])
plt.title('Wine recognition dataset [scatter plot]')
plt.xlabel('hue')
plt.ylabel('malic_acid')
plt.show()


#original source code and data: rowannicholls.github.io
