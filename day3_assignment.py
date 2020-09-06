altitude = int(input("CURRENT ALTITUDE:"))

if altitude <=1000:            
    print("You can land the plan")
elif altitude > 1000 and altitude < 5000:
    print("Come down to 1000")
else:
    print("Turn around")

