# You are given a list of integers. Implement a function, remove_duplicates(lst: str) -> str, that removes duplicates from the list while preserving the order of elements. Your function should return a new list with duplicates removed, represented as a comma-separated string.

# Input:

# A string representing a list of integers separated by commas.

# Output:

# A string representing a list of integers with duplicates removed, separated by commas.

# Sample Input:

# 1,2,3,3,4,5,6,6,7

# Sample Output:

# 1,2,3,4,5,6,7

#==============================================================================================
# -----------
# Source code:
# -----------


def remove_duplicates(lst_str):
  # Convert the input string to a list of integers
  lst = list(map(int, lst_str.split(',')))

  # Initialize an empty set to store unique elements
  unique_elements = set()

  # Initialize an empty list to store elements in order
  result = []

  # Iterate through the list and add non-duplicate elements to the result list
  for num in lst:
      if num not in unique_elements:
          result.append(num)
          unique_elements.add(num)

  # Convert the result list to a comma-separated string
  result_str = ','.join(map(str, result))

  return result_str

# Taking input for the list of integers
lst_str = input()

# Calling the function and printing the result
result = remove_duplicates(lst_str)
print(result)
