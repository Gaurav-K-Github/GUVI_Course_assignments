# You are given a list of integers. Perform the following operations on the NumPy arrays:
# Create a NumPy array from the given list.
# Print the shape of the array.
# Transpose the array.
# Print the sum of the elements in each row.
# Print the minimum element in the array.

# Input:

# The input consists of the following:

# An integer n (1 <= n <= 100) representing the size of the list. n space-separated integers representing the elements of the list.

# Output:

# Output the results of the operations as described below.

# Shape of array
# Transposed array
# Sum of elements in each row
# Minimum element in the array

# Sample Input:

# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Sample Output:

# (3, 3)
# [[1 4 7]
# [2 5 8]
# [3 6 9]]
# [ 6 15 24]
# 1
#==============================================================================================

# -----------
# Source code:
# -----------
import numpy as np

def process_array(input_array):
    # Shape of array
    shape = np.shape(input_array)
    print(shape)

    # Transposed array
    transposed = np.transpose(input_array)
    print(transposed)

    # Sum of elements in each row
    row_sums = np.sum(input_array, axis=1)
    print(row_sums)

    # Minimum element in the array
    min_element = np.min(input_array)
    print(min_element)

# Read input
n = int(input())
input_array = []
for _ in range(n):
    row = list(map(int, input().split()))
    input_array.append(row)

# Convert to numpy array
input_array = np.array(input_array)

# Process and print results
process_array(input_array)
