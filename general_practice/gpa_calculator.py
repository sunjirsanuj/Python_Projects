marks = int(input("Enter your marks: "))

if marks<0 or marks>100:
    print("Invalid input!")
elif marks<=100 and marks>=80:
    print("Congratulations! You get A+")
elif marks<80 and marks>=70:
    print("You get A")
elif marks<70 and marks>=60:
    print("You get A-")
elif marks<60 and marks>=50:
    print("You get B")
elif marks<50 and marks>=40:
    print("You get C")
elif marks<40 and marks>=33:
    print("You get D")
else:
    print("You are fail.")