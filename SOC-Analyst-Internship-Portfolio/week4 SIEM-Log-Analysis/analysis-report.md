# SIEM Log Analysis Report

## Objective
To analyze security logs and identify malicious or suspicious activity using SIEM-based detection techniques.

---

## Methodology
- Created and analyzed structured log dataset
- Applied filtering techniques
- Identified patterns using statistical grouping
- Detected suspicious PowerShell execution
- Identified brute-force login attempts

---

## Analysis Performed

### 1. Brute Force Detection
- Multiple failed login attempts observed
- Same user targeted repeatedly
- Indicates possible brute-force attack

---

### 2. Successful Login After Failures
- Successful login detected after multiple failures
- Suggests possible credential compromise

---

### 3. Suspicious PowerShell Activity
- Encoded PowerShell commands detected (-enc)
- Execution policy bypass attempts identified
- Malicious web requests observed (Invoke-WebRequest)

---

### 4. Hidden Execution Detection
- PowerShell executed in hidden mode
- Indicates possible stealth attack behavior

---

## Security Findings
- Brute-force attack pattern identified
- Suspicious PowerShell execution detected
- External malicious URL access observed
- High-risk command execution behavior detected

---

## MITRE ATT&CK Mapping
- T1059.001 ? PowerShell Execution
- T1110 ? Brute Force Attack
- T1027 ? Obfuscated Files or Information
- T1562 ? Defense Evasion

---

## Conclusion
The SIEM analysis successfully identified multiple attack patterns including brute-force login attempts and malicious PowerShell execution behavior. This demonstrates effective threat detection using log analysis techniques.