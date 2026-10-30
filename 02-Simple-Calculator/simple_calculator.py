
print("==============================")
print("       SIMPLE CALCULATOR")
print("==============================")

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the available operations
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

# Perform the selected operation
if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", result)

elif choice == "4":
    if num2 == 0:
        print("Error! You cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid choice! Please try again.")

print("Thank you for using my calculator!")
