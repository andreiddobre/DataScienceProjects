#pip install numpy

#importing required modules
import numpy as np

#creating the numpy arrays
arr1=np.arange(18,36,2).reshape(3,3)
arr2=np.arange(38,56,2).reshape(3,3)

#displaying the original arrays
print("The first array or matrix is =",arr1)
print("The second array or matrix is =",arr2)

#calculating the einstein summation
result = np.einsum("ij,jk", arr1, arr2)

#displaying the einstein summation of the given arrays
print("The Einstein Summation is =", result)
