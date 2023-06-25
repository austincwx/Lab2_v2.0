weight = int(input("What is your weight?" ))
Unit = input("K(g) or (L)bs: " )
if Unit.upper() == "K":
    converted1 = weight / 0.45
    print("Weight in Lbs: " + str(converted1))
else:
    converted2 = weight * 0.45
    print("Weight in Kgs: " + str(converted2))