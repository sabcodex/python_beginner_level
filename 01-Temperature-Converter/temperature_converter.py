
print("================================")
print("     TEMPERATURE CONVERTER")
print("================================")

print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

# Ask the user which unit they want to convert from
choice = input("Choose your starting temperature (1-3): ")

# Ask for the temperature
temperature = float(input("Enter the temperature: "))

# Convert Celsius to another unit
if choice == "1":

    print("Convert Celsius to:")
    print("1. Fahrenheit")
    print("2. Kelvin")

    convert_to = input("Your choice: ")

    if convert_to == "1":
        result = (temperature * 9/5) + 32
        print(temperature, "°C =", round(result, 2), "°F")

    elif convert_to == "2":
        result = temperature + 273.15
        print(temperature, "°C =", round(result, 2), "K")

    else:
        print("Invalid choice!")

# Convert Fahrenheit to another unit
elif choice == "2":

    print("Convert Fahrenheit to:")
    print("1. Celsius")
    print("2. Kelvin")

    convert_to = input("Your choice: ")

    if convert_to == "1":
        result = (temperature - 32) * 5/9
        print(temperature, "°F =", round(result, 2), "°C")

    elif convert_to == "2":
        result = (temperature - 32) * 5/9 + 273.15
        print(temperature, "°F =", round(result, 2), "K")

    else:
        print("Invalid choice!")

# Convert Kelvin to another unit
elif choice == "3":

    print("Convert Kelvin to:")
    print("1. Celsius")
    print("2. Fahrenheit")

    convert_to = input("Your choice: ")

    if convert_to == "1":
        result = temperature - 273.15
        print(temperature, "K =", round(result, 2), "°C")

    elif convert_to == "2":
        result = (temperature - 273.15) * 9/5 + 32
        print(temperature, "K =", round(result, 2), "°F")

    else:
        print("Invalid choice!")

else:
    print("Invalid starting choice!")

print("Thank you for using my converter!")
