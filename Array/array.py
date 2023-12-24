import array

my_array= array.array('i') # Time complexity - O(1)
print(my_array)

my_array1 = array.array("i", [1,2,3,4,5])
print(my_array1)

import numpy as np
np_array= np.array([],dtype=int) # Time complexity - O(1)
print(np_array)

np_array1= np.array([1.1j,2,3,4,5]) # Time complexity - O(N)
print(np_array1)