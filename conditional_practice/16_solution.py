
print("\n***** SECRET NUMBER TESTING PROGRAM *****\n")

sec_num = 6
num = int(input("Enter a number: "))

if num == sec_num:
    print("Bingo! Correct answer.")
else:
    numGap = num - sec_num

    if numGap == 1 or numGap == -1:
        print("Close enough to the correct answer")
    else:
        print("Sorry! It is not the correct answer.")