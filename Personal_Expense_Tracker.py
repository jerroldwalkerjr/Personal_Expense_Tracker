import csv

# Global variables
expenses = []
monthly_budget = 0


# Step 1: Add an expense
def add_expense():
    date = input("Enter the expense date (YYYY-MM-DD): ")
    category = input("Enter the expense category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    description = input("Enter a brief description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!")


# Step 2: View expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n--- Your Expenses ---")
    print("-" * 50)
    for exp in expenses:
        if all(key in exp and exp[key] for key in ["date", "category", "amount", "description"]):
            print(f"Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']:.2f} | Description: {exp['description']}")
        else:
            print("Skipping incomplete expense entry")
    print("-" * 50)


# Step 3: Budget functions
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to ${monthly_budget:.2f}")
    except ValueError:
        print("Invalid input! Please enter a number.")

def track_budget():
    total_spent = sum(exp["amount"] for exp in expenses if "amount" in exp)
    print(f"\nTotal spent so far: ${total_spent:.2f}")
    if monthly_budget > 0:
        if total_spent > monthly_budget:
            print("You have exceeded your budget!")
        else:
            remaining = monthly_budget - total_spent
            print(f"You have ${remaining:.2f} left for the month.")
    else:
        print("Budget not set yet. Please set a budget first.")


# Step 4: Save & load
def save_expenses(filename="expenses.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved successfully!")

def load_expenses(filename="expenses.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])  # convert back to float
                expenses.append(row)
        print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No saved expenses found. Starting fresh.")


# Step 5: Menu system
def menu():
    load_expenses()  # load saved data at startup
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            if monthly_budget == 0:
                set_budget()
            track_budget()
        elif choice == "4":
            save_expenses()
        elif choice == "5":
            save_expenses()
            print("Goodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid option. Please try again.")


# Run the program
if __name__ == "__main__":
    menu()
