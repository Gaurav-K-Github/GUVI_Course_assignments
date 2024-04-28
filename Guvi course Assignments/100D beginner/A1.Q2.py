# You are given a string. Implement a function, is_palindrome(s: str) -> bool, to determine if the given string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. Your function should return True if the string is a palindrome, and False otherwise.

# Input:

# A string s containing a sequence of characters.

# Output:

# A boolean value indicating whether the input string is a palindrome or not.

# Sample Input:

# racecar

# Sample Output:

# True
  
#==============================================================================================

# -----------
# Source code:
# -----------
def is_palindrome(s):
  # Clean the string by removing spaces and punctuation, and converting to lowercase
  cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

  # Check if the cleaned string is equal to its reverse
  return cleaned_s == cleaned_s[::-1]

# Taking input for the string
s = input()

# Calling the function and printing the result
result = is_palindrome(s)
print(result)
