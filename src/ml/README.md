# ML Component

## Goal
Classify each Semgrep alert as true positive or false positive using commit context, to cut alert noise without losing real vulnerabilities.

## Scope and limitation
The model only filters what Semgrep found. It does not find new vulnerabilities, so system recall cannot exceed Semgrep's recall.

## Data
- CVEfixes
- Cleaning: remove duplicates and noisy labels

## Labeling
- Take code before the fix commit.
- Run Semgrep on it.
- Alert on a line changed by the fix -> TP. Other alerts -> FP.

## Split
Project-based or time-based (not random).

## Model input/output
- Input: alert(rule, file, line), diff, surrounding code, commit message
- Output: label(TP/FP), confidence(0-1)

## Baselines
- B1 accept all alerts
- B2 Semgrep with simple rule: ignore test files
- B3 XGBoost on hand-made features
- Proposed: Semgrep and CodeBERT with context
- Comparison with and without context

## Metrics
Recall, Precision, F1, FPR, MCC, PR-AUC, latency

## Measurement conditions
Same test set and Semgrep rules, fixed seeds, 3-5 runs: mean +- SD, same hardware for latency.

## Success criteria
- >= 30% fewer false alarms than raw Semgrep at similar recall
- Median analysis time <= 10s