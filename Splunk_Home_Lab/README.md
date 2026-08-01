# ??? Splunk Home Lab – SIEM & Log Management

## ?? Project Overview

This project demonstrates the design and implementation of a **Splunk Home Lab** for Security Information and Event Management (SIEM). The lab was built to simulate real-world SOC environments by collecting, indexing, monitoring, and analyzing logs from multiple sources including Windows systems, Apache Web Server, and FortiGate Firewall.

The project focuses on log collection, data ingestion, event analysis, dashboard creation, and basic security monitoring using Splunk Enterprise.

---

# ?? Objectives

- Install and configure Splunk Enterprise
- Learn SIEM fundamentals
- Collect logs from multiple sources
- Configure Splunk Universal Forwarder
- Integrate Apache Web Server logs
- Configure FortiGate Syslog
- Create Splunk dashboards
- Perform basic log analysis
- Develop SOC monitoring skills

---

# ??? Lab Environment

| Component | Details |
|----------|---------|
| SIEM | Splunk Enterprise |
| Operating System | Ubuntu Linux / Windows |
| Web Server | Apache2 |
| Firewall | FortiGate |
| Log Collection | Splunk Universal Forwarder |
| Protocol | Syslog |

---

# ?? Project Structure

```
Splunk-Home-Lab/
?
??? README.md
??? Installation_Guide.pdf
??? Screenshots/
??? Configurations/
?   ??? inputs.conf
?   ??? outputs.conf
?   ??? props.conf
?
??? Dashboards/
??? Reports/
??? Notes/
```

---

# ??? Lab Architecture

```
Apache Server
        ?
        ?
Universal Forwarder
        ?
        ?
  Splunk Enterprise
        ?
        ?
     FortiGate
        ?
      Syslog
```

---

# ?? Lab Implementation

## Step 1 – Install Splunk Enterprise

Completed:

- Splunk Installation
- Initial Configuration
- Web Interface Access

---

## Step 2 – Configure Splunk

Configured:

- Admin Account
- Default Index
- Search Head
- Data Management

---

## Step 3 – Upload Sample Data

Performed:

- Manual Data Upload
- Data Indexing
- Search Verification

---

## Step 4 – Configure Universal Forwarder

Configured:

- Forwarder Installation
- outputs.conf
- inputs.conf
- Connection to Splunk Server

---

## Step 5 – Apache Log Integration

Configured:

- Apache Access Logs
- Apache Error Logs
- Log Forwarding
- Splunk Indexing

---

## Step 6 – FortiGate Integration

Configured:

- Syslog
- FortiGate Logging
- Log Forwarding
- Splunk Data Collection

---

## Step 7 – Dashboard Creation

Created dashboards for:

- Log Overview
- Event Monitoring
- Search Results
- Basic Security Monitoring

---

## Step 8 – Log Analysis

Performed:

- Search Queries
- Event Filtering
- Log Investigation
- Data Review

---

# ?? Features Implemented

- Splunk Installation
- Data Upload
- Log Indexing
- Universal Forwarder
- Apache Log Collection
- FortiGate Syslog Integration
- Dashboard Creation
- Event Search
- Basic Monitoring
- SIEM Fundamentals

---

# ??? Tools & Technologies

- Splunk Enterprise
- Splunk Universal Forwarder
- Ubuntu Linux
- Windows
- Apache Web Server
- FortiGate Firewall
- Syslog
- CLI
- TCP/IP Networking

---

# ?? Screenshots Included

- Splunk Installation
- Splunk Login
- Introduction to Splunk
- Data Upload
- Data Indexing
- Apache Forwarder Configuration
- Apache Input & Output Configuration
- Apache Log Integration
- FortiGate Installation
- FortiGate Configuration
- FortiGate Dashboard
- Syslog Configuration
- FortiGate Logs in Splunk
- Dashboard Creation
- Data Review
- Search Results

---

# ?? Skills Demonstrated

- SIEM Administration
- Splunk Enterprise
- Log Collection
- Log Forwarding
- Splunk Universal Forwarder
- Apache Integration
- FortiGate Integration
- Syslog Configuration
- Dashboard Development
- Log Analysis
- Security Monitoring

---

# ?? Learning Outcomes

After completing this lab, I gained practical experience in:

- Installing Splunk Enterprise
- Configuring Splunk Universal Forwarder
- Managing data ingestion
- Indexing security logs
- Integrating Apache server logs
- Configuring FortiGate Syslog
- Building Splunk dashboards
- Performing log analysis
- Understanding SOC workflows

---

# ?? Career Relevance

This project demonstrates practical skills relevant to:

- SOC Analyst
- SIEM Engineer
- Blue Team Analyst
- Security Analyst
- Cybersecurity Analyst
- System Administrator
- Network Security Engineer

---

# ?? Conclusion

This Splunk Home Lab simulates a real-world Security Operations Center (SOC) environment by integrating multiple log sources into Splunk Enterprise. Through log collection, indexing, dashboard creation, and event analysis, the project provides hands-on experience with SIEM operations, security monitoring, and incident investigation techniques commonly used by cybersecurity professionals.

---

## ????? Author

**Muhammad Talha**

Cyber Security Student | SOC Analyst | Splunk | SIEM | Blue Team | Threat Hunting | Network Security