
print("\n***** GRADE TESTING PROGRAM *****\n")

mark = int(input("Enter your mark: "))

if mark > 100 or mark < 0:
    print("\n****INVALIED INPUT****")
    print("Try again....")
elif mark <= 100 and mark >= 80:
    print("You get A")
elif mark < 80 and mark >= 70:
    print("You get B")
elif mark < 70 and mark >= 60:
    print("You get C")
elif mark < 60 and mark >= 50:
    print("You get D")
else:
    print("You get F")