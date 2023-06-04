#pip install mlxtend
from mlxtend.data import iris_data
from mlxtend.preprocessing import standardize
from mlxtend.feature_extraction import 

#loading data
X, y = iris_data()
#standardizing the features
X = standardize(X)

#dimensionality reduction
lda = LinearDiscriminantAnalysis(n_discriminants=2)
lda.fit(X,y)
X_lda = lda.transform(X)

print('X_lda: \n', X_lda)

import matplotlib.pyplot as plt

with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(9, 3))
    for lab, col in zip((0, 1, 2),
                        ('blue', 'red', 'green')):
        plt.scatter(X_lda[y == lab, 0],
                    X_lda[y == lab, 1],
                    label=lab,
                    c=col)
    plt.xlabel('Linear Discriminant 1')
    plt.ylabel('Linear Discriminant 2')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
