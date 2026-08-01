# ?? RDP Brute Force Attack Investigation using Splunk

## ?? Project Overview

This project demonstrates the investigation of a **Remote Desktop Protocol (RDP) Brute Force Attack** using **Splunk Enterprise**. The objective was to identify repeated failed RDP login attempts, analyze attacker behavior, investigate targeted user accounts, correlate successful authentication events, and determine whether unauthorized access was achieved.

The investigation follows a real-world Security Operations Center (SOC) workflow using Windows Security Event Logs and Splunk Search Processing Language (SPL).

---

# ?? Objectives

- Detect failed RDP authentication attempts
- Identify brute-force attack patterns
- Analyze attacker source IP addresses
- Investigate targeted user accounts
- Correlate failed and successful logins
- Identify Indicators of Compromise (IOCs)
- Map findings to the MITRE ATT&CK Framework
- Document incident findings and recommendations

---

# ??? Lab Environment

| Component | Details |
|----------|---------|
| SIEM | Splunk Enterprise |
| Data Source | Windows Security Event Logs |
| Log Type | Authentication Logs |
| Event IDs | 4624, 4625 |
| Logon Type | 10 (Remote Desktop Protocol) |
| Framework | MITRE ATT&CK |

---

# ?? Skills Demonstrated

- Splunk SPL
- Log Analysis
- RDP Investigation
- Brute Force Detection
- Threat Hunting
- SOC Investigation
- Windows Security Monitoring
- MITRE ATT&CK Mapping
- Incident Response

---

# ?? Project Structure

```
RDP-BruteForce-Investigation/
?
??? README.md
??? Investigation_Report.pdf
??? SPL_Queries.md
??? Screenshots/
?   ??? Failed_Logins.png
?   ??? Source_IP_Analysis.png
?   ??? User_Analysis.png
?   ??? Threshold_Detection.png
?   ??? Successful_Login.png
?   ??? Correlation.png
?   ??? Dashboard.png
?
??? Logs/
    ??? rdp_logs.txt
```

---

# ?? Investigation Workflow

```
Windows Authentication Logs
            ?
            ?
      Splunk Ingestion
            ?
            ?
 Failed Login Analysis (4625)
            ?
            ?
 Source IP Investigation
            ?
            ?
 User Account Analysis
            ?
            ?
 Brute Force Detection
            ?
            ?
 Successful Login Correlation
            ?
            ?
 IOC Identification
            ?
            ?
 MITRE ATT&CK Mapping
            ?
            ?
 Incident Report
```

---

# ?? Investigation Steps

## Step 1 – Log Collection

Authentication logs were uploaded into Splunk and indexed for analysis.

---

## Step 2 – Failed Login Analysis

### SPL Query

```spl
index=rdp eventcode=4625 logon_type=10
```

Purpose:

- Detect failed RDP logins
- Identify brute-force attempts

---

## Step 3 – Source IP Investigation

### SPL Query

```spl
index=rdp eventcode=4625
| stats count by src_ip
| sort - count
```

Purpose:

- Identify attacker IP addresses
- Rank IPs by failed login attempts

---

## Step 4 – User Account Analysis

### SPL Query

```spl
index=rdp eventcode=4625
| stats count by user
| sort - count
```

Purpose:

- Identify targeted user accounts
- Detect attacks against privileged users

---

## Step 5 – Brute Force Detection

### SPL Query

```spl
index=rdp eventcode=4625
| stats count by src_ip
| where count > 5
```

Purpose:

- Apply threshold-based detection
- Flag suspicious source IPs

---

## Step 6 – Successful Login Correlation

### SPL Query

```spl
index=rdp (eventcode=4624 OR eventcode=4625)
| stats values(eventcode) as codes count by src_ip user
```

Purpose:

- Correlate failed and successful logins
- Identify possible account compromise

---

# ?? Indicators of Compromise (IOCs)

| IOC Type | Value |
|----------|-------|
| Attack Type | RDP Brute Force |
| Failed Login | Event ID 4625 |
| Successful Login | Event ID 4624 |
| Logon Type | 10 (RDP) |
| Activity | Multiple Failed Logins |
| Activity | Successful Login After Failures |

---

# ??? MITRE ATT&CK Mapping

| Tactic | Technique | MITRE ID |
|---------|-----------|-----------|
| Credential Access | Brute Force | T1110 |
| Lateral Movement | Remote Services (RDP) | T1021.001 |
| Defense Evasion | Valid Accounts | T1078 |

---

# ?? Key Findings

- Multiple failed RDP authentication attempts detected.
- A single source IP generated excessive failed login attempts.
- Administrative accounts were repeatedly targeted.
- Successful authentication occurred after repeated failures.
- Attack behavior matched brute-force techniques.
- Potential unauthorized system access identified.

---

# ?? Risk Assessment

Potential risks include:

- Unauthorized system access
- Credential compromise
- Privilege escalation
- Lateral movement
- Data theft
- Persistence within the environment

---

# ??? Security Recommendations

- Enable Multi-Factor Authentication (MFA)
- Restrict RDP access through VPN
- Implement account lockout policies
- Continuously monitor Windows authentication logs
- Investigate suspicious IP addresses
- Review privileged account activity
- Deploy automated Splunk alerts
- Strengthen password policies

---

# ?? Learning Outcomes

After completing this project, I gained practical experience in:

- Investigating RDP brute-force attacks
- Writing Splunk SPL queries
- Correlating Windows Event Logs
- Detecting credential attacks
- Identifying Indicators of Compromise (IOCs)
- Applying MITRE ATT&CK mapping
- Conducting SOC investigations
- Developing incident response documentation

---

# ?? Conclusion

This project demonstrates a complete SOC-style investigation of an RDP brute-force attack using Splunk Enterprise. By analyzing Windows authentication logs, correlating failed and successful login events, identifying attacker behavior, and mapping findings to the MITRE ATT&CK Framework, the investigation highlights practical skills required for SOC Analysts, Blue Team professionals, and Incident Responders.

---

## ????? Author

**Muhammad Talha**

Cyber Security Student | SOC Analyst | Splunk | Threat Hunting | Blue Team | Incident Response | MITRE ATT&CK