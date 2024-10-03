
print("\n***** LAST DIGIT DIVISIBLE BY 3 CHECKING PROGRAM *****\n")

num = int(input("Enter a number: "))

remainder = num % 10
print("Last digit of",num,"is",str(remainder)+".")

if remainder % 3 == 0:
    print(remainder,"is divisible by 3.")
else:
    print(remainder,"is not divisible by 3.")