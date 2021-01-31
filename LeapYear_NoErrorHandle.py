# Written by Gabriel Crew
# Function to determine whether a given year is a leap  year
leapStr = input("Enter a Year and I'll tell you if it's a leap year or not:" )
print("You chose: "+ leapStr)
leapNum = int(leapStr)
if (leapNum % 4) == 0:
  if(leapNum%100) == 0:
    if(leapNum%400) == 0:
      print("The year " + leapStr + " is a leap year")
    else:
      print("They year " + leapStr + " is not a leap year")
  else:
    print("The year " + leapStr + " is a leap year")
else:
  print("The year " + leapStr + " is not a leap year") 
