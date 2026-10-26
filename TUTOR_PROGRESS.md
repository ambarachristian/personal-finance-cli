# Tutor progress: Personal finance CLI

## Where we are
Milestone 5 of 5 · Steps 5-7 given together, at the learner's request (nan bug test + fix, README, final commit + push), plus the end-of-project review questions. Waiting for "done" and the answers.

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
- 2026-10-26 · M3 Step 6 · commit: done. 108efad "Add the add command with validation and a spend entry point" (4 files), pushed, tree clean. First use of `git add .`.
- MILESTONE 3 DONE.
- 2026-10-26 · M4 Step 1 · report + --month: done. parse_month (line 95), report subparser, `elif` in main printing args. All checks matched; help lists {add,report}.
- 2026-10-26 · M4 Step 2 · filter_by_month: done (line 66, list comprehension). Test data added: 30 food 2026-09-15 "september test", 7 coffee 2025-10-03. expenses.json now has 7 entries; Oct 2026 has 5.
- 2026-10-26 · M4 Step 3 · totals_by_category: done (line 74). Oct 2026 gives {'food': 12.5, 'transport': 5.0, 'coffee': 5.95}.
- 2026-10-26 · M4 Step 4 · print_report: done (line 81); main's report branch wired. Oct/Sep/Nov and the default month all print correctly. CHECKPOINT: `spend report --month 2026-10` works. Both commands of "finished when" are now met; only 10+ tests remain.
- 2026-10-26 · M4 Step 5 · CSV export: done. write_report_csv (line 95), --csv on report, main branch updated. october.csv is correct and git-ignored. An empty month writes just the header row.
- 2026-10-26 · M4 Step 6 · commit: done. 0d15398 "Add the report command with monthly totals and CSV export", pushed, tree clean.
- MILESTONE 4 DONE.
- 2026-10-26 · M5 Step 1 · pytest: done. pytest 9.1.1 in .venv; tests/test_spend.py with 2 tests; "2 passed".
- 2026-10-26 · M5 Step 2 · tmp_path tests: done. 5 passed; real expenses.json still has 7 entries. (The learner dropped the blank line between `import datetime` and `import pytest`. Not mentioned.)
- 2026-10-26 · M5 Step 3 · fixture + filter/totals tests: done. 9 passed.
- 2026-10-26 · M5 Step 4 · output tests: done. 12 passed. FINAL CHECKPOINT MET: `spend add` works, `spend report --month 2026-10` works, 10+ tests pass.
- 2026-10-26 · The learner asked for all remaining steps at once ("give the full remaining of activities"). Gave Steps 5, 6 and 7 in one message, followed by the review questions.

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

## End-of-project review questions (asked 2026-10-26, along with Steps 5-7)
1. Without the guard, what would happen when pytest imports spend? (main() runs, argparse reads pytest's arguments, and it errors/exits before any test runs.)
2. Why does expense_to_dict turn the date into a string? (JSON has no date type; json.dumps would raise TypeError.)
3. Why does add_expense load first instead of just calling save_expenses([new], path)? (save replaces the whole file, so the old expenses would be lost.)
4. When does `except FileNotFoundError` run, and why catch only that? (Only when the file is missing; other errors like broken JSON should be visible, not hidden.)
5. Why `type=float` without () but `default=datetime.date.today()` with ()? (Hand argparse the function to call later vs. call it now and use the result.)
6. In totals_by_category, what does `totals.get(category, 0)` do the first time a category appears? (Returns 0 because the key isn't there yet.)
7. Why do the tests use tmp_path instead of DATA_FILE? (A fresh empty folder per test, so the real data is never touched and tests don't affect each other.)

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

- CSV export: `--csv PATH` (type=Path, default None) on report; write_report_csv(totals, path) uses `with path.open("w", newline="", encoding="utf-8")` and csv.writer; header row `category,amount`, amounts formatted "12.50", biggest first, no total row. The CSV path is relative to the current folder (unlike DATA_FILE), and *.csv is git-ignored.

- Tests live in tests/test_spend.py and use `import spend` (works because of the editable install). pytest 9.1.1 verified in the scratch copy: "2 passed", configfile pyproject.toml.

## Next
Check Steps 5-7 together:
- Step 5: test_parse_amount_rejects_nan_and_infinity added (first run: 1 failed, "DID NOT RAISE"); spend.py has `import math` and `if not math.isfinite(amount): raise ... "'{text}' is not a usable amount, e.g. 12.50"` before the `<= 0` check; 13 passed; `spend add nan food` is refused. (Verified in the scratchpad.)
- Step 6: README.md with setup, usage (add, report, --csv), data location, tests.
- Step 7: commit "Add pytest tests, reject nan amounts, and write a README" (README.md, tests/test_spend.py, spend.py, TUTOR_PROGRESS.md; no .pytest_cache), pushed, 5 commits.
Then review the answers to the 7 end-of-project questions, re-explain any that are wrong (especially Q1, the guard), mark the project DONE here, and suggest a final small commit of this file.

## Milestone 5 plan
1. Install pytest (pip install pytest), create tests/test_spend.py with the first 2 tests (parse_category tidies text; parse_amount rejects <= 0 with pytest.raises), run `pytest`. Note: tests import spend, so the `__name__` guard matters here (revisit the M1 concept).
2. Storage tests with tmp_path: save → load round trip; load on a missing file gives []; add_expense keeps existing ones.
3. Report logic tests: filter_by_month (year check), totals_by_category (sum + empty), parse_month/parse_date errors.
4. Output tests: print_report with capsys; write_report_csv content via tmp_path. That reaches 10+ tests.
5. "A test finds a bug": test that `nan` is rejected; it fails; fix parse_amount with math.isfinite; it passes.
6. README.md with install + usage examples; requirements / dev note for pytest.
7. Commit + push; final checkpoint; end-of-project review questions.

## Milestone 4 plan
1. `report` subparser with `--month YYYY-MM`: parse_month returns the first day of the month as a date; the default is the current month
2. filter_by_month(expenses, month) returns a list (compare .year and .month; a list comprehension is introduced here)
3. totals_by_category(expenses) returns a dict (dict.get(key, 0) + amount), sorted by total
4. print_report: aligned table with f-string widths (`{name:<15}{total:>10.2f}`), plus a grand total line
5. --csv PATH option: write the report rows with csv.writer and `with path.open("w", newline="", encoding="utf-8")`
6. Commit + push (checkpoint: `spend report --month 2026-10` works)
