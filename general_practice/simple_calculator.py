
print("Operations")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

choice = int(input("Enter which operation: "))

if choice==1:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    sum = num1 + num2

    print("Sumassion of",num1,"and",num2,"is",sum)
elif choice==2:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    diff = num1 - num2

    print("Difference of",num1,"and",num2,"is",diff)
elif choice==3:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    mul = num1 * num2

    print("Multification of",num1,"and",num2,"is",mul)
else:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if num2==0:
        print("The result is infinite!")
    else:
        div = num1/num2
        print("Division of",num1,"and","is",div)
