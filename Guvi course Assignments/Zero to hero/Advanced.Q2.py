# You are required to write a Python function to divide two numbers. Handle the ZeroDivisionError exception that may occur when the divisor is zero.

# Input:

# The input will consist of two integers, representing the dividend and divisor.

# Output:

# Return the result of dividing the dividend by the divisor. If the divisor is zero, handle the exception and return "Cannot divide by zero".

# Sample Input:

# 10 2

# Sample Output:

# 5.0

#==============================================================================================
# -----------
# Source code:
# -----------

def divide_numbers(dividend, divisor):
  try:
      # Attempt to divide the numbers
      result = dividend / divisor
      return result
  except ZeroDivisionError:
      # Handle the ZeroDivisionError exception
      return "Cannot divide by zero"

# Taking input for dividend and divisor
dividend, divisor = map(int, input().split())

# Calling the function and printing the result
result = divide_numbers(dividend, divisor)
print(result)
