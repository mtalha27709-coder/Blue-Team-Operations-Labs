# Week 4 — pfSense Firewall and Advanced Monitoring

## Objective
Deploy pfSense as a managed network perimeter, integrate threat intelligence feeds, enable vulnerability detection, and produce SOC-style dashboards and reports for both technical and non-technical audiences.

## What I Did

### pfSense Firewall Setup
- Deployed pfSense as a virtual firewall/router with WAN and LAN interfaces
- Reconfigured all lab VMs (Ubuntu, Windows 10, Kali) to route through pfSense as their default gateway
- Created firewall rules on the LAN interface with logging enabled for full traffic visibility
- Configured pfSense to forward syslog to the Wazuh Manager and confirmed firewall events appearing in the Wazuh dashboard alongside existing host/network alerts

### Threat Intelligence Integration
- Configured a **VirusTotal** integration in Wazuh to automatically submit file hashes from FIM events and flag known-malicious files
- Enabled the **MITRE ATT&CK** module and mapped existing alerts (SSH brute-force, FIM events, Suricata network alerts) to specific ATT&CK techniques
- Built CDB (lookup table) integrations using threat feeds from **URLhaus** and **Abuse.ch**, and wrote a rule that fires when an alert field matches a known-malicious indicator
- Documented an IOC summary from observed activity, including indicator type, source, and recommended action

### Vulnerability Assessment
- Enabled Wazuh's vulnerability detection module (NVD-based CVE matching against installed software)
- Confirmed both Linux and Windows agents were reporting software inventory via `syscollector`
- Reviewed vulnerability findings for both agents, researched the top CVEs individually, and built a prioritized remediation list ordered by CVSS score plus contextual risk factors
- Simulated the remediation cycle: patched a vulnerable package on the Linux agent, waited for rescan, and confirmed the CVE no longer appeared

### SOC Dashboards and Reporting
- Built a custom Wazuh dashboard with panels for: 7-day alert volume by severity, agent health status, top 10 firing rules, and top source IPs
- Wrote a detailed **technical SOC summary report** covering all alert categories from the week (auth events, FIM, Suricata, pfSense, vulnerabilities, threat intel hits)
- Wrote a separate **one-page executive summary** in plain language for a non-technical audience — no unexplained jargon, focused on risk posture and recommendations

## Deliverables
- pfSense configuration screenshots and firewall rule documentation
- VirusTotal/MITRE ATT&CK/threat feed integration screenshots + IOC summary
- Vulnerability report with prioritized CVE list and remediation verification
- Custom Wazuh dashboard screenshot
- Technical SOC summary report + executive summary

## Key Takeaway
Week 4 completed the defensive picture: a managed network perimeter, threat intelligence enrichment on top of raw detections, proactive vulnerability visibility, and the ability to communicate findings clearly to both technical and non-technical audiences — the last of which was, honestly, harder than any of the technical configuration.
