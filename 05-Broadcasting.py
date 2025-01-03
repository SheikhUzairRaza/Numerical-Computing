import numpy as np

# Define a NumPy array 'arr' with values [1, 2, 3]
arr = np.array([1, 2, 3])
print(arr * 3)  # Element-wise multiplication of 'arr' by 3 

# In mathematics, x + 3 is not possible for a scalar x (without using an identity matrix).
# However, in NumPy, broadcasting makes this operation possible.

print(arr + 3)  # Broadcasting 3 over 'arr', resulting in [4, 5, 6]

# General rules for broadcasting:
# Two arrays are compatible if:
# -- their shapes are the same, or
# -- one of them has a dimension of size 1.

# Create a Rank-1 tensor 'arr1'
arr1 = np.arange(4)  # Generates array [0, 1, 2, 3]

# Reshape 'arr1' into a column vector 'arr1_col' (Rank-2 tensor)
arr1_col = arr1.reshape(4, 1)

# Create other arrays 'arr2' (Rank-1 tensor) and 'arr3' (Rank-2 tensor)
arr2 = np.ones(5)  # Array of five 1s
arr3 = np.ones((3, 4))  # 3x4 matrix of 1s

# Print arrays and their shapes
print("arr1 = ", arr1)
print("arr1_col = ", arr1_col)
print("arr2 = ", arr2)
print("arr3 = ", arr3)

print("Shapes: ")
print(arr1.shape)  # Shape of arr1 (4,)
print(arr1_col.shape)  # Shape of arr1_col (4, 1)
print(arr2.shape)  # Shape of arr2 (5,)
print(arr3.shape)  # Shape of arr3 (3, 4)

# Attempting to add arrays with incompatible shapes:
# arr1 has shape (4,) and arr2 has shape (5,)
# This results in an error as they can't be broadcasted together
# print(arr1 + arr2)  # Error: operands could not be broadcast together with shapes (4,) (5,)

# Broadcasting arr2 over arr1_col because arr1_col has second dimension 1
print(arr1_col + arr2)  # Result is a 4x5 array

# Shape of the result from broadcasting arr1_col and arr2
print((arr1_col + arr2).shape)  # Shape is (4, 5)

# Demonstrating broadcasting with a scalar (Rank-1 tensor of size 1)
print(np.array([1]) + arr2)  # Scalar array [1] is broadcasted over arr2

# Adding arr3 and arr1 (broadcasting happens because arr3 has shape (3, 4) and arr1 has shape (4,))
print(arr3 + arr1)  # Result is a 3x4 array

# Demonstrating broadcasting when dimensions match
arr4 = np.ones((3, 4))  # 3x4 matrix of ones
arr5 = np.ones(4)  # 1D array of 4 ones
print(arr4)
print(arr5)

# Adding arr4 and arr5 works because both have compatible shapes for broadcasting
print(arr4 + arr5)  # Broadcasting arr5 over each row of arr4

# Using a scalar in an operation with a matrix
arr6 = np.array([[0.0, 0.0, 0.0],
                 [10.0, 10.0, 10.0],
                 [20.0, 20.0, 20.0],
                 [30.0, 30.0, 30.0]])

arr7 = np.array([1.0, 2.0, 3.0])  # 1D array of 3 elements
print(arr7.shape)

# Broadcasting arr7 over arr6 (because arr6's shape is (4, 3) and arr7's shape is (3,))
print(arr6 + arr7)

# Reshaping arr7 into a 1x3 array 'arr7_reshaped' (making it a column vector)
arr7_reshaped = arr7.reshape(1, 3)
print(arr7_reshaped.shape)

# Adding arr6 and arr7_reshaped works due to broadcasting
print(arr6 + arr7_reshaped)

# Define two 1D arrays 'a' and 'b'
a = np.array([0.0, 0.0, 0.0, 0.0])
b = np.array([1.0, 2.0, 3.0])

# Reshape 'b' into a column vector 'b_reshaped'
b_reshaped = b.reshape(3, 1)

# Adding reshaped 'b' to 'a' works because 'b_reshaped' has shape (3, 1) and 'a' has shape (4,)
# Broadcasting occurs, and the result is an array with shape (3, 4)
print(b_reshaped + a)
