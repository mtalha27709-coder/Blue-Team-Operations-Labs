# ?? Blue Team Investigation

## ?? Overview

Following the successful execution of the insider threat simulation, the investigation phase focused on reconstructing the complete attack timeline using Wazuh Security Information and Event Management (SIEM), File Integrity Monitoring (FIM), and CyberChef.

The objective was not only to confirm that malicious activity occurred, but also to determine exactly how the attack unfolded, what data was affected, and how the attacker attempted to evade detection.

This phase demonstrates the practical workflow of a Security Operations Center (SOC) analyst performing threat hunting, forensic analysis, and evidence collection during an insider threat investigation.

---

# ?? Objectives

- Investigate Wazuh File Integrity Monitoring alerts
- Reconstruct the complete attack timeline
- Identify Indicators of Compromise (IOCs)
- Decode the exfiltrated Base64 payload
- Correlate attacker activities with forensic evidence
- Prepare evidence for the Incident Response Report

---

# ??? Investigation Environment

| Component | Purpose |
|----------|---------|
| Wazuh Dashboard | Security Event Investigation |
| File Integrity Monitoring | File Activity Detection |
| Discover | Log Analysis |
| CyberChef | Base64 Decoding |
| Kali Linux | Captured Exfiltrated Evidence |
| Windows Endpoint | Source of Attack |

---

# Investigation Workflow

```
Attack Completed
        ?
        ?
Collect Wazuh Alerts
        ?
        ?
Threat Hunting
        ?
        ?
Timeline Reconstruction
        ?
        ?
Decode Exfiltrated Data
        ?
        ?
Evidence Collection
```

---

# ?? Investigation Tasks

## Task 1 — FIM Threat Hunting

The investigation began by reviewing File Integrity Monitoring alerts generated throughout the attack.

The following Wazuh rule IDs were analyzed:

| Rule ID | Description |
|---------|-------------|
| 550 | File Creation / Modification |
| 553 | File Deletion |

For each alert, the following information was collected:

- Timestamp
- File Path
- Event Type
- Agent Name
- User Context (when available)
- Rule ID

These events were used to reconstruct the attack timeline.

---

## Task 2 — Timeline Reconstruction

Using the collected security events, the entire attack sequence was reconstructed.

### Timeline

| Stage | Activity |
|--------|----------|
| 1 | Confidential file created |
| 2 | Base64 file generated |
| 3 | Data exfiltrated to Kali Linux |
| 4 | Files deleted from endpoint |

The reconstructed timeline confirmed that the attacker attempted to conceal their activity by deleting the staged files after successful exfiltration.

---

## Task 3 — Evidence Decoding

The Base64 payload captured on the Kali Linux listener was analyzed using CyberChef.

The payload was decoded back into its original plaintext, revealing the confidential client information that had been staged and exfiltrated during the attack.

This step confirmed the exact data targeted by the attacker and provided direct forensic evidence of the data exfiltration.

---

# ?? Indicators of Compromise (IOCs)

The following indicators were identified during the investigation.

| IOC Type | Value |
|----------|-------|
| Directory | `C:\Espionage` |
| Sensitive File | `Client_Database.txt` |
| Encoded File | `system_cache.b64` |
| Tool | `certutil.exe` |
| Protocol | HTTP POST |
| Port | 8080 |

---

# ?? MITRE ATT&CK Mapping

| Technique | Description |
|-----------|-------------|
| T1074 | Data Staged |
| T1027 | Obfuscated Files or Information |
| T1048 | Exfiltration Over Alternative Protocol |
| T1070 | Indicator Removal on Host |

---

# ?? Evidence Collected

The investigation produced the following forensic evidence:

- File Creation Alerts
- File Modification Alerts
- File Deletion Alerts
- Wazuh Discover Logs
- Attack Timeline
- CyberChef Decoded Output
- Base64 Payload
- IOC Summary

---

# ?? Investigation Findings

The investigation confirmed that an insider successfully staged confidential data inside the monitored directory before encoding it into Base64 format. The encoded payload was then transferred over HTTP to an attacker-controlled system.

After completing the exfiltration, the attacker attempted to remove all traces by deleting the files. Despite this effort, Wazuh File Integrity Monitoring preserved the necessary security events, allowing the complete attack timeline to be reconstructed and verified.

---

# ?? Skills Demonstrated

- Threat Hunting
- Digital Forensics
- Wazuh Investigation
- File Integrity Monitoring
- IOC Identification
- Timeline Reconstruction
- Evidence Collection
- Log Correlation
- CyberChef Analysis
- MITRE ATT&CK Mapping

---

# ? Outcome

The investigation successfully reconstructed the complete insider threat attack from available security logs and forensic evidence. By correlating Wazuh alerts with decoded exfiltrated data, the full attack lifecycle was identified, documented, and prepared for incident response and detection engineering activities.