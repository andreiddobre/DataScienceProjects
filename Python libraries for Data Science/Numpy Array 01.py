#pip install numpy

import numpy as np

#basic numpy 'array' creation routine
first_numpy_array  = np.array([1,2,3,4])
print('First numpy array\n', first_numpy_array)

#'array' manipulation routine using 'zeros' and 'empty'
array_with_zeros = np.zeros((3,3))
array_with_empty = np.empty((2,3))
print('Array with zeros\n', array_with_zeros)
print('Array with empty\n', array_with_empty)

#numpy 'arange' creation routine and 'reshape' manipulation routine
np_arrange = np.arange(12)
print('NumPy arrange\n', np_arrange)
print('NumPy arrange reshape\n', np_arrange.reshape(3,4))

#numpy 'linspace' creation routine
np_linespace = np.linspace(1,6,5)
print('NumPy linespace\n', np_linespace)

#One dimension 'arange' creation routine
oneD_array = np.arange(18)
print('1D array\n', oneD_array)

#Two dimensional 'reshape' manipulation routine
TwoD_array = oneD_array.reshape(2,9)
print('2D array\n', TwoD_array)

#Three dimensional 'reshape' manipulation routine
ThreeD_array = np.arange(36).reshape(3,3,4)
print('3D array\n', ThreeD_array)
