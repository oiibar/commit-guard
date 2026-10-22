# Literature Review

## 1.Introduction
Automatically identifying vulnerability-fixing commits (VFCs) is a key task for security auditing and patch management. This review covers 12 studies, which fall into four groups:

1.**Datasets:** linking CVEs to commits (CrossVul).

2.**Classical ML and NLP approaches:** classifiers over commit messages and diffs.

3.**Deep learning and graph-based models:** using code context and dependencies.

4.**Hybrid LLM + SLM approaches:** ensembles that combine commit messages and patches.

## 2.Summary Table
| № | Research Study | Main Idea & Methodology | Main Findings | Limitations | Application to our project|
|---|---|---|---|---|---|
| 1 | Nikitopoulos et al. (2021). CrossVul: A Cross-Language Vulnerability Dataset with Commit Data | Built a large-scale cross-language vulnerability dataset linking CVEs directly to Git commits across 40+ programming languages. | Proved that commit diffs and metadata are essential for training robust vulnerability detection models. | Focuses purely on dataset curation and mapping; does not provide an active automated classification or filtering system. | Use CVE-linked code pairs for dataset preparation.|
| 2 | Nguyen et al. (2022). VulCurator: A Vulnerability-Fixing Commit Detector | A deep learning stacking ensemble combined with an Issue Linker to identify vulnerability-fixing commits. | Achieved high accuracy in identifying security patches across large repositories like TensorFlow. | Heavily relies on issue tracker links and commit messages; struggles with noise, short commit logs, and code length constraints. | Combine code diffs with commit and issue context.|
| 3 | Jiang et al.(2020).A Machine Learning Approach for Vulnerability Curation  | Applied Word2Vec vectorization and classical ML ensembles (Random Forest, SVM) on patch diffs and commit text. | Demonstrated that classical ML with ensemble meta-learning achieves high execution speed and precision. | Does not utilize advanced transformer models (like CodeBERT/DistilBERT) or structural code graph context (PDG). | Use classical ML as a baseline for model comparison|
| 4 | Zhou & Sharma (2017).Automated identification of security issues from commit messages and bug reports | Applied Natural Language Processing (NLP) classifiers strictly to commit messages and bug report texts. | Showed that developer commit comments contain strong semantic signals about security flaws. | Ignores actual source code changes (diffs), leading to misclassifications and high false positive rates when messages are vague. | Use commit messages and issue reports as extra signals|
| 5| Zheng et al. (2025).Enhancing Vulnerability -Fixing Commit Classification: The Synergy of User-Guided and LLM | Proposes a user-guided DistilBERT message classifier combined with a Qwen LLM patch classifier using a stacking meta-classifier | Achieved 94% F1-score on TensorFlow dataset, outperforming HERMES and VulCurator. | Prone to diminishing returns after iterative human interventions (over-intervention risks overfitting); high computational cost for long contexts. | Incorporate human feedback to improve uncertain predictions|
| 6 | Li et al. (2023).Commit-level, Neural VulnerabilityDetection and Assessment | Context-aware, graph-based model (VDA) using Multi-Task Learning to jointly perform vulnerability detection and CVSS assessment. | Outperformed DeepCVA by 25–33% in F1/MCC and improved detection over baselines | Does not work well for code changes affecting distant, unchanged parts; fails on complex event-driven program dependencies. | Consider code dependencies when evaluating contextual limitations|
| 7 | Wan Liuyang (2019).Automated Vulnerability Detection System Based on Commit Messages. | Built a web-based triage system for manual labeling and implemented a deep neural network (LSTM + CNN) on commit messages. | Achieved precision up to 0.88 and recall of 0.89 on C datasets, outperforming K-fold stacking. | Keyword-filtering relies on regex matching, which can accidentally filter out security-relevant commits lacking specific keywords; restricted to text analysis. | Avoid relying only on commit messages and security keywords|
| 8 | Loose et al. (2026). A Comprehensive Evaluation of Code Language Models for Security Patch Detection | Analysis of code language models for software security tasks. | Assessing the effectiveness of generative and encoder models in vulnerability analysis. | Resource requirements for inference and fine‑tuning on specific code. | Evaluate false positives and generalization with project-separated tests|
| 9 | Cui et al.(2026). VFCionX: Bridging Large and Small Models for Robust Vulnerability-Fixing Commit Identification | The VFCionX hybrid framework combines LLM and SLM to search for vulnerability fix commits (VFCI) and consists of three modules: Message Classifier, Patch Classifier, Ensemble Classifier.| On a dataset consisting of 5 popular C/C++ repositories (24,630 commits), VFCionX achieves an F1‑score of 81.47%, outperforming the best existing alternatives by 9.42%. | The complexity of the multi‑stage pipeline coordination between the macro‑context of messages and the micro‑context of code patches; sensitivity to the maximum message length and the volume of changes (LOC). | Compare lightweight and hybrid ML approaches|
| 10 | Russell et al.(2019). Automated Vulnerability Detection in Source Code  Using Deep Representation Learning  | The application of machine learning methods for analyzing code version history. | Automated classification of changes to support security audits.| The difficulty of interpreting the features extracted from large commit histories.| Evaluate deep learning as an alternative to traditional detection|
| 11 |Santos et al.(2025). Reducing Software Vulnerabilities Using Machine Learning Static Application Security Testing | A study of security patterns and repository metrics in open‑source software. | Identifying correlations between commit activity and component vulnerabilities. | Dependence on the initial purity of repository metadata and commit history. | Compare ML-based filtering with static analysis results|
| 12 | Dong etal.(2025). VFProber: A Vulnerability-Fixing Identification Framework Based on Code Changes and Semantic Adjustment | Methods for software analysis of repository source code to detect anomalies. | Building security metrics based on the history of changes and the activity of the authors. | Limited adaptability to new programming languages without retraining the heuristics. | Evaluate code-change semantics beyond commit messages|

## 3. Synthesis
### What the literature shows
- **Commit messages alone are not enough:** message-only models produce many false positives when messages are short or vague.
- **The best results come from combining signals:** commit message, code diff and issue context.
- **Hybrid ensembles outperform single models:** Zheng et al. report 94% F1 on TensorFlow, and VFCionX reaches 81.47% F1 on five C/C++ repositories.
- Classical ML (Word2Vec + Random Forest/SVM) remains a fast and precise baseline.

### Common limitations
 - Dependence on the quality of metadata, issue links and commit history.
 - High computational cost and sensitivity to message length and patch size (LOC).
 - Weak generalization to new languages and projects without retraining.
 - Insufficient modeling of code dependencies outside the changed lines.

 ## 4. Implications for Our Project
-  Use CVE-linked commit pairs to prepare the dataset (CrossVul).
- Combine the code diff, commit message and issue context. 
- Use classical ML as a baseline and compare it with hybrid/LLM approaches.
- Evaluate false positives and generalization with project-separated test sets.
- Consider human-in-the-loop feedback for uncertain predictions.
- Compare ML-based filtering with static application security testing (SAST) results.