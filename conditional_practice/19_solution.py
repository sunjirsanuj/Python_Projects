
print("\n***** SEASON CHECKING PROGRAM *****\n")

month = input("Enter any month(January, February, March, April, May, June, July, August, September, October, November, December): ")

if month == 'September' or month == 'October' or month == 'November':
    print("The season is Autumn.")
elif month == 'December' or month == 'January' or month == 'February':
    print("The season is Winter.")
elif month == 'March' or month == 'April' or month == 'May':
    print("The season is Spring.")
elif month == 'June' or month == 'July' or month == 'August':
    print("The season is Spring.")
else:
    print("\n*****INVALIED INPUT*****")
    print("Try again....")