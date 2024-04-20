# You are required to create a class to represent a rectangle with attributes like length and width. Write methods to calculate the area and perimeter of the rectangle.

# Input:

# The input will consist of two integers, representing the length and width of the rectangle, respectively.

# Output:

# For each method call, return the calculated area and perimeter of the rectangle.

# Sample Input:

# 5 3

# Sample Output:

# 15
# 16

#==============================================================================================
# -----------
# Source code:
# -----------

class Rectangle:
  def __init__(self, length, width):
      self.length = length
      self.width = width

  def calculate_area(self):
      # Calculate the area of the rectangle
      area = self.length * self.width
      return area

  def calculate_perimeter(self):
      # Calculate the perimeter of the rectangle
      perimeter = 2 * (self.length + self.width)
      return perimeter

# Taking input for length and width of the rectangle
length, width = map(int, input().split())

# Create an instance of Rectangle class
rectangle = Rectangle(length, width)

# Calculate and print the area
area = rectangle.calculate_area()
print(area)

# Calculate and print the perimeter
perimeter = rectangle.calculate_perimeter()
print(perimeter)
