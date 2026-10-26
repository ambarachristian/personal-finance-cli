"""spend: a command-line tool for tracking expenses."""

import argparse
import csv
import datetime
import json
from dataclasses import dataclass
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


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

def add_expense(expense: Expense, path: Path) -> None:
    """Add one expense to the file at path, keeping the ones already there."""
    expenses = load_expenses(path)
    expenses.append(expense)
    save_expenses(expenses, path)

def filter_by_month(expenses: list[Expense], month: datetime.date) -> list[Expense]:
    """Keep only the expenses in the same year and month as month."""
    return [
        expense
        for expense in expenses
        if expense.date.year == month.year and expense.date.month == month.month
    ]

def totals_by_category(expenses: list[Expense]) -> dict[str, float]:
    """Add up the amounts for each category."""
    totals = {}
    for expense in expenses:
        totals[expense.category] = totals.get(expense.category, 0) + expense.amount
    return totals

def print_report(totals: dict[str, float], month: datetime.date) -> None:
    """Print one line per category, biggest first, then the total."""
    print(f"Spending for {month:%B %Y}")
    if not totals:
        print("No expenses this month.")
        return
    print(f"{'Category':<15}{'Amount':>10}")
    print("-" * 25)
    for category in sorted(totals, key=totals.get, reverse=True):
        print(f"{category:<15}{totals[category]:>10.2f}")
    print("-" * 25)
    print(f"{'Total':<15}{sum(totals.values()):>10.2f}")

def write_report_csv(totals: dict[str, float], path: Path) -> None:
    """Save the totals to a CSV file, one row per category, biggest first."""
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["category", "amount"])
        for category in sorted(totals, key=totals.get, reverse=True):
            writer.writerow([category, f"{totals[category]:.2f}"])


def parse_amount(text: str) -> float:
    """Turn text into a positive number, or explain what is wrong."""
    try:
        amount = float(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{text}' is not a number, e.g. 12.50")
    if amount <= 0:
        raise argparse.ArgumentTypeError(f"must be more than 0, got {text}")
    return amount


def parse_date(text: str) -> datetime.date:
    """Turn YYYY-MM-DD text into a date, or explain what is wrong."""
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"'{text}' is not a valid date, use YYYY-MM-DD, e.g. 2026-10-26"
        )


def parse_category(text: str) -> str:
    """Tidy up a category name, and refuse an empty one."""
    category = text.strip().lower()
    if not category:
        raise argparse.ArgumentTypeError("can't be empty")
    return category

def parse_month(text: str) -> datetime.date:
    """Turn YYYY-MM text into the first day of that month, or explain what is wrong."""
    try:
        return datetime.date.fromisoformat(text + "-01")
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"'{text}' is not a valid month, use YYYY-MM, e.g. 2026-10"
        )


def build_parser() -> argparse.ArgumentParser:
    """Describe the commands and options that spend understands."""
    parser = argparse.ArgumentParser(
        prog="spend",
        description="Track your expenses from the terminal.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="record a new expense")
    add_parser.add_argument(
        "amount", type=parse_amount, help="how much you spent, e.g. 12.50"
    )
    add_parser.add_argument("category", type=parse_category, help="what it was for, e.g. food")
    add_parser.add_argument(
        "--date",
        type=parse_date,
        default=datetime.date.today(),
        help="when you spent it, as YYYY-MM-DD (default: today)",
    )
    add_parser.add_argument("--note", default="", help="optional extra detail")

    report_parser = subparsers.add_parser("report", help="show totals for one month")
    report_parser.add_argument(
        "--month",
        type=parse_month,
        default=datetime.date.today().replace(day=1),
        help="which month, as YYYY-MM (default: this month)",
    )
    report_parser.add_argument(
        "--csv", type=Path, help="also save the report to this CSV file"
    )



    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "add":
        expense = Expense(args.amount, args.category, args.date, args.note)
        add_expense(expense, DATA_FILE)
        print(f"Added {expense.amount:.2f} for {expense.category} on {expense.date}.")
    elif args.command == "report":
        expenses = filter_by_month(load_expenses(DATA_FILE), args.month)
        totals = totals_by_category(expenses)
        print_report(totals, args.month)
        if args.csv:
            write_report_csv(totals, args.csv)
            print(f"Saved the report to {args.csv}")




if __name__ == "__main__":
    main()
