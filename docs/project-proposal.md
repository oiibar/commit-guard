# Project Proposal - Commit Guard
 Diploma Topic: Development of an intelligent system for contextual analysis of Git commits to identify vulnerabilities and reduce false positives using machine learning methods.

**Project name:** Commit Guard

**University:** Astana IT University

**Group:** SE-2423

**Team:** Aiymzhan Abilgazy, Aibar Tolegenov, Marzhan Tulebayeva

**Supervisor:** Tulebayev Yersultan Bakhytovich

## 1. Problem Statement
Traditional Static Application Security Testing (SAST) tools can generate numerous false-positive alerts and may not adequately consider the context of individual code changes, such as Git diffs and commit messages. As a result, developers may spend significant time reviewing irrelevant warnings. Excessive alert noise can also make genuine security issues harder to prioritize.

Commit Guard proposes to combine static analysis with contextual machine learning to help distinguish relevant security findings from likely false positives when analyzing Git commits.

## 2. Aim 
To develop an intelligent system for contextual analysis of Git commits using machine learning, with the goal of
**reducing false-positive static-analysis alerts while preserving vulnerability recall.**

The effectiveness of this approach will be assessed experimentally rather than assumed in advance.

## 3. Objectives
1. **Analysis and review:** Study scientific publications and existing methods for detecting vulnerabilities in commits and reducing false-positive alerts.
2. **Data work:** Collect, label, clean, and prepare a dataset of Git commits, including code changes and available metadata.
3. **Architecture and backend:** Design the database and implement a server-side REST API with Git integration.
4. **Machine-learning models:** Train and evaluate models that classify security alerts using commit context.
5. **Integration and testing:** Combine the browser extension, backend, static analyzer, and ML component; compare results with baseline approaches such as Semgrep alone, rule-based filtering, and XGBoost where feasible.

## 4. Target Users
|**User group** | **Intented Value** |
|---|---|
|**Software developers**|Receive timely security feedback on commit changes with less irrelevant alert noise.|
|**DevSecOps and cybersecurity specialists**|Support commit-level vulnerability checks and reduce manual triage effort.|
|**QA and code-quality engineers**|Review potential security issues before changes are merged into production branches.|

## 5. Proposed Solution
Commit Guard is planned as a browser extension for GitHub commit and pull-request pages, supported by a backend analysis service. The proposed workflow is:
1. A user opens a supported GitHub commit or pull-request page and requests an analysis.
2. The extension obtains the relevant commit identifier or page context and sends an analysis request to the backend.
3. The backend retrieves and parses Git changes and related metadata.
4. Semgrep produces candidate static-analysis findings.
5. A contextual ML component assesses the findings using available code-change context.
6. The interface displays prioritized findings, their locations, risk indicators, and explanations.

## 6. Expected Outcomes
|Deliverable|Expected result|
|---|---|
|Browser extension|Browser extension for on-demand analysis from GitHub commit or pull-request pages|
|Context-aware ML pipeline|Analysis of code diffs and, when available, commit messages to help reduce false positives.|
|Findings view|Risk indicators, highlighted findings, and understandable explanations.|
|Backend REST API|FastAPI-based service for analysis requests and integration, with PostgreSQL storage as planned in the proposal.|
|Evaluation report| Comparative results for Semgrep-only and proposed filtering methods, including precision, recall, F1, false-positive behavior, and runtime.|

## 7. Project Scope
**In scope**
- Git metadata extraction and code-diff parsing.
- Dataset preparation, labeling, and preprocessing.
- ML/NLP model training and evaluation for contextual alert classification.
- Core REST API using FastAPI and a PostgreSQL database.
- Chrome/Edge browser extension for GitHub analysis.
- Integration with Semgrep static analysis.
- Benchmark-based evaluation against baseline methods.

## 8. Evaluation Approach
The main evaluation question is:

Can a contextual ML filter reduce false-positive Semgrep alerts on Git commit changes without substantially reducing recall for real vulnerabilities?

The planned comparison includes Semgrep, rule-based filtering, and an XGBoost baseline, where a suitable labeled dataset allows fair comparison, against the proposed Semgrep + contextual ML pipeline.

The evaluation will report precision, recall, F1-score, false-positive measures, and analysis latency. The team will document the dataset, labeling procedure, train/test separation, and relevant limitations.

## 9. Project Team and Responsibilities
 |Team member| Role|Main responsibilities|
 |---|---|---|
 |Aiymzhan Abilgazy|Frontend Developer & Data Engineer|Data collection and preprocessing, database design, UI/UX implementation.|
 |Aibar Tolegenov|Machine Learning Engineer|Model development, training, false-positive filtering, baseline comparison, evaluation metrics.|
 |Marzhan Tulebayeva|System Architect & Backend Engineer|System architecture, backend development, integration, and testing.|

 ## 10.Project Resources
- GitHub repository: https://github.com/oiibar/commit-guard.git
- YouTrack project: https://commit-guard.youtrack.cloud/projects/DIPLOMA
