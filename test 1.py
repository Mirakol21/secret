import numpy as np
from numpy import random

print("--- PART A: Array Creation and Basic Operations ---")
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(type(arr1))

arr3 = np.array((7, 8, 9, 10))

print("\n--- PART B: Indexing and Slicing ---")
a = np.array([5, 10, 15, 20, 25, 30, 35])
print(a[0])
print(a[3])
print(a[2] + a[4])
print(a[1:5])
print(a[:4])

print("\n--- PART C: Data Type, Copy, and View ---")
b = np.array([1, 2, 3, 4])
print(b.dtype)

b_copy = b.copy()
b[0] = 99
print("Original b:", b)
print("Copy of b:", b_copy)

c = np.array([1, 2, 3, 4])
c_view = c.view()
c_view[0] = 88
print("Original c:", c)
print("View of c:", c_view)

print("\n--- PART D: Shape and Reshape ---")
d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(d.shape)

arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_4x3 = arr_1d.reshape(4, 3)
print(arr_4x3)

arr_2x3x2 = arr_1d.reshape(2, 3, 2)
print(arr_2x3x2)

arr_nd = np.array([1, 2, 3, 4], ndmin=5)
print(arr_nd.shape)

print("\n--- PART E: Iteration ---")
e = np.array([2, 4, 6])
for x in e:
    print(x)

f = np.array([[1, 2], [3, 4]])
for x in f:
    for y in x:
        print(y)

g = np.array([10, 20, 30])
for idx, x in np.ndenumerate(g):
    print(idx, x)

print("\n--- PART F: Joining and Splitting Arrays ---")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

joined = np.concatenate((x, y))
print(joined)

stacked = np.stack((x, y), axis=1)
print(stacked)

vstacked = np.vstack((x, y))
print(vstacked)

arr_to_split = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.array_split(arr_to_split, 3)
print(split_arr)

print("\n--- PART G: Searching, Sorting, and Filtering ---")
h = np.array([1, 4, 2, 4, 5, 4])
indexes = np.where(h == 4)
print(indexes)

i = np.array([9, 3, 7, 1])
print(np.sort(i))

j = np.array([1, 2, 3, 4, 5, 6, 7, 8])
filter_arr = j % 2 == 0
even_nums = j[filter_arr]
print(even_nums)

print("\n--- PART H: Random and Vectorized Computation ---")
rand_ints = random.randint(100, size=(5))
print(rand_ints)

rand_val = random.choice([3, 5, 7, 9])
print(rand_val)

p = np.array([10, 20, 30])
q = np.array([1, 2, 3])
summed_arr = np.add(p, q)
print(summed_arr)