# Frontend requirements
# Commit Guard — Frontend Requirements (FR/NFR)
#### **YouTrack task:** DIPLOMA-28 — Documentation: Frontend requirements (FR/NFR)
#### **Status:** Proposed specification; implementation and acceptance tests pending
#### **Scope:** Chrome/Edge extension user interface and its integration boundaries

## 1. Purpose and scope
This document extracts frontend responsibilities from the Commit Guard system-level requirements presented at the first pre-defense. It retains the original FR identifiers, priorities, and acceptance criteria to ensure traceability. It does not claim that the requirements have been implemented or tested.

The extension is intended to operate on supported GitHub commit and pull-request pages, initiate analysis via the backend REST API, and present analysis results. The backend is responsible for retrieving diffs and metadata, extracting code context, running Semgrep, and performing ML classification.

 *The following functional and non-functional requirements are derived from the system-level Requirements Specification documented in requirements.md. Only requirements relevant to the frontend are included, while the original requirement IDs and priorities are preserved for consistency and traceability.*

## 2. Frontend functional requirements
|Original ID|Requirement| Priority |Acceptance criteria from project specification|Frontend responsibility|
|---|---|---|---|---|
|FR-1|Extension detects GitHub commit/PR page and extracts repo/SHA.|Must|Works on 10/10 test commit URLs without errors.|Detect supported pages; extract repository and commit identifier; handle unsupported URLs|
|FR-2|Extension sends an analysis request to the REST API backend.|Must|Request reliably reaches the server.|Initiate the request and handle its loading, success, and failure outcomes.|
|FR-7|Output overall commit risk level (Low / Medium / High).|Must|Risk score returned for 100% of analyzed commits.|Display the risk level returned by the backend; backend owns score generation.|
|FR-8|Highlight vulnerable code lines with explanation, confidence score and suggested fix.|Should|Display vulnerability type and brief description.|Render finding locations and the available explanation, confidence and fix information.|
|FR-9|User feedback collection (Correct / False Alert).|Should|Feedback saved to DB for model retraining.|DB for model retraining.	Capture and submit the user's selection; backend owns persistence and retraining processes.|
|FR-10|Export analysis results (JSON / CSV).|Could|User can download report via extension UI.|Offer download controls for supported result formats.|

## 3. System requirements that the frontend depends on
|Original ID|Requirement|Priority|Original acceptance criteria|Frontend dependency|
|---|---|---|---|---|
|FR-3|Backend fetches commit diff and metadata via GitHub REST API.|Must|Diff matches real GitHub diff for 10 test commits.|The UI supplies a valid repository/commit reference.|
|FR-4|Context extraction (code changes, surrounding code, commit message).|Must|Context extracted for ≥ 90% of functions in supported languages.|Context is processed by backend services.|
|FR-5|Execution of Semgrep static analyzer to fetch initial alerts.|Must|Analyzer outputs alerts for all supported languages.|The UI presents returned findings.|
|FR-6|ML model classifies alerts as True Positive or False Positive.|Must|Meets ML evaluation criteria.|The UI displays available classification output.|

## 4. Non-functional requirements relevant to the frontend
The source slides assign NFRs by quality attribute rather than by numbered ID. The IDs below are local document identifiers, not replacements for the system specification.

|Local ID|Quality attribute|System-level requirement|Priority|Acceptance criteria from project specification|Frontend relevance|
|---|---|----|----|---|----|
|FE-NFR-01|Performance|Fast processing for typical commits (≤ 500 changed lines).|Must|Median latency ≤ 10s; 95th percentile ≤ 30s.|Keep the interface responsive and show progress while the backend processes the request; latency is measured end-to-end.|
|FE-NFR-02|Security|Secure data transfer over HTTPS; no API tokens in logs.|Must|Pass Security Review Checklist.|Use secure API communication; avoid logging tokens or sensitive content.|
|FE-NFR-03|Accuracy|Significant reduction in False Positive Rate (FPR).|Must|FPR reduced by ≥ 30% vs. raw analyzer at similar recall.|Display results accurately; the ML/backend evaluation owns the FPR target.|
|FE-NFR-04|Compatibility|Cross-browser support for extension.|Must|Extension tests pass on latest Chrome & Edge.|Test extension functionality on both browsers.|
|FE-NFR-05|Usability|Intuitive first-time user experience.|Should|≥ 80% task success rate; SUS score ≥ 68.|Provide understandable controls, statuses, and findings; participate in usability testing.|
|FE-NFR-06|Maintainability|Modular architecture & API documentation.|Should|Unit test code coverage ≥ 60%.|Use separable UI components and documented API contracts; track frontend test coverage.|
|FE-NFR-07|Reproducibility|Reproducible ML models and deployment.|Should|Fixed random seeds, versioned data, Dockerized setup|Primarily an ML/deployment requirement; frontend should document its build and configuration during implementation.|

## 5. Main user interaction flow
1. The user opens a supported GitHub commit or pull-request page.
2. The extension identifies the repository and relevant commit reference (FR-1).
3. The user starts an analysis and the extension submits a backend request (FR-2).
4. The interface waits for the response while remaining usable (FE-NFR-01).
5. The interface displays the overall risk level (FR-7) and, when available, detailed findings (FR-8).
6. Optionally, the user submits feedback (FR-9) or exports results (FR-10).
Open design decision: The method for selecting a commit on pull-request pages, the exact API schema, and the location of code highlighting will be defined in DIPLOMA-29 and DIPLOMA-30. They are not finalized by these requirements.

## 6. Acceptance and verification checklist
- FR-1 is verified against 10 supported GitHub commit URLs.
- FR-2 is verified with a backend test endpoint and error handling scenarios.
- FR-7 displays the backend risk level for valid analysis results.
- FR-8 displays vulnerability type and description; extended fields are checked if supported by the API.
- FR-9 feedback is persisted by the backend when the feature is implemented.
- FR-10 downloads valid JSON and CSV files when the feature is implemented.
- Extension compatibility tests pass on the latest Chrome and Edge.
- Security review verifies HTTPS use and absence of token logging.
- Usability testing checks task success and SUS against the specified targets.
- Frontend test coverage is measured against the project's maintainability target.

## 7. Traceability and boundaries
- Source: Commit Guard pre-defense presentation, Requirements Specification slides (FR-1 through FR-10 and Non-Functional Requirements).
- Related project documentation: docs/requirements.md (system-wide requirements).
- Next design tasks: DIPLOMA-29 (Chrome extension architecture) and DIPLOMA-30 (frontend system design).
- Out of scope for this task: Implementing the extension, backend GitHub fetching, Semgrep execution, ML model training, and proving the system-wide FPR target.
This file documents requirements, not completed functionality. Numerical thresholds and priorities reflect the supplied project presentation and should be revised only through team/supervisor agreement.