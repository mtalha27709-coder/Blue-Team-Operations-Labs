# ??? Detection Engineering

## ?? Overview

Following the investigation of the insider threat incident, the final technical phase focused on **Detection Engineering**. The objective was to improve the organization's detection capability by creating a custom Wazuh rule capable of identifying suspicious Base64-encoded files within a monitored directory.

While the default File Integrity Monitoring (FIM) rules successfully detected file creation and deletion events, they did not specifically identify the creation of encoded payloads. A custom detection rule was therefore developed to generate a high-priority alert whenever a `.b64` file was created or modified inside the staging directory.

This phase demonstrates how security analysts transition from investigating incidents to improving future detection capabilities.

---

# ?? Objectives

- Develop a custom Wazuh detection rule
- Detect suspicious Base64 encoded files
- Generate a high-priority alert
- Reduce attacker dwell time
- Improve visibility for future insider threat activity
- Validate the custom rule within the Wazuh environment

---

# ??? Detection Environment

| Component | Purpose |
|-----------|---------|
| Wazuh Manager | Rule Processing |
| Wazuh Agent | Endpoint Monitoring |
| File Integrity Monitoring | File Event Collection |
| local_rules.xml | Custom Detection Rules |
| Windows 10 | Event Generation |
| Wazuh Dashboard | Alert Verification |

---

# Detection Strategy

The insider used Base64 encoding to disguise sensitive information before exfiltration.

Although Wazuh detected normal file activity, a dedicated detection rule was created to specifically identify encoded payloads stored with the `.b64` extension inside the monitored directory.

The rule generates a **Level 10** alert, allowing SOC analysts to immediately investigate suspicious encoding activity.

---

# Detection Workflow

```text
File Created
      ?
      ?
Wazuh FIM Detects Event
      ?
      ?
Custom Rule Evaluation
      ?
      ?
.b64 File Identified
      ?
      ?
Level 10 Alert Generated
      ?
      ?
SOC Analyst Investigation
```

---

# Custom Detection Rule

The custom rule was added to:

```text
/var/ossec/etc/rules/local_rules.xml
```

### Detection Logic

The rule performs the following actions:

- Detects file creation or modification events
- Monitors only the `C:\Espionage` directory
- Identifies files ending with the `.b64` extension
- Generates a Level 10 alert
- Maps the activity to the MITRE ATT&CK Framework

---

# Rule Validation

After saving the custom rule:

1. The Wazuh Manager service was restarted.
2. The manager log was reviewed for XML parsing errors.
3. The attack simulation was partially repeated by recreating the Base64 file.
4. The custom alert successfully appeared in the Wazuh Dashboard.

This confirmed that the rule was functioning correctly and detecting the intended activity.

---

# Detection Coverage

| Detection | Status |
|-----------|--------|
| File Creation | ? |
| File Modification | ? |
| Base64 File Detection | ? |
| High Severity Alert | ? |
| MITRE ATT&CK Mapping | ? |

---

# MITRE ATT&CK Mapping

| Technique | Description |
|-----------|-------------|
| T1027 | Obfuscated Files or Information |

The attacker encoded sensitive data using Base64 before transferring it across the network. The custom rule was designed to identify this behavior and provide early detection.

---

# Security Value

This custom rule enhances endpoint visibility by detecting encoded payloads that may otherwise appear as ordinary files.

Benefits include:

- Faster detection of suspicious activity
- Reduced investigation time
- Improved SOC visibility
- Enhanced insider threat detection
- Additional monitoring beyond default Wazuh rules

---

# Evidence

Include the following screenshots:

- Custom Rule (`local_rules.xml`)
- Wazuh Manager Restart
- Successful Rule Validation
- Custom Alert in Wazuh Dashboard
- Rule ID and Alert Details

---

# Skills Demonstrated

- Detection Engineering
- Wazuh Rule Development
- XML Rule Authoring
- Security Monitoring
- Threat Detection
- MITRE ATT&CK Mapping
- Alert Validation
- Blue Team Operations

---

# Lessons Learned

During this phase, it became clear that default monitoring provides visibility into general file activity but may not identify specific attacker behaviors. By creating a targeted detection rule, encoded payloads can be detected immediately, enabling faster investigation and response.

Detection Engineering is an essential Blue Team capability because every investigated incident provides an opportunity to improve monitoring and reduce the likelihood of similar attacks succeeding in the future.

---

# ? Outcome

A custom Wazuh detection rule was successfully developed, validated, and integrated into the monitoring environment. The new rule enhanced detection coverage by generating a high-priority alert whenever a suspicious Base64-encoded file was created or modified within the monitored directory, strengthening the organization's ability to detect future insider threat activity.