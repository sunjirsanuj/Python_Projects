
print("\n***** AGE TESTING PROGRAM *****\n")

my_age = 20
your_age = int(input("Enter your age: "))

if my_age == your_age:
    print("Wow! You and I at same age.")
elif your_age > my_age:
    ageGap = your_age - my_age

    if ageGap <= 1:
        print("You are one year older than me.")
    else:
        print("You are",ageGap,"years older than me.")
else:
    print("You are younger than me.")