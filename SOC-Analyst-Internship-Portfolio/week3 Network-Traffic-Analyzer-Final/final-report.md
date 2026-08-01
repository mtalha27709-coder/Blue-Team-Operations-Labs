# Final Traffic Analysis Report

## Objective
To analyze captured network traffic and identify suspicious behavior using Wireshark and external threat intelligence tools.

---

## Methodology
- Captured live traffic using Wireshark
- Applied protocol filters (DNS, TCP, HTTP)
- Investigated traffic patterns
- Performed deep packet inspection using stream follow
- Verified suspicious domains/IPs using VirusTotal

---

## Analysis Performed

### DNS Analysis
- DNS traffic was captured and analyzed
- Suspicious domains were identified
- Domains were checked on VirusTotal for reputation

### TCP Analysis
- TCP handshake observed
- Multiple external TCP connections analyzed
- Suspicious TCP streams investigated

### Endpoint Analysis
- TCP endpoints analyzed
- Top communicating hosts identified

### Stream Analysis
- TCP streams followed for payload inspection
- Unencrypted communication observed

---

## Suspicious Activity Findings
- Suspicious DNS queries identified
- Certain domains flagged and verified using VirusTotal
- TCP streams showed unusual external communication
- High traffic endpoints detected

---

## Security Insight
- DNS can reveal user browsing behavior
- TCP streams help detect hidden communication
- External threat intelligence improves accuracy

---

## Conclusion
Wireshark combined with VirusTotal provided deep visibility into network traffic and helped identify potentially suspicious activity in a real-world scenario.