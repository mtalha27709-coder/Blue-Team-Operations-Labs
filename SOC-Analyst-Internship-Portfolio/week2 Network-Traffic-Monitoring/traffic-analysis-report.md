# Traffic Analysis Report

## Overview
This report documents the analysis of captured network traffic using Wireshark. The objective was to identify normal and suspicious network behavior through protocol inspection and external threat validation.

---

## Tools Used
- Wireshark
- VirusTotal (for threat intelligence validation)

---

## Analysis Performed

### 1. DNS Traffic Analysis
- DNS queries were captured and analyzed
- Multiple domain lookups were observed
- Suspicious DNS requests were identified
- Selected domains were verified using VirusTotal for reputation analysis

---

### 2. TCP Traffic Analysis
- TCP communication between internal and external hosts was observed
- TCP handshake process was verified (SYN, SYN-ACK, ACK)
- TCP streams were followed for deeper inspection

---

### 3. TCP Endpoints Analysis
- Endpoints were analyzed to identify active communicating IPs
- Unusual external IP communication was reviewed

---

### 4. TCP Top Endpoints
- Top talkers in the network were identified
- High traffic endpoints were analyzed for abnormal behavior

---

### 5. Stream Follow Analysis
- Suspicious TCP streams were followed using Wireshark
- Payload-level inspection was performed

---

## Suspicious Activity Investigation

The following suspicious behaviors were analyzed:

- Suspicious DNS traffic identified during capture
- DNS domains checked on VirusTotal for threat reputation
- Suspicious TCP connections identified
- TCP streams followed for payload inspection
- TCP endpoints analyzed for unusual external communication
- Top endpoints reviewed for abnormal traffic volume

---

## Key Findings
- Some DNS queries required external validation via VirusTotal
- TCP connections showed multiple external communications
- Stream analysis helped in understanding packet-level behavior
- Endpoint analysis helped identify communication patterns

---

## Conclusion
Wireshark provided deep visibility into network traffic. Combining packet analysis with VirusTotal threat intelligence helped in identifying and validating suspicious network activity effectively.