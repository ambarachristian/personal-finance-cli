# Tutor progress: Personal finance CLI

## Where we are
Milestone 1 of 5 · Step 5 (first commit). Step given, waiting for the learner's result.

## Environment
- Windows 11, PowerShell terminal inside VS Code.
- Python 3.13.14. `python3` works globally. Inside the venv, use `python` (Windows venvs have no python3.exe).
- git 2.45.1. Global user.name and user.email are already set.
- GitHub CLI (gh) 2.96.0 is installed (can be used for creating the repo in Step 6).

## Milestone plan
1. Project setup
   1. Create and activate a virtual environment (.venv)
   2. git init
   3. .gitignore
   4. spend.py that prints a greeting
   5. First commit
   6. Public GitHub repo and push
   7. Review questions
2. Data model and storage (Expense dataclass, save/load JSON with pathlib + json)
3. The add command with argparse (amount, category, date default today, optional note, validation)
4. The report command (filter by month, totals by category with a dict, aligned table, --csv export)
5. Tests and docs (10+ pytest tests with tmp_path, README)

Finished when: `spend add` and `spend report --month 2026-10` work, and 10+ tests pass.

## Log
- 2026-10-25 · Step 0 · Setup check: done. Python 3.13.14 and git 2.45.1 both work. Project folder was empty.
- 2026-10-25 · M1 Step 1 · venv: done. `python3 -m venv .venv`, activated with `.venv\Scripts\Activate.ps1` (no execution-policy error). pip 26.1.2 inside .venv. Python 3.13 venv writes its own `.venv\.gitignore` containing `*`, so git ignores .venv automatically.

- 2026-10-25 · M1 Step 2 · git init: done. Repo on branch main, no commits yet, TUTOR_PROGRESS.md untracked.

- 2026-10-25 · M1 Step 3 · .gitignore: done. 13 lines (.venv/, __pycache__/, *.pyc, .pytest_cache/, expenses.json, *.csv). check-ignore confirmed line 12.
- 2026-10-25 · M1 Step 4 · spend.py: done. Docstring, `main()` with print, `if __name__ == "__main__":` guard. `python spend.py` prints the greeting.

## Decisions
- The real data file will be `expenses.json` in the project folder. It is git-ignored (personal data), as are `*.csv` exports.

- TUTOR_PROGRESS.md is committed with the project, so resuming works from any copy of the repo.
- core.autocrlf is true (system gitconfig), so "LF will be replaced by CRLF" warnings are expected and harmless.

## Next
Check Step 5 result: `git log --oneline` shows one commit on main; `git status` is clean (TUTOR_PROGRESS.md may show modified after tutor edits; that's expected). Then Step 6: public GitHub repo + push. gh is installed; check `gh auth status` first. Also mention commit email is the hotmail address from git config; if the GitHub account uses another email, add it in GitHub settings so commits link to the profile.
