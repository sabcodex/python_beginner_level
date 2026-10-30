
print("==============================")
print("         MY TO-DO LIST")
print("==============================")

tasks = []

while True:

    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add a new task
    if choice == "1":
        task = input("Enter your new task: ")
        tasks.append({"name": task, "completed": False})
        print("Task added successfully!")

    # Display all tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("Your Tasks:")

            for i in range(len(tasks)):
                if tasks[i]["completed"]:
                    status = "Completed"
                else:
                    status = "Not completed"

                print(i + 1, "-", tasks[i]["name"], "-", status)

    # Mark a task as completed
    elif choice == "3":
        if len(tasks) == 0:
            print("There are no tasks to complete.")
        else:
            task_number = int(input("Enter the task number: "))

            if task_number >= 1 and task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

    # Delete a task
    elif choice == "4":
        if len(tasks) == 0:
            print("There are no tasks to delete.")
        else:
            task_number = int(input("Enter the task number: "))

            if task_number >= 1 and task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(deleted_task["name"], "was deleted!")
            else:
                print("Invalid task number!")

    # Exit the program
    elif choice == "5":
        print("Thank you for using My To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")
