# SIEM Log Analysis - Final Report

## Objective
To build a complete SIEM-based detection system for identifying brute-force attacks and malicious PowerShell activity.

---

## Summary
This project simulates real-world SOC operations by analyzing logs and detecting suspicious security events.

---

## Attack Types Detected

### 1. Brute Force Attack
- Multiple failed login attempts detected
- Threshold-based detection applied

### 2. Account Compromise
- Successful login after multiple failures

### 3. PowerShell Attacks
- Encoded commands detected
- Execution policy bypass observed
- Malicious download attempts identified

---

## Detection Techniques Used
- Log correlation
- Pattern recognition
- Threshold-based alerts
- Behavioral analysis

---

## MITRE ATT&CK Mapping
- T1110 ? Brute Force
- T1059.001 ? PowerShell
- T1027 ? Obfuscation
- T1078 ? Valid Accounts

---

## Security Value
This system demonstrates how SOC analysts detect and respond to real-world threats using SIEM tools and log analysis.

---

## Conclusion
The project successfully simulates enterprise-level security monitoring and threat detection workflows.