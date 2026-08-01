# ?? Wireshark Network Traffic Analysis Lab

## ?? Project Overview

This repository documents my hands-on learning and practical exercises using **Wireshark**, the world's leading network protocol analyzer. The project focuses on packet capture, protocol analysis, traffic inspection, network troubleshooting, and basic threat hunting techniques commonly used by SOC Analysts, Blue Team operators, Incident Responders, and Network Security Engineers.

Through this lab, I analyzed network communications, investigated DNS requests, examined TCP sessions, identified endpoints, and developed practical packet analysis skills.

---

# ?? Objectives

- Learn Wireshark fundamentals
- Capture network traffic
- Analyze common protocols
- Understand packet structure
- Investigate DNS activity
- Analyze TCP communications
- Identify network endpoints
- Follow TCP streams
- Perform basic threat hunting
- Develop packet analysis skills

---

---

# ?? Topics Covered

## ?? Packet Capture

- Live Packet Capture
- Interface Selection
- Capture Options
- Saving PCAP Files

---

## ?? Protocol Analysis

- Ethernet
- IPv4
- IPv6
- TCP
- UDP
- ICMP
- ARP
- DNS
- HTTP
- HTTPS
- DHCP

---

## ?? Packet Inspection

- Packet Details
- Packet Bytes
- Header Analysis
- Payload Inspection

---

## ?? DNS Analysis

Activities:

- DNS Queries
- DNS Responses
- Domain Resolution
- Suspicious Domain Investigation

---

## ?? TCP Analysis

Activities:

- Three-Way Handshake
- TCP Flags
- Session Analysis
- TCP Streams
- Connection Tracking

---

## ??? Endpoint Analysis

Performed:

- Endpoints Statistics
- Conversations
- Top Talkers
- Communication Frequency

---

## ?? Statistics & Monitoring

- Protocol Hierarchy
- IO Graphs
- Endpoints
- Conversations
- Packet Length Analysis

---

## ??? Basic Threat Hunting

- Suspicious DNS Requests
- Unknown External IPs
- High Traffic Endpoints
- Unusual Connections
- Packet Stream Review

---

# ??? Tools Used

- Wireshark
- Windows
- Ubuntu Linux
- VirusTotal (Threat Validation)
- Command Prompt
- PowerShell

---

# ?? Common Display Filters

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

# ?? Investigation Workflow

```
Capture Packets
       ?
       ?
Protocol Analysis
       ?
       ?
DNS Investigation
       ?
       ?
TCP Session Review
       ?
       ?
Endpoint Analysis
       ?
       ?
Follow TCP Stream
       ?
       ?
Threat Validation
       ?
       ?
Investigation Report
```

---

# ?? Skills Demonstrated

- Packet Capture
- Protocol Analysis
- Network Troubleshooting
- DNS Investigation
- TCP Analysis
- Endpoint Analysis
- Traffic Monitoring
- Packet Inspection
- Threat Hunting
- Incident Investigation

---

# ?? Learning Outcomes

After completing this lab, I gained practical experience in:

- Capturing live network traffic
- Understanding packet structures
- Investigating DNS activity
- Analyzing TCP sessions
- Identifying active hosts
- Following TCP streams
- Using Wireshark filters
- Performing basic threat hunting
- Creating investigation reports

---

# ?? Career Relevance

This project demonstrates practical skills relevant to:

- SOC Analyst
- Blue Team Analyst
- Network Security Engineer
- Incident Responder
- Threat Hunter
- Cybersecurity Analyst

---

# ?? Screenshots Included

- Wireshark Installation
- Packet Capture
- Interface Selection
- DNS Analysis
- TCP Three-Way Handshake
- Follow TCP Stream
- Protocol Hierarchy
- Conversations
- Endpoints
- IO Graphs
- Display Filters
- Investigation Results

---

# ?? Conclusion

This Wireshark Learning Lab provides hands-on experience in network traffic analysis, packet inspection, protocol analysis, and basic threat hunting. The project strengthens practical networking and security investigation skills that are widely used in SOC environments, incident response, and network security operations.

---

## ????? Author

**Muhammad Talha**

Cyber Security Student | SOC Analyst | Wireshark | Network Security | Blue Team | Threat Hunting