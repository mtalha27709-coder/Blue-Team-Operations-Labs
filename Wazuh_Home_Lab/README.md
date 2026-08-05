# 🔷 Enterprise Blue Team SOC Lab with Wazuh, Suricata & pfSense

<div align="center">

![Wazuh](https://img.shields.io/badge/SIEM-Wazuh-0266C8?style=for-the-badge)
![Suricata](https://img.shields.io/badge/IDS-Suricata-EF3B2D?style=for-the-badge)
![pfSense](https://img.shields.io/badge/Firewall-pfSense-212121?style=for-the-badge)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)
![NIST](https://img.shields.io/badge/NIST-SP800--61-success?style=for-the-badge)
![Blue Team](https://img.shields.io/badge/Blue-Team-blue?style=for-the-badge)

**A complete enterprise-style Security Operations Center (SOC) laboratory featuring SIEM deployment, network intrusion detection, firewall monitoring, threat intelligence integration, malware analysis, detection engineering, and a full insider threat incident response simulation.**

</div>

---

# 📖 Project Overview

This repository documents the design, deployment, and operation of an **Enterprise Blue Team SOC Lab** built to simulate the workflows and technologies commonly used in modern **Security Operations Centers (SOC)**.

The lab combines **Wazuh SIEM**, **Suricata IDS**, **pfSense Firewall**, **VirusTotal**, **Threat Intelligence**, **Custom Detection Rules**, **Malware Analysis**, and **Incident Response** into a single enterprise security environment.

The primary objective of this project was to gain practical experience in **security monitoring**, **detection engineering**, **network intrusion detection**, **vulnerability management**, **malware analysis**, **threat hunting**, and **incident response** using industry-standard tools and frameworks.

---

# 🎯 Project Objectives

- Build an enterprise-style Blue Team SOC laboratory
- Deploy and configure Wazuh SIEM
- Implement endpoint monitoring using Wazuh Agents
- Configure File Integrity Monitoring (FIM)
- Develop custom Wazuh detection rules
- Deploy and configure Suricata IDS
- Integrate Suricata alerts into Wazuh
- Configure pfSense firewall logging
- Integrate threat intelligence feeds
- Perform vulnerability assessment
- Conduct malware analysis
- Simulate an insider threat attack
- Perform end-to-end incident response
- Map attacker behavior to MITRE ATT&CK
- Produce professional security documentation

---

# 🏗 Enterprise Lab Architecture

```text
                     Internet
                         │
                         ▼
                    pfSense Firewall
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Ubuntu Server      Windows 10      Kali Linux
 (Wazuh SIEM)         Agent          Attacker + IDS

        │
        ▼

 Threat Intelligence
 VirusTotal
 URLhaus
 Abuse.ch

        │
        ▼

 Malware Analysis
 ANY.RUN
 CyberChef

        │
        ▼

 Detection Engineering
 Incident Response
```

---

# 🛠 Technologies Used

| Category | Technologies |
|------------|-------------|
| SIEM | Wazuh Manager, Indexer, Dashboard |
| IDS | Suricata |
| Firewall | pfSense, iptables, ipset |
| Threat Intelligence | VirusTotal, URLhaus, Abuse.ch |
| Malware Analysis | ANY.RUN, CyberChef, ExifTool, Binwalk, Strings |
| Platforms | Windows 10, Ubuntu Server, Kali Linux |
| Frameworks | MITRE ATT&CK, NIST SP 800-61 |
| Virtualization | VirtualBox |

---

# 📂 Repository Structure

```text
Enterprise-Blue-Team-SOC-Lab/

│
├── 01-Wazuh-SIEM/
├── 02-Detection-Rules/
├── 03-File-Integrity-Monitoring/
├── 04-Suricata-IDS/
├── 05-pfSense-Firewall/
├── 06-Threat-Intelligence/
├── 07-Vulnerability-Management/
├── 08-Malware-Analysis/
├── 09-Incident-Response/
├── 10-MITRE-Mapping/
├── 11-Screenshots/
├── 12-Reports/
└── README.md
```

---

# 🚀 Project Highlights

## 🔹 SIEM Deployment

- Installed Wazuh Manager, Indexer & Dashboard
- Connected Windows & Kali agents
- Configured centralized log collection
- Built enterprise monitoring environment

---

## 🔹 Detection Engineering

Developed custom Wazuh detection rules for:

- New User Creation
- SSH Brute Force
- USB Device Detection
- Custom Insider Threat Detection
- Active Response Automation

---

## 🔹 File Integrity Monitoring

Configured monitoring for critical directories including:

- `/etc`
- `/var/log`
- `C:\Windows\System32`

Validated unauthorized file modifications through Wazuh alerts.

---

## 🔹 Suricata Network IDS

Implemented custom Suricata signatures to detect:

- Nmap Scanning
- HTTP Exploit Attempts
- ICMP Flood Attacks

Integrated `eve.json` alerts into Wazuh for centralized analysis.

---

## 🔹 Firewall Monitoring

Configured pfSense to:

- Route all lab traffic
- Generate firewall logs
- Forward Syslog events to Wazuh
- Provide centralized visibility into network activity

---

## 🔹 Threat Intelligence Integration

Integrated multiple threat intelligence sources:

- VirusTotal
- URLhaus
- Abuse.ch

Validated malicious hashes and indicators automatically during investigations.

---

## 🔹 Vulnerability Management

Performed vulnerability assessments using Wazuh's Vulnerability Detection module.

Activities included:

- CVE Identification
- CVSS Prioritization
- Patch Validation
- Remediation Verification

---

## 🔹 Malware Analysis

Performed both static and dynamic malware analysis.

### Static Analysis

- file
- strings
- exiftool
- binwalk

### Dynamic Analysis

- ANY.RUN Sandbox
- Process Tree Analysis
- Registry Analysis
- Network Activity
- File System Monitoring

Extracted IOCs and converted them into custom detection rules.

---

# 🕵️ Insider Threat Capstone

Performed a complete enterprise incident response simulation.

### Attack Chain

- Data Staging
- Base64 Obfuscation
- HTTP Data Exfiltration
- Anti-Forensics

### Investigation Activities

- Timeline Reconstruction
- IOC Extraction
- CyberChef Analysis
- Detection Rule Development
- MITRE Mapping
- NIST Incident Response Documentation

---

# 🛡 MITRE ATT&CK Techniques

| Technique | Description |
|------------|-------------|
| T1074 | Data Staging |
| T1027 | Obfuscated Files |
| T1048 | Exfiltration Over Alternative Protocol |
| T1070 | Indicator Removal |

---

# 📊 Skills Demonstrated

- SIEM Administration
- Detection Engineering
- Threat Hunting
- Security Monitoring
- Blue Team Operations
- Incident Response
- Malware Analysis
- File Integrity Monitoring
- Network Intrusion Detection
- Firewall Administration
- Threat Intelligence
- Vulnerability Management
- IOC Analysis
- MITRE ATT&CK Mapping
- Security Documentation

---

# 🎓 Key Learning Outcomes

Throughout this project, I gained practical experience in:

- Building an enterprise SOC environment
- Developing custom detection rules
- Performing endpoint and network monitoring
- Integrating threat intelligence
- Conducting malware analysis
- Investigating insider threats
- Developing incident response workflows
- Mapping attacks to MITRE ATT&CK
- Following the NIST Incident Response lifecycle
- Strengthening Detection Engineering capabilities

---

# 💼 Career Relevance

This project demonstrates practical skills applicable to:

- Detection Engineer
- SOC Analyst (L1/L2)
- Blue Team Analyst
- Threat Hunter
- Incident Responder
- Security Operations Engineer
- SIEM Engineer
- Cybersecurity Analyst

---

# 🏁 Conclusion

The successful completion of this **Enterprise Blue Team SOC Lab** demonstrates hands-on experience in designing, deploying, monitoring, and defending an enterprise security environment.

By combining SIEM, IDS, firewall monitoring, threat intelligence, malware analysis, custom detection engineering, and incident response into a unified workflow, this project closely reflects the day-to-day responsibilities of SOC Analysts, Detection Engineers, and Blue Team professionals working in modern enterprise environments.

This repository serves as a comprehensive portfolio project showcasing practical expertise in enterprise defensive security operations.

---

# 👨‍💻 Author

**Muhammad Talha**

**Aspiring Cloud Security Engineer | SOC Analyst | Detection Engineer | SIEM | Wazuh | Splunk | Threat Hunting | Blue Team | MITRE ATT&CK**
