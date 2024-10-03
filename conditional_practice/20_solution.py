
print("\n***** TRAFFIC SIGNAL CHECKING PROGRAM *****\n")

sig_color = input("Enter a color(Red, Yellow, Green): ")

if sig_color == 'Red':
    print("Vehicles must stop")
if sig_color == 'Yellow':
    print("Vehicles should get ready to move")
if sig_color == 'Green':
    print("Vehicles can move now")
else:
    print("\n*****INVALIED INPUT*****")
    print("Try again....")