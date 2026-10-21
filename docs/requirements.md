# Functional and Non-Functional Requirements

Priorities use MoSCoW: **Must** (the project fails without it), **Should** (important, but a working product could exist without it), **Could** (only if time remains).

## Functional requirements

| ID | Requirement | Priority | Acceptance criteria |
|---|---|---|---|
| FR-1 | The extension detects a GitHub commit or pull request page and extracts the repository and commit SHA. | Must | Works on 10 test commit URLs without errors. |
| FR-2 | The extension sends an analysis request to the REST API backend. | Must | The request reliably reaches the backend. |
| FR-3 | The backend fetches the commit diff and metadata via the GitHub REST API. | Must | The diff matches the real GitHub diff for 10 test commits. |
| FR-4 | Context extraction: code changes, surrounding code and commit message. | Must | Context is extracted for at least 90% of changed functions in supported languages. |
| FR-5 | The Semgrep static analyzer is run to obtain the initial alerts. | Must | The analyzer runs and returns alerts for all supported languages. |
| FR-6 | The ML model classifies each alert as true positive or false positive. | Must | Meets the ML evaluation criteria (see evaluation-plan.md). |
| FR-7 | The system outputs an overall commit risk level (Low / Medium / High). | Must | A risk level is returned for 100% of analyzed commits. |
| FR-8 | Vulnerable code lines are highlighted with an explanation, confidence score and suggested fix. | Should | Each finding shows the vulnerability type, a brief description, the confidence score and a suggested fix. |
| FR-9 | User feedback collection (Correct / False alarm). | Should | Feedback is saved to the database for model retraining. |
| FR-10 | Export of analysis results (JSON / CSV). | Could | The user can download a report from the extension UI. |

## Non-functional requirements

| ID | Quality attribute | Requirement | Priority | Acceptance criteria |
|---|---|---|---|---|
| NFR-1 | Performance | Fast processing for typical commits (up to 500 changed lines). | Must | Median latency up to 10 s; 95th percentile up to 30 s. |
| NFR-2 | Security | Secure data transfer over HTTPS; no API tokens in logs. | Must | Passes the security review checklist. |
| NFR-3 | Accuracy | Significant reduction of the false positive rate (FPR). | Must | FPR reduced by at least 30% versus the raw analyzer at similar recall. |
| NFR-4 | Compatibility | Cross-browser support for the extension. | Must | Extension tests pass on the latest Chrome and Edge. |
| NFR-5 | Usability | Intuitive first-time user experience. | Should | At least 80% task success rate; SUS score at least 68. |
| NFR-6 | Maintainability | Modular architecture and API documentation. | Should | Unit test coverage at least 60%. |
| NFR-7 | Reproducibility | Reproducible ML models and deployment. | Should | Fixed random seeds, versioned data, Dockerized setup. |
