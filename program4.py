age = int(input("Enter your age: "))
if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Valid age and Eligible for voting")
else:
    print("Valid age but Not eligible for voting")