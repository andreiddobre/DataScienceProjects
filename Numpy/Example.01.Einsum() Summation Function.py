#importing required modules
import numpy as np

#determining length of array
N,j=int(input("Enter size of arrays= ")),0

#for two matrices at a time
while(j<2):
  arrayy=[]
  for i in range(N):
    #taking user input of individual elements
    ele=int(input("Enter "+str(i+1)+"th element of the "+str(j+1)+"th array = "))
    arrayy.append(ele)
  if(j==0):
    #creating the first matrix
    arr1=np.array(arrayy)
  else:
    #creating the second matrix
    arr2=np.array(arrayy)
  j+=1

# Original arrays after taking user input
print("The first array or matrix is =",arr1)
print("The second array or matrix is =",arr2)

#calculating the einstein summation
result = np.einsum("n,n", arr1, arr2)

#displaying the einstein summation of the given arrays
print("The Einstein Summation is =", result)
