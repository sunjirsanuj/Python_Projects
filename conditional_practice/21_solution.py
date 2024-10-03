
print("\n***** WEEK DAY CHECKING PROGRAM *****\n")

day = input("Enter day name(Sunday, Monday, Thursday, Wednesday, Tuesday, Friday, Saturday): ")

if day == 'Sunday' or day == 'Monday' or day == 'Thursday' or day == 'Wednesday' or day == 'Tuesday':
    print("It's a week day.")
elif day == 'Friday' or day == 'Saturday':
    print("It's weekend")
else:
    print("\n*****INVALIED INPUT*****")
    print("Try again....")