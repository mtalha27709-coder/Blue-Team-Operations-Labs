# mac-ip-address-investigation
Analyzing MAC and IP address behavior in local and remote network communication using Cisco Packet Tracer simulation mode.





# 🔍 Packet Tracer - Identify MAC and IP Addresses






## 📌 Overview
This project demonstrates how MAC and IP addresses behave during network communication using Cisco Packet Tracer simulation mode.



The lab focuses on analyzing how Protocol Data Units (PDUs) travel across a network and how addressing changes depending on whether communication is local or remote.



---



## 🎯 Objectives




### Part 1: Local Network Communication
- Capture and analyze PDUs between devices in the same network
- Observe MAC and IP address behavior without using a default gateway




### Part 2: Remote Network Communication
- Analyze how PDUs travel across different networks
- Understand the role of routers in modifying MAC addresses



---




## 🧪 Tools Used
- Cisco Packet Tracer
- Simulation Mode (PDU Analysis)




---




## 🔍 Key Observations




- MAC addresses change at each hop (Layer 2 behavior)
- IP addresses remain constant from source to destination (Layer 3 behavior)
- Local communication does not require a default gateway
- Remote communication requires routing via a gateway
- PDUs encapsulate data differently across OSI layers



---




## 📊 Sample PDU Analysis

| Device          | Src MAC        | Dest MAC       | Src IP       | Dest IP      |
|-----------------|---------------|---------------|-------------|-------------|
| 172.16.31.3     | 0060.7036.2849| 000C.85CC.1DA7| 172.16.31.3 | 172.16.31.2 |



---




## 💡 Key Learnings

- Understanding packet flow is essential for networking and cybersecurity
- Layer 2 and Layer 3 addressing play different roles
- Packet Tracer simulation is powerful for visualizing real network behavior
- Strong foundation for roles in networking, SOC, and cybersecurity



---



## 🚀 Future Improvements
- Add screenshots of simulation steps
- Expand analysis for complex network topologies
- Include Wireshark comparison



---



## 👨‍💻 Author
Talha – Cybersecurity & Networking Learner
