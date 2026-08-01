# ?? Red Team Execution – Insider Threat Simulation

## ?? Overview

This phase simulated the actions of a malicious insider operating from a legitimate Windows endpoint. The objective was to stage sensitive information, disguise it using Base64 encoding, exfiltrate it to an attacker-controlled system, and finally remove the evidence in an attempt to evade detection.

The attack generated realistic security events that were later investigated using Wazuh File Integrity Monitoring (FIM), CyberChef, and custom detection rules.

---

# ?? Objective

The objective of this phase was to simulate a realistic insider threat attack capable of generating forensic artifacts for investigation and incident response.

---

# ??? Lab Environment

| Component | Purpose |
|-----------|---------|
| Windows 10 | Victim Machine |
| Kali Linux | Attacker Machine |
| Wazuh Agent | Endpoint Monitoring |
| Wazuh SIEM | Log Collection & Analysis |
| Netcat | Data Exfiltration Listener |
| PowerShell | Attack Execution |
| CertUtil | Base64 Encoding |

---

# ?? Attack Scenario

A rogue employee with legitimate system access attempted to steal confidential client information.

The attack consisted of four stages:

1. Data Staging
2. Data Obfuscation
3. Data Exfiltration
4. Anti-Forensics Cleanup

---

# ?? Attack Workflow

```
Create Sensitive File
          ?
          ?
Encode File (Base64)
          ?
          ?
HTTP POST Exfiltration
          ?
          ?
Delete Evidence
```

---

# Step 1 — Attacker Listener

A Netcat listener was started on the Kali Linux system to receive exfiltrated data over HTTP.

### Purpose

- Simulate an attacker-controlled server
- Receive stolen data
- Capture forensic evidence

---

# Step 2 — Data Staging

A confidential client database was created inside the monitored directory.

```
C:\Espionage\Client_Database.txt
```

This represented sensitive business information targeted by the insider.

---

# Step 3 — Data Obfuscation

The attacker used Microsoft's built-in **CertUtil** utility to encode the file into Base64.

Generated file:

```
system_cache.b64
```

The filename was intentionally chosen to resemble a legitimate system file in an attempt to avoid casual inspection.

---

# Step 4 — Data Exfiltration

The encoded file contents were transmitted from the Windows endpoint to the Kali Linux listener using an HTTP POST request.

This simulated internal data exfiltration to an attacker-controlled system.

---

# Step 5 — Anti-Forensics

After successfully transferring the data, the attacker deleted every file inside the staging directory.

Objective:

- Remove evidence
- Hide attacker activity
- Complicate forensic investigation

Although the files were deleted, Wazuh File Integrity Monitoring preserved the security events required to reconstruct the attack timeline.

---

# ?? MITRE ATT&CK Mapping

| Technique | Description |
|-----------|-------------|
| T1074 | Data Staged |
| T1027 | Obfuscated Files or Information |
| T1048 | Exfiltration Over Alternative Protocol |
| T1070 | Indicator Removal on Host |

---

# ?? Attack Timeline

| Stage | Activity |
|--------|----------|
| 1 | Netcat Listener Started |
| 2 | Confidential File Created |
| 3 | Base64 File Generated |
| 4 | HTTP Data Exfiltration |
| 5 | Evidence Deleted |

---

# ?? Evidence

Include screenshots for:

- Kali Netcat Listener
- PowerShell Attack Commands
- Client_Database.txt Creation
- system_cache.b64 Creation
- HTTP Exfiltration
- File Deletion
- Wazuh FIM Alerts

---

# ?? Security Impact

This attack demonstrates how an insider with legitimate access can:

- Stage confidential information
- Obfuscate sensitive data
- Transfer information across the network
- Attempt to remove forensic evidence

Without proper endpoint monitoring, these activities could remain undetected.

---

# ?? Skills Demonstrated

- Red Team Simulation
- Insider Threat Emulation
- PowerShell Operations
- Windows Security
- HTTP Data Exfiltration
- Base64 Obfuscation
- MITRE ATT&CK Mapping
- Attack Simulation
- Blue Team Validation

---

# ? Outcome

The insider threat simulation successfully generated realistic security events across multiple stages of the attack lifecycle. These events provided the evidence required for threat hunting, forensic analysis, detection engineering, and the final incident response investigation.