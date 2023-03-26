from sklearn.datasets import load_diabetes
from sklearn import datasets

#loading the dataset using "as_frame" parameter which causes the ‘data’ and ‘target’ values to be loaded as data frames inside the Bunch object
diabetes = datasets.load_diabetes(as_frame=True)
print('Dataset diabetes: \n', diabetes)
print(type(diabetes['data']))

#showing the dataset's keys
print(list(diabetes))

#describing the dataset
print(diabetes['DESCR'])

#locating the CSV file containing the data being imported
print(diabetes['data_filename'])

#locating the CSV file containing the target data being imported
print(diabetes['target_filename'])

#names of the 10 groups of data
print(diabetes['feature_names'])

import pandas as pd
import numpy as np

#creating the dataframe
df = pd.DataFrame(data = np.c_[diabetes['data'],diabetes['target']], columns = diabetes['feature_names']+['target'])
print('DataFrame \n', df)

#check for any missing values or outlier data in the dataframe
df.isnull().any()

#the target data, namely a quantitative measure of disease progression one year after baseline
print(diabetes['target'][:20])

import matplotlib.pyplot as plt

#boxplot for each column of the dataframe
for column in df:
    print('plt.fig', plt.figure())
    df.boxplot([column])
plt.show()

#don't plot the sex data
features = diabetes['feature_names']
features.remove('sex')
print('Don\'t plot the sex data: \n', features)

#plot
fig, axs = plt.subplots(3, 3)
fig.suptitle('Diabetes Dataset')
for i in range(3):
    for j in range(3):
        n = j + i * 3
        feature = features[n]
        axs[i, j].scatter(diabetes['data'][feature], diabetes['target'], s=1)
        axs[i, j].set_xlabel(feature)
        axs[i, j].set_ylabel('target')
plt.tight_layout()
plt.show()
