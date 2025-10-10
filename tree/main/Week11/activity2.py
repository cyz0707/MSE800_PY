import unittest

class ExpenseCalculator:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description):
        if amount < 0:
            raise ValueError("Expense amount cannot be negative")
        self.expenses.append([amount, description])

    def total_expenses(self):
        return sum(amount for amount, _ in self.expenses)

class TestMathOperations(unittest.TestCase):
    def test_add_expense(self):
        calculator = ExpenseCalculator()
        calculator.add_expense(50, "food")
        calculator.add_expense(20, "bus")
        calculator.add_expense(210, "rent")
        self.assertEqual(calculator.total_expenses(), 270)

    
def main():
    amount = float(input("Enter an expense amount (or -1 to finish): "))
    description = input("Enter a description for the expense: ")
    calculator = ExpenseCalculator()
    while amount != -1:
        try:
            calculator.add_expense(amount, description)
        except ValueError as e:
            print(e)
        amount = float(input("Enter an expense amount (or -1 to finish): "))
        if amount != -1:
            description = input("Enter a description for the expense: ")
    for amt, desc in calculator.expenses:
        print(f"Expense: {desc}, Amount: {amt}")
    print(f"Total expenses: {calculator.total_expenses()}")

if __name__ == "__main__":
    main()
