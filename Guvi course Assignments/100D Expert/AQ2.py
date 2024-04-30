# You are required to implement a Python program to handle HTTP methods: GET, POST, PUT, and DELETE. Your program should perform different actions based on the HTTP method received.

# Input:

# The input consists of the following:

# HTTP method (GET, POST, PUT, or DELETE).
# Data payload (for POST and PUT methods).

# Output:

# The output is the result of the action performed based on the HTTP method:

# For GET method: Print "Requested resource data"
# For POST method: Print "Resource created successfully: {payload}"
# For PUT method: Print "Resource updated successfully: {payload}"
# For DELETE method: Print "Resource deleted successfully"

# Sample Input:

# POST
# {"name": "John", "age": 25}

# Sample Output:

# Resource created successfully: {"name": "John", "age": 25}

#==============================================================================================

# -----------
# Source code:
# -----------

def process_http_request(method, payload=None):
  if method == "GET":
      print("Requested resource data")
  elif method == "POST":
      print("Resource created successfully:", payload)
  elif method == "PUT":
      print("Resource updated successfully:", payload)
  elif method == "DELETE":
      print("Resource deleted successfully")
  else:
      print("Invalid HTTP method")

# Read input
method = input().strip()
payload = None

# For POST and PUT methods, read the payload
if method in ["POST", "PUT"]:
  payload = input().strip()

# Process and print the result
process_http_request(method, payload)
