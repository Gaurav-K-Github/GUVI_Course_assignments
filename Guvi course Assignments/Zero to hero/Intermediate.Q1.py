# You are required to write a Python program to merge two dictionaries into a new dictionary.

# Input:

# The input will consist of two dictionaries, each containing distinct keys.

# Output:

# Return a new dictionary that contains all the key-value pairs from both input dictionaries.

# Sample Input:

# {'a': 1, 'b': 2}

# {'c': 3, 'd': 4}

# Sample Output:

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#==============================================================================================
# -----------
# Source code:
# -----------

def merge_dicts(dict1, dict2):
  # Creating a new dictionary by merging the input dictionaries
  merged_dict = {**dict1, **dict2}
  return merged_dict

# Taking input for the first dictionary
dict1_input = input()
dict1 = eval(dict1_input)

# Taking input for the second dictionary
dict2_input = input()
dict2 = eval(dict2_input)

# Calling the function and printing the result
result = merge_dicts(dict1, dict2)
print(result)
