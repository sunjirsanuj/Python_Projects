
print("\n***** AGE TESTING PROGRAM *****\n")

age = int(input("Enter your age: "))

ageGap = 18 - age

if age >= 18:
    print("You are old enough to drive.")
else:
    print("You need",ageGap,"more years to learn to drive.")