# Detection Rules

## Rule 1: Brute Force Detection
IF failed login attempts > 5 from same user or IP
THEN generate alert

---

## Rule 2: Suspicious PowerShell Execution
IF commandline contains:
- -enc
- ExecutionPolicy Bypass
- Invoke-WebRequest
- DownloadString
THEN flag as suspicious

---

## Rule 3: Hidden Execution Detection
IF commandline contains:
- WindowStyle Hidden
THEN flag as high risk

---

## Rule 4: Combined Attack Pattern
IF failed logins followed by successful login
THEN possible brute-force compromise

---

## Rule 5: Threat Intelligence Rule
IF external URL present in PowerShell command
THEN investigate domain reputation