age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in kg): "))

if age >= 18:  # Outer condition: Age must be at least 18
    if weight >= 50:  # Inner condition: Weight must be at least 50 kg
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood because your weight is less than 50 kg.")
else:
    print("You are not eligible to donate blood because you are under 18 years of age.")
