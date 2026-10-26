"""Tests for spend.py. Run them with: pytest"""

import argparse
import datetime
import pytest

import spend


def test_parse_category_tidies_text():
    assert spend.parse_category("  Food ") == "food"


def test_parse_amount_rejects_zero_and_negative():
    with pytest.raises(argparse.ArgumentTypeError):
        spend.parse_amount("0")
    with pytest.raises(argparse.ArgumentTypeError):
        spend.parse_amount("-5")

def test_save_then_load_gives_back_the_same_expenses(tmp_path):
    path = tmp_path / "expenses.json"
    expenses = [
        spend.Expense(12.5, "food", datetime.date(2026, 10, 26), "lunch"),
        spend.Expense(2.0, "transport", datetime.date(2026, 10, 25)),
    ]
    spend.save_expenses(expenses, path)
    assert spend.load_expenses(path) == expenses


def test_load_missing_file_gives_empty_list(tmp_path):
    assert spend.load_expenses(tmp_path / "missing.json") == []


def test_add_expense_keeps_existing_ones(tmp_path):
    path = tmp_path / "expenses.json"
    lunch = spend.Expense(12.5, "food", datetime.date(2026, 10, 26))
    coffee = spend.Expense(4.75, "coffee", datetime.date(2026, 10, 26))
    spend.add_expense(lunch, path)
    spend.add_expense(coffee, path)
    assert spend.load_expenses(path) == [lunch, coffee]

@pytest.fixture
def expenses():
    """Three expenses in October 2026, one in September, one in October 2025."""
    return [
        spend.Expense(12.5, "food", datetime.date(2026, 10, 26)),
        spend.Expense(4.75, "coffee", datetime.date(2026, 10, 3)),
        spend.Expense(1.25, "coffee", datetime.date(2026, 10, 20)),
        spend.Expense(30.0, "food", datetime.date(2026, 9, 15)),
        spend.Expense(7.0, "coffee", datetime.date(2025, 10, 3)),
    ]


def test_filter_by_month_keeps_only_that_month(expenses):
    october = spend.filter_by_month(expenses, datetime.date(2026, 10, 1))
    assert [e.amount for e in october] == [12.5, 4.75, 1.25]


def test_filter_by_month_checks_the_year_too(expenses):
    october_2025 = spend.filter_by_month(expenses, datetime.date(2025, 10, 1))
    assert [e.amount for e in october_2025] == [7.0]


def test_totals_by_category_adds_up_each_category(expenses):
    october = spend.filter_by_month(expenses, datetime.date(2026, 10, 1))
    assert spend.totals_by_category(october) == {"food": 12.5, "coffee": 6.0}


def test_totals_by_category_of_no_expenses_is_empty():
    assert spend.totals_by_category([]) == {}

def test_parse_month_gives_first_day_and_rejects_bad_text():
    assert spend.parse_month("2026-10") == datetime.date(2026, 10, 1)
    with pytest.raises(argparse.ArgumentTypeError):
        spend.parse_month("2026-13")


def test_print_report_shows_biggest_first_then_total(capsys):
    spend.print_report({"coffee": 6.0, "food": 12.5}, datetime.date(2026, 10, 1))
    lines = capsys.readouterr().out.splitlines()
    assert lines[0] == "Spending for October 2026"
    assert lines[3].split() == ["food", "12.50"]
    assert lines[4].split() == ["coffee", "6.00"]
    assert lines[-1].split() == ["Total", "18.50"]


def test_write_report_csv_writes_header_and_rows(tmp_path):
    path = tmp_path / "report.csv"
    spend.write_report_csv({"coffee": 6.0, "food": 12.5}, path)
    assert path.read_text(encoding="utf-8").splitlines() == [
        "category,amount",
        "food,12.50",
        "coffee,6.00",
    ]

def test_parse_amount_rejects_nan_and_infinity():
    for text in ["nan", "inf"]:
        with pytest.raises(argparse.ArgumentTypeError):
            spend.parse_amount(text)
