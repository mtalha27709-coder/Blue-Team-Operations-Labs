# 🔐 Packet Tracer - Explore File and Data Encryption



## 📌 Overview


This Cisco Packet Tracer lab demonstrates how encrypted files and credentials can be securely transferred and decrypted using FTP and OpenSSL.

The project focuses on:
- File encryption & decryption
- FTP authentication
- Secure file transfer concepts
- OpenSSL cryptographic operations
- Basic cybersecurity data protection practices

It simulates a real-world scenario where employees securely exchange confidential customer data using encrypted files.



---



# 🎯 Objectives



## Part 1: Discover FTP Credentials for Mary


- Access encrypted FTP login data
- Use OpenSSL to decrypt credentials
- Understand AES-256 encryption basics



## Part 2: Upload Confidential Data using FTP


- Connect to FTP server
- Upload encrypted sensitive data
- Analyze risks of plaintext FTP communication



## Part 3: Discover FTP Credentials for Bob


- Decrypt another encrypted credential file
- Understand secure credential storage concepts



## Part 4: Download Confidential Data using FTP


- Retrieve encrypted files from FTP server
- Verify secure transfer workflow



## Part 5: Decrypt Sensitive Files


- Use OpenSSL to decrypt encrypted documents
- Analyze confidentiality and encryption limitations



---



# 🛠 Technologies & Tools Used



- Cisco Packet Tracer
- OpenSSL
- FTP Protocol
- AES-256-CBC Encryption
- Kali Linux / CSE-LABVM
- VirtualBox

- 

---



# 🔍 Key Cybersecurity Concepts



## ✅ Encryption & Decryption


Learned how AES-256-CBC encryption protects sensitive information using passwords and cryptographic algorithms.



## ✅ FTP Security Risks


Observed how traditional FTP sends authentication and traffic in plaintext, making it insecure without additional protections.



## ✅ Password-Based Key Derivation


Explored PBKDF2 for generating cryptographic keys from passwords.



## ✅ Secure File Handling


Practiced secure transfer and decryption of confidential customer information.



## ✅ Threat Awareness



Understood why encrypted storage matters even when network protocols are insecure.



---



# 📂 Lab Workflow


text
Encrypted Credentials
        ↓
OpenSSL Decryption
        ↓
FTP Authentication
        ↓
Encrypted File Upload
        ↓
File Download
        ↓
OpenSSL File Decryption

🔐 OpenSSL Commands Used
Decrypt Credential Data
        ↓
Access Sensitive Data
echo 'encrypted_text_here' | openssl aes-256-cbc -pbkdf2 -a -d

Decrypt Encrypted File
openssl aes-256-cbc -pbkdf2 -a -d -in clientinfo.enc -out clientinfo.txt


---


⚠ Security Lessons Learned


FTP is NOT secure for sensitive communication
Encryption protects data confidentiality
Weak passwords weaken encryption security
Modern environments should use:
SFTP
FTPS
SSH-based transfers
Strong integrity verification

---


📸 Skills Practiced
File encryption/decryption
Linux terminal usage
OpenSSL operations
FTP authentication
Secure data transfer analysis
Cybersecurity troubleshooting


---


🚀 Learning Outcome

This lab helped strengthen my understanding of:

Cryptography fundamentals
Data confidentiality
Secure file handling
Encryption workflows
Practical cybersecurity operations

It also demonstrated how encryption can protect sensitive data even when transferred over insecure protocols.


---


👨‍💻 Author

Muhammad Talha

🌐 Connect With Me

GitHub: https://github.com/mtalha27709-coder


---



⭐ Disclaimer

This lab is for educational purposes only.

The encryption methods demonstrated here should NOT be used in production environments for protecting highly sensitive data.
