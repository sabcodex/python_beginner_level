
print("================================")
print("          CONTACT BOOK")
print("================================")

contacts = []

while True:

    print("What would you like to do?")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add a new contact
    if choice == "1":

        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        print("Contact added successfully!")

    # View all contacts
    elif choice == "2":

        if len(contacts) == 0:
            print("Your contact book is empty.")

        else:
            print("Your Contacts:")

            for contact in contacts:
                print("------------------------")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    # Search for a contact
    elif choice == "3":

        search_name = input("Enter the name to search: ")
        found = False

        for contact in contacts:

            if contact["name"].lower() == search_name.lower():

                print("Contact found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                found = True

        if found == False:
            print("Contact not found.")

    # Delete a contact
    elif choice == "4":

        delete_name = input("Enter the name to delete: ")
        found = False

        for contact in contacts:

            if contact["name"].lower() == delete_name.lower():

                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if found == False:
            print("Contact not found.")

    # Exit the program
    elif choice == "5":

        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")
