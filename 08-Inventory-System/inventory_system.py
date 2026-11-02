
products = []

while True:
    print("==============================")
    print("      SIMPLE INVENTORY SYSTEM ")
    print("==============================")
    print("1. Add a product")
    print("2. View all products")
    print("3. Search for a product")
    print("4. Delete a product")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)
        print("Product added successfully!")

    elif choice == "2":
        if len(products) == 0:
            print("The inventory is empty.")
        else:
            print("----- PRODUCT LIST -----")

            for product in products:
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
                print("-----------------------")

    elif choice == "3":
        search_name = input("Enter product name to search: ")
        found = False

        for product in products:
            if product["name"].lower() == search_name.lower():
                print("Product found!")
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
                found = True
                break

        if found == False:
            print("Product not found.")

    elif choice == "4":
        delete_name = input("Enter product name to delete: ")
        found = False

        for product in products:
            if product["name"].lower() == delete_name.lower():
                products.remove(product)
                print("Product deleted successfully!")
                found = True
                break

        if found == False:
            print("Product not found.")

    elif choice == "5":
        print("Thank you for using the inventory system!")
        break

    else:
        print("Invalid choice. Please try again.")
