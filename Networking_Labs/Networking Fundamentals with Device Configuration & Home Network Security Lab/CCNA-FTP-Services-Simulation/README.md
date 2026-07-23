# ccna-ftp-services-simulation
Simulated FTP file upload, download, rename, and delete operations using Cisco Packet Tracer to understand File Transfer Protocol (FTP) client-server communication over port 21/20.



# 📡 Packet Tracer - FTP Services Lab



## 📌 Overview


This project demonstrates how File Transfer Protocol (FTP) works in a network environment using Cisco Packet Tracer. It simulates real-world client-server communication for file upload, download, rename, and deletion operations.

FTP is a standard network protocol used to transfer files between a client and a server over a TCP/IP network using:
- Port 21 (Command Control)
- Port 20 (Data Transfer)

- 

---



## 🎯 Objectives


- Upload a file from a client PC to an FTP server
- Download a file from an FTP server to a client PC
- Rename files on the FTP server
- Delete files from the FTP server
- Understand FTP command-line operations



---



## 🖧 Network Details



| Device         | Interface | IP Address        | Subnet Mask        |
|----------------|----------|------------------|--------------------|
| FTP Server     | NIC      | 209.165.200.226  | 255.255.255.224    |



---



## ⚙️ Key FTP Commands Used



- `ftp <server-ip>` → Connect to FTP server
- `dir` → List files
- `put <file>` → Upload file
- `get <file>` → Download file
- `rename <old> <new>` → Rename file
- `delete <file>` → Delete file
- `quit` → Exit FTP session



---



## 📂 Lab Activities



### Part 1: Upload File to FTP Server
- Locate `sampleFile.txt` on PC
- Connect to FTP server using CLI
- Upload file using `put sampleFile.txt`



---



### Part 2: Download File from FTP Server
- Rename file on server:rename sampleFile.txt sampleFile_FTP.txt
- Download file using: get sampleFile_FTP.txt 



---



### Part 3: Delete File from FTP Server
- Connect to FTP server
- Remove file using:delete sampleFile_FTP.txt

- 
---

## 🧠 Key Learning Outcomes


- Understanding FTP client-server architecture
- Practical use of file transfer commands
- Network communication using TCP ports 20/21
- Hands-on experience with Cisco Packet Tracer simulation



---



## 🚀 Tools Used


- Cisco Packet Tracer
- FTP Protocol Simulation

---





## 📌 Author

Cybersecurity & Networking Lab Practice

