# spend

A command-line tool that records your expenses and prints monthly reports by category.
Written in Python with only the standard library (pytest is used for the tests).

## Setup

```
git clone https://github.com/ambarachristian/personal-finance-cli.git
cd personal-finance-cli
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

## Usage

Record an expense. The date defaults to today, and the note is optional:

```
spend add 12.50 food --note "lunch"
spend add 3 transport --date 2026-10-20
```

Show the totals for a month (defaults to the current month):

```
spend report --month 2026-10
```

```
Spending for October 2026
Category           Amount
-------------------------
food                12.50
coffee               5.95
transport            5.00
-------------------------
Total               23.45
```

Also save the report as a CSV file:

```
spend report --month 2026-10 --csv october.csv
```

Your expenses are saved in `expenses.json`, next to `spend.py`.

## Running the tests

```
pip install pytest
pytest
```
