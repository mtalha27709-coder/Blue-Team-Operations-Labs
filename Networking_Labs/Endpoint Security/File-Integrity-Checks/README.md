# 🔐 Packet Tracer - File and Data Integrity Checks



## 📌 Overview


This Cisco Packet Tracer lab focuses on verifying file integrity using hashing and HMAC techniques in a simulated enterprise network environment.

The project demonstrates how cybersecurity professionals:
- Detect file tampering
- Recover files after cyber attacks
- Validate integrity using hashes
- Use HMAC for secure verification
- Investigate compromised files

This lab provides practical experience with integrity verification techniques commonly used in cybersecurity, SOC operations, and digital forensics.



---



# 🎯 Objectives



## Part 1: Recover Files After a Cyber Attack


- Access enterprise servers
- Recover backup files using FTP
- Validate downloaded files



## Part 2: Verify File Integrity Using Hashing


- Generate MD5 hashes
- Compare archived and computed hashes
- Detect tampered files
- Escalate incidents to supervisors

## Part 3: Verify File Integrity Using HMAC
- Generate SHA-256 HMAC values
- Use secret keys for authentication
- Understand secure integrity validation



---



# 🛠 Technologies & Tools Used



- Cisco Packet Tracer
- OpenSSL
- MD5 Hashing
- HMAC-SHA256
- FTP Protocol
- Kali Linux / CSE-LABVM
- VirtualBox




---



# 🔍 Key Cybersecurity Concepts



## ✅ File Integrity Verification


Learned how hashes help detect unauthorized modifications in files.



## ✅ MD5 Hashing


Generated and compared MD5 hashes to identify tampered files.



## ✅ HMAC Authentication


Used HMAC with SHA-256 and secret keys to strengthen integrity validation.



## ✅ Incident Escalation


Simulated reporting suspicious activity to supervisors for further investigation.



## ✅ Secure Data Validation


Understood how organizations ensure files remain unchanged during storage and transfer.



---



# 📂 Lab Workflow



```text
Backup Files Download
        ↓
Generate File Hashes
        ↓
Compare Original Hashes
        ↓
Detect Tampered Files
        ↓
Escalate Incident
        ↓
Transfer Suspicious Files
        ↓
Perform HMAC Verification
```



---



# 🔐 Commands Used



## Generate MD5 Hash


```bash
echo -n 'file-contents' | md5sum
```



## Generate HMAC SHA-256


```bash
openssl dgst -sha256 -hmac cisco123 income.txt
```


## FTP Commands


```bash
ftp hq.corp
dir
get filename.txt
quit
```



---



# ⚠ Security Lessons Learned



- File integrity is critical in cybersecurity
- Even one-bit changes produce different hashes
- MD5 helps detect tampering but is not ideal for modern security
- HMAC is stronger because it uses a secret key
- Integrity validation is essential during backups and file transfers



---



# 📸 Skills Practiced



- File hashing
- HMAC generation
- FTP file transfer
- Cyber attack investigation
- Integrity validation
- Linux terminal operations
- Incident escalation workflow



---



# 🚀 Learning Outcome



This lab strengthened my understanding of:
- Data integrity principles
- Cryptographic hashing
- HMAC authentication
- Incident response workflows
- Practical cybersecurity operations

It also demonstrated how organizations detect file tampering and protect critical business data from unauthorized changes.



---


# 👨‍💻 Author



Muhammad Talha

## 🌐 Connect With Me
GitHub: https://github.com/mtalha27709-coder



---



# ⭐ Disclaimer

This project is for educational purposes only.
The lab environment is designed to help students understand cybersecurity concepts related to file integrity and secure verification techniques.
