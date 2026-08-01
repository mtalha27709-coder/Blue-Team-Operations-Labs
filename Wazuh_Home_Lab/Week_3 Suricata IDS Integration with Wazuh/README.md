# Week 3 — Suricata IDS Integration with Wazuh

## Objective
Deploy Suricata as a network intrusion detection system, write custom rules for specific threats, integrate it with Wazuh for correlated visibility, and implement GeoIP-based firewall blocking.

## What I Did

### Suricata Installation and Configuration
- Installed Suricata on the Kali VM in **IDS mode** (detection only, no inline blocking)
- Identified the correct network interface and configured it in the `af-packet` section of `suricata.yaml`
- Verified Suricata was actively capturing traffic by generating activity (ping, curl, nmap scan) and confirming alerts in `fast.log`
- Reviewed `eve.json`, the full structured JSON log used later for Wazuh integration

### Custom Suricata Rule Writing
- Ran `suricata-update` to pull the latest Emerging Threats ruleset
- Wrote three custom rules:
  1. **Nmap scan detection** — based on TCP flag patterns (SYN/NULL/FIN scans)
  2. **HTTP exploit attempt detection** — matching suspicious URI/payload strings
  3. **ICMP flood detection** — threshold-based rule for high-volume ping traffic
- Triggered each rule and confirmed correct alerts in `fast.log`

### Suricata + Wazuh Integration
- Configured the Wazuh agent on Kali to monitor `eve.json` as a JSON-formatted log source
- Verified Wazuh's built-in Suricata decoder and ruleset were processing the events correctly
- Generated test traffic (nmap scan, HTTP request, ping flood) and confirmed Suricata alerts appeared inside the Wazuh dashboard
- Performed a correlation exercise: triggered an nmap scan (Suricata alert) followed by a file change on the target (Wazuh FIM alert), and used the Threat Hunting module to view both events together as a single attack narrative

### GeoIP Blocking and Firewall Rules
- Installed `ipset` and `xtables-addons` for GeoIP-based iptables matching
- Downloaded country-level IP blocklists from ipdeny.com and loaded them into `ipset`
- Created iptables rules to drop traffic from selected country ranges
- Configured UFW/hosts-based blocking for specific domains as a secondary access-control technique
- Documented the real-world limitations of GeoIP blocking (VPNs, Tor, spoofing) as a layer of friction rather than a complete control

## Deliverables
- Suricata installation and configuration screenshots
- Custom rules file with explanation document
- Suricata–Wazuh integration screenshots + correlation analysis
- Firewall ruleset documentation (ipset/iptables + UFW)

## Key Takeaway
Week 3 added network-layer visibility to complement the host-layer visibility from Weeks 1–2. Correlating a Suricata network alert with a Wazuh host alert from the same activity gave a fuller picture of an attack than either tool alone.
