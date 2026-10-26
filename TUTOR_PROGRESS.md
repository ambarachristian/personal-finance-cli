# Tutor progress: Personal finance CLI

## Where we are
Milestone 2 of 5 · Step 5 (fix blank lines, commit + push). Step given, waiting for the learner's result.

## Environment
- Windows 11, PowerShell terminal inside VS Code.
- Python 3.13.14. `python3` works globally. Inside the venv, use `python` (Windows venvs have no python3.exe).
- git 2.45.1. Global user.name and user.email are already set.
- GitHub CLI (gh) 2.96.0 installed, logged in as ambarachristian (https, repo scope). Credential helper: Git Credential Manager.
- Repo: https://github.com/ambarachristian/personal-finance-cli (public), origin set, main tracks origin/main.

## Milestone plan
1. Project setup: DONE
2. Data model and storage
   1. Expense dataclass (imports + class at the top of spend.py), tried in the REPL
   2. to_dict / from_dict conversion (date <-> "YYYY-MM-DD" string)
   3. save_expenses(expenses, path) with json + pathlib
   4. load_expenses(path), returning [] when the file doesn't exist (first exception lesson). Its check also covers the save → load round trip.
   5. Fix blank lines, commit, push
3. The add command with argparse (amount, category, date default today, optional note, validation)
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

## Next
Check M2 Step 5: blank lines fixed (two before each top-level def), commit "Add Expense dataclass with JSON save and load" includes spend.py + TUTOR_PROGRESS.md, pushed; `git status` clean and up to date with origin/main; 2 commits in the log. Don't edit TUTOR_PROGRESS.md between giving this step and checking it, or status won't be clean. Then M3 Step 1: argparse skeleton with an `add` subcommand. Remind that add = load, append, save (because save replaces the file).
