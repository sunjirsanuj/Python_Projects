
print("\n***** SIMPLE CALCULATOR PROGRAM *****\n")

num1 = int(input("Enter a integer number: "))
num2 = int(input("Enter another integer number: "))
oper = input("Enter a operator(+, -, *, /, %): ")

if oper == '+':
    sum = num1 + num2
    print("Summation of",num1,"and",num2,"is",sum)
elif oper == '-':
    dif = num1 - num2
    print("Diffrence of",num1,"and",num2,"is",dif)
elif oper == '*':
    mul = num1 * num2
    print("Multification of",num1,"and",num2,"is",mul)
elif oper == '/':
    div = num1 / num2
    print("Division of",num1,"and",num2,"is",div)
elif oper == '%':
    rem = num1 % num2
    print("Remainder of",num1,"and",num2,"is",rem)
else:
    print("\n*****INVALIED INPUT*****")
    print("Try again....")
