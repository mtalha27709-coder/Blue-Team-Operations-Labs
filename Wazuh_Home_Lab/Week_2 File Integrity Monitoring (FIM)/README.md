# Week 2 — Detection, Custom Rules, and Log Analysis

## Objective
Configure meaningful detection capabilities in Wazuh, write custom detection rules, develop daily SOC log analysis skills, and implement automated active response.

## What I Did

### File Integrity Monitoring (FIM)
- Configured Wazuh's `syscheck` module to monitor `/etc`, `/var/log` (Linux) and `C:\Windows\System32` (Windows)
- Enabled `realtime` monitoring and `report_changes` (content diffing) on high-value directories
- Generated test file create/modify/delete events and confirmed alerts appeared with full forensic context (file path, event type, agent, timestamp, user)

### Custom Wazuh Detection Rules
- Learned Wazuh's rule engine architecture: decoder → rule matching → alert, and how custom rules chain onto default rules via `if_sid`
- Wrote three custom rules in `local_rules.xml`:
  1. **New user account creation** detection
  2. **SSH brute-force detection** — frequency-based rule (5+ failures within a 2-minute window)
  3. **USB device insertion** detection on Windows
- Tested each rule by triggering its condition and confirmed correct alert firing in the dashboard
- Tuned rules to reduce false positives and documented the tuning process

### Log Analysis Fundamentals
- Investigated Linux logs (`auth.log`, `syslog`) and Windows Security Event Log entries — specifically Event IDs 4625 (failed login), 4672 (privilege use), 4720 (account creation)
- Correlated failed-login patterns with subsequent successful logins to identify potential compromise indicators
- Used the Wazuh Threat Hunting module to query and correlate events across multiple agents and time windows
- Exported critical events to CSV and built a chronological timeline of suspicious activity

### Active Response
- Configured Wazuh Active Response to automatically run `firewall-drop` (iptables block) after 5 failed SSH attempts, with a 300-second timeout
- Tested end-to-end: triggered the brute-force condition from Kali, confirmed the IP was blocked at the OS level via `iptables`, and confirmed the SSH connection was refused while the block was active
- Documented the risks of active response in production (false positives, IP spoofing) and appropriate safeguards

## Deliverables
- FIM configuration report + event analysis
- Custom rules XML file with tuning notes
- Log analysis report (Linux + Windows sources) with CSV export and suspicious activity timeline
- Active response configuration and test documentation

## Key Takeaway
Week 2 moved the lab from passive logging to active detection and automated response — writing, testing, and tuning my own detection rules rather than relying on defaults.
