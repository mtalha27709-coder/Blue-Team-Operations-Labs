# 🔷 Enterprise PowerShell Threat Detection & Investigation using Splunk

<div align="center">

![Splunk](https://img.shields.io/badge/SIEM-Splunk-black?style=for-the-badge&logo=splunk)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell)
![Windows](https://img.shields.io/badge/Windows-Event%20Logs-0078D6?style=for-the-badge&logo=windows)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)
![Threat Hunting](https://img.shields.io/badge/Threat-Hunting-success?style=for-the-badge)
![Detection Engineering](https://img.shields.io/badge/Detection-Engineering-blueviolet?style=for-the-badge)

**A real-world SOC investigation focused on detecting malicious PowerShell activity, developing Splunk detections, performing threat hunting, and mapping attacker behavior to the MITRE ATT&CK Framework.**

</div>

---

# 📖 Project Overview

This project demonstrates a complete **SOC investigation and Detection Engineering workflow** for identifying suspicious **PowerShell activity** using **Splunk Enterprise**.

The investigation focuses on detecting attacker techniques commonly observed during **initial compromise, post-exploitation, malware execution, and defense evasion**, including encoded commands, execution policy bypass, hidden execution, and malicious web requests.

Using **Splunk Search Processing Language (SPL)**, Windows PowerShell Operational Logs, and the **MITRE ATT&CK Framework**, this lab simulates how SOC Analysts and Detection Engineers investigate suspicious activity, validate detections, identify Indicators of Compromise (IOCs), and improve enterprise monitoring capabilities.

---

# 🎯 Project Objectives

- Detect malicious PowerShell activity using Splunk
- Identify Base64 encoded PowerShell commands
- Detect Execution Policy Bypass attempts
- Investigate hidden PowerShell execution
- Analyze outbound PowerShell web requests
- Hunt for attacker behavior using SPL
- Identify Indicators of Compromise (IOCs)
- Map detections to the MITRE ATT&CK Framework
- Strengthen Detection Engineering skills
- Document SOC investigation findings

---

# 🏗️ Lab Architecture

```text
Windows Endpoint
(PowerShell Operational Logs)
            │
            ▼
   Splunk Enterprise SIEM
            │
            ▼
     SPL Threat Hunting
            │
            ▼
 IOC Identification & Analysis
            │
            ▼
 MITRE ATT&CK Mapping
            │
            ▼
 Incident Investigation Report
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Splunk Enterprise | SIEM Platform |
| Windows Event Logs | Log Source |
| PowerShell Operational Logs | Endpoint Telemetry |
| SPL | Detection Queries |
| MITRE ATT&CK | Threat Classification |
| Windows 10 | Target Endpoint |

---

# 📂 Project Structure

```text
Enterprise-PowerShell-Threat-Detection/

│
├── README.md
├── Investigation_Report.pdf
├── SPL_Queries.md
├── Logs/
│   └── powershell_logs.txt
├── Screenshots/
│   ├── Encoded_Command.png
│   ├── ExecutionPolicy_Bypass.png
│   ├── Hidden_PowerShell.png
│   ├── Invoke_WebRequest.png
│   ├── Threat_Hunting.png
│   └── Dashboard.png
```

---

# 🔍 Investigation Workflow

```text
PowerShell Logs
        │
        ▼
Splunk Data Ingestion
        │
        ▼
Detection Queries (SPL)
        │
        ▼
Threat Hunting
        │
        ▼
IOC Analysis
        │
        ▼
MITRE ATT&CK Mapping
        │
        ▼
Incident Investigation
        │
        ▼
Security Recommendations
```

---

# 🚀 Investigation Scenarios

### ✅ Encoded PowerShell Detection

Detected Base64 encoded PowerShell commands commonly used to evade detection and execute malicious payloads.

**MITRE:** T1059.001

---

### ✅ Execution Policy Bypass

Identified PowerShell executions attempting to bypass default security restrictions.

**MITRE:** T1562

---

### ✅ Hidden PowerShell Execution

Detected PowerShell launched with hidden windows to avoid user awareness.

**MITRE:** T1027

---

### ✅ Invoke-WebRequest Activity

Investigated outbound HTTP requests initiated by PowerShell to identify possible payload downloads and command-and-control communications.

**MITRE:** T1105

---

### ✅ Threat Hunting

Performed proactive hunting using custom SPL queries to identify suspicious PowerShell behavior and validate detection coverage.

---

# 📊 Indicators of Compromise (IOCs)

| IOC | Description |
|------|-------------|
| Base64 Encoded Commands | Obfuscated PowerShell execution |
| ExecutionPolicy Bypass | Security control bypass |
| Hidden Window Execution | Stealth execution |
| Invoke-WebRequest | Payload retrieval / C2 communication |
| Suspicious Command Lines | Potential attacker activity |

---

# 🛡️ MITRE ATT&CK Mapping

| Tactic | Technique | MITRE ID |
|---------|-----------|-----------|
| Execution | PowerShell | T1059.001 |
| Execution | Command & Scripting Interpreter | T1059 |
| Defense Evasion | Obfuscated Files & Information | T1027 |
| Defense Evasion | Impair Defenses | T1562 |
| Command & Control | Ingress Tool Transfer | T1105 |

---

# 📈 Key Findings

- Base64 encoded PowerShell commands successfully detected.
- Multiple Execution Policy Bypass attempts identified.
- Hidden PowerShell execution observed.
- Outbound web requests investigated.
- Suspicious command-line behavior analyzed.
- Detection coverage validated using SPL.
- Events successfully mapped to MITRE ATT&CK techniques.

---

# ⚠️ Risk Assessment

Potential risks identified include:

- Malware execution
- Payload downloads
- Command-and-control communication
- Defense evasion
- Unauthorized administrative activity
- Post-exploitation behavior
- Lateral movement preparation

---

# 🔐 Security Recommendations

- Enable Script Block Logging
- Enable Module Logging
- Enable PowerShell Transcription
- Monitor Base64 encoded commands
- Alert on Execution Policy Bypass
- Deploy Sysmon for enhanced telemetry
- Investigate suspicious outbound PowerShell traffic
- Restrict unnecessary PowerShell usage
- Develop custom Splunk detection rules
- Continuously validate detection coverage

---

# 💡 Skills Demonstrated

- Detection Engineering
- Splunk Enterprise
- SPL Query Development
- Threat Hunting
- Windows Event Log Analysis
- PowerShell Investigation
- IOC Analysis
- MITRE ATT&CK Mapping
- SOC Investigation
- Incident Response
- Blue Team Operations
- Security Monitoring

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Investigating PowerShell-based attacks
- Developing Splunk detection queries
- Detecting obfuscated PowerShell activity
- Identifying attacker tradecraft
- Performing enterprise threat hunting
- Mapping detections to MITRE ATT&CK
- Conducting SOC investigations
- Improving SIEM detection coverage

---

# 💼 Career Relevance

This project demonstrates practical skills applicable to:

- Detection Engineer
- SOC Analyst (L1/L2)
- Threat Hunter
- Blue Team Analyst
- Incident Responder
- Security Analyst
- SIEM Engineer

---

# 🏁 Conclusion

This project demonstrates an enterprise-style **PowerShell Threat Detection and Investigation** workflow using Splunk Enterprise.

By combining **Splunk SPL**, **PowerShell Operational Logs**, **IOC analysis**, and **MITRE ATT&CK mapping**, the lab reflects the day-to-day responsibilities of SOC Analysts and Detection Engineers responsible for identifying malicious PowerShell activity, validating detections, and strengthening enterprise security monitoring.

This repository serves as a practical portfolio project showcasing hands-on experience in Detection Engineering, Threat Hunting, SIEM Operations, and Blue Team investigations.

---

# 👨‍💻 Author

**Muhammad Talha**

**Aspiring Cloud Security Engineer | SOC Analyst | Detection Engineer | SIEM | Splunk | Wazuh | Threat Hunting | Blue Team | MITRE ATT&CK**
