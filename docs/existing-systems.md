# Existing Systems Comparison

We compared five existing systems that reduce noise in security checks or analyze commits, and added Commit Guard as the sixth column. Two of the systems are commercial platforms with free tiers, one is a commercial platform without one, and two are research tools

| Evaluation Criteria | Semgrep Assistant | GitGuardian | GitHub Advanced Security | ZeroFalse | VulCurator | Commit Guard (proposed) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **System Type** | Commercial platform built on top of open-source Semgrep CE | Commercial platform | Commercial platform | Research prototype (arXiv preprint 2510.02534) | Research tool (ESEC/FSE 2022, demo track) | Research prototype (diploma project) |
| **Analyzed Objects** | Semgrep findings: code, dependencies, and secrets | Secrets in commits, pull requests, and repositories | Code via CodeQL, secrets via secret scanning, dependencies via Dependabot | Static analysis findings | Commits: whether a commit fixes a vulnerability | Semgrep findings in a GitHub commit or pull request |
| **Noise Reduction Mechanism** | ML classification of findings as true or false positives with confidence scoring | FP Remover ML model (restricted to generic secrets) | Focus on detection and automated fixes (Autofix); no dedicated AI noise triage found in reviewed sources | LLM-based finding evaluation | Not a noise filter: classifies commits | CodeBERT classifies alerts as true or false positives using commit context |
| **Context Awareness** | Stores developer feedback as project context | Partial | Partial | Data flow traces, code context, and CWE knowledge | Commit messages, code diffs, and task/issue descriptions | Code diff, surrounding code, commit message |
| **Decision Explanation** | Natural language explanations | Risk score (0–100) with explanation | Not specified in open sources | Not specified in open sources | Not specified (classifier output) | Highlighted lines, risk level, confidence score, suggested fix |
| **Claimed Efficiency** | ~60% triage automation; >96% decision agreement rate (vendor data) | Up to 50% false positives removed, 0.3% true positives missed (vendor data) | No data found | Fewer false positives while maintaining coverage (authors) | Up to 16.1% better F1 than baselines (authors) | Target: ≥ 30% lower FPR, recall drop ≤ 5 pp (to be measured) |
| **Availability / Pricing** | Free for teams up to 10 contributors; paid plans start at \$30/month per contributor | Free plan for up to 25 developers; custom enterprise pricing | Paid service (~\$19 to \$30/month per active committer) | Not specified in open sources | Open-source on GitHub | Not decided yet |
| **Trigger Point / Stage** | After scan in CI/CD | Commit and pull request checks | Push protection blocks pushes with secrets; code scanning on pull requests | After analyzer run (post-processing) | After the fact (inspects existing commits) | On demand on GitHub commit and PR pages |

*Data from vendor documentation and publications; pricing checked in October 2026. Efficiency figures are claims of vendors or authors. The values for Commit Guard are design goals, not measured results*

## Key takeaways

- Noise filtering exists, but each tool covers its own scope: Semgrep Assistant works on Semgrep findings, and FP Remover only on generic secrets
- VulCurator classifies whether a commit fixes a vulnerability, but it does not filter static analysis alerts
- Commit Guard filters Semgrep alerts using the context of the commit and shows the result on demand on the GitHub commit page
- Price is not the difference: Semgrep and GitGuardian have free plans for small teams. The difference to be tested is using the commit context as a signal for alert filtering