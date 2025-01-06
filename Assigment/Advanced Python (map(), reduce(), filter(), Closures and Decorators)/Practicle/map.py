def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

print("Original List:", numbers)
print("Squared List:", list(squared_numbers))
