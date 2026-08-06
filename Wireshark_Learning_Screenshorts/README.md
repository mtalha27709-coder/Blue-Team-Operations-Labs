# 🌐 Wireshark Network Traffic Analysis & Threat Hunting Lab

A hands-on network traffic analysis and threat hunting lab demonstrating practical experience with packet capture, protocol analysis, network troubleshooting, and security investigations using Wireshark.

This project simulates real-world SOC workflows by analyzing captured network traffic to identify suspicious activity, investigate communication patterns, inspect network protocols, and validate potential Indicators of Compromise (IOCs). The lab focuses on developing practical Blue Team skills used by SOC Analysts, Incident Responders, Threat Hunters, and Detection Engineers.

---

# 📌 Project Objectives

- Capture and analyze live network traffic
- Inspect packets across multiple network protocols
- Investigate DNS, HTTP, HTTPS, TCP, UDP, ICMP, and ARP traffic
- Analyze TCP sessions and application-layer communications
- Identify active hosts, endpoints, and communication patterns
- Detect suspicious network behavior using packet analysis
- Perform basic threat hunting using Wireshark
- Validate network-based Indicators of Compromise (IOCs)
- Improve packet analysis and incident investigation skills

---

# 🏗️ Lab Environment

| Component | Details |
|-----------|----------|
| Packet Analyzer | Wireshark |
| Operating Systems | Windows & Ubuntu Linux |
| Network Protocols | TCP/IP, DNS, HTTP, HTTPS, ICMP, ARP |
| Threat Validation | VirusTotal |
| Utilities | PowerShell, Command Prompt |

---

# 🔎 Investigation Methodology

```
Network Traffic Capture
          │
          ▼
Protocol Analysis
          │
          ▼
DNS & Endpoint Investigation
          │
          ▼
TCP Session Analysis
          │
          ▼
Traffic Statistics & Flow Analysis
          │
          ▼
Threat Hunting
          │
          ▼
IOC Validation
          │
          ▼
Investigation Report
```

---

# 📂 Investigation Scenarios

## 1️⃣ Packet Capture & Traffic Collection

Performed live packet capture from active network interfaces.

Activities:

- Interface Selection
- Capture Filters
- Live Packet Collection
- PCAP File Management

---

## 2️⃣ Protocol Analysis

Analyzed multiple network protocols including:

- Ethernet
- IPv4
- IPv6
- TCP
- UDP
- DNS
- HTTP
- HTTPS
- ICMP
- ARP
- DHCP

Focused on packet headers, payloads, protocol behavior, and communication patterns.

---

## 3️⃣ DNS Investigation

Investigated DNS activity to identify suspicious communications.

Analysis Included:

- DNS Queries
- DNS Responses
- Domain Resolution
- Suspicious Domains
- External Name Servers

---

## 4️⃣ TCP Session Analysis

Reviewed complete TCP communications.

Activities:

- Three-Way Handshake
- Session Establishment
- TCP Flags
- Retransmissions
- Follow TCP Stream
- Connection Tracking

---

## 5️⃣ Endpoint & Traffic Analysis

Identified communicating systems and traffic behavior.

Investigated:

- Endpoints
- Conversations
- Top Talkers
- Communication Frequency
- Traffic Volume
- Active Hosts

---

## 6️⃣ Threat Hunting

Performed proactive network investigations to identify suspicious behavior.

Examples:

- Suspicious DNS Queries
- Unknown External Connections
- High-Traffic Endpoints
- Unexpected Network Sessions
- Packet Stream Analysis
- IOC Validation using VirusTotal

---

# 📊 Wireshark Features Used

- Packet Capture
- Display Filters
- Protocol Hierarchy
- Endpoints
- Conversations
- Follow TCP Stream
- IO Graphs
- Packet Bytes
- Expert Information
- Statistics Dashboard

---

# 🔍 Common Display Filters

```text
ip
tcp
udp
dns
arp
icmp
http
https
tcp.port==80
tcp.port==443
dns.qry.name
ip.addr==192.168.1.10
tcp.flags.syn==1
tcp.analysis.retransmission
```

---

# 🛠️ Tools & Technologies

- Wireshark
- Windows
- Ubuntu Linux
- VirusTotal
- PowerShell
- Command Prompt
- TCP/IP Networking

---

# 📂 Repository Structure

```
Wireshark-Network-Traffic-Analysis/

├── README.md
├── PCAP Files/
├── Investigation Reports/
├── Screenshots/
│   ├── Packet Capture
│   ├── DNS Analysis
│   ├── TCP Streams
│   ├── Protocol Hierarchy
│   ├── Endpoints
│   ├── Conversations
│   ├── IO Graphs
│   └── Investigation Results
├── Display Filters/
└── Notes/
```

---

# 🎯 Skills Demonstrated

- Network Traffic Analysis
- Packet Inspection
- Protocol Analysis
- DNS Investigation
- TCP Session Analysis
- Endpoint Analysis
- Network Troubleshooting
- Threat Hunting
- IOC Validation
- Incident Investigation
- Blue Team Operations

---

# 🚀 Career Relevance

This project demonstrates practical skills applicable to:

- SOC Analyst (L1/L2)
- Blue Team Analyst
- Detection Engineer
- Threat Hunter
- Incident Responder
- Network Security Engineer
- Cybersecurity Analyst

---

# ✅ Learning Outcomes

After completing this project, I gained hands-on experience in:

- Capturing and analyzing live network traffic
- Investigating network protocols and communications
- Following TCP conversations
- Performing DNS investigations
- Identifying suspicious network activity
- Validating Indicators of Compromise (IOCs)
- Conducting network-based threat hunting
- Documenting investigation findings

---

# 🏁 Conclusion

This project demonstrates practical experience in network traffic analysis using Wireshark through a structured SOC investigation workflow. By capturing and analyzing network packets, investigating protocol behavior, identifying suspicious communications, and validating Indicators of Compromise (IOCs), the lab strengthens the packet analysis and threat hunting skills required for modern SOC, Blue Team, and Detection Engineering roles.

---

## 👨‍💻 Author

**Muhammad Talha**

**Aspiring Cloud Security Engineer & SOC Analyst | Detection Engineering | Threat Hunting | SIEM (Splunk & Wazuh) | Blue Team Operations | Network Security | MITRE ATT&CK**
