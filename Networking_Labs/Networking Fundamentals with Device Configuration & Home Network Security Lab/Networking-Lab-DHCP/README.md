# networking-lab-dhcp
Packet Tracer DHCP configuration practical on wireless router with 3 PCs.
🧪 Packet Tracer Lab: DHCP on Wireless Router
🎯 Objective
3 PCs ko wireless router se connect karna
DHCP enable karke automatic IP assign karwana
Custom DHCP range configure karna
Network connectivity verify karna
🧠 Overview

This lab demonstrates how a wireless router assigns IP addresses automatically using DHCP and how to modify DHCP settings for a custom network.

🛠️ Step 1: Network Setup
Added 3 PCs (PC0, PC1, PC2)
Connected all PCs to Wireless Router using straight-through cables
Waited until link lights turned green








📡 Step 2: Default DHCP Observation
On PC0:
Go to Desktop → IP Configuration
Select DHCP
📌 Default Gateway:
192.168.0.1
Router Access:
Open Web Browser
Enter gateway IP
Login:
Username: admin
Password: admin
Observations:
DHCP is enabled by default
Router automatically assigns IP range
Default network is visible in settings






🔧 Step 3: Change Router IP Address
New IP:
192.168.5.1
Save settings
Router disconnects temporarily (normal behavior)
Reconnect:
PC0 → IP Configuration → DHCP renew
Open browser:
http://192.168.5.1




📶 Step 4: Modify DHCP Range
Updated Settings:
Starting IP:
192.168.5.126
Maximum Users:
75
Save settings
📌 PC0 New IP:
192.168.5.x (assigned via DHCP)





💻 Step 5: Enable DHCP on Other PCs
PC1:
Desktop → IP Configuration → DHCP
PC1 IP:
192.168.5.x
PC2:
Desktop → IP Configuration → DHCP
PC2 IP:
192.168.5.x





🔍 Step 6: Connectivity Test
On PC2:
Check IP:
ipconfig
Ping Router:
ping 192.168.5.1
Ping PC1:
ping 192.168.5.127
✅ Results






✔ All PCs received IP via DHCP
✔ Router successfully configured
✔ Network communication working
✔ Pings successful between devices










🧾 Conclusion

This lab helped in understanding:






DHCP configuration on wireless router
Automatic IP assignment
Custom network setup
Basic network troubleshooting







🚀 Author

Talha (Cybersecurity Student)
Packet Tracer Networking Practice 💻
