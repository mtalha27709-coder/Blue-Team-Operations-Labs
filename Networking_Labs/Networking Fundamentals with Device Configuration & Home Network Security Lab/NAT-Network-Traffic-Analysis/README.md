# NAT-Network-Traffic-Analysis
A hands-on networking project using Cisco Packet Tracer to explore NAT functionality on a wireless router. The project covers DHCP setup, IP addressing, and packet-level traffic analysis to understand how private networks access the internet securely.





# 🌐 Packet Tracer - Examine NAT on a Wireless Router




## 📌 Project Description
This project demonstrates how Network Address Translation (NAT) works on a wireless router using Cisco Packet Tracer. It focuses on configuring DHCP, analyzing internal and external IP addressing, and observing real-time traffic flow across a network.

---



## 🎯 Objectives

- Examine NAT configuration on a wireless router
- Configure multiple PCs using DHCP
- Analyze internal (private) and external (public) IP addressing
- Observe NAT translation using simulation mode

---



## 🛠️ Tools & Technologies
- Cisco Packet Tracer
- Networking Fundamentals (TCP/IP, DHCP, NAT)

---



## ⚙️ Project Setup



### 🔹 Step 1: External Network Configuration
- Connected a PC to the wireless router
- Enabled DHCP to obtain IP automatically
- Accessed router via default gateway
- Observed ISP-assigned IP (Public IP)

---



### 🔹 Step 2: Internal Network Configuration
- Checked Local Network settings
- Analyzed DHCP range
- Identified private IP addressing



---




### 🔹 Step 3: Connect Multiple Devices
- Connected 4 PCs to the router
- Assigned IPs via DHCP
- Verified configuration using:



ipconfig /all



---




### 🔹 Step 4: NAT Simulation
- Enabled Simulation Mode
- Created HTTP traffic using Complex PDU
- Observed packet flow between PC and server



---



### 🔹 Step 5: Packet Analysis
- Inspected inbound and outbound PDU details
- Observed change in Source IP due to NAT
- Understood how private IP is translated to public IP



---




## 📚 Key Concepts Learned
- NAT (Network Address Translation)
- DHCP (Dynamic Host Configuration Protocol)
- Private vs Public IP Addressing
- Packet Flow & Header Analysis
- TCP/HTTP Traffic Behavior



---




## 🌍 Real-World Applications
- Home and enterprise network configuration
- Internet access using NAT
- Network troubleshooting and monitoring
- Cybersecurity fundamentals (traffic inspection)



---




## 💡 Key Takeaway
NAT allows multiple devices in a private network to communicate with external networks using a single public IP, ensuring efficient IP usage and added security.



---



## 🚀 Future Improvements
- Implement Port Forwarding
- Explore PAT (Port Address Translation)
- Add firewall rules for enhanced security



---



## 📸 Screenshots

---



## 👨‍💻 Author
Talha – Cybersecurity & Networking Student
