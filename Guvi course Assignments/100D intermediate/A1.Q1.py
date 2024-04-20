# Write a program that takes a list of names as input and sorts them in alphabetical order using a sorting algorithm of your choice.

# Input:

# The input consists of an integer n (1 <= n <= 1000) representing the number of names in the list, followed by n lines each containing a name. Each name consists of at most 100 characters and contains only uppercase and lowercase English letters.

# Output:

# Output the sorted list of names in alphabetical order, one name per line.

# Sample Input:

# 3
# John
# Alice
# Bob

# Sample Output:

# Alice
# Bob
# John

#==============================================================================================
# -----------
# Source code:
# -----------

def sort_names(names):
  # Sort the list of names in alphabetical order
  sorted_names = sorted(names)
  return sorted_names

# Taking input for the number of names
n = int(input())

# Taking input for the list of names
names = [input() for _ in range(n)]

# Calling the function to sort the names
sorted_names = sort_names(names)

# Printing the sorted list of names
for name in sorted_names:
  print(name)
