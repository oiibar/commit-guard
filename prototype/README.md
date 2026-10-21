# UX Prototype
## 1.Overview 

We are creating an intelligent system for analyzing Git commits to identify potential security vulnerabilities and reduce false-positive alerts using machine learning.

This folder contains the approved UX/UI prototype of the Commit Guard browser extension and its integration with GitHub commit pages.

## 2.Figma Design 
**Design tool:** Figma

**Prototype status:** Approved by the project supervisor

**Figma prototype:** https://www.figma.com/design/VoR6uSJm0GcrpxgoARPnIx/Commit-Guard?node-id=0-1&t=CxOapwv2GMFGicDK-1

## 3.UI Screens
The prototype includes 11 interface screens covering the main functionality and user interaction scenarios.
### 3.1 Browser Extension Popup

### Ready to Analyze
The initial popup screen allows the user to start analyzing the current Git commit.

<img src="designs/Popup%20%C2%B7%20Analyzing%20commit.png" alt="Analyzing Commit" width="350">

### Analyzing Commit
Displays the analysis progress while the system processes the selected commit.

<img src="designs/Popup%20%C2%B7%20Analyzing%20commit.png" alt="Analyzing Commit" width="350">

### No Recent Analyses
Displays an empty state when the user has no previous analyses.

<img src="designs/Popup%20%C2%B7%20No%20recent%20analyses.png" alt="No Recent Analyses" width="350">

### Analysis Error
Displays an error message when the commit analysis cannot be completed.

<img src="designs/Popup%20%C2%B7%20Analysis%20error.png" alt="Analysis Error" width="350">

### Unsupported Language
Informs the user when the selected commit contains a programming language that is not supported by the analysis system.

<img src="designs/Popup%20%C2%B7%20Unsupported%20language.png" alt="Unsupported Language" width="350">

### 3.2 GitHub Commit Page

### High-Risk Commit
Displays detected security findings and the overall risk level directly on a GitHub commit page.

<img src="designs/Commit%20page%20%C2%B7%20High%20risk.png" alt="High-Risk Commit" width="800">

### Finding Details
Provides additional information about an identified security issue.

<img src="designs/Commit%20page%20%C2%B7%20Finding%20detail.png" alt="Finding Details" width="800">

### False Alarm Feedback
Allows the user to mark a security finding as a false alarm.


<img src="designs/Commit%20page%20%C2%B7%20False%20alarm%20feedback.png" alt="False Alarm Feedback" width="800">

### 3.3  History and Settings

### History and Settings
Provides access to previous analyses and extension settings.

<img src="designs/History%20and%20settings.png" alt="History and Settings" width="350">

### Empty History
Displays the interface when no analysis history is available.

<img src="designs/History%20and%20settings%20%C2%B7%20Empty.png" alt="Empty History" width="350">

### Token Saved
Confirms that the user's access token has been saved.

<img src="designs/Settings%20%C2%B7%20Token%20saved.png" alt="Token Saved" width="350">

## 4. Main User Flow
1.The developer opens a GitHub commit page.

2.The developer opens the Commit Guard browser extension.

3.The extension identifies the selected commit.

4.The developer starts the security analysis.

5.The system analyzes the commit using static analysis and machine learning.

6.The results display the risk level and detected security findings.

7.The developer reviews the findings and may mark a finding as a false alarm.

8.The developer can access previous analyses and manage extension settings.


## 5. Prototype Status
The UX/UI prototype has been approved by the project supervisor.

The designs serve as a reference for frontend implementation and future integration with the backend and machine learning components.

YouTrack task: DIPLOMA-20

Git branch: docs/ux-prototype

