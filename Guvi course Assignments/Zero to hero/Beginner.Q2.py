# Write a Python program to calculate the factorial of a given number using a loop.

# Input:

# An integer n (0 ≤ n ≤ 100).

# Output:

# Return the factorial of n.

# Sample Input:

# 5

# Sample Output:

# 120

#==============================================================================================
# -----------
# Source code:
# -----------

def factorial(n):
  if n < 0 or n > 100:
      return "Invalid input: n should be between 0 and 100 inclusive."

  result = 1
  for i in range(1, n + 1):
      result *= i
  return result

# Input
n = int(input())

# Calculate factorial
result = factorial(n)

# Output
print(result)
