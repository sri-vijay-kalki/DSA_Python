import array

my_array= array.array('i') # Time complexity - O(1)
print(my_array)

my_array1 = array.array("i", [1,2,3,4,5])
print(my_array1)


my_array1.insert(0,6) #inser will not overide the position
print(my_array1)
my_array1.remove(1) # remove the element with value 1
# In array module we don't have  a method to remove the element at a specific index


def traverseArray(arr):
    for i in arr:
        print(i)


traverseArray(my_array1)

def linear_search (arr, target):
    for i in range (len (arr)): #time complexity of len(arr) is O(1)
        # range time complexity is O(1) as it create a iterator.
        if arr[i] == target:
            return i
    return -1

print("leaner search result = ",linear_search (my_array1, 8))




import numpy as np
np_array= np.array([],dtype=int) # Time complexity - O(1)
print(np_array)

np_array1= np.array([1.1j,2,3,4,5]) # Time complexity - O(N)
print(np_array1)