#pip install sklearn
from sklearn.datasets import load_breast_cancer

#load the dataset
breast_cancer = load_breast_cancer()

#show the dataset's keys
print('Print dataset keys: \n', list(breast_cancer))

#description of the dataset
print('Print description of the dataset: \n', breast_cancer['DESCR'])

#location of the CSV file containing the data being imported
print('Print location of the CSV file: \n', breast_cancer['filename'])

#names of the 30 groups of data
print('Print names of the 30 groups of data: \n', breast_cancer['feature_names'])

#the 569 data points in each of the 30 groups of data, formatted as a 569x30 array
print('Print data points: \n', breast_cancer['data'][:2])

#names of the 2 categorisations (malignant and benign)
print('Print the names of the 2 categorisations: \n', breast_cancer['target_names'])

#which categorisation each data point is in (1 = malignant, 0 = benign)
print('Print in which categorisation each data point belongs: \n', breast_cancer['target'])

import matplotlib.pyplot as plt

#scatter plot
plt.scatter(breast_cancer['data'][:, 0], breast_cancer['data'][:, 8], c=breast_cancer['target'])
plt.title('Breast cancer wisconsin (diagnostic) dataset [scatter plot]')
plt.xlabel(breast_cancer['feature_names'][0])
plt.ylabel(breast_cancer['feature_names'][8])
plt.show()

#the data is much easier to work with if it is converted into a data frame:
import pandas as pd

#extract the data
data = pd.DataFrame(breast_cancer['data'], columns=breast_cancer['feature_names'])
#extract the target
target = pd.DataFrame(breast_cancer['target'], columns=['Categorisation'])
#combine into one dataset
df = pd.concat([target, data], axis='columns')

#plot dataframe converted
plt.scatter(df['mean area'], df['mean smoothness'], c=df['Categorisation'])
plt.title('Breast cancer wisconsin (diagnostic) dataset [dataframe converted]')
plt.xlabel('mean area')
plt.ylabel('mean smoothness')
plt.show()

#original source code and data: rowannicholls.github.io
