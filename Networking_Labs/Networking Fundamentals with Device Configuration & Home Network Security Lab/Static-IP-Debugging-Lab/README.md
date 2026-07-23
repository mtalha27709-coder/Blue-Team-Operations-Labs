# static-ip-debugging-lab
A networking troubleshooting lab using Cisco Packet Tracer to identify and resolve incorrect static IP configurations using ipconfig /all.


# Packet Tracer - IP Configuration Troubleshooting Lab



## 📌 Overview


This project demonstrates how to troubleshoot network connectivity issues using the **ipconfig /all** command in Cisco Packet Tracer. A small office network is configured with static IP addressing, and one PC contains incorrect settings causing internet connectivity failure.



---



## 🎯 Objectives


- Use `ipconfig /all` to verify network configuration
- Identify incorrect IP configuration in a LAN
- Understand static IP addressing in a /24 network
- Correct misconfigured network settings using IP Configuration tool
- Restore connectivity to a web server (www.cisco.pka)



---



## 🧾 Network Scenario


- All PCs are configured with static IPs in `192.168.1.0/24` network
- Default gateway and subnet mask must be correctly configured
- One PC is misconfigured and cannot access the internet/web server



---



## 🔧 Tools Used


- Cisco Packet Tracer
- Command Prompt (`ipconfig /all`)
- Desktop > IP Configuration



---


## 🛠️ Steps Performed



### 1. Check IP Configuration
On each PC, open Command Prompt and run:
bash id="4b7h6m"
ipconfig /all

---


Recorded the following:

IP Address
Subnet Mask
Default Gateway

---


2. Identify the Problem
Compared all PCs’ configurations
Found one PC with incorrect IP settings causing network failure
3. Fix Misconfiguration
Opened Desktop > IP Configuration
Corrected:
IP Address
Subnet Mask
Default Gateway


---


🔐 Key Learning Outcomes
ipconfig /all is essential for network troubleshooting
Incorrect IP settings can break network connectivity
Static IP networks require careful manual configuration
Troubleshooting follows a systematic comparison approach


---


🚀 Conclusion

This lab demonstrates basic but critical network troubleshooting skills used in real-world IT and SOC environments to diagnose and fix IP configuration issues.


---


👨‍💻 Author

Talha — Networking & Cybersecurity Learner


---

## 💾 Commit Message Options

### 🔹 Simple
``` id="q8n1df"
Update README.md
