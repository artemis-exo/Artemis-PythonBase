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

#Airthematic Operations
import numpy as np
arrr=np.array([[1,2,3],[4,5,6]])
print(arrr+5)
print(arrr*5)
print(arrr**5)

# Aggregation Functions - Summarize , Average or Highest product
import numpy as np
num=np.array([1,2,3,4,5])
# 1. Sum
print(np.sum(num))
print(num.sum())
# 2. Mean
print(np.mean(num))
print(num.mean())
# 3. Min
print(np.min(num))
print(num.min())
# 4. Max
print(np.max(num))
print(num.max())
# 5. Standard Deviation
print(np.std(num))
print(num.std())
# 6. Median
print(np.median(num))

# INDEXING AND SLICING
'''
Numpy uses 0 based indexing
It has both Positive and Negative Indexing
array[index]- for 1D array
array[row,column]- for 2D array
'''
import numpy as np
arre=np.array([1,2,3,4,5,6,7])
print(arre[0])
print(arre[1])
print(arre[-1])

'''
Slicing is extracting a SubArray from a Parent array
array[start:end:step]- Syntax , start to end-1
negative step, -1 reverse
In this stop pointer is excluded
'''
import numpy as np
aero=np.array([1,2,3,4,5,6,7])
print(aero[1:5])
print(aero[:4])
print(aero[::2])
print(aero[::-1])

# FANCY INDEXING
'''
selecting multiple elements at once
It only modifies the copy of the array not the original Data 
'''

import numpy as np
aeroo=np.array([1,2,3,4,5,6,7])
print(aeroo[[0,2,4]])

# BOOLEAN MASKING
'''
Filter elements on the basis of the specified condition 
'''
import numpy as np
aric=np.array([33,4,514,14,5677,5,12,34,5,44,545,55,4,66,7,5,23,325,325,5,353,5535,235,3])
print(aric[aric>14])

# RESHAPING AND MANIPULATING
'''
Changing the dimensions of an Array without modifying the data
To convert 1D array to 2D array without changing its data
arr.reshape()
reshape(rows,cols) specify new shape
can only reshape if the dimensions match

Reshaping does not create copy it returns a view
'''
# 1. Reshaping
import numpy as np
amm=np.array([1,2,3,4,5,6])
reshape_Arr=amm.reshape(3,2)
print(reshape_Arr)

# 2. Flattening Array
'''
It is used when we need to convert the Multidimensional array into 1D array
.ravel() -> returns views
.flatten() -> returns copy
'''
import numpy as np
amero=np.array([[1,2,3],[4,5,6]])
print(amero.ravel())
print(amero.flatten())

# ARRAY MODIFICATION
'''
Insert - np.insert(array, index,axis=None)
array - original array
index -
value -
axis - if it is none then it is inserted into a flattened array 
axis = 0, row-wise 
1 column wise
'''
# For 1D array
import numpy as np
aex=np.array([10,20,30,40,50,60,70])
print(aex)
new_arr=np.insert(aex,4,45)
print(new_arr)

# For 2D array
import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d)
# Inserting a new row at index 1
new_arr2D=np.insert(arr_2d,1,[7,8,9], axis=0)
print(new_arr2D)
# Inserting a new column at index 1
newie=np.array([[10,20,30],[40,50,60]])
print(newie)
newiw_2D=np.insert(newie,1,[14,18],axis=1)
print(newiw_2D)

# Append Function
'''
np.concatenate((ar1,ar2),axis=None))
axis 0> vertical stacking
axis 1> horizontal stacking
'''
import numpy as np
arr=np.array([10,20,30])
aww=np.array([40,50,60])
new=np.concatenate((arr,aww))
print(new)
neck=np.concatenate((arr,aww,arr),axis=0)
print(neck)

# Removing Elements of array
'''
np.delete(array, index, axis=None)
flatten array
'''
# For 1D array
rel=np.array([10,20,30,40,50,60])
print(rel)
new_del=np.delete(rel,0,axis=0)
print(new_del)

# For 2D array
am=np.array([[1,2,3],[4,5,6]])
print(am)
new_arr=np.delete(am,0,axis=0)
print(new_arr)

# Stacking
'''
vertically
horizontally

vstack() -> row wise stacking
hstack() -> column wise stacking
'''
# Vertical Stacking and Horizontal Stacking
import numpy as np
acv=np.array([1,2,3])
acb=np.array([4,5,6])
print(np.vstack((acv,acb)))
print(np.hstack((acv,acb)))

# Spilting
'''
np.split()
equal

np.vsplit()
np.hsplit()
'''
import numpy as np
awp=np.array([10,20,30,40,50,60])
print(np.split(awp,3))

# BROADCASTING AND VECTORIZATION
'''
1. Broadcasting - It is a mechanism that allows this to happen even when arrays have different shapes. To perform mathematical operations on arrays
It is a Numpy way by which we can perform different mathematical operations without using loops
Performs very fast mathematical opertions

It expands smaller arrays to larger to match

Can expand and reshape the 1D array to 2D array

Rules
1. Matching Dimensions -> [1,2,3] + [4,5,6] =[5,7,9]
2. Expanding single elements -> [1,2,3] + 10 =[11,12,13]
3. Incompatible Shapes -> [1,2,3]+[1,2]= will throw an error
 can reshape it to overcome the 3 pointer

'''
prices=[100,200,300,400,500]
discount=10 # 10%

final_prices=[]
for price in prices:
    final_price=price-(price*discount/100)
    final_prices.append(final_price)
print(final_prices)

import numpy as np
prim=np.array([100,200,300,400,500])
discount=15
final_prim=prim-(prim*discount/100)
print(final_prim)

mul=prim*2
print(mul)

# How Numpy handles arrays of different shapes
import numpy as np
matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([10,20,30]) # 1D Array
rem=matrix+vector
print(rem)

'''
2. Vectorization is the process of performing an operation on entire array at once, rather than element by element
   in a loop.
   
   Works on entire array , 100x faster than loops
   
   works on matrix operations
'''

list1=[1,2,3]
list2=[4,5,6]
rwk=[x+y for x,y in zip(list1,list2)]
print(rwk)

import numpy as np
sem=np.array([1,2,3])
tem=np.array([4,5,6])
yem=sem+tem
print(yem)

mem= yem*4
print(mem)

# HANDLING MISSING VALUES
'''
It provides built -in functions to overcome the Missing Values
np.isnan() - detects missing values
Nan means - not a number 
np.isinf() - detects infinite values() - 
np.isneginf()
'''

# Isnan Function
import numpy as np
awx=np.array([1,2,3,np.nan,5,np.nan])
print(np.isnan(awx))

#np.nan_to_num(array,nan=value) default -0
import numpy as np
ayu=np.array([1,2,3,np.nan,5,np.nan])
cleaned_arr=np.nan_to_num(ayu)
print(cleaned_arr)
reves=np.nan_to_num(ayu,nan=64)
print(reves)

# Isinf function
import numpy as np
acv=np.array([1,2,3,np.inf,5,-np.inf])
print(np.isinf(acv))

#np.nan_to_num(array,posinf=1000,neginf=-1000)
import numpy as np
huc=np.array([1,2,3,np.inf,5,-np.inf])
print(np.isinf(huc))
cleano=np.nan_to_num(huc,posinf=1000,neginf=-1000)
print(cleano)

































