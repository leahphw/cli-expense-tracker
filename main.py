categories = ["Housing", "Utilities", "Insurance", "Food and Grocery", "Transportation", "Personal",\
                         "Savings", "Others"]


def print_categories() -> None:
    for i in range(len(categories)):
        print(str(i + 1) + ". " + categories[i])
    
        
def add_expense() -> None:
    print("Which category does your expense belong to?\n")
    print_categories()

    while True:
        try:
            category_num = int(input("Enter the number according to the category: "))
            if 1 <= category_num <= len(categories):
                break
            else:
                print("Invalid category number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    category = categories[category_num - 1]

    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount >= 0:
                break
            else:
                print("Amount must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    description = input("Enter a brief description: ")

    try:
        with open('expenses.txt', 'a') as file:
            file.write(f"{category}, {amount}, {description}\n")
        print("Expense added!\n")
    except IOError:
        print("An error occurred while writing to the file. Please check file permissions or file existence.")


def view_expenses():
    print_categories()
    category_num = input("Enter a category number to filter (leave empty to show all): ")

    try:
        if category_num:
            category_num = int(category_num)
            category_filter = categories[category_num - 1]
            with open('expenses.txt', 'r') as file:
                for line in file:
                    category, amount, description = line.strip().split(', ')
                    if category_filter == category:
                        print(f"Category: {category}, Amount: {amount}, Description: {description}")
        else:
            with open('expenses.txt', 'r') as file:
                for line in file:
                    category, amount, description = line.strip().split(', ')
                    print(f"Category: {category}, Amount: {amount}, Description: {description}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid category number.")
    except IOError:
        print("An error occurred while reading the file. Please check if 'expenses.txt' exists.")


def delete_expense():
    try:
        with open('expenses.txt', 'r') as file:
            expenses = file.readlines()
        if not expenses:
            print("No expenses to delete.")
            return
        print("Select an expense to delete:")
        for i, expense in enumerate(expenses):
            print(f"{i + 1}. {expense.strip()}")
        while True:
            try:
                choice = int(input("Enter the number of the expense to delete: "))
                if 1 <= choice <= len(expenses):
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        with open('expenses.txt', 'w') as file:
            for i, expense in enumerate(expenses):
                if i + 1 != choice:
                    file.write(expense)
        print("Expense deleted!\n")
    except IOError:
        print("An error occurred while reading/writing the file. Please check if 'expenses.txt' exists or file permissions.")


while True:
    print("\n***** Expense Tracker *****\n")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Delete an expense")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")