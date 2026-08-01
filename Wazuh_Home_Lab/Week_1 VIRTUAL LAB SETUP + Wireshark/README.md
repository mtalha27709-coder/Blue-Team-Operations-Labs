# Week 1 — SOC Foundations and Lab Setup

## Objective
Build a working defensive lab environment from scratch and develop a practical understanding of network traffic analysis and SIEM architecture.

## What I Did

### Networking Fundamentals
- Reviewed the TCP/IP and OSI models, subnetting, and CIDR notation
- Studied core SOC-relevant ports and protocols: SSH (22), HTTP (80), HTTPS (443), SMTP (25), DNS (53), SMB (445), RDP (3389)
- Captured live traffic with Wireshark and identified multiple protocols (ARP, DNS, HTTP, HTTPS, ICMP) in a real capture

### VirtualBox Lab Setup
- Built a 3-VM lab: **Kali Linux** (attacker machine), **Ubuntu Server** (Wazuh host), **Windows 10** (monitored endpoint)
- Configured dual network adapters on each VM — Host-Only (internal lab communication) + NAT (internet access)
- Verified connectivity between all three VMs and confirmed internet access on each
- Took baseline snapshots of each VM before proceeding to installation work

### Wazuh Manager Installation
- Assigned a static IP to the Ubuntu Server VM on the Host-Only network
- Installed Wazuh Manager, Indexer, and Dashboard using the official quickstart installation
- Verified all three services (`wazuh-manager`, `wazuh-indexer`, `wazuh-dashboard`) active via `systemctl status`
- Logged into the Wazuh Dashboard and explored the Overview, Agents, and Security Events sections

### Wazuh Agent Deployment
- Deployed Wazuh agents on Kali Linux and Windows 10 using the dashboard's deployment wizard
- Confirmed both agents showing as **Active** in the dashboard
- Reviewed `ossec.conf` structure — server block, syscheck block, localfile blocks
- Generated test alerts via repeated failed SSH login attempts from Kali → Ubuntu, confirming the full pipeline (endpoint → manager → dashboard) was working

### Alert Triage
- Spent time navigating the Wazuh Security Alerts view and understanding rule severity levels (0–15)
- Used the Threat Hunting module to filter alerts by agent, time range, and rule level
- Reviewed the MITRE ATT&CK module and how alerts map to it
- Identified the 10 most frequent alert types in the environment and assessed each as routine vs. worth investigating

## Deliverables
- Network topology diagram
- Wireshark capture with identified protocols
- Full Wazuh Manager + Agent installation report with screenshots
- Alert triage report covering 10 alert types with rule ID, level, and analyst assessment

## Key Takeaway
By the end of Week 1, I had a working SIEM pipeline end-to-end — from endpoint activity to a triaged alert on a dashboard — and a working understanding of how log data moves from an agent through to analyst-ready alerts.
