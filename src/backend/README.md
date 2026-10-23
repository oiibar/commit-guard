# Backend

FastAPI server of Commit Guard. It receives the repository and commit SHA from the browser extension, fetches the commit from the GitHub API, runs Semgrep on the changed files and returns the results

Right now only the first steps are done: getting the commit from GitHub, finding the added lines and a running server with `/health`

## Files

| File | What it does | Status |
|---|---|---|
| `fetch_diff.py` | Gets a commit from the GitHub REST API: message, changed files, status and patch of each file | Done |
| `diff_parser.py` | Reads a patch and returns the line numbers added by the commit (from the `@@ -a,b +c,d @@` headers) | Done |
| `main.py` | FastAPI app with the `/health` endpoint | Done |
| `requirements.txt` | Libraries for the backend | Done |

## Why we need the added lines

Semgrep checks the whole file, so it also finds alerts in old code that the commit did not change. We keep only alerts on the lines added by the commit, and `diff_parser.py` gives us these line numbers

Example: for the header `@@ -10,3 +10,4 @@` with one deleted and two added lines, `added_lines()` returns `[11, 12]`. A deleted line does not increase the counter, because we count lines of the new version of the file

## How to run

From the root of the repository:

```bash
pip install -r src/backend/requirements.txt
```

Get the changes of a commit:

```bash
python src/backend/fetch_diff.py <owner> <repo> <sha>
python src/backend/fetch_diff.py oiibar commit-guard 610db04
```

Without arguments the script prints a usage hint and stops

Start the server:

```bash
cd src/backend
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/health, the answer is `{"status": "ok"}`. API docs are at http://127.0.0.1:8000/docs

## Endpoints

| Method | Path | Answer | Status |
|---|---|---|---|
| GET | `/health` | `{"status": "ok"}` | Done |
| POST | `/analyze` | Risk level and findings for a commit | Planned |

## Known limitations

- Only public repositories for now. Private ones need a GitHub token (planned)
- Without a token GitHub allows about 60 requests per hour, after that it returns 403
- For binary and very large files GitHub does not send `patch`, so the script prints a note instead

## Next steps

1. `/analyze` endpoint: takes repo and SHA, returns changed files and added lines
2. `scanner.py`: run Semgrep on the changed files and read its JSON output
3. `context.py`: context of each alert (function around the line with tree-sitter, commit message)
4. `classifier.py`: first a stub that accepts all alerts (baseline B1), later the CodeBERT model
5. `db.py`: save results and "False alarm" feedback to PostgreSQL

Tokens are never committed. They are kept in a local `.env` file, which is in `.gitignore`