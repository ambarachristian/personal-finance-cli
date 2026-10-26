"""spend: a command-line tool for tracking expenses."""

import datetime
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Expense:
    """One expense: how much, what for, and when."""

    amount: float
    category: str
    date: datetime.date
    note: str = ""

def expense_to_dict(expense: Expense) -> dict:
    """Turn an Expense into a plain dict that JSON can store."""
    return {
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date.isoformat(),
        "note": expense.note,
    }


def expense_from_dict(data: dict) -> Expense:
    """Turn a dict loaded from JSON back into an Expense."""
    return Expense(
        amount=data["amount"],
        category=data["category"],
        date=datetime.date.fromisoformat(data["date"]),
        note=data.get("note", ""),
    )

def save_expenses(expenses: list[Expense], path: Path) -> None:
    """Write all expenses to a JSON file, replacing what was there."""
    data = []
    for expense in expenses:
        data.append(expense_to_dict(expense))
    text = json.dumps(data, indent=2)
    path.write_text(text, encoding="utf-8")

def load_expenses(path: Path) -> list[Expense]:
    """Read all expenses from a JSON file. Return [] if the file doesn't exist yet."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    data = json.loads(text)
    expenses = []
    for item in data:
        expenses.append(expense_from_dict(item))
    return expenses

def main():
    print("Hello! spend is ready to track your expenses.")


if __name__ == "__main__":
    main()
