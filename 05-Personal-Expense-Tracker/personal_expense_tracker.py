
print("================================")
print("     PERSONAL EXPENSE TRACKER   ")
print("================================")

expenses = []
balance = float(input("Enter your starting balance: "))

while True:

    print("What would you like to do?")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total expenses")
    print("4. View remaining balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add a new expense
    if choice == "1":

        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount > balance:
            print("Not enough money in your balance!")

        else:
            expenses.append({"name": name, "amount": amount})
            balance = balance - amount
            print("Expense added successfully!")

    # View all expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses recorded yet.")

        else:
            print("Your Expenses:")

            for i in range(len(expenses)):
                print(
                    i + 1, "-",
                    expenses[i]["name"],
                    ":", expenses[i]["amount"]
                )

    # Calculate total expenses
    elif choice == "3":

        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total expenses:", round(total, 2))

    # View remaining balance
    elif choice == "4":

        print("Remaining balance:", round(balance, 2))

    # Exit
    elif choice == "5":

        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
