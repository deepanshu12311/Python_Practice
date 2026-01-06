#Build a script that asks the user for a temperature and a unit (C or F) and converts it to the other scale.
temp = float(input("Enter temperature: "))
unit = input("Enter the unit of temperature(c or f): ").lower()

if(unit=="c"):
    F = (temp*(9/5))+32
    print("The tempetature in fahrenheit is",F)

if(unit=="f"):
    C = (temp-32)*(5/9)
    print("The tempetature in celcius is",C)
