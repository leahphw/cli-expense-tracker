# Expense Tracker CLI Application

This is a simple command-line interface (CLI) application for tracking daily expenses. Users can log expenses, view them, delete entries, and perform additional tasks as described below.

## Features

### Basic Features

1. **Add an Expense**: Log an expense by selecting a category, entering the amount, and adding a brief description.

2. **View Expenses**: List all expenses, optionally filtered by category.

3. **Delete an Expense**: Remove a specific expense entry.

### Data Storage

- All expense data is stored in a text file named `expenses.txt`.

### User Interaction

- The program interacts with the user through Python's `input()` function, providing clear prompts and confirmation messages.

### Bonus Features

4. **Summarize Expenses**: Provide a summary of total expenses and totals by category.

5. **Search Expenses by Description**: Find expenses containing a specific keyword in their description.

## How to Use

1. Run the application by executing the script in preferred Python environment.

2. You'll be presented with a menu to choose from the following options:
   - Add an expense (Option 1)
   - View expenses (Option 2)
   - Delete an expense (Option 3)
   - Summarize expenses (Option 4, bonus feature)
   - Search expenses by description (Option 5, bonus feature)
   - Quit (Option 6)

3. Follow the prompts and make selections according to your desired actions.

4. The application will guide you through the process of adding, viewing, and managing expenses.

## Error Handling

- The application includes error handling for various scenarios, such as invalid input, file I/O errors, and more to be added.

## Data Storage

- All expenses are stored in the `expenses.txt` file in format: `Category, Amount, Description`.
