
print("\n***** TEMPERATURE TESTING PROGRAM *****\n")

tem = int(input("Enter temperature: "))

if tem >= 40:
    print("It is too hot outside.")
elif tem < 40 and tem >= 30:
    print("The Weather today is Normal.")
elif tem < 30 and tem >= 20:
    print("Today's Weather is cool.")
elif tem < 20:
    print("OMG! Toady's weather is so cool.")