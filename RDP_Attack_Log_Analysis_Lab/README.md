<div align="center">

# 🛡️ Enterprise RDP Brute Force Attack Investigation with Splunk

### 🔍 Detect • Investigate • Correlate • Respond • Report

<p>
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Splunk-Enterprise-black?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SOC-Investigation-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Threat-Hunting-darkgreen?style=for-the-badge"/>
<img src="https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge"/>
</p>

<p>
<img src="https://img.shields.io/badge/Event%20ID-4624-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Event%20ID-4625-red?style=flat-square"/>
<img src="https://img.shields.io/badge/RDP-Logon%20Type%2010-darkgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/SPL-Detection%20Engineering-black?style=flat-square"/>
</p>

</div>

---

# 📖 Project Overview

The **Enterprise RDP Brute Force Attack Investigation with Splunk** demonstrates a real-world Security Operations Center (SOC) investigation into a Remote Desktop Protocol (RDP) brute-force attack using **Splunk Enterprise** and **Windows Security Event Logs**.

The objective of this lab was to detect repeated failed authentication attempts, identify attacker infrastructure, investigate targeted user accounts, correlate failed and successful logins, validate Indicators of Compromise (IOCs), and assess the likelihood of account compromise.

Following a structured SOC investigation methodology, Windows authentication events were ingested into Splunk, analyzed using Search Processing Language (SPL), mapped to the **MITRE ATT&CK Framework**, and documented with professional incident response findings.

This project reflects the day-to-day responsibilities of SOC Analysts, Detection Engineers, Blue Team professionals, and Incident Responders responsible for monitoring enterprise authentication systems.

---

# 🎯 Project Objectives

This investigation focused on the following objectives:

- Detect repeated failed Remote Desktop logins
- Identify brute-force attack patterns
- Investigate attacker source IP addresses
- Analyze targeted user accounts
- Correlate authentication events
- Validate Indicators of Compromise (IOCs)
- Map findings to the MITRE ATT&CK Framework
- Produce professional incident investigation documentation

---

# 🏗️ Investigation Workflow

```text
Windows Authentication Logs
              │
              ▼
      Splunk Log Ingestion
              │
              ▼
 Failed Login Investigation
              │
              ▼
 Source IP Analysis
              │
              ▼
 User Account Analysis
              │
              ▼
 Authentication Correlation
              │
              ▼
 IOC Validation
              │
              ▼
 MITRE ATT&CK Mapping
              │
              ▼
 Risk Assessment
              │
              ▼
 Incident Report
```

---

# 🖥️ Investigation Environment

| Component | Purpose |
|-----------|---------|
| SIEM Platform | Splunk Enterprise |
| Log Source | Windows Security Event Logs |
| Event IDs | 4624 & 4625 |
| Authentication Type | RDP (Logon Type 10) |
| Detection Language | SPL |
| Framework | MITRE ATT&CK |

---

# 📂 Repository Structure

```text
Enterprise-RDP-BruteForce-Investigation/

│
├── README.md
├── Investigation_Report.pdf
├── SPL_Queries.md
│
├── Logs/
│   └── rdp_logs.txt
│
├── Screenshots/
│   ├── Failed_Logins
│   ├── Source_IP_Analysis
│   ├── User_Analysis
│   ├── Threshold_Detection
│   ├── Authentication_Correlation
│   ├── Dashboard
│   └── IOC_Investigation
│
└── MITRE_Mapping/
```

---

# 🔍 Investigation Phases

## 🔹 Phase 1 — Log Collection

Authentication logs were ingested into Splunk for centralized analysis.

Activities included:

- Log Upload
- Data Parsing
- Index Validation
- Event Verification

---

## 🔹 Phase 2 — Failed Authentication Analysis

Repeated failed login attempts were investigated using Windows Security Event ID **4625**.

Analysis focused on:

- Authentication failures
- Failed RDP logins
- Login frequency
- Suspicious authentication patterns

---

## 🔹 Phase 3 — Source IP Investigation

Attacker infrastructure was analyzed by reviewing source IP activity.

Investigation included:

- Source IP frequency
- Geographic analysis (where applicable)
- Failed login volume
- High-risk IP identification

---

## 🔹 Phase 4 — User Account Investigation

Targeted accounts were analyzed to determine attack focus.

Activities included:

- Privileged account targeting
- Username frequency
- Account enumeration indicators
- Authentication attempts

---

## 🔹 Phase 5 — Authentication Correlation

Failed and successful authentication events were correlated to identify possible compromise.

Correlation included:

- Event ID 4625
- Event ID 4624
- Source IP matching
- User account matching
- Authentication timeline

---

## 🔹 Phase 6 — IOC Validation

