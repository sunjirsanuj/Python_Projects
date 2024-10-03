
print("\n***** MARK SHEET PROGRAM *****\n")

sub_1 = int(input("Enter first subject mark: "))
sub_2 = int(input("Enter second subject mark: "))
sub_3 = int(input("Enter third sunject mark: "))

if (sub_1 > 100 or sub_1 < 0 or sub_2 > 100 or sub_2 < 0 or sub_3 > 100 or sub_3 < 0):
    print("\n*****INVALIED INPUT*****")
    print("Try again....")
else:
    total_mark = sub_1 + sub_2 + sub_3
    percentage = (total_mark * 100) / 300

    print("\nMark Sheet")
    print("Total Marks: 300")
    print("Marks Obtained:",total_mark)
    print("Percentage:",int(percentage),"%")

    if percentage <=100 and percentage >= 80:
        print("Grade: A+")
        print("Remarks: Excellent")
    elif percentage < 80 and percentage >= 70:
        print("Grade: A")
        print("Remarks: Good")
    elif percentage < 70 and percentage >= 60:
        print("Grade: B")
        print("Remarks: You need to improve")
    else:
        print("Grade: Fail")
        print("Remarks: Sorry")