# Tutor progress: Personal finance CLI

## Where we are
Milestone 3 of 5 · Step 6 (commit + push). Step given, waiting for the learner's result.

## Environment
- Windows 11, PowerShell terminal inside VS Code.
- Python 3.13.14. `python3` works globally. Inside the venv, use `python` (Windows venvs have no python3.exe).
- git 2.45.1. Global user.name and user.email are already set.
- GitHub CLI (gh) 2.96.0 installed, logged in as ambarachristian (https, repo scope). Credential helper: Git Credential Manager.
- Repo: https://github.com/ambarachristian/personal-finance-cli (public), origin set, main tracks origin/main.

## Milestone plan
1. Project setup: DONE
2. Data model and storage: DONE (commit 1fc603b)
3. The add command with argparse
   1. argparse skeleton: build_parser() with an `add` subcommand (amount, category as strings); main prints args
   2. --date (default today) and --note options; type=float for amount, type=datetime.date.fromisoformat for --date (shows argparse's default, ugly error messages)
   3. Validation and clear error messages: parse_amount / parse_date functions raising argparse.ArgumentTypeError (amount > 0, friendly date message), non-empty category
   4. Save the expense: DATA_FILE, load, append, save, print confirmation
   5. Make `spend` a real command: pyproject.toml with [project.scripts] spend = "spend:main", `[tool.setuptools] py-modules = ["spend"]`, `pip install -e .`
   6. Commit and push
4. The report command (filter by month, totals by category with a dict, aligned table, --csv export)
5. Tests and docs (10+ pytest tests with tmp_path, README)

Finished when: `spend add` and `spend report --month 2026-10` work, and 10+ tests pass.

## Log
- 2026-10-25 · Step 0 · Setup check: done. Python 3.13.14 and git 2.45.1 both work. Project folder was empty.
- 2026-10-25 · M1 Step 1 · venv: done. `python3 -m venv .venv`, activated with `.venv\Scripts\Activate.ps1` (no execution-policy error). pip 26.1.2 inside .venv. Python 3.13 venv writes its own `.venv\.gitignore` containing `*`.
- 2026-10-25 · M1 Step 2 · git init: done. Branch main.
- 2026-10-25 · M1 Step 3 · .gitignore: done. 13 lines (.venv/, __pycache__/, *.pyc, .pytest_cache/, expenses.json, *.csv).
- 2026-10-25 · M1 Step 4 · spend.py: done. Docstring, `main()` with print, `if __name__ == "__main__":` guard.
- 2026-10-25 · M1 Step 5 · first commit: done. cc3ee1c "Set up project with greeting script and .gitignore".
- 2026-10-25 · M1 Step 6 · GitHub: done. Public repo created with gh, `git push -u origin main`.
- 2026-10-26 · M1 Step 7 · review: Q1, Q2 fine. Q3 (the `__name__` guard) shaky; the learner asked to move on. Gave the correct answer briefly and tied it to M2 Step 1 (importing spend doesn't print the greeting). Revisit in M5 when tests import spend.
- M1 closing: TUTOR_PROGRESS.md changes were not committed separately; they go into the milestone 2 commit.
- 2026-10-26 · M2 Step 1 · Expense dataclass: done. spend.py lines 3-14: `import datetime`, `from dataclasses import dataclass`, `@dataclass class Expense` (amount: float, category: str, date: datetime.date, note: str = ""). Import + repr verified.
- 2026-10-26 · M2 Step 2 · to/from dict: done. Round trip verified (== True). Style note given: only one blank line before `expense_to_dict` and before `main` (PEP 8 wants two); asked to fix during Step 3.
- 2026-10-26 · M2 Step 3 · save_expenses: done. expenses.json written with lunch + bus, correctly git-ignored. Blank lines only partly fixed: before main is now 2, but still 1 before expense_to_dict (line 17) and 1 before save_expenses (line 36). Mentioned again.
- 2026-10-26 · M2 Step 4 · load_expenses: done. Returns the 2 expenses from expenses.json and [] for a missing file. Blank lines still single at lines 17, 36, 44, 56. Learner seems to skip style notes; folded the fix into the M2 commit step instead of repeating it.
- 2026-10-26 · M2 Step 5 · commit: done. 1fc603b "Add Expense dataclass with JSON save and load" (spend.py + TUTOR_PROGRESS.md), pushed; working tree clean. Blank lines were NOT fixed (spend.py unchanged). Decided to stop mentioning it; new code blocks show correct spacing.
- MILESTONE 2 DONE.
- 2026-10-26 · M3 Step 1 · argparse skeleton: done. build_parser() with add subcommand (amount, category); main prints Namespace. No-command error and exit code 2 verified.
- 2026-10-26 · M3 Step 2 · --date/--note: done. amount type=float, --date type=fromisoformat default today, --note default "". Verified: -5 is accepted (to fix in Step 3), and the bad date gives "invalid fromisoformat value".
- 2026-10-26 · M3 Step 3 · validation: done. parse_amount, parse_date, parse_category (lines 58-84) wired into build_parser. All five checks gave the expected messages.
- 2026-10-26 · M3 Step 4 · save: done. DATA_FILE (line 9), add_expense (lines 60-64), main dispatches on "add". `add 4.75 coffee --note "with Sam"` appended, so expenses.json has 3 entries.
- 2026-10-26 · M3 Step 5 · spend command: done. pyproject.toml created; `*.egg-info/` added to .gitignore; `pip install -e .` gave .venv\Scripts\spend.exe. `spend add` works, including from the parent folder (data stays in the project; expenses.json has 5 entries). CHECKPOINT: `spend add` works (half of "finished when").

## Decisions
- The real data file will be `expenses.json` in the project folder. It is git-ignored (personal data), as are `*.csv` exports.
- TUTOR_PROGRESS.md is committed with the project, so resuming works from any copy of the repo.
- core.autocrlf is true (system gitconfig), so "LF will be replaced by CRLF" warnings are expected and harmless.
- The whole tool stays in one file, spend.py, for this level.
- amount is a float (simple; rounding pitfall explained; round to 2 decimals when printing).
- The date field is a `datetime.date`, using `import datetime` (not `from datetime import date`) so the type doesn't clash with the field name `date`.

## Learner notes
- The learner prefers to keep moving. When they say "next" or "start X", give a short correction and continue rather than holding them back.
- RULE CHANGE (2026-10-26, from the learner): no review questions at the end of each milestone. Collect them and ask them all at the end of the project (after Milestone 5). Each milestone still ends with a commit + push.
- The `__name__` guard concept is not yet solid. Reinforce it when tests import spend.

## End-of-project review questions (ask after Milestone 5)
- M1: Without the `if __name__ == "__main__":` guard, what happens on `python spend.py` vs `import spend`? (First two answers were off.)
- M2: Why does expense_to_dict turn the date into a string? What happens if it doesn't? (json.dumps raises TypeError: Object of type date is not JSON serializable.)
- M2: When does `except FileNotFoundError:` run in load_expenses, and why not catch every error?
- M2: The file has 2 expenses; then save_expenses([coffee], path). How many are left, and why? (1, because write_text replaces the file.)
- Add 1-2 per later milestone (M3 argparse/validation, M4 dict totals/CSV, M5 tmp_path).

- Conversion uses plain functions `expense_to_dict(expense: Expense) -> dict` and `expense_from_dict(data: dict) -> Expense` (not methods/classmethods, to keep concepts small). Note uses `data.get("note", "")`.

- save_expenses uses a for loop + append (not a list comprehension yet), `json.dumps(data, indent=2)`, and `path.write_text(text, encoding="utf-8")`. `with open` is saved for the CSV export in M4.

- load_expenses uses try/except FileNotFoundError around `path.read_text(encoding="utf-8")`, returning []. Broken JSON is NOT caught yet (it should crash loudly for now; friendly messages come in M3).

- argparse: `build_parser()` returns the parser; subparsers with `dest="command", required=True`; `prog="spend"`. Step 1 keeps amount as a string on purpose so Step 2's `type=float` shows the difference. The greeting print is removed from main.
- `main(argv=None)` for testability is deferred to M5 (a refactor lesson).
- Data file location (decided in M3 Step 4): `DATA_FILE = Path(__file__).parent / "expenses.json"`, so data always sits next to spend.py (git-ignored) no matter which folder `spend` runs from. No --file option; tests call add_expense / load_expenses with tmp_path directly.
- `add_expense(expense, path)` only does load → append → save. Building the Expense from args and printing the confirmation happen in main, which keeps add_expense easy to test.

- Validation lives in argparse `type=` functions that raise argparse.ArgumentTypeError (parse_amount, parse_date, parse_category). Categories are stored as `.strip().lower()` so the report groups "Food" and "food" together.
- Known gap left on purpose: `add nan food` (and `inf`) passes parse_amount, because `nan <= 0` is False. Save it for M5 as a "test finds a bug" lesson (fix with math.isfinite).
- Windows PowerShell 5.1 drops empty "" arguments before Python sees them. Test empty categories with "   " instead.

- pyproject.toml: setuptools backend, name "personal-finance-cli", version 0.1.0, requires-python >=3.12, [project.scripts] spend = "spend:main", [tool.setuptools] py-modules = ["spend"]. Tested in the scratchpad: the editable install works, spend.exe runs from another folder, and the data file lands next to spend.py. The install creates `personal_finance_cli.egg-info/`, so `*.egg-info/` is added to .gitignore. pip prints a "new release available" notice, which is harmless.

## Next
Check M3 Step 6: commit "Add the add command with validation and a spend entry point" contains .gitignore, pyproject.toml, spend.py, TUTOR_PROGRESS.md (learner uses `git add .` for the first time, after checking git status); pushed; 3 commits; working tree clean. Don't edit TUTOR_PROGRESS.md until checked. Then M4 Step 1: report subcommand with --month (parse_month to (year, month), validation).

## Milestone 4 draft plan
1. `report` subparser with `--month YYYY-MM` (parse_month returns the text after validating; default = current month)
2. filter_by_month(expenses, month) returns a list (a list comprehension, introduced here)
3. totals_by_category(expenses) returns a dict (dict.get(key, 0) + amount), sorted by total
4. print_report: aligned table with f-string widths (`{name:<15}{total:>10.2f}`), plus a grand total line
5. --csv PATH option: write the report rows with csv.writer and `with path.open("w", newline="", encoding="utf-8")`
6. Commit + push (checkpoint: `spend report --month 2026-10` works)
