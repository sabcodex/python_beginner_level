
students = []

while True:
    print("==============================")
    print("      STUDENT GRADE MANAGER   ")
    print("==============================")
    print("1. Add a student")
    print("2. View all students")
    print("3. Calculate student average")
    print("4. Check pass or fail")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")

        grade1 = float(input("Enter first grade: "))
        grade2 = float(input("Enter second grade: "))
        grade3 = float(input("Enter third grade: "))

        student = {
            "name": name,
            "grades": [grade1, grade2, grade3]
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students available.")
        else:
            print("----- STUDENT LIST -----")

            for student in students:
                print("Name:", student["name"])
                print("Grades:", student["grades"])
                print("------------------------")

    elif choice == "3":
        search_name = input("Enter student name: ")
        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                average = sum(student["grades"]) / len(student["grades"])

                print("Student:", student["name"])
                print("Average:", round(average, 2))

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        search_name = input("Enter student name: ")
        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                average = sum(student["grades"]) / len(student["grades"])

                print("Student:", student["name"])
                print("Average:", round(average, 2))

                if average >= 10:
                    print("Result: PASSED!")
                else:
                    print("Result: FAILED!")

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "5":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
