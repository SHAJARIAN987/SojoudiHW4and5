length_in_cm = float(input("Enter your length in centimeters: "))

if(length_in_cm > 0):
    print("This length equals ", length_in_cm/2.54, "cm")
else:
    print("This length is invalid because it is a negative value.")

temp = float(input("Enter your temperature: "))
type = (input("Type your units: ")[0]).capitalize()

if(type == "C"):
    print("This temperature in farenheit is ", (temp*(9/5) + 32), "degrees.")
elif(type == "F"):
    print("This temperature in celcius is ", (temp-32)*(5/9), "degrees.")
else:
    print("Invalid temperature unit.")

temp_in_c = float(input("Enter a temperature in celcius: "))

if(temp_in_c < -273.15):
    print("This temperature is invalid because it is less than absolute 0.")
elif(temp_in_c == -273.15):
    print("This temperature is absolute 0.")
elif(temp_in_c < 0 and temp_in_c > -273.15):
    print("This temperature is below freezing.")
elif(temp_in_c == 0):
    print("This temperature is at freezing.")
elif(temp_in_c > 0 and temp_in_c < 100):
    print("This temperature is in the normal range.")
elif(temp_in_c == 100):
    print("This temperature if at the boiling point.")
else:
    print("This temperature is above the boiling point.")