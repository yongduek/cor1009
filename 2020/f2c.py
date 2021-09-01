# farenheit -> celsius

print("This program convert farenheit to celsius.")

farenheit = float( input("provide farenheit: ") )
# farenheit = int(farenheit)
celsius = (float(farenheit) - 32.) * (5./9.)
print("It is ", celsius, "Celsius")

# EOF