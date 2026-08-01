# ? Suspicious PowerShell Activity Investigation using Splunk

## ?? Project Overview

This project demonstrates the investigation of **Suspicious PowerShell Activity** using **Splunk Enterprise**. The objective was to detect malicious PowerShell execution patterns such as encoded commands, execution policy bypass attempts, hidden execution, and outbound web requests that are commonly associated with attacker techniques and post-exploitation activities.

The investigation follows a real-world SOC workflow by analyzing PowerShell execution logs, identifying Indicators of Compromise (IOCs), and mapping the findings to the **MITRE ATT&CK Framework**.

---

# ?? Objectives

- Detect encoded PowerShell commands
- Identify Execution Policy Bypass attempts
- Detect hidden PowerShell execution
- Investigate outbound web requests
- Hunt for suspicious PowerShell behavior
- Develop Splunk detection queries
- Map findings to MITRE ATT&CK
- Document investigation findings

---

# ??? Lab Environment

| Component | Details |
|----------|---------|
| SIEM | Splunk Enterprise |
| Data Source | PowerShell Operational Logs |
| Log Type | PowerShell Execution Logs |
| Framework | MITRE ATT&CK |

---

# ?? Skills Demonstrated

- Splunk SPL
- PowerShell Threat Hunting
- Log Analysis
- Detection Engineering
- Incident Investigation
- MITRE ATT&CK Mapping
- Blue Team Operations
- SOC Investigation

---

# ?? Project Structure

```
PowerShell-Investigation/
?
??? README.md
??? Investigation_Report.pdf
??? SPL_Queries.md
??? Screenshots/
?   ??? Encoded_Command.png
?   ??? ExecutionPolicy_Bypass.png
?   ??? Hidden_PowerShell.png
?   ??? Invoke_WebRequest.png
?   ??? Threat_Hunting.png
?   ??? Dashboard.png
?
??? Logs/
    ??? powershell_logs.txt
```

---

# ?? Investigation Workflow

```
PowerShell Logs
        ?
        ?
Splunk Data Ingestion
        ?
        ?
Encoded Command Detection
        ?
        ?
Execution Policy Analysis
        ?
        ?
Hidden Execution Detection
        ?
        ?
Web Request Investigation
        ?
        ?
Threat Hunting
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

PowerShell execution logs were uploaded into Splunk and indexed for analysis.

---

## Step 2 – Encoded Command Detection

### SPL Query

```spl
index=powershell commandline="*-enc*"
```

Purpose:

- Detect Base64 encoded PowerShell commands
- Identify obfuscated script execution

---

## Step 3 – Execution Policy Bypass

### SPL Query

```spl
index=powershell commandline="*ExecutionPolicy Bypass*"
```

Purpose:

- Detect attempts to bypass PowerShell security restrictions

---

## Step 4 – Web Request Investigation

### SPL Query

```spl
index=powershell commandline="*Invoke-WebRequest*"
```

Purpose:

- Detect payload downloads
- Identify suspicious outbound communications

---

## Step 5 – Hidden PowerShell Execution

### SPL Query

```spl
index=powershell commandline="*Hidden*"
```

Purpose:

- Detect hidden PowerShell windows
- Identify stealthy execution techniques

---

## Step 6 – Threat Hunting

Review all suspicious PowerShell activity and correlate events to identify attacker behavior.

---

# ?? Indicators of Compromise (IOCs)

| IOC Type | Description |
|----------|-------------|
| Encoded Commands | Base64 encoded PowerShell execution |
| Execution Policy Bypass | Security restriction bypass |
| Hidden Execution | Stealth PowerShell execution |
| Invoke-WebRequest | Payload download or external communication |
| Suspicious Command Line | Potential attacker activity |

---

# ??? MITRE ATT&CK Mapping

| Tactic | Technique | MITRE ID |
|---------|-----------|-----------|
| Execution | PowerShell | T1059.001 |
| Execution | Command and Scripting Interpreter | T1059 |
| Defense Evasion | Obfuscated Files and Information | T1027 |
| Defense Evasion | Impair Defenses | T1562 |

---

# ?? Key Findings

- Encoded PowerShell commands detected
- Execution Policy Bypass attempts observed
- Hidden PowerShell execution identified
- Outbound web requests detected
- Suspicious command-line behavior analyzed
- Multiple events aligned with common attacker techniques

---

# ?? Risk Assessment

Potential risks include:

- Malware execution
- Script-based attacks
- Payload download
- Defense evasion
- Unauthorized administrative activity
- Post-exploitation behavior

---

# ??? Security Recommendations

- Enable PowerShell Script Block Logging
- Enable Module Logging
- Enable PowerShell Transcription
- Monitor encoded PowerShell commands
- Alert on Execution Policy Bypass attempts
- Investigate outbound web requests
- Deploy Sysmon for enhanced visibility
- Restrict unnecessary PowerShell usage
- Continuously monitor PowerShell activity in Splunk

---

# ?? Learning Outcomes

After completing this project, I gained practical experience in:

- Investigating PowerShell-based attacks
- Writing Splunk SPL queries
- Detecting obfuscated PowerShell execution
- Identifying attacker techniques
- Mapping findings to MITRE ATT&CK
- Performing threat hunting
- Conducting SOC investigations
- Building PowerShell detection logic

---

# ?? Career Relevance

This project demonstrates practical skills relevant to:

- SOC Analyst (L1/L2)
- Blue Team Analyst
- Threat Hunter
- Incident Responder
- Detection Engineer
- Security Analyst

---

# ?? Conclusion

This project demonstrates a practical SOC investigation of suspicious PowerShell activity using Splunk Enterprise. By identifying encoded commands, execution policy bypass attempts, hidden execution, and outbound web requests, the investigation highlights attacker tradecraft commonly seen during post-exploitation. The project strengthens hands-on experience in threat hunting, detection engineering, and PowerShell security monitoring.

---

## ????? Author

**Muhammad Talha**

Cyber Security Student | SOC Analyst | Splunk | Threat Hunting | Blue Team | Detection Engineering | MITRE ATT&CK