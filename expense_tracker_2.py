import os
import csv
from datetime import datetime

# load the expenses from the file 
def load_expenses():
    expenses = []
    with open("expense.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)

    return expenses

# saving the data into file
def save_expenses(expenses):
    with open ("expense.csv", "w", newline="") as file:
        fieldnames = ["Date", "Category", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()     
        writer.writerows(expenses)

# View total expense 
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(
            f"Date: {expense['Date']} | "
            f"Category: {expense['Category']} | "
            f"Amount: ₹{expense['Amount']} "
  
        )
# filtering the perticular expense and showing total expense
def filter_expenses(Category):
    expenses = load_expenses()

    filtered = []
    Total = 0

    for expense in expenses:
        if expense["Category"].lower() == Category.lower():
            filtered.append(expense)
            Total += expense["Amount"]

    return filtered, Total

# return the total expense
def total_expenses():
    expenses = load_expenses()

    total = 0
    for expense in expenses:
        total += expense["Amount"]

    return total

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                while True:
                    Date = input("Enter the date (yyyy-mm-dd):")
                    try:
                        valid_date = datetime.strptime(Date, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Enter valid date form")

                Category = input("Enter the category: ")
                while True:
                    try:
                        Amount = float(input("Enter the amount: "))
                        break
                    except ValueError:
                        print("Enter the integer")

                expenses = load_expenses()

                expenses.append({
                    "Date": Date,
                    "Category": Category,
                    "Amount": Amount
                })

                save_expenses(expenses)

                print("Expense added successfully!")

            case "2":
                view_expenses()

            case "3":
                category = input("Enter category to filter: ")
                filtered, total = filter_expenses(category)

                if not filtered:
                    print("No matching expenses found.")
                else:
                    for expense in filtered:
                        print(expense)
                    print(total)     

            case "4":
                total = total_expenses()
                print("Total Expense:", total)

            case "5":
                print("Exiting...")
                break

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()

