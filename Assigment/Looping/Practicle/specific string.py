List1 = ['Apple', 'Banana', 'Mango']

# Get user input
s = input("Enter String: ")

# Use a for loop to iterate through the list
for i in List1:
    if i.lower() == s.lower():  # Compare case-insensitively
        print(f"'{s}' is True!!")  # If found, print True
        break  # Exit the loop once the item is found
else:
    # If the loop completes without finding the item
    print(f"'{s}' is False!!")
