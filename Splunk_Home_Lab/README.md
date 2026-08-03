# 🔷 Enterprise Splunk SIEM Home Lab

<div align="center">

![Splunk](https://img.shields.io/badge/SIEM-Splunk-black?style=for-the-badge&logo=splunk)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge&logo=ubuntu)
![Windows](https://img.shields.io/badge/Windows-10-0078D6?style=for-the-badge&logo=windows)
![Apache](https://img.shields.io/badge/Apache-Web%20Server-D22128?style=for-the-badge&logo=apache)
![Fortinet](https://img.shields.io/badge/FortiGate-Firewall-EE3124?style=for-the-badge&logo=fortinet)
![SOC](https://img.shields.io/badge/SOC-Lab-blue?style=for-the-badge)
![Blue Team](https://img.shields.io/badge/Blue-Team-success?style=for-the-badge)

*A complete enterprise-style Splunk SIEM laboratory demonstrating log collection, data ingestion, centralized monitoring, dashboard development, security investigations, and SOC workflows.*

</div>

---

# 📖 Project Overview

This repository documents the design, deployment, and operation of an **Enterprise Splunk SIEM Home Lab** built to simulate a real-world **Security Operations Center (SOC)** environment.

The lab integrates multiple data sources—including **Windows endpoints**, **Apache Web Server**, and a **FortiGate Firewall**—into **Splunk Enterprise** for centralized log collection, indexing, visualization, and security monitoring.

Throughout this project, I gained practical experience with **SIEM administration**, **log forwarding**, **dashboard creation**, **search optimization**, **event correlation**, and **security monitoring**, following workflows commonly used by SOC Analysts, Detection Engineers, and Blue Team professionals.

---

# 🎯 Project Objectives

- Design an enterprise-style Splunk SIEM lab
- Install and configure Splunk Enterprise
- Configure Splunk Universal Forwarder
- Collect and index logs from multiple sources
- Integrate Apache Web Server logs
- Configure FortiGate Syslog forwarding
- Build operational dashboards
- Perform security log analysis
- Practice SOC monitoring workflows
- Improve SIEM administration skills

---

# 🏗️ Lab Architecture

```text
                    Windows Endpoint
                           │
                           │
                Splunk Universal Forwarder
                           │
                           ▼
                   Splunk Enterprise
                  (Ubuntu Linux Server)
                    /              \
                   /                \
        Apache Web Server      FortiGate Firewall
         Access/Error Logs          Syslog
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Splunk Enterprise | SIEM Platform |
| Splunk Universal Forwarder | Log Collection |
| Ubuntu Linux | Splunk Server |
| Windows 10 | Endpoint |
| Apache Web Server | Web Log Source |
| FortiGate Firewall | Firewall Logging |
| Syslog | Log Transport |
| CLI | System Administration |
| TCP/IP | Network Communication |

---

# ⚙️ Project Structure

```text
Enterprise-Splunk-SIEM-Home-Lab/

│
├── 01-Installation/
├── 02-Splunk-Configuration/
├── 03-Universal-Forwarder/
├── 04-Apache-Integration/
├── 05-FortiGate-Integration/
├── 06-Log-Collection/
├── 07-Dashboards/
├── 08-Log-Analysis/
├── 09-Screenshots/
├── 10-Documentation/
└── README.md
```

---

# 🚀 Lab Implementation

## Phase 1 — Splunk Enterprise Deployment

- Installed Splunk Enterprise
- Configured administrative settings
- Verified web interface
- Created indexes
- Configured data management

---

## Phase 2 — Universal Forwarder

Configured Splunk Universal Forwarder for secure log forwarding.

Completed:

- Installation
- inputs.conf
- outputs.conf
- Connectivity testing
- Log forwarding validation

---

## Phase 3 — Apache Log Integration

Integrated Apache Web Server logs into Splunk.

Collected:

- Access Logs
- Error Logs
- HTTP Requests
- Status Codes

---

## Phase 4 — FortiGate Integration

Configured FortiGate Firewall to forward Syslog events.

Collected:

- Firewall Events
- Traffic Logs
- Security Events
- Network Activity

---

## Phase 5 — Dashboard Development

Created dashboards for:

- Log Overview
- Security Events
- Host Activity
- Apache Monitoring
- Firewall Monitoring
- Event Trends

---

## Phase 6 — Security Monitoring

Performed:

- Log Searching
- Event Filtering
- Security Investigation
- Dashboard Analysis
- Data Validation

---

# 📊 Features Implemented

- ✅ Splunk Enterprise Deployment
- ✅ Universal Forwarder Configuration
- ✅ Apache Log Collection
- ✅ FortiGate Syslog Integration
- ✅ Log Indexing
- ✅ Search & Reporting
- ✅ Dashboard Development
- ✅ Event Monitoring
- ✅ Security Log Analysis
- ✅ SIEM Administration

---

# 📸 Evidence Included

This repository contains screenshots demonstrating:

- Splunk Installation
- Web Interface
- Universal Forwarder Configuration
- Apache Integration
- FortiGate Configuration
- Syslog Events
- Search Queries
- Dashboards
- Indexed Logs
- Monitoring Results

---

# 🧠 Skills Demonstrated

- SIEM Administration
- Splunk Enterprise
- Splunk Universal Forwarder
- Log Collection
- Log Parsing
- Data Ingestion
- Event Correlation
- Dashboard Development
- Apache Log Analysis
- FortiGate Integration
- Syslog Configuration
- Security Monitoring
- SOC Operations
- Log Investigation
- Blue Team Operations

---

# 🎓 Key Learning Outcomes

Through this project, I developed practical experience in:

- Deploying and managing Splunk Enterprise
- Building a centralized log management solution
- Configuring Universal Forwarders
- Integrating enterprise log sources
- Developing dashboards for security visibility
- Investigating security events
- Monitoring infrastructure activity
- Understanding SOC monitoring workflows
- Performing SIEM administration tasks

---

# 💼 Career Relevance

This project demonstrates practical skills applicable to:

- SOC Analyst (L1/L2)
- SIEM Engineer
- Detection Engineer
- Security Analyst
- Blue Team Analyst
- Cybersecurity Analyst
- Security Operations Engineer
- Infrastructure Security Engineer

---

# 🏁 Conclusion

The successful completion of this **Enterprise Splunk SIEM Home Lab** demonstrates practical experience in designing, deploying, and operating a centralized security monitoring platform.

By integrating multiple log sources into Splunk Enterprise, configuring data ingestion pipelines, creating dashboards, and performing security investigations, this project reflects real-world SOC workflows used by modern Security Operations Centers.

This repository showcases hands-on experience with SIEM administration, log management, event analysis, and enterprise security monitoring, providing a strong foundation for roles in SOC Operations, Detection Engineering, Threat Hunting, and Blue Team Security.

---

# 👨‍💻 Author

**Muhammad Talha**

**Aspiring Cloud Security Engineer | SOC Analyst | Detection Engineer | SIEM | Splunk | Wazuh | Threat Hunting | Blue Team | MITRE ATT&CK**
