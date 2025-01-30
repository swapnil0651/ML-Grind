import numpy as np
arr1=np.array([1,2,3,4,5])
#print (arr1)
#rint(type(arr1))
#print(dir(np))
arr2=np.array([
    [1,2],
    [3,4]])
#print(arr2)
#print(type(arr2))
zarr=np.zeros((3,4))
#print(zarr)
one_arr=np.ones((3,4))
#print(one_arr)
rand_arr=np.random.randint((2,2))
#print(rand_arr)
arr3=np.array([
    [1,2],
    [3,4]
])
arr4=np.array([
    [5,6],
    [7,8]
])
print(arr3+arr4) #simple add and multi
print(arr3*arr4)
dotprod=np.dot(arr3,arr4) #for dot product
print (dotprod)
print(arr3.T) #to print transpose
print(np.sqrt(arr3)) #for square root
print(np.argmax(arr4)) #print the index of the largest number