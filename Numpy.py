import numpy as np
temps=([38.9,44.4,33.6,40.5,48.9])
avg=np.mean(temps)
print(avg)

'''
1.It is the library of python which allows us to handle the large amount of data
using arrays
2.No loops faster calculation , can access large set of data

Features of Numpy 
1.Speed 50-100 times faster than normal list.
2.Consumes Less Memory 
3.Easy Math Operations 

'''

# List vs Numpy

list=[1,2,3,4,5]
print(list)  # It is comma separated

import numpy as np
numpy_array = np.array([1,2,3,4,5])
print(numpy_array)  # It is not

# 1D Array
import numpy as np
ar_1 = np.array([1,2,3,4,5,6,7,8,9])
print(ar_1)

# 2D Array
import numpy as np
ar_2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(ar_2)

# Multidimensional Array
import numpy as np
arr_md=np.array([[2,4,6],
                 [8,10,12]])
print(arr_md)

# With default values
# np.zeroes(shape) (3) then id, (3,3) 2d

import numpy as np
zeroes_array=np.zeros(3)
print(zeroes_array)

# For ones value
import numpy as np
ones_array=np.ones((2,3))
print(ones_array)

# For Specific value use Full Function
# full(shape,value)

import numpy as np
fill_array=np.full((3,3),5)
print(fill_array)

# For creating sequences of numbers in numpy array
# arange() function
# arange(start,stop,step)

import numpy as np
arr=np.arange(0,10,2)
print(arr)

# Creating Identity Matrices
# eye(size)
import numpy as np
iden_matrix=np.eye(6)
print(iden_matrix)

# Shape Attribute - Means row and column of the matrix , Arrays
import numpy as np
arr_4d=np.array([[1,2,3],
                 [4,5,6]])
print(arr_4d.shape)

arr_1=np.array([1,2,3])
arr_2=np.array([[1,2,3],[4,5,6]])
arr_3=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr_1.shape)
print(arr_2.shape)
print(arr_3.shape)


# Size Attribute - Means it returns the size of or the number of elements in array
import numpy as np
arr=np.array([34,5,25,52,55,2,5,424,25,425,6,7,55,5,125,5,125,25,54])
arr1=np.array([[0,10,2,4,6,8,3,85],[66,53,65,3,55,53,55,5]])
print(arr.size)
print(arr1.size)

# Ndim Attribute - Means it checks the Number of dimensions of the array
import numpy as np
arr_1d=np.array([1,2,3])
arr_2d=np.array([[1,2,3],[4,5,6]])
arr_3d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

# Dtype - To check and return  the data type of elements
import numpy as np
data=np.array([3,245,35,78.78])
print(data.dtype)

# AStype - To change the data type to another data type
import numpy as np
conv=np.array([1.4,6.8,4.6])
int_arr=conv.astype(int)
print(int_arr)
print(int_arr.dtype)






