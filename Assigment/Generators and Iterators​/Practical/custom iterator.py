class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # The iterator object returns itself

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration  # Stop iteration when the end is reached

# Using the custom iterator
integers = [10, 20, 30, 40]
custom_iter = CustomIterator(integers)

print("Iterating over the list:")
for number in custom_iter:
    print(number)
