# You are required to create a Python class to represent a bank account, and use the assert statement to ensure that the initial balance is non-negative.

# Input:

# The input will consist of a single integer representing the initial balance of the bank account.

# Output:

# The output will be either "Assertion Error" if the initial balance is negative, or "Assertion Passed" if the initial balance is non-negative.

# Sample Input:

# 1000

# Sample Output:

# Assertion Passed

#==============================================================================================
# -----------
# Source code:
# -----------

class BankAccount:
  def __init__(self, initial_balance):
      self.assert_balance(initial_balance)
      self.balance = initial_balance

  def assert_balance(self, balance):
      assert balance >= 0, "Assertion Error"

# Taking input for initial balance
initial_balance = int(input())

# Creating an instance of BankAccount class
try:
  account = BankAccount(initial_balance)
  print("Assertion Passed")
except AssertionError as e:
  print(e)
