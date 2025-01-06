numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_odd(num):
    return num % 2 != 0

odd_numbers = filter(is_odd, numbers)

print("Original List:", numbers)
print("Filtered List (Odd Numbers):", list(odd_numbers))
