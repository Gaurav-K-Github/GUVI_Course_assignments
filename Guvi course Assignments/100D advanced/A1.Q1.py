# You are required to implement a Python class called Calculator with methods for addition, subtraction, multiplication, and division.

# Input:

# The input consists of two integers representing the operands for the calculator methods.

# Output:

# The output will be the result of the respective calculator operation.

# Sample Input:

# 3 5

# Sample Output:

# 8
# -2
# 15
# 0.6


#==============================================================================================
# -----------
# Source code:
# -----------

class Calculator:

  def add(self, a, b):
      return a + b

  def subtract(self, a, b):
      return a - b

  def multiply(self, a, b):
      return a * b

  def divide(self, a, b):
      if b == 0:
          raise ValueError("Cannot divide by zero")
      return a / b

# Create an instance of Calculator
calc = Calculator()

# Get user inputs for operands
try:
  a, b = map(int, input().split())
except ValueError:
  print("Please enter two integers separated by a space.")
  exit()

# Addition
result_add = calc.add(a, b)
print(result_add)

# Subtraction
result_subtract = calc.subtract(a, b)
print(result_subtract)

# Multiplication
result_multiply = calc.multiply(a, b)
print(result_multiply)

# Division
try:
  result_divide = calc.divide(a, b)
  print(result_divide)
except ValueError as e:
  print(e)

