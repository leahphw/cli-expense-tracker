# List of expense categories
categories = ["Housing", "Utilities", "Insurance", "Food and Grocery", "Transportation", "Personal",\
                         "Savings", "Others"]


# Function to print expense categories
def print_categories() -> None:
    for i in range(len(categories)):
        print(str(i + 1) + ". " + categories[i])


# Function to add an expense
def add_expense() -> None:
    print("Which category does your expense belong to?\n")
    print_categories()

    # Try-catch for valid input
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

    # Try-catch for valid input
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

    
    # Write the expense to the 'expenses.txt' file
    try:
        with open('expenses.txt', 'a') as file:
            file.write(f"{category}, {amount}, {description}\n")
        print("Expense added!\n")
    except IOError:
        print("An error occurred while writing to the file. Please check file permissions or file existence.")


# Function to view expenses
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

    # Errors catching
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid category number.")
    except IOError:
        print("An error occurred while reading the file. Please check if 'expenses.txt' exists.")


# Function to delete an expense
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
            # Try-catch for valid input
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

    # File I/O error catching
    except IOError:
        print("An error occurred while reading/writing the file. Please check if 'expenses.txt' exists or file permissions.")


# Function to summarize expenses - Bonus Feature
def summarize_expenses():
    with open('expenses.txt', 'r') as file:
        total = 0
        category_totals = {}
        for line in file:
            category, amount, description = line.strip().split(', ')
            amount = float(amount)
            total += amount
            category_totals[category] = category_totals.get(category, 0) + amount

        print(f"Total Expenses: {total}")
        print("Expenses by Category:")
        for category, amount in category_totals.items():
            print(f"{category}: {amount}")
    
    # Error handling to be added


# Function to search expenses by description - Bonus Feature
def search_expenses():
    search_term = input("Enter a search term: ")
    with open('expenses.txt', 'r') as file:
        for line in file:
            category, amount, description = line.strip().split(', ')
            if search_term in description:
                print(f"Category: {category}, Amount: {amount}, Description: {description}")

    # Error handling to be added


# Main loop for the program
while True:
    print("\n***** Expense Tracker *****\n")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Delete an expense")
    print("4. Summarize expenses")
    print("5. Search expense by description")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        summarize_expenses()
    elif choice == "5":
        search_expenses()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")