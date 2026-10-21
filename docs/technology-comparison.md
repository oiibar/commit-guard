# Technology Comparison

# Technology Comparison

This section explains which technologies we chose for Commit Guard, which alternatives we considered, and why. Each decision is linked to our requirements

## Decisions

| Decision | Alternatives considered | Selected | Why (linked to requirements) |
|---|---|---|---|
| Backend framework | FastAPI, Django REST Framework, Flask | FastAPI | Same Python ecosystem as the ML pipeline and Semgrep; async I/O for GitHub API calls (NFR Performance); automatic OpenAPI docs (NFR Maintainability). Django adds admin/ORM overhead we do not need; Flask needs extra libraries for validation |
| Database | PostgreSQL, SQLite, MongoDB | PostgreSQL | Relational data (users, commits, findings, feedback) with ACID guarantees; JSONB for raw analyzer output; handles concurrent writes for feedback storage (FR-9). SQLite has limited concurrency; flexible schema of MongoDB is not needed |
| Component communication | REST over HTTPS, WebSocket, gRPC | REST over HTTPS (JSON) | Natively supported by browser extensions via fetch; stateless and easy to test (NFR Security, Maintainability). Analysis takes about 10 s, so status polling is enough. WebSocket adds connection management; gRPC needs a proxy (gRPC-Web) in browsers |
| Static analyzer | Semgrep, CodeQL, Bandit | Semgrep | Multi-language, rule-based, runs on changed files (NFR latency ≤ 10 s). CodeQL builds a code database first, which is heavier; Bandit supports Python only |
| ML model | CodeBERT (fine-tuned), XGBoost on hand-made features, LLM via API | CodeBERT with commit context | Pre-trained on code, fine-tuned on CVEfixes, runs on our server so code does not leave it. XGBoost is fast but needs manual features (kept as baseline B3); LLM API is costly, slower and harder to reproduce (NFR Reproducibility)

## Key takeaways

- **One ecosystem:** Python for backend and ML (FastAPI, Semgrep, CodeBERT), so the model and the API share code and tooling
- **Simple by default:** REST over HTTPS and PostgreSQL are chosen to fit the latency and security requirements without extra infrastructure
- **Privacy and reproducibility:** a local CodeBERT instead of an external LLM API keeps code on our server and allows fixed-seed experiments
- **Trade-offs accepted:** status polling instead of streaming; an on-demand extension instead of automatic webhooks (future work)