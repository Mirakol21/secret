Part A

1. Import NumPy using the alias np
import numpy as np

2. Create a 1-D NumPy array named arr1 containing 10, 20, 30, 40, 50.
arr1 = np.array([10, 20, 30, 40, 50])

3. Create a 2-D NumPy array named arr2 with the values [[1, 2, 3], [4, 5, 6]].
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

4. Print the type of arr1.
print(type(arr1))

5. Create an array from the tuple (7, 8, 9, 10) and store it in arr3.
arr3 = np.array((7, 8, 9, 10))

Part B. Indexing and Slicing

6. Use a = np.array([5, 10, 15, 20, 25, 30, 35]). Print the first element.
a = np.array([5, 10, 15, 20, 25, 30, 35])
print(a[0])

7. Using the same array a, print the fourth element.
print(a[3])
    
8. Using the same array a, print the sum of the third and fifth elements.
print(a[2] + a[4])
    
9. Using the same array a, slice elements from index 1 to index 5.
print(a[1:5])
    
10. Using the same array a, slice elements from the beginning up to index 4.
print(a[:4])
    
Part C. Data Type, Copy, and View
11. Create an array b = np.array([1, 2, 3, 4]) and print its dtype.
b = np.array([1, 2, 3, 4])
print(b.dtype)

12. Make a copy of b, change b[0] = 99, then print both arrays.
copy_b = b.copy()
b[0] = 99
print(b)
print(copy_b)

13. Make a view of c = np.array([1, 2, 3, 4]), change the view's first value to 88, then print
both arrays.
c = np.array([1, 2, 3, 4])
view_c = c.view()
view_c[0] = 88
print(c)
print(view_c)

Part D. Shape and Reshape

14. Create d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) and print its shape.
d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(d.shape)

15. Create a 1-D array with values from 1 to 12, then reshape it into a 4 x 3 array.
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshaped_arr = arr_1d.reshape(4, 3)

16. Reshape the same 1-D array into a 2 x 3 x 2 array.
reshaped_arr_3d = arr_1d.reshape(2, 3, 2)

17. Create an array with ndmin=5 using [1, 2, 3, 4] and print its shape.
arr_ndmin = np.array([1, 2, 3, 4], ndmin=5)
print(arr_ndmin.shape)

Part E. Iteration

18. Iterate through e = np.array([2, 4, 6]) and print each value.
e = np.array([2, 4, 6])
for x in e:
print(x)

19. Iterate through f = np.array([[1, 2], [3, 4]]) and print each scalar value.
f = np.array([[1, 2], [3, 4]])
for x in f:
for y in x:
print(y)

20. Use np.ndenumerate() to print the index and value of each element in g = np.array([10,
20, 30]).

g = np.array([10, 20, 30])
for idx, x in np.ndenumerate(g):
 print(idx, x)
Part F. Joining and Splitting Arrays

21. Using x = np.array([1, 2, 3]) and y = np.array([4, 5, 6]), join x and y using
np.concatenate().
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
joined_arr = np.concatenate((x, y))

22. Using x and y, stack them column-wise using np.stack(..., axis=1).
stacked_col = np.stack((x, y), axis=1)

23. Use np.vstack() on x and y.
stacked_v = np.vstack((x, y))

24. Split np.array([1, 2, 3, 4, 5, 6]) into 3 parts using np.array_split().
arr_to_split = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.array_split(arr_to_split, 3)
Part G. Searching, Sorting, and Filtering

25. Use np.where() to find the indexes of value 4 in h = np.array([1, 4, 2, 4, 5, 4]).
h = np.array([1, 4, 2, 4, 5, 4])
indexes = np.where(h == 4)
print(indexes)

26. Sort i = np.array([9, 3, 7, 1]) in ascending order.
i = np.array([9, 3, 7, 1])
sorted_i = np.sort(i)
print(sorted_i)

27. Filter and print only the even numbers from j = np.array([1, 2, 3, 4, 5, 6, 7, 8]).
j = np.array([1, 2, 3, 4, 5, 6, 7, 8])
filter_even = j % 2 == 0
even_nums = j[filter_even]
print(even_nums)

Part H. Random and Vectorized Computation

28. Generate a 1-D array of 5 random integers from 0 to 99.
from numpy import random
random_ints = random.randint(100, size=(5))

29. Generate one random value from [3, 5, 7, 9] using random.choice().
random_val = random.choice([3, 5, 7, 9])

30. Add p = np.array([10, 20, 30]) and q = np.array([1, 2, 3]) using np.add().
p = np.array([10, 20, 30])
q = np.array([1, 2, 3])
sum_pq = np.add(p, q) 
