# You are required to create a Python function to extract all occurrences of a specific pattern (e.g., dates in the format MM/DD/YYYY) from a given text using regular expressions and quantifiers.

# Input:

# The input will consist of a string representing the text.

# Output:

# Return a list containing all occurrences of the specified pattern found in the text.

# Sample Input:

# Today is 03/26/2024 and tomorrow is 03/27/2024.

# Sample Output:

# 03/26/2024, 03/27/2024

#==============================================================================================
# -----------
# Source code:
# -----------

import re

def extract_dates(text):
    # Define the pattern for MM/DD/YYYY date format
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'

    # Find all occurrences of the pattern in the text
    dates = re.findall(pattern, text)

    return dates

# Taking input for the text
text = input()

# Calling the function and printing the result
result = extract_dates(text)
print(', '.join(result))
