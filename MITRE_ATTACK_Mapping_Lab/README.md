<div align="center">

# 🛡️ MITRE ATT&CK Detection Lab with Splunk

### 🔍 Detect • Hunt • Investigate • Map • Improve

<p>
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Splunk-Enterprise-black?style=for-the-badge&logo=splunk"/>
<img src="https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Threat-Hunting-darkgreen?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Detection-Engineering-blue?style=for-the-badge"/>
</p>

<p>
<img src="https://img.shields.io/badge/SPL-Query%20Language-000000?style=flat-square"/>
<img src="https://img.shields.io/badge/Windows-Event%20Logs-0078D6?style=flat-square&logo=windows"/>
<img src="https://img.shields.io/badge/SOC-Investigation-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Blue-Team-0052CC?style=flat-square"/>
</p>

</div>

---

# 📖 Project Overview

The **MITRE ATT&CK Detection Lab with Splunk** is a hands-on Security Information and Event Management (SIEM) project designed to simulate real-world Security Operations Center (SOC) investigations using **Splunk Enterprise** and the **MITRE ATT&CK Framework**.

Rather than relying on production environments or live malware, this lab uses carefully crafted security events that represent common attacker behaviors. These logs are ingested into Splunk, queried using SPL, mapped to MITRE ATT&CK techniques, and investigated through a structured SOC workflow.

The project provides practical experience in **log analysis, detection engineering, threat hunting, security investigations, and SIEM operations**, helping bridge the gap between theoretical cybersecurity knowledge and enterprise-level defensive practices.

---

# 🎯 Project Objectives

The primary objectives of this lab include:

- Configure Splunk Enterprise for security monitoring
- Import and index custom security logs
- Develop practical SPL search queries
- Detect malicious and suspicious activities
- Perform hypothesis-driven threat hunting
- Map detections to the MITRE ATT&CK Framework
- Strengthen SOC investigation methodologies
- Improve detection engineering skills

---

# 🏗️ Lab Architecture

```text
Custom Security Logs
          │
          ▼
     Splunk Enterprise
          │
          ▼
      Data Indexing
          │
          ▼
      SPL Queries
          │
          ▼
 Threat Detection
          │
          ▼
MITRE ATT&CK Mapping
          │
          ▼
 SOC Investigation
          │
          ▼
Detection Validation
          │
          ▼
Detection Improvement
```

---

# 🖥️ Lab Environment

| Component | Technology |
|-----------|------------|
| 📊 SIEM Platform | Splunk Enterprise |
| 📄 Log Source | Custom MITRE Sample Logs |
| 📁 Index | main |
| 📂 Log Format | TXT |
| 🧩 Detection Framework | MITRE ATT&CK |
| 💻 Operating System | Windows |
| 🔎 Query Language | SPL |

---

# 📂 Repository Structure

```text
MITRE-ATTACK-Splunk-Lab/
│
├── README.md
├── mitre_logs.txt
│
├── Queries/
│   └── MITRE_SPL_Queries.md
│
├── Screenshots/
│   ├── Upload
│   ├── Dashboard
│   ├── PowerShell Detection
│   ├── Failed Logins
│   ├── Discovery
│   ├── Persistence
│   ├── Credential Access
│   ├── Command & Control
│   ├── Exfiltration
│   └── Ransomware
```

---

# 🔄 Detection Workflow

```text
Generate Security Logs
          │
          ▼
Import into Splunk
          │
          ▼
Index Security Events
          │
          ▼
Analyze using SPL
          │
          ▼
Detect Suspicious Activity
          │
          ▼
Map to MITRE ATT&CK
          │
          ▼
SOC Investigation
          │
          ▼
Detection Validation
          │
          ▼
Improve Detection Coverage
```

---

# 🔍 Detection Scenarios

The lab demonstrates detection logic for several enterprise attack techniques.

### ⚡ Execution

- PowerShell Execution
- Encoded PowerShell Commands
- Script-Based Activity

**MITRE:** T1059.001

---

### 🔑 Credential Access

- Failed Login Attempts
- Brute Force Activity
- LSASS Access
- Credential Dumping Indicators

**MITRE:** T1110 • T1003

---

### 🔎 Discovery

- System Information Discovery
- User Enumeration
- Process Discovery
- Network Enumeration

**MITRE:** T1082 • T1087 • T1057

---

### 🔒 Persistence

- Scheduled Tasks
- Registry Run Keys
- Windows Services

**MITRE:** T1053.005 • T1547

---

### 📡 Command & Control

- HTTP Beaconing
- DNS Tunneling
- Remote Communications

**MITRE:** T1071

---

### 📤 Exfiltration

- Suspicious Data Transfers
- Outbound Connections
- File Exfiltration

**MITRE:** T1041

---

### 💥 Impact

- File Encryption
- Ransomware Simulation
- Shadow Copy Deletion

**MITRE:** T1486

---

# 🧩 MITRE ATT&CK Coverage

The project validates detections across multiple ATT&CK tactics including:

- Initial Access
- Execution
- Persistence
- Discovery
- Credential Access
- Lateral Movement
- Defense Evasion
- Command & Control
- Exfiltration
- Impact

---

# 🛠️ Technologies Used

### SIEM

- Splunk Enterprise

### Detection Engineering

- SPL
- MITRE ATT&CK

### Security Monitoring

- Windows Event Logs
- Custom Security Logs

### Investigation

- Threat Hunting
- IOC Analysis
- Event Correlation

---

# 📊 Skills Demonstrated

- Splunk Administration
- SPL Query Development
- Threat Hunting
- Detection Engineering
- Log Analysis
- MITRE ATT&CK Mapping
- Security Investigation
- Incident Detection
- Blue Team Operations
- SOC Workflow

---

# 📚 Learning Outcomes

This project strengthened my practical understanding of:

- Splunk Enterprise Administration
- Security Log Analysis
- SPL Query Writing
- Threat Hunting Methodologies
- Detection Validation
- MITRE ATT&CK Mapping
- SOC Investigation Workflow
- Enterprise Detection Engineering

---

# 🚀 Future Improvements

Future enhancements may include:

- Windows Event Log Integration
- Sysmon Log Collection
- Sigma-to-Splunk Rule Conversion
- Correlation Searches
- Detection Dashboards
- Alert Automation
- Threat Intelligence Integration
- Detection-as-Code Workflows

---

# 🏆 Conclusion

This project demonstrates the complete lifecycle of **SIEM-based threat detection** using **Splunk Enterprise** and the **MITRE ATT&CK Framework**.

From importing security logs and developing SPL queries to performing threat hunting, mapping attacker techniques, validating detections, and documenting findings, the lab reflects the practical workflow used by SOC Analysts, Detection Engineers, and Blue Team professionals in enterprise security environments.

This repository serves as a strong portfolio project showcasing practical SIEM, threat detection, and detection engineering skills relevant to modern Security Operations Centers.

---

# 📊 Project Status

| Component | Status |
|-----------|--------|
| 🚀 Project | ✅ Completed |
| 📊 Splunk Configuration | ✅ Completed |
| 🔍 Threat Hunting | ✅ Completed |
| 🧩 MITRE ATT&CK Mapping | ✅ Completed |
| 📑 SPL Queries | ✅ Completed |
| 📄 Documentation | ✅ Completed |
| 🏆 Overall Outcome | ✅ Successful |

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a Star!

**Made with ❤️ by Muhammad Talha**

</div>