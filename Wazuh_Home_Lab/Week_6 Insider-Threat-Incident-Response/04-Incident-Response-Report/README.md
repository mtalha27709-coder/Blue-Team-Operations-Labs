# ?? Incident Response Report

## ?? Overview

The final phase of this capstone project focused on documenting the insider threat investigation through a professional Incident Response Report based on the **NIST SP 800-61 Computer Security Incident Handling Guide**.

The report transforms technical findings into structured documentation suitable for Security Operations Centers (SOC), Incident Response teams, management, legal departments, and other stakeholders.

It summarizes the incident, reconstructs the attack timeline, analyzes the collected evidence, recommends response actions, and documents improvements made through Detection Engineering.

---

# ?? Objectives

- Document the complete security incident
- Present technical findings in a structured format
- Correlate evidence collected during the investigation
- Recommend containment, eradication, and recovery actions
- Document lessons learned
- Improve future detection capabilities

---

# ?? Reporting Standard

The report follows the **NIST SP 800-61 Incident Response Framework**, a widely recognized industry standard for handling and documenting cybersecurity incidents.

---

# Report Structure

## 1?? Executive Summary

Provides a high-level overview of the incident suitable for non-technical stakeholders.

This section includes:

- Incident summary
- Impact assessment
- Affected data
- Investigation outcome
- Overall response

---

## 2?? Detection and Analysis

This section contains the complete technical investigation.

It includes:

- Attack timeline
- Wazuh FIM evidence
- CyberChef decoded evidence
- Indicators of Compromise (IOCs)
- MITRE ATT&CK mapping
- Investigation findings

---

## 3?? Containment, Eradication and Recovery

This section explains how the incident should be handled within an enterprise environment.

Topics covered include:

### Containment

- Isolate the compromised endpoint
- Disable the compromised account
- Block malicious communications
- Preserve forensic evidence

### Eradication

- Remove malicious artifacts
- Review endpoint for persistence
- Validate system integrity
- Review privileged access

### Recovery

- Restore normal operations
- Re-enable user access
- Continue monitoring
- Verify successful remediation

---

## 4?? Post-Incident Activity

The final section documents improvements made after the investigation.

It includes:

- Custom Wazuh Detection Rule
- Detection Engineering improvements
- Lessons Learned
- Recommendations
- Future monitoring enhancements

---

# Investigation Summary

The investigation confirmed that an insider staged confidential information within a monitored directory before encoding it using Base64. The encoded data was transferred to an attacker-controlled system over HTTP before the attacker attempted to delete all related files.

Despite the cleanup attempt, Wazuh File Integrity Monitoring successfully preserved forensic evidence, allowing the complete attack timeline to be reconstructed.

---

# Evidence Included

The report contains evidence collected throughout the investigation, including:

- File Integrity Monitoring Alerts
- Attack Timeline
- Wazuh Discover Logs
- CyberChef Decoded Output
- Indicators of Compromise (IOCs)
- MITRE ATT&CK Mapping
- Custom Detection Rule
- Detection Validation

---

# MITRE ATT&CK Techniques

| Technique | Description |
|-----------|-------------|
| T1074 | Data Staged |
| T1027 | Obfuscated Files or Information |
| T1048 | Exfiltration Over Alternative Protocol |
| T1070 | Indicator Removal on Host |

---

# Skills Demonstrated

- Incident Response
- Digital Forensics
- Threat Hunting
- Security Documentation
- Detection Engineering
- Wazuh SIEM
- MITRE ATT&CK Mapping
- IOC Analysis
- Timeline Reconstruction
- NIST SP 800-61 Reporting

---

# Deliverables

This folder contains:

```text
Incident-Response-Report.pdf
OR
Incident-Response-Report.docx
```

The report serves as the final deliverable of the Week 6 Capstone project and documents the complete lifecycle of the insider threat incident, from initial compromise through investigation, detection engineering, and post-incident recommendations.

---

# Key Learning Outcomes

This phase reinforced the importance of structured incident documentation alongside technical investigation. Writing a formal incident response report demonstrated how technical evidence can be translated into actionable information for both technical and non-technical stakeholders.

The project also highlighted the relationship between threat hunting, forensic analysis, detection engineering, and incident response within a modern Security Operations Center.

---

# ? Outcome

A professional Incident Response Report was successfully produced, documenting the complete insider threat investigation using the NIST SP 800-61 framework. The report consolidates technical evidence, forensic findings, response recommendations, and detection improvements into a single document suitable for real-world SOC operations.