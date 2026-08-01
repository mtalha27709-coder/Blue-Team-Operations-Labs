# Improved Detection Rules

## Rule 1: Brute Force Detection
IF failed login attempts > 5 in 5 minutes
THEN trigger HIGH severity alert

---

## Rule 2: Account Compromise Detection
IF failed logins followed by success login
THEN flag as suspicious authentication

---

## Rule 3: PowerShell Threat Detection
IF command contains:
- -enc
- ExecutionPolicy Bypass
- Invoke-WebRequest
THEN trigger alert

---

## Rule 4: Lateral Movement Indicator
Multiple logins from same IP to different users
? Investigate suspicious activity