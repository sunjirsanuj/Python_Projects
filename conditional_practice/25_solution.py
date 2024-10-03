
print("\n***** TAX SHOWING PROGRAM *****\n")

cost = int(input("Enter the price of your bike: "))

if cost > 100000:
    tax = (cost * 15) / 100
    print("Tax of your bike:",tax,"taka only.")
elif cost <= 100000 and cost > 50000:
    tax = (cost * 10) / 100
    print("Tax of your bike:",tax,"taka only.")
elif cost <= 50000:
    tax = (cost * 5) / 100
    print("Tax of your bike:",tax,"taka only.")