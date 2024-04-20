# Write a Python function to find the greatest common divisor (GCD) of two numbers.

# Input:

# Two integers num1 and num2 (-10^9 ≤ num1, num2 ≤ 10^9).

# Output:

# Return the greatest common divisor (GCD) of num1 and num2.

# Sample Input:

# 12 18

# Sample Output:

# 6

#==============================================================================================
# -----------
# Source code:
# -----------

def gcd(num1, num2):
  while num2:
      num1, num2 = num2, num1 % num2
  return abs(num1)

num1, num2 = map(int, input().split())

result = gcd(num1, num2)

print(result)
