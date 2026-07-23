# packet-tracer-telnet-ssh-lab
A networking lab simulating secure and insecure remote access methods (Telnet vs SSH) using Cisco Packet Tracer. Focuses on authentication, connectivity testing, and secure management of network devices.


# Packet Tracer - Telnet and SSH Remote Access Lab



## 📌 Overview


This project demonstrates how to remotely access a Cisco router using **Telnet (insecure)** and **SSH (secure)** in a simulated network environment using Cisco Packet Tracer.


It highlights the importance of secure communication methods in network administration.



---



## 🎯 Objectives


- Verify network connectivity using IP configuration and ping
- Understand DHCP-assigned addressing for PCs
- Attempt remote access using Telnet
- Establish secure remote access using SSH
- Compare secure vs insecure remote management

- 

---



## 🧾 Network Details



| Device | Interface | IP Address   | Subnet Mask       |
|--------|----------|--------------|-------------------|
| HQ Router | G0/0/1   | 64.100.1.1   | 255.255.255.0     |
| PC0    | NIC      | DHCP         | Automatically assigned |
| PC1    | NIC      | DHCP         | Automatically assigned |



---



## 🔧 Steps Performed



### 1. Connectivity Check


- Verified IP address using:
bash
ipconfig ping 64.100.1.1

Telnet Access Attempt

Command used:

telnet 64.100.1.1

SSH Access

Command used:

ssh -l admin 64.100.1.1
Password:

class

Successful login confirms secure remote access via SSH.


---


🔐 Key Learning Outcomes
Telnet sends data in plaintext and is insecure
SSH provides encrypted and secure remote access
Network devices should always use SSH for management
DHCP simplifies IP assignment for end devices
🚀 Conclusion

This lab demonstrates why SSH is preferred over Telnet for secure network administration and how remote access is configured and tested in Cisco Packet Tracer.

👨‍💻 Author

Talha — Networking & Cybersecurity Learner


---

If you want, I can also:
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- Or :contentReference[oaicite:2]{index=2}

Just tell me 👍
