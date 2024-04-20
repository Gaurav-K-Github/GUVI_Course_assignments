# You are required to write a Python program to create a list of squares of numbers using list comprehension.

# Input:

# The input will consist of a single integer n (1 ≤ n ≤ 100), representing the number of elements in the list.

# Output:

# Return a list containing the squares of numbers from 1 to n, inclusive.

# Sample Input:

# 5

# Sample Output:

# 1, 4, 9, 16, 25

#==============================================================================================
# -----------
# Source code:
# -----------

def squares_list(n):
  # Using list comprehension to create a list of squares
  squares = [i*i for i in range(1, n+1)]
  return squares

# Taking input for the number of elements
n = int(input())

# Calling the function and printing the result
result = squares_list(n)
print(', '.join(map(str, result)))
