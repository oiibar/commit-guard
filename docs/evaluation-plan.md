# Evaluation Plan

## Software testing

| Level | What is tested |
|---|---|
| Unit | Parser, context extractor, risk scorer |
| Integration | Extension, API, GitHub API, analyzer, ML model |
| End-to-end | Full flow on real commit pages |
| Usability | 5 real users complete four scenarios; task success rate and SUS questionnaire |
| Non-functional | Response time (median and 95th percentile), HTTPS and no tokens in logs, Chrome and Edge compatibility |

## ML evaluation

- **Data:** CVEfixes (vulnerabilities and their fixes from open-source software). Duplicates and noisy labels are removed.
- **Labeling:** Semgrep is run on the pre-fix version of each CVEfixes commit. Alerts on lines changed by the fix are labeled true positives, the other alerts false positives.
- **Split:** project-based or time-based, not random, to prevent data leakage.
- **Limitations:** labels come from a heuristic and are approximate; recall is measured only over alerts that Semgrep raises.

| Metric | Formula | Meaning |
|---|---|---|
| Recall | TP / (TP + FN) | Of all real vulnerabilities, how many are found |
| Precision | TP / (TP + FP) | Of the alerts shown, how many are real |
| F1 | 2 x P x R / (P + R) | Balance of precision and recall |
| FPR | FP / (FP + TN) | Of all false alarms, how many are still shown |
| MCC | (TP x TN - FP x FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN)) | Reliable on imbalanced data (-1 to +1) |
| PR-AUC | Area under the precision-recall curve | Trade-off across thresholds |
| Latency | Time to analyze one commit | Median and 95th percentile |

## Baselines

| ID | Description |
|---|---|
| B1 | Accepts all Semgrep alerts |
| B2 | Semgrep plus a simple rule (for example ignore alerts in test files) |
| B3 | XGBoost on hand-made features |
| Proposed | Semgrep plus CodeBERT with commit context |

## Measurement conditions

Same test set and Semgrep rules for every system; fixed random seeds; 3-5 runs reported as mean and standard deviation; same hardware for latency; runs with and without commit context.

## Success criteria

| Criterion | Target |
|---|---|
| False positive reduction | At least 30% lower FPR than B1, recall drop at most 5 percentage points |
| Latency | Median up to 10s; 95th percentile up to 30s |
| Usability | SUS >= 68 |
| Functional compliance | 100% of Must requirements pass their acceptance criteria |
| NFRs | HTTPS, no tokens in logs; Chrome and Edge tests; unit test coverage at least 60%; Docker and fixed seeds |
