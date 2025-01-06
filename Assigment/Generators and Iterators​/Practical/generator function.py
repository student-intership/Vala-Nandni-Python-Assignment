def even_numbers():
    num = 2
    for _ in range(10):
        yield num
        num += 2

# Using the generator
for even in even_numbers():
    print(even)
