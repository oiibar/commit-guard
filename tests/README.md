# Tests

Unit tests for the backend, written with pytest

## How to run

From the root of the repository:

```bash
pip install -r src/backend/requirements.txt
python -m pytest
```

Expected result: `3 passed`

To see the name of each test:

```bash
python -m pytest -v
```

## What is tested

`test_diff_parser.py` checks `added_lines()` from `src/backend/diff_parser.py`:

| Test | Patch | Expected |
|---|---|---|
| `test_added_lines_with_deletion` | one unchanged line, one deleted, two added, one unchanged (`@@ -10,3 +10,4 @@`) | `[11, 12]` |
| `test_new_file_single_line` | new file with one line (`@@ -0,0 +1 @@`) | `[1]` |
| `test_only_deletion_returns_empty_list` | only a deleted line | `[]` |

The tests do not call the GitHub API, so they work without internet and without a token

## Notes

- The test file adds `src/backend` to `sys.path`, so `diff_parser` can be imported when pytest runs from the root
- VS Code (Pylance) may show "Import could not be resolved" for this import. It is only an editor warning, the tests still run
- New tests are added together with new backend files (for example, for the Semgrep output parser and the context extractor)