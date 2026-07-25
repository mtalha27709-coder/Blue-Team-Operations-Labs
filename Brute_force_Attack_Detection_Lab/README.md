# ?? Splunk Brute Force Detection Project

## ?? Project Overview

This project demonstrates how to detect **Brute Force Login Attacks** using **Splunk Enterprise** by analyzing Windows Security Event Logs. The project focuses on identifying repeated failed login attempts, analyzing attacker IP addresses, monitoring targeted user accounts, creating detection rules, and configuring automated SOC alerts.

---

# ?? Objective

- Detect failed login attempts.
- Identify brute-force attacks.
- Analyze attacker IP addresses.
- Identify targeted user accounts.
- Create threshold-based detections.
- Build Splunk alerts for SOC monitoring.

---

# ??? Lab Environment

| Component | Details |
|-----------|---------|
| SIEM | Splunk Enterprise |
| Log Source | Windows Event Logs |
| Operating System | Windows |
| Event ID | 4625 (Failed Login) |
| Search Language | SPL (Search Processing Language) |

---

# ?? Skills Demonstrated

- Splunk SPL Queries
- Windows Event Log Analysis
- Brute Force Detection
- Threat Hunting
- SOC Investigation
- Alert Engineering
- Statistical Analysis
- Security Monitoring

---

# ?? Step 1 – Verify Data Collection

Ensure that logs are successfully indexed.

### SPL Query

```spl
index=* sourcetype=*
```

### Expected Result

- Available indexes
- Available sourcetypes
- Log collection verified

---

# ?? Step 2 – Search Windows Security Logs

Filter only Windows Event Logs.

### SPL Query

```spl
index=wineventlog
```

### Expected Result

Display all Windows Security Events.

---

# ?? Step 3 – Detect Failed Login Events

Filter failed login attempts using Event ID **4625**.

### SPL Query

```spl
index=wineventlog EventCode=4625
```

### Event Meaning

| Event ID | Description |
|----------|-------------|
| 4625 | Failed Login Attempt |

---

# ?? Step 4 – Identify Attacking IP Addresses

Count failed login attempts by source IP.

### SPL Query

```spl
index=wineventlog EventCode=4625
| stats count by src_ip
| sort - count
```

### Purpose

- Identify attacker IPs
- Rank IPs by failed login attempts

---

# ?? Step 5 – Detect Targeted User Accounts

Identify which users are being targeted.

### SPL Query

```spl
index=wineventlog EventCode=4625
| stats count by user
| sort - count
```

### Purpose

- Detect targeted accounts
- Identify high-risk users

---

# ?? Step 6 – Apply Brute Force Threshold

Flag IPs with excessive failed logins.

### SPL Query

```spl
index=wineventlog EventCode=4625
| stats count by src_ip
| where count > 5
```

### Detection Logic

- More than **5 failed login attempts**
- Mark as **Suspicious Activity**

---

# ?? Step 7 – Time-Based Detection

Visualize login failures over time.

### SPL Query

```spl
index=wineventlog EventCode=4625
| timechart span=5m count by src_ip
```

### Purpose

Detect:

- Login spikes
- Automated attacks
- Brute-force tools

---

# ?? Step 8 – Advanced Detection

Identify attacker IPs targeting multiple users.

### SPL Query

```spl
index=wineventlog EventCode=4625
| stats count by src_ip user
| where count > 5
| sort - count
```

### Purpose

- Detect coordinated attacks
- Map attacker IPs to targeted users

---

# ?? Step 9 – Configure Splunk Alert

Create an automated detection rule.

## Alert Settings

| Setting | Value |
|----------|-------|
| Alert Type | Scheduled |
| Schedule | Every 5 Minutes |
| Trigger | Number of Results > 0 |
| Action | Email / Webhook |

### Benefit

Generate real-time alerts whenever brute-force activity is detected.

---

# ?? Step 10 – SOC Investigation Summary

### Analyst Interpretation

Potential brute-force attack activity was detected based on repeated failed login attempts originating from single source IP addresses targeting one or more user accounts. Threshold-based detection logic was implemented using Windows Security Event ID **4625** and statistical aggregation in Splunk.

---

# ?? Bonus Detection – Geo-IP Analysis

Identify attacker locations.

### SPL Query

```spl
index=wineventlog EventCode=4625
| iplocation src_ip
| stats count by Country
```

### Purpose

- Detect foreign login attempts
- Identify suspicious countries

---

# ?? Bonus Detection – Success vs Failure Comparison

Compare successful and failed logins.

### SPL Query

```spl
index=wineventlog (EventCode=4625 OR EventCode=4624)
| stats count by EventCode
```

### Event IDs

| Event ID | Description |
|----------|-------------|
| 4624 | Successful Login |
| 4625 | Failed Login |

---

# ?? Detection Workflow

```
Windows Logs
      ?
      ?
Splunk Indexing
      ?
      ?
Event ID 4625 Filter
      ?
      ?
IP Analysis
      ?
      ?
Username Analysis
      ?
      ?
Threshold Detection
      ?
      ?
Time-Based Analysis
      ?
      ?
Alert Generation
      ?
      ?
SOC Investigation
```

---

# ??? MITRE ATT&CK Mapping

| Technique | ID |
|-----------|----|
| Password Guessing | T1110.001 |
| Brute Force | T1110 |
| Valid Accounts | T1078 |


---

# ?? Key Takeaways

- Collected and analyzed Windows Security Event Logs.
- Detected failed login attempts using Event ID **4625**.
- Identified attacker IP addresses and targeted users.
- Implemented threshold-based brute-force detection.
- Visualized login activity over time.
- Configured automated Splunk alerts.
- Enhanced detections with Geo-IP enrichment.
- Compared successful and failed authentication events.
- Applied SOC investigation methodology for threat detection.

---

# ?? Conclusion

This project demonstrates a practical SOC use case by leveraging Splunk Enterprise to detect brute-force attacks through Windows Security Event Logs. It showcases essential blue-team skills including log analysis, SPL query development, threat detection, alert creation, and security monitoring, making it a strong portfolio project for SOC Analyst and Cybersecurity roles.

---

## ????? Author

**Muhammad Talha**

Cyber Security | SOC Analyst | Splunk | Threat Detection | Blue Team | SIEM