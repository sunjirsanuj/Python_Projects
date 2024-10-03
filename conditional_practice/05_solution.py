
print("\n***** GREATER AND SMALLER NUMBER TESTING PROGRAM *****\n")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > b:
    print(a,"is greater than",b)
elif b > a:
    print(a,"is smaller than",b)
else:
    print(a,"is equal to",b)