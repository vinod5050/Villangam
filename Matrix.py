### Multi dimentional array
from numpy import *
### Array conversion
arr = array([
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,9]
])
print(arr)
print(arr.dtype) # type
print(arr.ndim) # no of dimension
print(arr.shape) # rows, columns
print(arr.size) # no of values
arr1 = arr.flatten() # convert to 1D array with all values from multi dimensional array
print(arr1)
arr3 = arr.reshape(2,6) # reshape the 2D
arr4 = arr1.reshape(2,6) # convert 1D to 2D
arr5 = arr.reshape(2,2,3) # 2D to 3D
print(arr3)
print(arr4)
print(arr5)
#########################################################################################################
### Matrix

m = matrix(arr)
print(m.max())