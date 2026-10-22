import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"/"backend"))


from diff_parser import added_lines

def test_added_lines_with_deletion():
    patch="\n".join([
        "@@ -10,3 +10,4 @@",
        " x = 1",
        "-return None",
        '+query = "SELECT" + user_id',
        "+return run(query)",
        " y = 2",
    ])
    assert added_lines(patch)==[11,12]

def test_new_file_single_line():
    patch="@@ -0,0 +1 @@\n+# Diagrams"
    assert added_lines(patch)==[1]

def test_only_deletion_returns_empty_list():
    patch="@@ -5,2 +5 @@\n a\n-b"
    assert added_lines(patch)==[]
    