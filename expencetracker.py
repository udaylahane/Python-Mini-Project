import json
import os

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, description, amount, category):
        expense = {
            'id': len(self.expenses) + 1,
            'description': description,
            'amount': amount,
            'category': category
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")

    def delete_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense['id'] != expense_id]
        self.save_expenses()

    def generate_report(self):
        report = {}
        for expense in self.expenses:
            category = expense['category']
            report[category] = report.get(category, 0) + expense['amount']
        return report

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Generate Report\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_expense(description, amount, category)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            tracker.delete_expense(expense_id)
        elif choice == '4':
            report = tracker.generate_report()
            print("Expense Report by Category:")
            for category, total in report.items():
                print(f"{category}: {total}")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
