# Backend
FastAPI server: receives repo and SHA from the extension, fetches the commit diff via GitHub API, runs Semgrep and returns results.