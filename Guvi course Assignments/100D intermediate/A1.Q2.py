# Implement a function that takes a list of integers as input and returns the sum of the list. Handle the TypeError exception if a non-integer value is encountered.

# Input:

# The input consists of a list of integers.

# Output:

# Return an integer representing the sum of the list.

# Sample Input:

# 1 2 3 4 5

# Sample Output:

# 15

#==============================================================================================

# -----------
# Source code:
# -----------

def sum_list(numbers):
  total = 0
  for num in numbers:
      try:
          total += num
      except TypeError:
          # Handle the TypeError exception
          return "Invalid input: Non-integer value found"
  return total

# Taking input for the list of integers
numbers = list(map(int, input().split()))

# Calling the function and printing the result
result = sum_list(numbers)
print(result)
