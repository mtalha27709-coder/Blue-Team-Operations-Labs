# 🔐 ACL Access Control Demonstration – Packet Tracer



This project demonstrates how Access Control Lists (ACLs) are used in networking to control traffic flow and enhance network security. The lab focuses on how ACLs can block specific traffic (like ping requests) and how removing them restores connectivity.



---



## 🎯 Objectives



- Verify local network connectivity
- Test ACL behavior on remote network communication
- Analyze ACL configuration using Cisco IOS commands
- Remove ACL and observe changes in connectivity

---



## 🧪 Lab Overview



### 📌 Part 1: Connectivity Testing with ACL



#### ✅ Local Network Testing


- PC1 successfully pings PC2 and PC3
- Reason: No restrictions within the same local network



#### ❌ Remote Network Testing


- PC1 fails to ping PC4 and DNS Server
- Reason: ACL blocks traffic from the source network


---

## 🚫 ACL Configuration Analysis

Using the command: show access-lists



Output:
Standard IP access list 11
10 deny 192.168.10.0 0.0.0.255
20 permit any



### 🔍 Explanation:


- `deny 192.168.10.0/24` → Blocks all traffic from this network
- `permit any` → Allows all other traffic


📌 The ACL is applied:


- **Interface:** Serial0/0/0  
- **Direction:** Outbound

---

## 🔄 Part 2: Removing ACL


### 🛠️ Commands Used:

interface se0/0/0
no ip access-group 11 out
no access-list 11



### ✅ Result:
- PC1 can now successfully ping PC4 and DNS Server
- Connectivity restored after ACL removal

---

## 🛠️ Tools Used
- Cisco Packet Tracer
- Cisco IOS CLI

---

## 🧠 Key Learnings

- ACLs control traffic based on rules (permit/deny)
- ACLs must be applied to interfaces to take effect
- Order of ACL rules matters
- Removing ACL restores blocked communication
- Important concept for network security & firewall logic

---

## 📸 Project Files


- `.pkt` file included
- (Optional) Add screenshots for better understanding



---


## 🚀 Future Improvements


- Implement Extended ACLs
- Apply ACLs on inbound direction
- Combine ACL with NAT & firewall scenarios



---



## 🤝 Connect With Me


Check out more networking & cybersecurity projects on my GitHub:  
👉 https://github.com/mtalha27709-coder


---


⭐ If you find this helpful, don’t forget to star the repo!