Indicators of Compromise were extracted and validated.

Examples included:

- Malicious IP Addresses
- Brute-force Activity
- Authentication Failures
- Successful Login After Failures

---

# 🚩 Indicators of Compromise (IOCs)

| IOC Type | Description |
|-----------|-------------|
| Event ID 4625 | Failed Authentication |
| Event ID 4624 | Successful Authentication |
| Logon Type 10 | Remote Desktop Login |
| Repeated Authentication Failures | Brute Force Activity |
| Source IP | Potential Attacker |
| Successful Login After Failures | Possible Account Compromise |

---

# 🗺️ MITRE ATT&CK Mapping

| Tactic | Technique | ID |
|---------|-----------|----|
| Credential Access | Brute Force | T1110 |
| Lateral Movement | Remote Services (RDP) | T1021.001 |
| Defense Evasion | Valid Accounts | T1078 |

---

# 📊 Key Findings

The investigation revealed:

- High-volume failed RDP authentication attempts
- Multiple authentication failures originating from a single source IP
- Repeated attacks targeting privileged accounts
- Successful authentication following repeated failures
- Indicators consistent with brute-force activity
- Potential unauthorized system access requiring immediate investigation

---

# ⚠️ Risk Assessment

Potential organizational risks included:

- Unauthorized Remote Desktop Access
- Credential Compromise
- Privilege Escalation
- Lateral Movement
- Data Exfiltration
- Persistence Within the Environment

---

# 🛡️ Security Recommendations

Recommended defensive actions include:

- Enforce Multi-Factor Authentication (MFA)
- Restrict RDP exposure through VPN
- Configure Account Lockout Policies
- Continuously monitor Windows authentication logs
- Block malicious IP addresses
- Review privileged account activity
- Deploy automated Splunk correlation searches
- Strengthen password policies

---

# 🛠️ Technologies & Tools

### SIEM

- Splunk Enterprise

### Log Sources

- Windows Security Event Logs

### Investigation

- Search Processing Language (SPL)
- Windows Authentication Analysis
- IOC Validation
- MITRE ATT&CK Mapping

---

# 📊 Skills Demonstrated

- Splunk Enterprise
- SPL Query Development
- Windows Event Log Analysis
- Authentication Monitoring
- RDP Investigation
- Brute Force Detection
- Threat Hunting
- SOC Investigation
- Detection Engineering
- IOC Validation
- MITRE ATT&CK Mapping
- Incident Response Documentation

---

# 📚 Learning Outcomes

This project strengthened practical skills in:

- Investigating Windows authentication events
- Detecting brute-force attacks
- Correlating security events
- Writing efficient SPL searches
- Identifying Indicators of Compromise
- Applying MITRE ATT&CK mapping
- Producing professional SOC investigation reports
- Following enterprise incident response workflows

---

# 🚀 Future Enhancements

Future improvements may include:

- Real-time Splunk Alerting
- Risk-Based Alerting (RBA)
- Splunk Enterprise Security Integration
- GeoIP Source IP Enrichment
- Threat Intelligence Integration
- Automated SOAR Response
- Windows Active Directory Attack Detection
- Splunk Dashboards for Authentication Monitoring

---

# 🏆 Conclusion

The **Enterprise RDP Brute Force Attack Investigation with Splunk** demonstrates a complete SOC investigation workflow for identifying and responding to authentication-based attacks in an enterprise environment.

By analyzing Windows Security Event Logs, developing SPL queries, correlating authentication events, validating Indicators of Compromise (IOCs), and mapping adversary behavior to the MITRE ATT&CK Framework, this project showcases practical experience in security monitoring, threat detection, incident investigation, and defensive security operations.

This repository reflects real-world investigative methodologies commonly used by **SOC Analysts, Detection Engineers, Threat Hunters, Blue Team professionals, and Incident Responders** to detect, investigate, and mitigate credential-based attacks.

---

# 📈 Project Status

| Component | Status |
|-----------|--------|
| 📥 Log Collection | ✅ Completed |
| 🔍 Authentication Analysis | ✅ Completed |
| 🌐 Source IP Investigation | ✅ Completed |
| 👤 User Account Analysis | ✅ Completed |
| 🔗 Authentication Correlation | ✅ Completed |
| 🚩 IOC Validation | ✅ Completed |
| 🗺️ MITRE ATT&CK Mapping | ✅ Completed |
| 📄 Investigation Report | ✅ Completed |
| 🎯 Overall Outcome | ✅ Successful |

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a Star!

**Made with ❤️ by Muhammad Talha**

*Building Enterprise SOC • Detection Engineering • Threat Hunting • Blue Team Projects*

</div>
