# ??? Pre-Engagement – Wazuh File Integrity Monitoring (FIM) Configuration

## ?? Overview

Before executing the insider threat simulation, Wazuh File Integrity Monitoring (FIM) was configured to monitor a custom staging directory on the Windows endpoint. By default, Wazuh does not monitor newly created custom directories, making this configuration essential for capturing file creation, modification, and deletion events throughout the attack simulation.

This preparation phase ensured that all attacker actions generated reliable forensic evidence for later investigation.

---

# ?? Objective

The objective of this phase was to configure Wazuh File Integrity Monitoring to observe activity within the `C:\Espionage` directory, enabling the collection of forensic evidence during the insider threat simulation.

---

# ??? Environment

| Component | Description |
|----------|-------------|
| Operating System | Windows 10 |
| SIEM | Wazuh |
| Monitoring Agent | Wazuh Agent |
| Feature | File Integrity Monitoring (Syscheck) |

---

# ?? Staging Directory

The following directory was created to simulate an attacker staging sensitive data before exfiltration.

```text
C:\Espionage
```

---

# ?? Wazuh Agent Configuration

The Wazuh Agent configuration file was updated by adding the staging directory inside the `<syscheck>` section.

```xml
<directories check_all="yes" realtime="yes">
C:\Espionage
</directories>
```

This configuration enables:

- Real-time monitoring
- File creation detection
- File modification detection
- File deletion detection
- Integrity checksum monitoring

---

# ?? Configuration Applied

After updating the configuration:

- Saved the configuration file
- Restarted the Wazuh Agent service
- Verified successful agent registration
- Confirmed the agent status was **Active** within the Wazuh Dashboard

---

# ? Validation

To verify the configuration, a test file was created inside the monitored directory.

Expected outcome:

- File creation alert generated
- Wazuh Rule 550 triggered
- Event successfully indexed within the Wazuh Dashboard

This confirmed that File Integrity Monitoring was functioning correctly before beginning the attack simulation.

---

# ?? Expected Monitoring Events

The configured directory was expected to generate alerts for:

- File Creation
- File Modification
- File Deletion
- Checksum Changes

These events provide the forensic evidence required during the investigation phase.

---

# ?? Evidence

Include screenshots demonstrating:

- Wazuh Agent Active Status
- Updated `ossec.conf`
- `C:\Espionage` directory creation
- Successful File Integrity Monitoring alert (Rule 550)

---

# ?? Security Importance

File Integrity Monitoring is a fundamental security control used to detect unauthorized changes to files and directories. Even if an attacker deletes malicious files after completing their objective, the recorded FIM events remain available for forensic investigation, enabling analysts to reconstruct attacker activity.

---

# ?? Skills Demonstrated

- Wazuh Administration
- File Integrity Monitoring
- Windows Endpoint Monitoring
- SIEM Configuration
- Security Validation
- SOC Preparation
- Blue Team Operations

---

# ? Outcome

The monitoring environment was successfully prepared before the attack simulation. Wazuh File Integrity Monitoring captured file system activity in real time, providing the necessary evidence for threat hunting, forensic analysis, and incident response during the later phases of the project.