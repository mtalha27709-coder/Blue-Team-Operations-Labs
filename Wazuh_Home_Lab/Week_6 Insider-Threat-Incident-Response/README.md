# ??? Week 6 – Insider Threat Incident Response

## ?? Project Overview

This project demonstrates a complete **end-to-end insider threat simulation** performed as part of the **Cyberster Blue Team Internship – Week 6 Capstone**. The objective was to simulate a realistic insider attack, investigate the incident using Wazuh SIEM and File Integrity Monitoring (FIM), create a custom detection rule, and document the findings through a professional Incident Response Report following the **NIST SP 800-61 Incident Response Framework**.

The project combines both offensive and defensive security operations by allowing the analyst to perform the attack, investigate the generated evidence, engineer a new detection rule, and produce a complete incident report similar to what would be required in a real Security Operations Center (SOC).

---

# ?? Objectives

- Configure Wazuh File Integrity Monitoring (FIM)
- Simulate an Insider Threat attack
- Generate security events using Windows and Kali Linux
- Investigate File Integrity Monitoring alerts
- Decode exfiltrated evidence using CyberChef
- Develop a custom Wazuh detection rule
- Map attacker activities to the MITRE ATT&CK Framework
- Produce a professional Incident Response Report based on NIST SP 800-61

---

# ?? Lab Architecture

```
                +--------------------+
                |     Kali Linux     |
                |  Netcat Listener   |
                +----------+---------+
                           ^
                           | HTTP POST
                           |
+--------------------------+--------------------------+
|                  Windows 10 Victim                  |
|-----------------------------------------------------|
| PowerShell                                          |
| certutil.exe                                        |
| Client_Database.txt                                 |
| system_cache.b64                                    |
|                                                     |
| Wazuh Agent + Sysmon                                |
+--------------------------+--------------------------+
                           |
                           |
                           v
               +------------------------+
               |     Wazuh Server        |
               | Manager + Dashboard     |
               | File Integrity Monitor  |
               +------------------------+
```

---

# ?? Technologies Used

| Category | Technology |
|----------|------------|
| SIEM | Wazuh |
| Operating System | Windows 10 |
| Attack Machine | Kali Linux |
| Monitoring | Wazuh Agent |
| File Integrity Monitoring | Syscheck |
| Detection Engineering | Wazuh Rules |
| Log Analysis | Wazuh Discover |
| Forensics | CyberChef |
| Framework | MITRE ATT&CK |
| Incident Handling | NIST SP 800-61 |

---

# ?? Attack Scenario

A rogue insider gained legitimate access to a Windows endpoint and performed the following activities:

1. Created a confidential client database.
2. Encoded the file into Base64 using CertUtil.
3. Exfiltrated the encoded data to an attacker-controlled Kali Linux listener over HTTP.
4. Deleted all evidence to hide the activity.

Although the attacker attempted to remove the evidence, Wazuh File Integrity Monitoring successfully recorded the events, allowing the complete attack timeline to be reconstructed.

---

# ?? Project Structure

```
Week-6-Insider-Threat-Incident-Response/
?
??? README.md
??? 00-Pre-Engagement-FIM-Configuration/
??? 01-Red-Team-Execution/
??? 02-Blue-Team-Investigation/
??? 03-Detection-Engineering/
??? 04-Incident-Response-Report/
??? 05-Screenshots/
```

---

# ?? Attack Timeline

| Phase | Description |
|---------|-------------|
| Preparation | Configure Wazuh File Integrity Monitoring |
| Data Staging | Create confidential client database |
| Obfuscation | Encode data into Base64 |
| Exfiltration | Transfer data via HTTP POST |
| Anti-Forensics | Delete evidence |
| Investigation | Analyze Wazuh FIM alerts |
| Detection Engineering | Create custom Wazuh rule |
| Incident Response | Produce professional investigation report |

---

# ?? MITRE ATT&CK Mapping

| Technique | Description |
|-----------|-------------|
| T1074 | Data Staged |
| T1027 | Obfuscated Files or Information |
| T1048 | Exfiltration Over Alternative Protocol |
| T1070 | Indicator Removal on Host |

---

# ?? Skills Demonstrated

- Blue Team Operations
- Security Monitoring
- File Integrity Monitoring (FIM)
- Digital Forensics
- Threat Hunting
- Detection Engineering
- Incident Response
- MITRE ATT&CK Mapping
- Wazuh SIEM Administration
- Windows Security Analysis
- CyberChef Evidence Analysis
- Security Documentation

---

# ?? Evidence Collected

The investigation includes:

- File Integrity Monitoring alerts
- File creation events
- File deletion events
- Base64 encoded payload
- CyberChef decoded evidence
- Custom Wazuh detection rule
- Detection validation
- Complete attack timeline
- Incident Response Report

---

# ?? Learning Outcomes

Through this capstone project, I gained practical experience in:

- Conducting a complete insider threat investigation.
- Performing forensic analysis using Wazuh SIEM.
- Reconstructing attack timelines from security logs.
- Engineering custom detection rules for suspicious activity.
- Mapping attacker behavior to the MITRE ATT&CK Framework.
- Writing professional Incident Response documentation following the NIST SP 800-61 standard.

---

# ?? Conclusion

This project demonstrates an end-to-end Security Operations Center (SOC) workflow, beginning with attack execution and ending with detection engineering and incident response. It highlights how effective logging, file integrity monitoring, and structured investigation techniques can uncover malicious activity even after an attacker attempts to remove evidence.