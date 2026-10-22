# Input (one request per commit)
{
 "schema_version": "1.0",
 "commit": {"repo": "owner/name", "sha": "abc123", "message": "Fix SQL injection in login"},
 "diff": "@@ -10,7 +10,7 @@ ...", # unified diff text for the commit
 "alerts": [
 {"alert_id": "a1", "rule_id": "python.lang.security...", "file": "app/db.py",
 "start_line": 42, "end_line": 42, "severity": "ERROR", "message": "...", "language": "python"}
 ],
 "files": {"app/db.py": "<full file text after change>"} # or the backend sends only needed parts
}

# Output (same order and ids)
{
 "schema_version": "1.0", "model_version": "dummy-0.1", "threshold": 0.5,
 "predictions": [{"alert_id": "a1", "label": "TP", "confidence": 0.87}]
}
