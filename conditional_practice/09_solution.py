
print("\n***** FUEL LEVEL TESTING PROGRAM *****\n")

fuel = float(input("Enter your car's fuel amount(in liters): "))

if fuel <= 0.25:
    print("\nPlease refill the fuel in your car.")
else:
    print("\nYour car's fuel level is perfect.")