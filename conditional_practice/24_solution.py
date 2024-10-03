
print("\n***** LEAF YEAR TESTING PROGRAM *****\n")

year = int(input("Enter any year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year,"is leaf year.")
else:
    print(year,"is not leaf year.")