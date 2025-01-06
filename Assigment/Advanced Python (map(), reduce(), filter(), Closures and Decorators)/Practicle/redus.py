from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Use reduce() to calculate the product of the list
product = reduce(multiply, numbers)

print("Original List:", numbers)
print("Product of List:", product)
