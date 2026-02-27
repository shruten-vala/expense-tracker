import csv

def load_expenses():
    expenses = []
    with open("expense.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)

    return expenses

def add_expense(date, category, amount):
    with open("expense.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def save_expenses(expenses):
    with open ("expense.csv", "w", newline="") as file:
        fieldnames = ["date", "category", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()     
        writer.writerows(expenses)

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(
            f"Date: {expense['date']} | "
            f"Category: {expense['category']} | "
            f"Amount: ₹{expense['amount']} "
        )

def filter_expenses(category):
    expenses = load_expenses()

    filtered = []

    for expense in expenses:
        if expense["Category"].lower() == category.lower():
            filtered.append(expense)

    return filtered

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
                date = input("Enter the date: ")
                category = input("Enter the category: ")
                amount = float(input("Enter the amount: "))

                expenses = load_expenses()

                expenses.append({
                    "date": date,
                    "category": category,
                    "amount": amount
                })

                save_expenses(expenses)

                print("Expense added successfully!")

            case "2":
                view_expenses()

            case "3":
                category = input("Enter category to filter: ")
                filtered = filter_expenses(category)

                if not filtered:
                    print("No matching expenses found.")
                else:
                    for expense in filtered:
                        print(expense)

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

