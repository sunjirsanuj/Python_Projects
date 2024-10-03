
print("\n***** PLURALIZER PROGRAM *****\n")

num = int(input("Please enter a number: "))
noun = input("Please enter a noun: ")

if num == 1:
    print(num,noun)
else:
    print(num,noun+"s")