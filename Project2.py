# Expense Tracker Application
import json
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(amount, category, description=""):
    expenses = load_expenses()
    expense = {
        "amount": float(amount),
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Logged ${amount:.2f} under '{category}'.")

def show_summary():
    expenses = load_expenses()
    total = sum(item["amount"] for item in expenses)
    print(f"\n--- Total Spent: ${total:.2f} ---")
    categories = {}
    for item in expenses:
        cat = item["category"]
        categories[cat] = categories.get(cat, 0) + item["amount"]
    for cat, amt in categories.items():
        print(f" - {cat}: ${amt:.2f}")